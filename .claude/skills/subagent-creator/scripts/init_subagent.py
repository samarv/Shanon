#!/usr/bin/env python3
"""
Subagent Initializer - Creates a new subagent from template

Usage:
    init_subagent.py <subagent-name> --scope <project|user>

Examples:
    init_subagent.py code-reviewer --scope project
    init_subagent.py data-analyzer --scope user
"""

import sys
from pathlib import Path
import os


SUBAGENT_TEMPLATE = """---
name: {subagent_name}
description: TODO - Clear description of what this subagent does and when Claude should delegate to it. Include specific scenarios, task types, or triggers.
# tools: Read, Grep, Glob  # Uncomment and customize, or remove to inherit all tools
model: inherit
---

# System Prompt for {subagent_title}

[TODO: Write clear instructions for what this subagent should do when invoked.

Key guidelines:
- Be specific about the subagent's task and approach
- Provide step-by-step workflows if applicable
- Include any domain expertise or special knowledge
- Specify output format or reporting style
- Keep it focused on one primary responsibility

Example structure:

You are a [role] specializing in [domain].

When invoked:
1. [First step]
2. [Second step]
3. [Third step]

Key practices:
- [Practice 1]
- [Practice 2]
- [Practice 3]

For each [task]:
- [Deliverable 1]
- [Deliverable 2]
- [Deliverable 3]

Focus on [primary goal].
]
"""


def title_case_name(name):
    """Convert hyphenated name to Title Case for display."""
    return ' '.join(word.capitalize() for word in name.split('-'))


def validate_name(name):
    """Validate subagent name follows conventions."""
    if not name:
        return False, "Subagent name cannot be empty"
    
    if len(name) > 40:
        return False, "Subagent name must be 40 characters or less"
    
    if not all(c.islower() or c.isdigit() or c == '-' for c in name):
        return False, "Subagent name must use lowercase letters, digits, and hyphens only"
    
    if name.startswith('-') or name.endswith('-'):
        return False, "Subagent name cannot start or end with a hyphen"
    
    if '--' in name:
        return False, "Subagent name cannot contain consecutive hyphens"
    
    return True, ""


def get_output_path(subagent_name, scope):
    """Determine output path based on scope."""
    if scope == 'project':
        # Get current working directory and look for .claude/agents/
        cwd = Path.cwd()
        agents_dir = cwd / '.claude' / 'agents'
        
        # If we're not in a project root, try to find it
        if not agents_dir.exists():
            # Check if we're in a subdirectory of a project
            for parent in cwd.parents:
                potential_agents = parent / '.claude' / 'agents'
                if potential_agents.exists():
                    agents_dir = potential_agents
                    break
        
        return agents_dir / f"{subagent_name}.md"
    
    elif scope == 'user':
        # User-level subagent in home directory
        home = Path.home()
        agents_dir = home / '.claude' / 'agents'
        return agents_dir / f"{subagent_name}.md"
    
    else:
        return None


def init_subagent(subagent_name, scope):
    """
    Initialize a new subagent from template.

    Args:
        subagent_name: Name of the subagent
        scope: Where to create it ('project' or 'user')

    Returns:
        Path to created subagent file, or None if error
    """
    # Validate name
    valid, error = validate_name(subagent_name)
    if not valid:
        print(f"❌ Error: {error}")
        return None
    
    # Determine output path
    output_path = get_output_path(subagent_name, scope)
    if output_path is None:
        print(f"❌ Error: Invalid scope '{scope}'. Must be 'project' or 'user'")
        return None
    
    # Create parent directory if needed
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Check if file already exists
    if output_path.exists():
        print(f"❌ Error: Subagent already exists: {output_path}")
        return None
    
    # Generate content from template
    subagent_title = title_case_name(subagent_name)
    content = SUBAGENT_TEMPLATE.format(
        subagent_name=subagent_name,
        subagent_title=subagent_title
    )
    
    # Write file
    try:
        output_path.write_text(content)
        print(f"✅ Created subagent: {output_path}")
    except Exception as e:
        print(f"❌ Error creating file: {e}")
        return None
    
    # Print next steps
    print(f"\n✅ Subagent '{subagent_name}' initialized successfully")
    print(f"   Location: {output_path}")
    print(f"   Scope: {scope}-level")
    print("\nNext steps:")
    print("1. Edit the file to complete the TODO items")
    print("2. Update the description field to clearly describe when to use this subagent")
    print("3. Configure tools (specify allowed tools or remove to inherit all)")
    print("4. Write the system prompt with clear instructions")
    print("5. Test using: 'Use the <subagent-name> subagent to...'")
    print("\nOptional:")
    print("- Run validate_subagent.py to check the configuration")
    print("- Use /agents command to manage and edit interactively")
    
    return output_path


def main():
    if len(sys.argv) < 4 or sys.argv[2] != '--scope':
        print("Usage: init_subagent.py <subagent-name> --scope <project|user>")
        print("\nSubagent name requirements:")
        print("  - Hyphen-case identifier (e.g., 'code-reviewer')")
        print("  - Lowercase letters, digits, and hyphens only")
        print("  - Max 40 characters")
        print("  - Must match the 'name' field in frontmatter")
        print("\nScope options:")
        print("  - project: Saved to .claude/agents/ in current project")
        print("  - user: Saved to ~/.claude/agents/ (available in all projects)")
        print("\nExamples:")
        print("  init_subagent.py code-reviewer --scope project")
        print("  init_subagent.py data-analyzer --scope user")
        sys.exit(1)
    
    subagent_name = sys.argv[1]
    scope = sys.argv[3]
    
    print(f"🚀 Initializing subagent: {subagent_name}")
    print(f"   Scope: {scope}")
    print()
    
    result = init_subagent(subagent_name, scope)
    
    if result:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
