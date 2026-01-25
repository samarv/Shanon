---
name: compounding-engineering-with-ai
description: A workflow for increasing team leverage by automating repetitive tasks and codifying professional "taste" into reusable AI agents. Use this when you find yourself repeating instructions, writing similar documents, or performing routine code/copy reviews.
---

# Compounding Engineering with AI

Compounding engineering is the practice of ensuring that every unit of work performed makes the next unit of work easier. Instead of just completing a task, you build a "simulation" of your decision-making process into an AI agent, creating permanent operational leverage for the team.

## The Compounding Workflow

### 1. Identify the "Broken Record" Tasks
Look for any task where a senior team member or manager is repeating themselves. Use the "CEO Benchmark": if you have to say the same thing in a meeting twice, it should be codified into a prompt.
- Common triggers: Headline feedback, copy editing for style, PRD formatting, or code style reviews.

### 2. Codify Your "Taste"
AI models like Claude 3.5 Sonnet or Opus 4 can now act as "judges" of quality if given the right context.
- **Record and Transcribe:** Record your verbal feedback to a teammate using tools like Granola or Otter.
- **Extract Principles:** Feed the transcript into an LLM and ask: "Based on this feedback, what are my core principles for [Subject]?"
- **Create the Style Guide:** Turn those principles into a specific "System Prompt" that the AI can use to evaluate future work.

### 3. Build the "Simulation of Self" Agent
Create a standalone tool or prompt that others must use *before* they come to you for review.
- **Input:** Raw drafts or "rambling thoughts."
- **Processing:** The AI applies your codified taste/style guide.
- **Output:** A refined version that meets 80% of your requirements.
- **Refinement:** If the output is wrong, don't just fix it manually. Update the prompt/style guide so the mistake never happens again.

### 4. Implement Technical Speed-ups
For engineering or product teams, move beyond one-off chats into shared automation.
- **Prompt Repositories:** Store all high-value prompts in a shared GitHub repository or internal tool (e.g., Every uses a library of "Slash Commands" in Claude Code).
- **PRD Generators:** Build a prompt that takes raw audio or messy notes and outputs a perfectly formatted PRD based on your team's specific template.
- **Automated Reviewers:** Set up agents (like "Charlie" or "Friday") to live in your GitHub or Slack and automatically flag deviations from your team's specific standards.

## Examples

**Example 1: Editorial Style Automation**
- **Context:** An Editor-in-Chief spends 2 hours daily fixing "punchiness" and tone in newsletters.
- **Application:** The Editor records 30 minutes of live feedback sessions. An AI Ops lead transforms this into an "Every Style Guide" prompt. 
- **Output:** A "Copy-Editor Agent" that writers run their drafts through. The Editor now only reviews the final 10% of nuance, saving 90 minutes a day.

**Example 2: The "Rambling to PRD" Loop**
- **Context:** A Product Manager has great ideas but struggles to spend hours writing formal PRDs.
- **Application:** The PM records a 5-minute "brain dump" into a voice recorder. They feed this into a "Compounding PRD" prompt that knows their specific technical stack and formatting preferences.
- **Output:** A high-fidelity PRD ready for an AI Coder (like Claude Code) to begin implementation immediately.

## Common Pitfalls

- **The Behavioral Gap:** Building the tool is easy; getting the team to use it is hard. You must make the AI-agent step a mandatory part of the workflow (e.g., "Don't send me a draft until the Style Agent has seen it").
- **Static Prompts:** Treating a prompt like a "set it and forget it" tool. Prompts need "context engineering"—regularly updating them with new examples of "Good" vs "Bad" outputs.
- **Manual Fixing:** Correcting an AI's mistake yourself instead of fixing the prompt. This kills the compounding effect. Always "fix the factory, not the product."
- **Over-specialization:** Hiring for narrow roles. In an allocation economy, you need generalists who can manage multiple agents across different domains (coding, writing, research).