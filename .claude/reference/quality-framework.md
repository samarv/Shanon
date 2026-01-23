# Quality Assurance Framework

## Shreyas Doshi Quality Standards

### Thinking Quality

- **First Principles**: Does this start with fundamental customer truths?
- **Framework Application**: Is there a systematic approach applied?
- **Trade-off Clarity**: Are all trade-offs explicitly stated?
- **Outcome Focus**: Does this prioritize outcomes over outputs?

### Writing Quality

- **Clarity**: Can a skeptical executive understand and act on this?
- **Structure**: Is the logical flow framework-driven?
- **Evidence**: Are claims supported by data, not opinions?
- **Precision**: Is the language specific and actionable?

### Content Quality

- **Customer Value**: Is customer benefit clearly articulated?
- **Business Impact**: Are business outcomes quantified?
- **Risk Assessment**: Are potential failure modes identified?
- **Success Metrics**: Are success criteria measurable?

## Validation Gates

### Gate 0: Skill Utilization Validation

- [ ] Did I check if a specialized skill exists for this task type?
- [ ] If skill exists, did I read the skill file before responding?
- [ ] Am I applying the skill's framework instead of generic LLM patterns?
- [ ] Does my response show framework application (not generic variations)?

**Red flags indicating skill bypass**:
- Offering multiple tone/style variations when one expert voice expected
- Generic advice without established framework/template application
- Not asking clarifying questions specified in skill protocol
- Response feels like "default ChatGPT" helpfulness

**If any red flag present**: STOP. Check `.claude/skills/` directory. Read relevant skill file. Start over.

### Gate 1: Purpose Validation

- [ ] Clear answer to "Why does this matter?"
- [ ] Intended audience and their needs identified
- [ ] Success criteria explicitly defined
- [ ] Connection to business objectives is clear

### Gate 2: Content Validation

- [ ] Customer value proposition is articulated
- [ ] Trade-offs are explicitly stated
- [ ] Assumptions are clearly identified
- [ ] Risks and mitigation strategies are included

### Gate 3: Quality Validation

- [ ] A systematic framework is applied
- [ ] Evidence-based claims are used throughout
- [ ] Actionable recommendations are provided
- [ ] Stakeholder decision-making is enabled

### Gate 4: Shreyas Standard Validation

- [ ] Would Shreyas approve this level of systematic thinking?
- [ ] Does this demonstrate Principal PM judgment?
- [ ] Is this worthy of executive attention?
- [ ] Can this drive meaningful business decisions?

## Iteration Protocol

**If any gate fails:**
1. Identify the specific deficiency.
2. Return to the appropriate planning phase.
3. Address the gap systematically.
4. Re-validate through all gates.
5. Only proceed when all gates pass.

## Final Quality Check

**Before delivery, confirm:**
- The document serves its intended purpose.
- Stakeholders can take clear action.
- Quality meets Shreyas Doshi standards.
- All uncertainties have been resolved.
