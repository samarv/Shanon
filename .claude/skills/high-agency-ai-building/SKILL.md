---
name: high-agency-ai-building
description: Leverage agentic IDEs to prototype, build, and refactor software. Use this skill when you need to build internal tools without dedicated engineering resources, when a PM wants to ship a functional PR instead of a mockup, or when refactoring complex logic across large codebases.
---

High-agency building shifts your role from a manual coder to an architect and reviewer. By using agentic IDEs, you bridge the gap between business intent and technical implementation, allowing non-engineers to build functional software and engineers to automate 90% of their output.

## The Agentic Building Workflow

### 1. Initialize with Context
Don't start from a blank slate. Provide the AI with the environment and visual constraints of your project.
*   **Start with Boilerplate:** Initialize a basic project (e.g., React, Python) and let the agent install dependencies.
*   **Visual Prompts:** Upload screenshots or sketches of your desired UI. The agent can translate image elements into functional components.
*   **Index the Codebase:** Ensure the tool has indexed your entire repository (even 100M+ line codebases) to understand local patterns and dependencies.

### 2. Issue Explicit Instructions
Treat the AI as a high-capacity intern. Being vague leads to irrelevant code changes.
*   **Be Ruthlessly Specific:** Instead of "make it look better," say "change the background of the hero section to #FF0000 and add a 'Book Now' button that links to /checkout."
*   **Start Small:** Do not ask for a directory-wide refactor in one go. Build one component or one function, verify it, and then expand.
*   **Use Point-and-Click:** Use the IDE’s previewer to select specific UI elements and issue commands directly against them (e.g., "Make this specific button retro-style").

### 3. Review and Refine
In an agentic world, your primary job is **Reviewing**. 
*   **Validate Intent:** Check if the agent’s "Plan" matches your goal before it starts writing files.
*   **Check Logic, Not Just Syntax:** The AI will get the syntax right, but you must ensure the business logic (e.g., the partner portal's permissions) is correct.
*   **Human-AI Collaboration:** If you don't like a variable name, change it manually in one file. A high-agency IDE will recognize your intent and offer to update that variable across the rest of the project automatically.

### 4. Deploy and Cannibalize
*   **Ship Internal Tools:** If a SaaS product doesn't exist or is too expensive for a niche need (e.g., a custom partner portal), build it yourself in a few hours.
*   **Iterate Every 6 Months:** Expect your tech stack or form factor to look "silly" within a year. Use the agent to completely refactor or rebuild the UI as your needs evolve.

## Examples

**Example 1: GTM Internal Tool**
*   **Context:** A Head of Partnerships needs a custom portal to track lead sharing because the current CRM is too clunky.
*   **Input:** A hand-drawn sketch of a table with "Partner Name," "Lead Status," and "Last Contact."
*   **Application:** Upload the sketch to the agentic IDE. Instruct: "Build a React app using this layout. Connect it to our existing Airtable API for the data source."
*   **Output:** A functional, private web app deployed internally, saving the company $15k/year in SaaS fees.

**Example 2: PM Feature Migration**
*   **Context:** A PM wants to rename a core metric from `conversion_rate` to `signup_efficiency` across the entire codebase to align with new branding.
*   **Input:** The production repository.
*   **Application:** Manually change the variable name in the main config file.
*   **Output:** The agent detects the change and prompts: "I noticed you changed this variable. Should I refactor all 42 instances across the backend and frontend?" The PM clicks "Apply" and creates a PR.

## Common Pitfalls

*   **The Kitchen Sink Request:** Asking the AI to "build an Airbnb clone" in one prompt. This leads to hallucinated dependencies. **Fix:** Build the landing page first, then the search bar, then the booking logic.
*   **Ignoring the Review Flow:** Accepting large code changes without reading the diff. **Fix:** Use the IDE's "Review Mode" to step through every file modification the agent made.
*   **Lack of "Dehydration":** Hiring a developer to build something that a high-agency PM could have built in an afternoon with AI. **Fix:** Only hire when the person is "underwater" and the task truly requires deep architectural problem-solving that AI cannot yet plan.
*   **Over-reliance on Frontier Models:** Assuming a general chat tool (like ChatGPT) is enough. **Fix:** Use a tool that has "Local Context" (indexing your specific files) to avoid sending billions of tokens to a cloud model.