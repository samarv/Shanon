---
name: high-context-prompt-engineering
description: Apply the "Context is All You Need" framework to transform generic AI outputs into high-fidelity, professional-grade results. Use this when drafting strategic documents (OKRs, PRDs), preparing for high-stakes meetings, or building custom GPTs.
---

# High-Context Prompt Engineering

Effective prompting is a human communication skill. Large Language Models (LLMs) are like high-intelligence peers with zero context; they eager to please but will provide generic "Crap In, Crap Out" responses if not properly grounded. This framework uses the "Context is All You Need" principle to maximize model performance.

## Core Principles

- **Context over Complexity:** The more specific details, examples, and background info you provide, the less "lazy" the model becomes.
- **The Human Peer Model:** Communicate with the AI as you would a brilliant but context-blind colleague. 
- **Nudge for Performance:** Small psychological or behavioral cues (e.g., "Take a breath") can marginally but significantly improve logic and tone.

## The High-Context Prompting Workflow

### 1. Ground the Model with External Data
Don't assume the model has up-to-date or deep knowledge of specific individuals or niche topics. 
- **Feed the Source:** Provide links to blogs, Twitter threads, or documentation.
- **Upload Files:** Use the file upload feature to give the model the "truth" to reference.
- **Search First:** Instruct the model to "Browse with Bing" to gather recent context before answering.

### 2. Define a Specific Persona
Instruct the model to adopt a specific communication style or professional mindset to avoid the "Standard AI Voice."
- **Bad:** "Give me 10 interview questions for a PM."
- **Good:** "Generate 10 interview questions in the style of Tyler Cowen—pointed, original, and deeply researched based on this guest's specific career history."

### 3. Apply Behavioral Nudges
Use these documented "performance hacks" to improve output quality:
- **Chain of Thought:** Tell the model to "Take a break/breath and think step-by-step" before answering.
- **Emotional Priming:** Use a smiley face `:)` at the end of the prompt to encourage a more helpful and thorough tone.
- **Reward Stakes:** Frame the importance of the task (e.g., "This is critical for my quarterly review").

### 4. Use the "Inference over Action" Structure
For complex tasks like planning, don't just ask for the result. Ask the model to analyze the components:
- **Identify Stakeholders:** "Who are the cross-functional partners for this project?"
- **Define Success:** "What are the specific metrics we should track for this goal?"
- **Generate Timeline:** "Based on the scope, create a realistic 12-week roadmap."

## Examples

### Example 1: Executive Interview Prep
**Context:** Preparing for a podcast interview with a tech leader.
**Input:** "I am interviewing Logan Kilpatrick from OpenAI. Here is a link to his recent blog posts and his Twitter feed. Based on these sources, identify his 3 most controversial opinions. Then, write 5 interview questions in the style of Tyler Cowen that challenge those specific views."
**Output:** A list of highly specific, non-obvious questions that move beyond "tell me about your job."

### Example 2: Quarterly Planning GPT
**Context:** Setting team OKRs for the next half.
**Input:** "Act as a Chief of Staff. I am going to provide my high-level goals. Your task is to force me to be rigorous. For every goal I provide: 1. Generate a timeline. 2. Identify 3 metrics for success. 3. List 5 cross-functional stakeholders who need to be informed. 4. Critique the goal for being too vague. :) "
**Output:** A structured planning session that prevents common "lazy" goal-setting mistakes.

## Common Pitfalls to Avoid

- **The "Blank Slate" Trap:** Expecting a great result from a one-sentence prompt. If the prompt is short, the answer will be generic.
- **Assuming Internal Knowledge:** Thinking the model knows your company's "voice" or your specific project history. You must provide the "voice" in the instructions.
- **Ignoring "Model Laziness":** If a model gives a truncated or lazy answer, it usually lacks sufficient grounding or was not told to "think step-by-step."
- **Over-Prompting for Simple Tasks:** Don't add 500 words of context for a simple grammar check. Match the context volume to the task complexity.