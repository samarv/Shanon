```yaml
---
name: ai-accelerated-development-management
description: Adapt product development processes when AI writes 70-90% of the code. Use this when engineering is no longer the primary bottleneck, and delays have shifted to decision-making, alignment, and code merging.
---
```

# AI-Accelerated Development Management

When code generation is no longer the bottleneck, product development shifts from a "building" problem to a "direction and validation" problem. This framework helps you manage teams where AI (like Claude Code) handles the majority of the implementation, requiring a re-architecting of the traditional PM/Engineering/Design relationship.

## Identify and Solve the New Bottlenecks

In an AI-native environment, the "Critical Path" moves from implementation to the "upstream" (alignment) and "downstream" (merging) phases.

### 1. Upstream: The Alignment Bottleneck
When engineers can ship at 10x speed, they require faster decision-making to avoid "running in the wrong direction."
*   **Provide Minimum Viable Strategy:** Create just enough strategic clarity to empower teams to explore at the edge of model capabilities without waiting for 100% certainty.
*   **AI-Partnered Prototyping:** Move prototyping earlier. PMs and Designers should use AI to build functional demos (using tools like Claude Artifacts) to make requirements tangible before an engineer touches the production codebase.
*   **The "Roast Me" Strategy Check:** Before finalizing a PRD or roadmap, prompt the model: *"Be brutal. Roast this product strategy. Tell me exactly where my logic is weak or where I'm falling into standard industry groupthink."*

### 2. Implementation: The "Founding Engineer" Model
The most effective functional unit is no longer a large scrum team, but a "Founding Engineer" pair.
*   **The Pair:** One high-agency engineer with an idea, supported by the right design/product context.
*   **Language Agnosticism:** Encourage engineers to solve problems in the best language for the job, even if they don't know it. Use AI to bridge the syntax gap (e.g., a Python dev using Claude to submit a TypeScript PR).

### 3. Downstream: The Validation Bottleneck
Huge volumes of AI-generated code will break traditional human-only merge queues and PR reviews.
*   **AI-to-AI Reviews:** Stop doing line-by-line manual reviews for AI-generated code. Use a separate instance of the model to perform the initial code review.
*   **Shift to Acceptance Testing:** Humans should move away from reading lines of code and toward "Acceptance Testing"—validating the functional outcome and edge cases rather than the syntax.
*   **Re-architect the Merge Queue:** If your deployment system assumes a human cadence, it will fail. Automate the "air traffic control" of landing changes to handle the increased PR volume.

## Managing "Overhang" (Capability vs. Usage)
"Overhang" is the delta between what the AI can do and how your team/users are actually using it.
*   **Close the Skills Gap:** Identify tasks that take 6 hours (e.g., building a prototype, data mapping) and challenge the team to do them in 20 minutes via AI delegation.
*   **Identify Scriptable Primitives:** Look for UI features that should actually be "agentic." Instead of building a button for every action, expose your product primitives via a protocol (like MCP) so the AI can script the actions directly.

## Examples

**Example 1: The Upstream Shift**
*   **Context:** A PM is planning a new "Memory" feature but is worried about the engineering timeline.
*   **Application:** Instead of writing a 10-page doc, the PM uses Claude to build a functional React prototype of the memory interface in 30 minutes. 
*   **Output:** The PM shows the functional demo to the engineer, who uses Claude Code to translate that logic into the production repo in a single afternoon.

**Example 2: The Downstream Shift**
*   **Context:** An engineering team finds their PR queue has grown from 5 to 50 pending reviews because of AI speed.
*   **Application:** The team implements a "Tiered Review" system: Tier 1 is an automated Claude review for syntax/security; Tier 2 is a human verifying the feature works as intended in a preview environment.
*   **Output:** PR cycle time drops from 48 hours to 2 hours.

## Common Pitfalls
*   **The "Anodyne" Partner:** Don't let the AI be too nice. If you ask "What do you think of this plan?", it will be supportive. You must explicitly prompt for "brutal" or "critical" feedback to find strategic holes.
*   **Line-by-Line Obsession:** Trying to manually review every line of a 1,000-line AI-generated PR. This creates a massive bottleneck. Shift focus to output validation.
*   **Waiting for the "Right" Language:** Engineers avoiding a project because it's in a different stack. AI removes the "I don't know that language" excuse.
*   **Neglecting Human Empathy:** Assuming AI has "taste." While AI is great at code, humans must still intervene for UI taste, psychological nuances, and "comprehensibility."