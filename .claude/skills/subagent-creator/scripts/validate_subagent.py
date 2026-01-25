#!/usr/bin/env python3
"""
Subagent Validator - Validates subagent configuration

Usage:
    validate_subagent.py <path-to-subagent.md>

Examples:
    validate_subagent.py .claude/agents/code-reviewer.md
    validate_subagent.py ~/.claude/agents/data-analyzer.md
"""

import sys
import re
from pathlib import Path
import yaml


# Available tools in Claude Code (from documentation)
AVAILABLE_TOOLS = {
    'Read', 'Write', 'Edit', 'Grep', 'Glob', 'Bash', 'Task',
    'AskUserQuestion', 'ListDir', 'FileSearch', 'CodebaseSearch'
}

# Valid permission modes
VALID_PERMISSION_MODES = {
    'default', 'acceptEdits', 'dontAsk', 'bypassPermissions', 'plan'
}

# Valid model values
VALID_MODELS = {
    'sonnet', 'opus', 'haiku', 'inherit'
}


class ValidationError:
    def __init__(self, severity, message, line=None):
        self.severity = severity  # 'error' or 'warning'
        self.message = message
        self.line = line
    
    def __str__(self):
        prefix = "❌" if self.severity == 'error' else "⚠️ "
        location = f" (line {self.line})" if self.line else ""
        return f"{prefix} {self.message}{location}"


def validate_frontmatter(frontmatter, errors):
    """Validate YAML frontmatter fields."""
    
    # Check required fields
    if 'name' not in frontmatter:
        errors.append(ValidationError('error', "Missing required field: 'name'"))
    else:
        name = frontmatter['name']
        
        # Validate name format
        if not isinstance(name, str):
            errors.append(ValidationError('error', "Field 'name' must be a string"))
        elif not name:
            errors.append(ValidationError('error', "Field 'name' cannot be empty"))
        elif len(name) > 40:
            errors.append(ValidationError('error', f"Field 'name' too long ({len(name)} chars, max 40)"))
        elif not re.match(r'^[a-z0-9-]+$', name):
            errors.append(ValidationError('error', "Field 'name' must use lowercase letters, digits, and hyphens only"))
        elif name.startswith('-') or name.endswith('-'):
            errors.append(ValidationError('error', "Field 'name' cannot start or end with hyphen"))
        elif '--' in name:
            errors.append(ValidationError('error', "Field 'name' cannot contain consecutive hyphens"))
    
    if 'description' not in frontmatter:
        errors.append(ValidationError('error', "Missing required field: 'description'"))
    else:
        desc = frontmatter['description']
        
        if not isinstance(desc, str):
            errors.append(ValidationError('error', "Field 'description' must be a string"))
        elif not desc or desc.strip() == '':
            errors.append(ValidationError('error', "Field 'description' cannot be empty"))
        elif len(desc) < 20:
            errors.append(ValidationError('warning', f"Field 'description' is very short ({len(desc)} chars). Include when to use this subagent."))
        elif '[TODO' in desc or 'TODO:' in desc:
            errors.append(ValidationError('warning', "Field 'description' contains TODO placeholder"))
    
    # Validate optional fields
    if 'tools' in frontmatter:
        tools = frontmatter['tools']
        
        if isinstance(tools, str):
            # Parse comma-separated tools
            tool_list = [t.strip() for t in tools.split(',')]
        elif isinstance(tools, list):
            tool_list = tools
        else:
            errors.append(ValidationError('error', "Field 'tools' must be a string or list"))
            tool_list = []
        
        # Check each tool
        for tool in tool_list:
            if tool not in AVAILABLE_TOOLS:
                errors.append(ValidationError('warning', f"Unknown tool: '{tool}'. Available: {', '.join(sorted(AVAILABLE_TOOLS))}"))
    
    if 'disallowedTools' in frontmatter:
        disallowed = frontmatter['disallowedTools']
        
        if isinstance(disallowed, str):
            tool_list = [t.strip() for t in disallowed.split(',')]
        elif isinstance(disallowed, list):
            tool_list = disallowed
        else:
            errors.append(ValidationError('error', "Field 'disallowedTools' must be a string or list"))
            tool_list = []
        
        for tool in tool_list:
            if tool not in AVAILABLE_TOOLS:
                errors.append(ValidationError('warning', f"Unknown disallowed tool: '{tool}'"))
    
    if 'model' in frontmatter:
        model = frontmatter['model']
        if not isinstance(model, str):
            errors.append(ValidationError('error', "Field 'model' must be a string"))
        elif model not in VALID_MODELS:
            errors.append(ValidationError('error', f"Invalid model: '{model}'. Valid: {', '.join(sorted(VALID_MODELS))}"))
    
    if 'permissionMode' in frontmatter:
        mode = frontmatter['permissionMode']
        if not isinstance(mode, str):
            errors.append(ValidationError('error', "Field 'permissionMode' must be a string"))
        elif mode not in VALID_PERMISSION_MODES:
            errors.append(ValidationError('error', f"Invalid permissionMode: '{mode}'. Valid: {', '.join(sorted(VALID_PERMISSION_MODES))}"))
    
    if 'skills' in frontmatter:
        skills = frontmatter['skills']
        if not isinstance(skills, list):
            errors.append(ValidationError('error', "Field 'skills' must be a list"))
        elif len(skills) == 0:
            errors.append(ValidationError('warning', "Field 'skills' is empty. Remove if not needed."))
    
    if 'hooks' in frontmatter:
        hooks = frontmatter['hooks']
        if not isinstance(hooks, dict):
            errors.append(ValidationError('error', "Field 'hooks' must be a dictionary"))
        else:
            valid_hook_events = {'PreToolUse', 'PostToolUse', 'Stop'}
            for event in hooks.keys():
                if event not in valid_hook_events:
                    errors.append(ValidationError('warning', f"Unknown hook event: '{event}'. Valid: {', '.join(sorted(valid_hook_events))}"))
    
    # Check for unknown fields
    known_fields = {
        'name', 'description', 'tools', 'disallowedTools', 'model',
        'permissionMode', 'skills', 'hooks'
    }
    for field in frontmatter.keys():
        if field not in known_fields:
            errors.append(ValidationError('warning', f"Unknown field in frontmatter: '{field}'"))


