---
name: systematic-ai-eval-design
description: Design and implement high-fidelity evaluation sets (Evals) to measure AI model performance. Use this when transitioning an AI feature from prototype to "vibe-based" testing to a production-ready system, or when trying to optimize a model's performance on a specific professional task.
---

In the era of AI, the Eval is the new Product Requirement Document (PRD). To improve a model, you must first define exactly what success looks like through systematic, high-fidelity benchmarks that allow researchers and developers to run experiments and measure progress.

## The Core Principle: Evals as PRDs
If the model is the product, the Eval is the requirement. A good Eval allows you to move away from subjective "vibe checks" and toward a systematic way of measuring how AI automates your core value chain.

## Workflow: Building a High-Fidelity Eval

### 1. Identify the Core Value Chain
Focus on the specific task that provides the most economic value.
*   **Narrow the scope:** Instead of "legal advice," focus on "redlining a Series A term sheet."
*   **Define the persona:** Identify the exact professional level required to judge the task (e.g., a McKinsey analyst, a Senior Software Engineer, or a Radiologist).

### 2. Define the "Gold Standard" Rubric
Create a multidimensional scoring system that translates expert intuition into machine-readable criteria.
*   **Identify Critical Failures:** List "non-negotiables" (e.g., "The model must not hallucinate a clause that wasn't in the original document").
*   **Weight the Criteria:** Assign points for specific achievements (e.g., +2 for identifying a missing indemnification clause, +1 for tone consistency).
*   **Create Verifiers:** For technical tasks, use unit tests or hard logic. For creative/reasoning tasks, use qualitative rubrics that a high-skilled human (or a stronger "judge model") can apply.

### 3. Source Expert Labor for "Post-Training" Data
High-quality models require high-quality feedback.
*   **Avoid Crowdsourcing:** Do not use low-skilled labor for complex professional tasks. The model will only be as good as the person training it.
*   **Focus on the Top 10%:** Recruit experts who are currently "underemployed" (e.g., top-tier engineers at slow-moving companies) to provide the initial "ground truth" data.

### 4. Implement AI Feedback (RLAIF)
Once you have a human-defined rubric, use it to automate the feedback loop.
*   Use the rubric to reward the model for "good" trajectories and penalize "bad" ones.
*   Scale the evaluation by having a "Judge LLM" apply the human-written rubric to thousands of model outputs.

## Examples

**Example 1: Legal Contract Analysis**
*   **Context:** A legal-tech startup building an AI contract reviewer.
*   **Input:** 50 complex NDAs with hidden "toxic" clauses.
*   **Eval Application:**
    1.  **Expert Task:** Hire a lawyer to redline these documents perfectly.
    2.  **Rubric:** 1) Did it catch the 3 hidden clauses? 2) Is the tone professional? 3) Is the explanation legally sound?
    3.  **Measurement:** The model is scored 0-10 on each document based on the lawyer's "ground truth."
*   **Output:** A percentage score showing model accuracy, used to decide if the model is ready for deployment.

**Example 2: Coding Assistant for Proprietary API**
*   **Context:** An internal tool helping engineers use a company's private libraries.
*   **Input:** 100 coding prompts based on internal documentation.
*   **Eval Application:**
    1.  **Technical Verifier:** Write a unit test for each prompt that the code must pass.
    2.  **Expert Rubric:** A senior engineer reviews the code for "idiomatic" use of the private API.
    3.  **RLHF:** The model generates 3 versions of the code; the engineer selects the most "correct" version to reinforce that style.
*   **Output:** A leaderboard of different model versions (e.g., GPT-4o vs. a fine-tuned Llama) to see which follows internal standards best.

## Common Pitfalls to Avoid

*   **Saturating the Eval:** If the model hits 100% accuracy, the Eval is too easy. You must constantly "raise the ceiling" by adding more difficult, long-horizon reasoning tasks (e.g., moving from "write a function" to "build a feature across three files").
*   **Vibe-Based Decisions:** Never ship an AI update because "it feels better." Without a numeric Eval score, you risk regressing on edge cases you aren't currently looking at.
*   **Ignoring the "Leading Indicators":** In fast-moving markets, the best Eval is the one that measures the capabilities your wealthiest customers are currently desperate for, not just academic benchmarks like MMLU.
*   **Reward Hacking:** Be careful with rubrics; if you reward "length of explanation," the model will become wordy and unhelpful. Ensure rubrics reward the *outcome*, not the *formatting*.