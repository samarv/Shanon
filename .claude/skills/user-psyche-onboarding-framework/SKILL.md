```yaml
---
name: user-psyche-onboarding-framework
description: Optimize product onboarding by identifying psychological blockers (the "bogeyman") and embedding intimidating tasks within familiar, high-value actions (the "hotdog" method). Use this when logical onboarding steps see high drop-off or when users face high-anxiety setup requirements.
---
```

The User Psyche Onboarding Framework shifts the focus from purely logical product flows to the emotional state of the user. It identifies where users feel "out of their depth" and uses "good friction" and strategic embedding to build confidence and drive conversion.

## Core Principles

### 1. Identify the "Bogeyman"
The "Bogeyman" is the specific task or concept that triggers a user's imposter syndrome or fear of failure (e.g., for developers at Twilio, it was "Telecom/Phone Configuration"). 
- **Identify it:** Use qualitative feedback to find the moment users feel they are "losing their footing."
- **Acknowledge it:** Recognize that users often expect new products to be difficult; your job is to prove them wrong immediately.

### 2. Distinguish Good Friction from Bad Friction
Not all friction is negative. 
- **Bad Friction:** Obstacles that provide no value to the user and only serve the company (e.g., complex password requirements).
- **Good Friction:** Steps that alleviate user anxiety by signaling the product "gets them" (e.g., asking for their coding language or specific use case).

### 3. Apply the "Pilling a Hotdog" Technique
When a user must complete a "scary" or complex task (the pill), do not make it Step 1. Embed it within a familiar, high-value environment (the hotdog).
- **The Hotdog:** A safe space, like documentation or a code editor, where the user feels competent.
- **The Pill:** The scary configuration or setup task hidden within that safe space.

## Implementation Workflow

### Step 1: Diagnose Psychological Drop-off
Look at your funnel data for "logical" steps that have unexpectedly high churn. 
- Conduct 5-10 user interviews specifically focused on their "headspace" during that step.
- Ask: "What did you think was going to happen when you clicked this?" and "What part of this felt like it wasn't for you?"

### Step 2: Implement "Good Friction" Questions
Insert 3-4 high-intent questions into the signup flow. 
- **The Questions:** Ask about their role, their primary programming language, or their specific goal.
- **The Psychological Goal:** Provide comfort by showing the product is tailoring itself to their specific expertise.
- **The Metric:** Watch for an *increase* in signup conversion, even though you added steps.

### Step 3: Embed the "Pill" (The Hotdog Method)
If a technical setup step is causing drop-off:
1. Identify the user's "Safe Place" (e.g., a documentation page or a demo environment).
2. Move the intimidating setup task *into* that environment.
3. Allow the user to interact with familiar elements (like code) before requiring the scary configuration.

### Step 4: Run "Embarrassing" MVPs
Validate psychological hypotheses using the "Embarrassment Metric."
- If the first iteration of your test isn't slightly embarrassing (e.g., manually kicking users to a docs page), you have over-invested.
- Prioritize speed of validation over polished UI for psychological tests.

## Examples

**Example 1: The "Good Friction" Signup**
- **Context:** A developer tool with a "minimalist" one-field signup has stagnant growth.
- **Input:** Insert a dropdown asking "What language do you code in?" (Python, JS, Ruby).
- **Application:** Users see their language and feel, "Okay, they support me."
- **Output:** A 5% increase in signup conversion because the "friction" provided psychological reassurance.

**Example 2: Pilling the Hotdog (The Twilio Method)**
- **Context:** Users drop off when asked to configure a phone number (The "Pill").
- **Input:** Move the configuration task into the API Documentation (The "Hotdog").
- **Application:** Instead of a standalone setup screen, the user sees a code block they understand. The phone number configuration is presented as a minor variable within that code block.
- **Output:** Higher completion rates because the user was in their "safe space" (code) while performing the scary task.

## Common Pitfalls

- **Over-Polishing the MVP:** Spending months building a custom onboarding flow before validating if the psychological blocker is real. *Fix: Use "painted door" tests or manual redirects to docs.*
- **Ignoring Qualitative "Whys":** Relying only on P-values without talking to users. *Fix: Corroborate quantitative anomalies with 1:1 user sessions to find the "Bogeyman."*
- **The 95% Confidence Trap:** Waiting for 95% statistical significance on every test. *Fix: In growth, accept lower confidence intervals (e.g., 80%) if it allows you to triple your experiment velocity, provided you harden the data with qualitative feedback.*
- **Assuming "Simple" is Always Better:** Removing questions that actually help users segment themselves. *Fix: Test adding intent-based questions to see if they improve downstream activation.*