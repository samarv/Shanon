---
name: growth-impact-and-learning-reviews
description: A structured ceremony for growth teams to socialize experiment results and data insights. Use this when growth findings are staying siloed, when teams are focusing on shipping rather than learning, or when you need to align cross-functional stakeholders on growth strategy.
---

The Impact and Learning Review is a recurring ceremony designed to shift a growth team's focus from "what we shipped" to "what we learned and how it changes our strategy." It treats learning as the primary output of experimentation to drive predictable impact.

## The Ceremony Structure

### 1. Team-Level Review (Weekly)
Run by the Product Manager or Experiment Lead, this 30–45 minute session focuses on the tactical results of the past week's activities.

*   **Preparation:** All team members (Eng, Design, Growth Marketing, Decision Science) document findings in a shared "Impact and Learnings" doc before the meeting.
*   **The Learning Log:** Discuss specific insights from data exploration, A/B tests, or user research. 
*   **The "So What":** For every learning, the team must identify the implication. Does this invalidate a current hypothesis? Should we double down on a specific channel?
*   **Metric Review:** Spend a small portion (approx. 20%) of the time on key KPIs to ensure the needle is moving.
*   **The Strict Rule:** **No Status Updates.** Do not spend time reviewing what people worked on. Focus exclusively on outcomes and insights.

### 2. Group-Level Review (Monthly)
Led by Directors, this meeting brings multiple growth teams together to share high-level strategic wins and failures.

*   **Cross-Pollination:** Share learnings that have utility for other teams (e.g., "We found that Node.js developers convert 2x better when shown a 'Fix' button vs. a 'Scan' button").
*   **Developer Insights:** Include a standing agenda item for the User Research team to share qualitative "Developer Insights."
*   **Visibility:** Record this session and share it with Sales, Marketing, and Core Product teams so they can leverage growth insights in their own roadmaps.

## Document Template
A simple document to facilitate the meeting should include:

| Section | Content |
| :--- | :--- |
| **The Learning** | What did the data/experiment/user tell us? (e.g., "Users drop off at the GitHub Auth step"). |
| **Evidence** | Link to the Amplitude chart, FullStory session, or research notes. |
| **Implication** | What will we do differently? (e.g., "We are pivoting to a CLI-first onboarding to bypass the Auth friction"). |
| **Metric Impact** | How did this affect the North Star or activation milestone? |

## Examples

**Example 1: SEO Sidecar Product**
*   **Context:** The growth marketer ran a test on a programmatically generated SEO page (Snyk Advisor).
*   **Learning:** Visitor traffic increased by 40%, but sign-up rates dipped by 5%.
*   **Implication:** The high-intent users are staying, but low-intent users are bouncing. The team decides to build a "Try without Sign-up" functional sidecar to capture more value from the high-intent traffic.
*   **Output:** Increased activation rates for the remaining sign-ups.

**Example 2: Activation Milestone Discovery**
*   **Context:** Decision Science analyzed long-term retention data.
*   **Learning:** Teams that fix their first vulnerability within 30 days are 3x more likely to be active 3 months later.
*   **Implication:** The team shifts focus from "Sign-ups" to "Time-to-first-fix."
*   **Output:** New onboarding flows that prioritize "Magic Fix" Pull Requests on GitHub immediately after account connection.

## Common Pitfalls
*   **Turning it into a Stand-up:** If you start talking about JIRA tickets or blockers, stop and redirect. This meeting is for *analyzing* results, not *managing* tasks.
*   **Hiding Failed Experiments:** Only sharing wins creates a "success theater." Failed experiments often provide the most valuable data on what *not* to build next.
*   **Lack of Actionable Implications:** A learning without a "So What" is trivia. Every documented insight must lead to a decision or a new hypothesis.
*   **Excluding Non-Product Stakeholders:** Growth insights (like why users churn or what triggers a purchase) are gold for Sales. Not socializing these broadly wastes the data's potential.