---
name: logic-design-engineering
description: Transition from manual code syntax writing to high-level intent specification. Use this when building software with AI-native tools (like Cursor), managing AI-generated codebases, or shifting an engineering team's focus from "how to write" to "what to build."
---

# Logic Design and Intent-Based Engineering

The "world after code" shifts the role of the engineer from a syntax writer to a "logic designer." Instead of painstakingly laying out symbols for a computer to execute, the engineer specifies intent, defines high-level logic, and applies "taste" to ensure the software works and looks exactly as intended.

## Core Principles

### 1. Shift from "How" to "What"
In traditional engineering, "carefulness" (syntax accuracy, boilerplate management) is the primary skill. In logic design, "taste" is the primary skill.
- **Define Logic:** Focus on the step-by-step behavior of the software in human-readable or pseudocode terms.
- **Set the Vibe:** Move beyond visual UI/UX to "logic taste"—the ability to correctly identify which features should exist and how they should interact.

### 2. High-Control Iteration
Avoid the "Chatbot Trap" (typing a vague prompt and hoping for the best). Maintain the driver's seat by using a "High-Frequency Loop":
- **Gesture and Point:** Use tools that allow you to point at specific lines or files to make precise changes.
- **Fast Duration Loops:** Do not wait for an agent to spend weeks in the background. Aim for changes that occur in seconds so you can verify them immediately.

## The "Chop-and-Verify" Workflow

Michael Truell suggests that the most successful AI users avoid massive, single-prompt instructions. Instead, they use a "chopped up" approach:

1.  **Specify a Micro-Task:** Describe one small, logical change or a single component.
2.  **Generate and Review:** Let the AI write the code for that specific slice.
3.  **Validate:** Verify the logic immediately while the context is fresh.
4.  **Repeat:** Build the next layer of logic on top of the validated foundation.

## Application Guide: Discovering Limits

To effectively use AI for logic design, you must develop a "gut feeling" for what the model can handle.

### "Go for Broke" Stress Test
On a side project or safe environment, intentionally try to "fall on your face":
- **Push Complexity:** Give the model a task you think is too hard (e.g., refactoring a complex state machine across five files).
- **Observe the Breakpoint:** Note exactly where the AI hallucinates or loses track of logic. This defines your "scoping boundary" for professional work.

### Developing Logic Taste
- **Logic vs. UI:** Use Figma to spec visuals, but use high-level "intent descriptions" (pseudocode) to spec the logic.
- **Precision over Breadth:** If the AI's output is unwieldy, provide more "gestures"—specific file references or logic constraints—rather than just "more words."

## Examples

**Example 1: Refactoring a Data Flow**
- **Context:** You need to change how a user's subscription status is checked across an entire app.
- **Input (Traditional):** Manually finding 12 files and changing the `checkStatus()` function calls.
- **Application (Logic Design):** Point the AI to the `subscription-logic.ts` file. 
- **Intent Specification:** "I want to change the status check to be asynchronous and pull from our new Redis cache. Update all calling functions to handle the Promise, but keep the error-handling logic in the UI components the same."
- **Output:** The AI generates a multi-file diff that you review file-by-file for logic alignment.

**Example 2: Building a New Feature with "Chop-and-Verify"**
- **Context:** Building a "Dark Mode" toggle.
- **Step 1:** "Create a React context provider for Theme with 'light' and 'dark' states." (Verify output).
- **Step 2:** "Add a toggle button to the Header component that switches this state." (Verify output).
- **Step 3:** "Update the Tailwind config to enable dark mode based on the 'dark' class on the body." (Verify output).
- **Result:** A fully functional feature built in three small, verified pulses rather than one massive, error-prone prompt.

## Common Pitfalls

- **Wholesale Reliance:** (The Junior Pitfall) Accepting large blocks of AI code without understanding the underlying logic. This creates "unwieldy" apps that eventually become impossible to change because the creator doesn't know how they work.
- **Underestimating the Model:** (The Senior Pitfall) Sticking to manual workflows for boilerplate because you assume the AI won't "get" the complexity.
- **The "Vibe Coding" Trap:** Generating 1,000 lines of code at once. This removes your "High-Control" and makes debugging exponentially harder. Always "chop" the task.
- **Ignoring Model "Personalities":** Failing to realize that a new model (e.g., moving from GPT-4 to Claude 3.5 Sonnet) has different logic-design quirks. Re-run your "stress tests" whenever you switch models.