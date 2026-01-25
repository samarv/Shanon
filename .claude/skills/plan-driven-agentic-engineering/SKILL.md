---
name: plan-driven-agentic-engineering
description: A workflow for collaborating with AI coding agents (like Codex) on complex, multi-step software tasks. Use this when porting features between platforms, building rapid prototypes ("vibe coding"), or resolving "gnarly" production bugs that require deep context.
---

# Plan-Driven Agentic Engineering

Traditional AI coding is often "prompt-to-patch"—asking for a single fix. This skill shifts the workflow to a "teammate" model, where the human and agent collaborate on a structured plan before execution to ensure the agent can handle long-running, complex tasks without drifting or losing context.

## The Workflow

### 1. Collaborative Planning (The plan.md Phase)
Before asking the agent to write a single line of production code, align on the logic.
- **Create a `plan.md` file:** Write out the intended changes in markdown within your IDE.
- **Context Loading:** Explicitly provide the agent with relevant files, API documentation, or existing patterns (e.g., "Look at the iOS implementation to plan the Android port").
- **Verifiable Steps:** Break the plan into a checklist. Each step should have a clear "Definition of Done" that the agent can eventually verify itself.
- **Iterate:** Ask the agent, "Given this plan, what am I missing?" or "What are the biggest risks in this architecture?"

### 2. Execution Loop
Once the plan is finalized, move into execution.
- **Delegation:** Point the agent to the `plan.md` and instruct it to execute a specific subset of tasks.
- **Sandbox Execution:** Allow the agent to run code, tests, and shell commands within a sandbox to validate its own work as it goes.
- **Compaction:** If the task is long-running (exceeding the context window), instruct the agent to "summarize the current state and remaining tasks into a fresh context" to maintain focus.

### 3. Mixed-Initiative Validation
The bottleneck of AI coding is often the human review. Shift the burden of proof to the agent.
- **AI-Led Verification:** Prompt the agent to "Write a test suite that proves your fix works" or "Verify your changes against these three edge cases."
- **Visual Previews:** For UI work, prioritize reviewing the image/preview output before diving into the code diff.
- **Catching Configuration Errors:** Use the agent to review infrastructure-as-code or configuration files specifically for "interesting mistakes" that humans often overlook in large PRs.

## Strategic Applications

### Vibe Coding (Rapid Prototyping)
Use the agent to build "throwaway" code to test an idea.
- **The Pattern:** Instead of writing a spec, ask the agent to "Build an interactive data viewer for this raw JSON" or "Vibe code a prototype of this animation in a standalone React file."
- **Goal:** Move from "talking about it" to "playing with it" in minutes.

### Feature Porting
The most efficient way to scale across platforms (e.g., iOS to Android).
- **The Input:** Feed the agent the source code of the finished platform.
- **The Prompt:** "Analyze this iOS Swift implementation. Create a plan to port this to Kotlin, maintaining the same state management logic and UI flow."

## Examples

**Example 1: Solving a "Gnarly" Production Bug**
- **Context:** A race condition in a high-traffic microservice that is difficult to replicate locally.
- **Input:** Provide the agent with the relevant service files, a recent stack trace, and Datadog logs.
- **Application:** 
    1. Ask the agent to analyze the logs and propose 3 potential causes in `plan.md`.
    2. Instruct the agent to write a stress-test script to attempt to reproduce the failure in the sandbox.
    3. Once reproduced, ask for a patch and a verification test.
- **Output:** A verified patch and a new regression test.

**Example 2: The Sora App "Port" Pattern**
- **Context:** Building an Android version of an existing, complex iOS app with only 2 engineers.
- **Input:** iOS repository and Android project scaffold.
- **Application:**
    1. Agent reads iOS source to understand business logic and API endpoints.
    2. Agent generates a 10-day roadmap of Kotlin tasks.
    3. Engineers use the agent to "translate" views while they focus on platform-specific performance tuning.
- **Output:** A GA-ready Android app in under 30 days.

## Common Pitfalls
- **The "Fresh Computer" Trap:** Giving an agent a task without the necessary passwords, API keys, or environment dependencies. Treat the agent like an intern: if they don't have the environment set up, they can't work.
- **Ignoring the Review Bottleneck:** Spending 5 minutes writing code with AI but 60 minutes reviewing it. Instead, instruct the agent to "Explain this diff to me like I'm a senior reviewer and highlight potential side effects."
- **Over-relying on Prompting:** If a task fails, don't just re-prompt. Check if the agent needs a better "harness" (e.g., a better test runner or access to a specific documentation site).
- **Dumb Tasks Only:** Using AI for only "easy" tasks. The highest value is found in giving the agent your "hardest problems" and collaborating on the plan.