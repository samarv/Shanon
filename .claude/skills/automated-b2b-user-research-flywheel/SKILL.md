---
name: automated-b2b-user-research-flywheel
description: Systematize customer discovery by automating the sourcing and scheduling of research calls. Use this when you are starting a new discovery phase, feel disconnected from "raw" customer material, or need a steady stream of interviews without manual sourcing.
---

# Automated B2B User Research Flywheel

Product Managers often settle for "looking through bent glass"—consuming processed research reports or second-hand sales feedback. To build better products, you must have direct, high-frequency exposure to raw customer material. This flywheel automates the sourcing, outreach, and scheduling process to ensure your calendar is consistently populated with relevant user interviews with zero manual effort.

## The Automation Workflow

### 1. Identify Intent Signals
Use your existing sales and support tools to find high-intent customers who are already talking about the problems you are solving.
*   **Gong/Chorus:** Set up keyword alerts for specific terms (e.g., "Competitor Name," "Feature Request X," "Pain Point Y").
*   **Support/Slack:** Use integrations to push messages containing specific keywords from support tickets or customer Slack channels into a dedicated "Research Signals" channel.

### 2. Bridge the Signal to Outreach
Use an automation platform like Zapier to connect your signals to your outreach tool.
1.  **Trigger:** A new post in your Slack "Research Signals" channel or a new tagged call in Gong.
2.  **Action:** Extract the customer’s email address and name.
3.  **Filter:** Ensure the customer matches your Ideal Customer Profile (ICP) or has not been contacted in the last 30 days.
4.  **Send:** Push this data to a sequence tool (e.g., Customer.io, Apollo, or Outreach).

### 3. The "Self-Scheduling" Sequence
Create an automated email sequence that feels personal but requires no management.
*   **Template Logic:** Reference the specific context (e.g., "I saw you were chatting with our sales team about [Topic]").
*   **The Ask:** Ask for 20 minutes to learn about their workflow, not to sell.
*   **The Link:** Include a specific Calendly link dedicated solely to user research.

## Implementation Guide

### Tool Stack
*   **Sourcing:** Gong (Sales calls) or UserInterviews.com (B2B-specific recruitment).
*   **Automation:** Zapier or Make.
*   **Communication:** Customer.io or email sequences.
*   **Scheduling:** Calendly or SavvyCal.

### High-Conversion Email Template
```text
Subject: Feedback on [Topic/Feature]

Hi [Name],

I’m a Product Manager at [Company] focused on [Problem Area]. I noticed you recently mentioned [Specific Keyword/Pain Point] in a conversation with our team.

We are currently refining our roadmap for this area and I’d love to hear how you handle [Process] today. I’m not selling anything—I just want to ensure we build this the right way for users like you.

If you have 20 minutes this week, you can grab a time on my calendar here: [Calendly Link]

Best,
[Your Name]
```

## Examples

**Example 1: Competitor Displacement Research**
*   **Context:** You are building a migration tool for customers moving away from a legacy competitor.
*   **Signal:** Gong alert for the keyword "Competitor X" and "Frustrated."
*   **Application:** Zapier triggers an email to the customer 2 hours after the sales call ends.
*   **Output:** Three interviews booked per week with customers currently using the competitor’s product.

**Example 2: New Feature Discovery**
*   **Context:** You want to understand why users are struggling with a new "Reporting" module.
*   **Signal:** Slack alert for any support ticket tagged with "Reports" and "Help."
*   **Application:** Automated email asks the user if they'd be willing to screen-share their current reporting workflow.
*   **Output:** A steady stream of "job-to-be-done" interviews showing real-world usage of the reporting feature.

## Common Pitfalls

*   **Ignoring the Sales/Success Team:** If you automate outreach to their active accounts without warning, they may feel you are "stepping on their toes." Always create a shared Slack channel so they can see who is being contacted and "opt-out" specific sensitive accounts.
*   **Over-Filtering:** Don't make the automated criteria too narrow. It is better to have one "okay" interview than zero interviews because your filters were too aggressive.
*   **Stale Calendars:** Ensure your Calendly has specific "Research Blocks" that don't conflict with your internal deep-work time. If you don't keep the link updated, the automation will fail.
*   **Static Keywords:** Failing to update your Gong/Slack keywords as your focus shifts. Treat your signal keywords like a living roadmap.