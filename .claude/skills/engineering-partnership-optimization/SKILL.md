---
name: engineering-partnership-optimization
description: Strategies to eliminate friction and build high-trust relationships between Product Managers and Engineers. Use this when starting a new project with a technical team, when engineering feels disconnected from the product vision, or when communication begins to feel like a "game of telephone."
---

Establishing a high-trust partnership with engineering is the difference between shipping a product that works and dealing with constant "over-engineering" or system rewrite requests. This skill focuses on increasing technical empathy, sharing credit, and involving engineers in the creative process to prevent the "creative outlet" trap where engineers build unnecessary technical complexity because they feel excluded from business decisions.

## The Partnership Framework

### 1. Eliminate the "Telephone" Protocol
Avoid acting as a bottleneck or a filter that adds no value. Being a "middleman" wastes time and introduces translation errors.
- **Identify the Level:** If a stakeholder asks a question requiring deep technical detail, do not try to relay the answer back and forth. 
- **Connect Directly:** Bring the engineer into the Slack channel or meeting briefly.
- **Provide Context, Not Just Tasks:** When connecting them, your job is to set the business context so the engineer knows *why* they are answering the question, then step back.
- **Trigger for Action:** If you find yourself saying "Let me get back to you" more than twice on the same technical topic, connect the parties directly.

### 2. Practice Technical Empathy
Engineers are annoyed when PMs act like details don't matter. Successful engineering is entirely about details.
- **Validate Complexity:** Even if you don't understand the specific code, acknowledge that the "small thing" might have massive architectural ramifications.
- **Ask Probing Questions:** Instead of "Why is this taking so long?", ask:
  - "What are the major technical challenges with implementing this?"
  - "Are there hidden dependencies in the old system that we haven't accounted for?"
  - "What part of this lift is the most fragile?"
- **Listen to the "Boring" Stuff:** Be patient when engineers explain details. It shows you value the craft, which builds the credit you'll need when you eventually have to ask for a shortcut.

### 3. Close the Creative Loop
When engineers are excluded from product ideation, they seek creative outlets elsewhere—often through over-engineering, picking "trendy" but unnecessary frameworks, or pushing for total system rewrites.
- **Involve Engineers Early:** Bring them into the "Why" and "What" phase, not just the "How."
- **Encourage Ideas:** Acknowledge that they may have better ways to solve the customer problem than the original spec.
- **The "Rewrite" Audit:** If engineers push for a rewrite, evaluate it against Camille Fournier's "Migration Trap" criteria:
  - Is the logic in the old system documented? (Usually no).
  - Have we accounted for the time to migrate users/data? (Usually underestimated).
  - Can we "uplift" one specific API instead of rebuilding the whole web framework?

### 4. Implement a Credit-Sharing Protocol
PMs are naturally the "front-facing" person for initiatives. Engineers often feel their "invisible" work is ignored.
- **Step Back:** In executive demos or company-wide announcements, let the engineer who built the feature do the talking.
- **Technical Glory:** Specifically call out the "technical lift" or the "scaling challenge" that was overcome, not just the user-facing benefit.
- **Avoid "I":** Use "The team built..." or "Engineering solved..." rather than "We shipped..." when talking to leadership.

## Common Pitfalls
- **Acting Threatened by Engineering Ideas:** Fearing that an engineer’s product idea undermines your role. Great PMs realize that better ideas from the team make the PM look better.
- **Dismissing "Legacy" Logic:** Assuming an old system is "just bad code." Most legacy systems contain thousands of unrecorded business rules; ignoring this leads to failed rewrites.
- **Defaulting to 1:1s for Everything:** Relying on private 1:1s to manage stakeholders rather than group transparency. This makes unhappy stakeholders feel isolated and makes you seem "whiny" when you try to relay feedback.
- **Premature Management:** Pushing high-performing IC engineers into management before they’ve hit "technical mastery" (typically 8-10 years of coding). This leads to anxious, hands-off managers who can’t effectively guide technical decisions.

## Examples

**Example 1: Managing a Technical Query**
*   **Context:** A Sales VP asks a PM about a specific database limitation regarding a high-value client's data.
*   **The "Annoying" Way:** The PM tries to explain it, gets the details wrong, goes back to the Lead Engineer, gets a 5-paragraph explanation, tries to summarize it, and confuses the Sales VP further.
*   **The Fournier Way:** The PM creates a temporary Slack channel: "Hey [Engineer], [Sales VP] has a question about the data constraints for Client X. I’ve briefed [Sales VP] on the business urgency. Could you explain the current architectural limit so we can find a path forward?"

**Example 2: Preventing the "Boredom" Rewrite**
*   **Context:** The engineering team is pushing to rewrite a 5-year-old billing module in a new language.
*   **The "Annoying" Way:** The PM says "No, we have no time, just build the new feature on top of the old one." (Engineer feels ignored and builds a "side project" framework that complicates the code).
*   **The Fournier Way:** The PM involves the Lead Engineer in a discovery session with the Finance team. They realize the real pain is a specific API’s latency. The PM says, "I hear you on the rewrite, but let’s focus on 'uplifting' just this one API path. It solves the Finance problem today and starts our path toward a modern system without a 12-month migration trap."