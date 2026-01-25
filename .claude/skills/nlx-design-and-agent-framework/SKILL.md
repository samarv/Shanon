---
name: nlx-design-and-agent-framework
description: Use this skill when designing natural language interfaces or defining autonomous agents. Use it to move beyond "black box" chat interfaces toward structured conversations that include editable plans, progress visibility, and multi-step autonomy.
---

# NLX Design and Agent Framework

In the AI era, Natural Language Interface (NLX) is the new UX. While traditional GUIs are rigid, NLX is elastic. However, a conversational interface is not a "no-design" zone; it requires a new set of invisible grammars, structures, and UI constructs to prevent the creation of "Frankenstein products."

## 1. Defining the Agent (The 3-Part Test)
When building an AI agent rather than a simple assistant, evaluate it against these three criteria:
*   **Autonomy:** Move from "human-in-the-driver's-seat" to delegation. It should operate on a spectrum of independence where you provide a goal, and the agent determines the path.
*   **Complexity:** The task must be multi-step and non-linear. If it is a "one-shot" task (e.g., "summarize this"), it is an assistant. If it is "build a prototype for this idea," it is an agent.
*   **Asynchronous Nature:** The agent should work when the user is not working. It should be able to join meetings, perform deep research, or execute background processes without constant human monitoring.

## 2. The NLX Design Construct
Treat natural language as a designed interface using these specific elements:
*   **The Prompt as the New PRD:** Use prompts to define the product’s logic and constraints. If you cannot prototype the behavior via a prompt set, the product is not yet defined.
*   **Editable Plans:** When a user provides a high-level goal, the agent should return a "Plan" construct. This plan must be visible and editable by the user before execution to build trust.
*   **Showing the Work (Thinking Aloud):** Design the "inference time" experience. 
    *   *Too verbose:* Feels like a technical script/cron job.
    *   *Too terse:* Creates a "black box" that reduces user confidence.
    *   *The Sweet Spot:* Provide enough breadcrumbs to show the agent is on the right path without overwhelming the user.
*   **Proactive Follow-ups:** Design the "happy path" by suggesting the next logical steps (e.g., if an image is generated, suggest "Make this high-resolution" or "Change the style to watercolor").

## 3. The "Frontier" Prototyping Workflow
Operationalize a "one-year-in-the-future" mindset by forcing the following workflow:
1.  **Demos Before Memos:** Never present a static document for a new AI feature. Present a live prototype or a prompt set.
2.  **The "WWXD" Test:** Use reasoning models to stress-test your strategy. (e.g., "What would [Target Stakeholder] think of this pitch? Identify the gaps in my persuasion.")
3.  **Solve Before Scale:** In the 0-to-1 phase, prioritize "the sound of the click" (qualitative delight) over traditional metrics like CTR or Retention, which are "grown-up metrics" that provide false precision early on.

## Examples

**Example 1: Designing a Research Agent**
*   **Context:** A PM needs to prepare for a leadership meeting regarding a roadmap change.
*   **Input:** "Research the public views and past internal statements of everyone in this meeting regarding AI agents."
*   **Application of NLX:** The agent provides an **Editable Plan**: "1. Identify attendees. 2. Scan internal docs for their project history. 3. Search public interviews. 4. Synthesize a persuasion pitch." The user edits step 4 to "Focus specifically on cost-efficiency."
*   **Output:** A structured briefing document with a "confidence score" on each insight.

**Example 2: Rapid Prototyping a New Feature**
*   **Context:** A designer wants to add a "Smart Budgeting" tool to a finance app.
*   **Input:** A prompt set that simulates the AI's logic for categorizing "messy" transactions.
*   **Application:** Instead of a Figma mock, the team builds a functional "Prompt-PRD" in a playground environment to see if the model can actually handle the reasoning required for edge-case transactions (e.g., "Venmo for rent" vs "Venmo for dinner").
*   **Output:** A functional demo that proves technical feasibility before any "bowels of the app" code is written.

## Common Pitfalls
*   **The Black Box Trap:** Assuming the "model eats the product" and therefore doesn't need UI. Conversations have grammar; if you don't design it, the user will feel lost.
*   **Stale Priors:** Relying on what AI couldn't do six months ago. The "baby grows up in a month"—always test the latest reasoning models before dismissing a feature as "impossible."
*   **Premature Scaling:** Moving to high-scale infrastructure before you have "Solved" the core user problem.
*   **The "Frankenstein" Product:** Allowing too many people to add AI "features" without a central "Tastemaker" or "Editor" role to maintain a cohesive product voice.