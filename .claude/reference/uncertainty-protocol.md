# Uncertainty Management Protocol

## Uncertainty Detection Triggers

**Stop and ask when uncertain about:**
- Whether a specialized skill exists for this task (check `.claude/skills/` first)
- Required information specified in skill file (if skill applies)
- Document purpose or intended audience
- Success criteria or quality standards
- Missing context or information
- Template requirements or structure
- Stakeholder expectations
- Business context or strategy
- Technical constraints or dependencies

## Question Escalation Framework

### Level 1: Clarification Questions

**Format**: "To create the most effective [document type], I need to understand: [specific question]?"

**Examples**:
- "What's the primary business objective this GTM strategy should achieve?"
- "Who is the intended audience for this product health review?"
- "What decision does this document need to enable?"

### Level 2: Context Questions

**Format**: "To ensure this aligns with your expectations: [specific context question]?"

**Examples**:
- "Should this strategy prioritize customer acquisition or retention?"
- "What's the timeline for implementing recommendations from this analysis?"
- "Are there specific competitive threats this should address?"

### Level 3: Validation Questions

**Format**: "Before I proceed, should I: [specific approach question]?"

**Examples**:
- "Should I create this as a detailed analysis or an executive summary?"
- "Do you want me to include technical implementation details?"
- "Should I focus on immediate actions or long-term strategy?"

## Pre-Response Skill Check

Before generating ANY content, verify:

1. **Skill Discovery Complete?**
   - Have I classified the task intent semantically?
   - Have I checked `.claude/skills/` for a matching skill?
   - If skill exists, have I read the SKILL.md file?

2. **Required Information Present?**
   - Does the skill file specify required inputs (channel type, audience, context)?
   - Are those inputs missing from the user query?
   - If missing, STOP and ask clarifying questions FIRST

3. **Framework Application Ready?**
   - Do I know which framework/template to apply?
   - Am I clear on the voice profile or style requirements?
   - Do I understand the quality standards?

**No-Generation Rule**: Never generate content if:
- A relevant skill exists but hasn't been read
- Skill-specified required context is missing
- Multiple valid approaches exist without user guidance
- You're about to offer "multiple variations" instead of one expert answer

## Question Asking Protocol

1. **Identify** the specific uncertainty.
2. **Categorize** the question type (clarification/context/validation).
3. **Formulate** ONE focused question.
4. **Wait** for the human response.
5. **Incorporate** the response into planning.
6. **Continue** with the updated context.

## Uncertainty Prevention

**Proactive Context Gathering**:
- Always ask about the document purpose upfront.
- Clarify audience and success criteria early.
- Validate assumptions before deep work.
- Check template requirements before starting.

**Documentation**:
- Record all clarifications received.
- Update working assumptions.
- Note context for future reference.