def validate_system_prompt(body, errors):
    """Validate the system prompt body."""
    
    if not body or body.strip() == '':
        errors.append(ValidationError('error', "System prompt (body after frontmatter) is empty"))
        return
    
    # Check for TODO placeholders
    if '[TODO' in body or 'TODO:' in body:
        errors.append(ValidationError('warning', "System prompt contains TODO placeholders"))
    
    # Check length
    if len(body) < 50:
        errors.append(ValidationError('warning', f"System prompt is very short ({len(body)} chars). Consider adding more guidance."))
    
    # Recommend structure elements
    has_role = any(phrase in body.lower() for phrase in ['you are', 'you\'re', 'acting as'])
    if not has_role:
        errors.append(ValidationError('warning', "Consider starting with role definition (e.g., 'You are a...')"))


def validate_file_structure(content, errors):
    """Validate overall file structure."""
    
    # Check for frontmatter delimiters
    if not content.startswith('---'):
        errors.append(ValidationError('error', "File must start with '---' (frontmatter delimiter)"))
        return None, None
    
    # Split frontmatter and body
    parts = content.split('---', 2)
    if len(parts) < 3:
        errors.append(ValidationError('error', "Missing closing '---' for frontmatter"))
        return None, None
    
    frontmatter_text = parts[1]
    body = parts[2].strip()
    
    # Parse YAML
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        if frontmatter is None:
            frontmatter = {}
    except yaml.YAMLError as e:
        errors.append(ValidationError('error', f"Invalid YAML in frontmatter: {e}"))
        return None, None
    
    return frontmatter, body


def validate_subagent(file_path):
    """
    Validate a subagent file.
    
    Returns:
        Tuple of (is_valid, errors)
    """
    errors = []
    
    # Check file exists
    path = Path(file_path)
    if not path.exists():
        errors.append(ValidationError('error', f"File not found: {file_path}"))
        return False, errors
    
    # Check file extension
    if path.suffix != '.md':
        errors.append(ValidationError('warning', f"Subagent file should have .md extension, found: {path.suffix}"))
    
    # Check filename matches convention
    filename = path.stem
    if not re.match(r'^[a-z0-9-]+$', filename):
        errors.append(ValidationError('warning', "Filename should use lowercase letters, digits, and hyphens only"))
    
    # Read file
    try:
        content = path.read_text()
    except Exception as e:
        errors.append(ValidationError('error', f"Cannot read file: {e}"))
        return False, errors
    
    # Validate structure
    frontmatter, body = validate_file_structure(content, errors)
    
    if frontmatter is None:
        return False, errors
    
    # Validate frontmatter
    validate_frontmatter(frontmatter, errors)
    
    # Check filename matches name field
    if 'name' in frontmatter and isinstance(frontmatter['name'], str):
        if frontmatter['name'] != filename:
            errors.append(ValidationError('warning', f"Filename '{filename}' doesn't match name field '{frontmatter['name']}'"))
    
    # Validate body
    validate_system_prompt(body, errors)
    
    # Determine if valid (no errors, only warnings allowed)
    has_errors = any(e.severity == 'error' for e in errors)
    
    return not has_errors, errors


def main():
    if len(sys.argv) < 2:
        print("Usage: validate_subagent.py <path-to-subagent.md>")
        print("\nExamples:")
        print("  validate_subagent.py .claude/agents/code-reviewer.md")
        print("  validate_subagent.py ~/.claude/agents/data-analyzer.md")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    print(f"🔍 Validating subagent: {file_path}")
    print()
    
    is_valid, errors = validate_subagent(file_path)
    
    if errors:
        for error in errors:
            print(error)
        print()
    
    if is_valid:
        if errors:
            print("✅ Subagent is valid (with warnings)")
        else:
            print("✅ Subagent is valid")
        sys.exit(0)
    else:
        print("❌ Subagent has errors and needs fixes")
        sys.exit(1)


if __name__ == "__main__":
    main()
