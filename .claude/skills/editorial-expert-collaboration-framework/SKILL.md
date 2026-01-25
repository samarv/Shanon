---
name: editorial-expert-collaboration-framework
description: A system of four recurring touchpoints to align product teams with high-pressure expert stakeholders (like journalists, traders, or surgeons). Use this when building internal tools for power users, migrating users to a new platform, or operating in environments where "breaking news" or emergencies frequently disrupt roadmaps.
---

# Editorial-Expert Collaboration Framework

In high-stakes environments, standard user interviews often fail because stakeholders are too busy or reactive to provide structured feedback. This framework, developed at CNN, uses four specific interaction models to build trust, earn respect, and ensure technical tools survive "stress tests" in real-world chaos.

## The Four Essential Touchpoints

### 1. Weekly Demo Days (Evangelism)
Open forums led by the Product, Design, and Tech leads. 
- **Format:** 30–60 minute show-and-tell.
- **Goal:** Smart repetition. Preview upcoming features, recreate current workflows, and evangelize the product to the broader business.
- **Key Metric:** Awareness and excitement across the organization.

### 2. Deep-Dive Working Sessions (Collaborative Feedback)
Move away from "User Testing" (which feels like a chore) to "Working Sessions" (which feels like a partnership).
- **Format:** 2-hour sessions with small breakout groups (3–6 sessions per onboarding cycle).
- **Activity:** Real-time recreation of specific workflows (e.g., how a Politics reporter posts vs. a Health reporter).
- **Outcome:** Identification of specific friction points and immediate "Why" discovery.

### 3. Breaking News Dress Rehearsals (Stress Testing)
Simulate a "worst-case scenario" to see if the tool holds up under maximum cognitive load.
- **The Script:** Create a minute-by-minute script of an emergency (e.g., an email alert from news-gathering leads to a video upload, then photo selection, then headline publishing).
- **The Run:** Execute the script in the platform with engineers and support teams observing.
- **Goal:** Identify breaks in the process that only appear when speed is the only priority. If it can't handle a three-minute emergency, the feature is "useless."

### 4. Accessible Office Hours (Troubleshooting)
Open blocks of time for ad-hoc support.
- **Frequency:** 1–2 times per week.
- **Team:** PM, Design, and Tech leads must be present.
- **Value:** Lowers the barrier for feedback. It allows users to vent about minor frustrations that they wouldn't normally report in a formal ticket.

## Implementation Principles

### Speak the Language of the Listener
Avoid technical jargon like "API latency" or "CMS infrastructure." Adopt the lingo of your users. At CNN, this means using the nicknames and shortcuts journalists use for their stories and desks.

### The Tech Lead is a Discovery Partner
Engineers should not be "resources" who receive tickets; they are partners in discovery.
- Bring the Tech Lead to Working Sessions and Dress Rehearsals.
- When engineers see a journalist struggle to publish a story in a crisis, they develop a higher degree of clarity on *why* a feature needs to be built, leading to better technical feasibility decisions.

### Build in "Chaos Buffers"
When working with expert users, prioritize their mission over your research. 
- Always have a "Plan B" for research sessions.
- Build buffers into your roadmap (days or weeks) specifically for when "breaking news" pulls your stakeholders away.

---

**Example 1: Internal Platform Migration**
*   **Context:** Moving 500+ editors from a legacy CMS to a new, faster platform.
*   **Input:** Existing workflows for the "Home Page" team.
*   **Application:** Conduct three **Working Sessions** to map exactly how they curate headlines. Follow up with a **Dress Rehearsal** simulating a major election night to ensure the new "Publish" button doesn't lag under high traffic.
*   **Output:** A validated, high-trust onboarding process where editors feel the new tool was "built for them," not "imposed on them."

**Example 2: Fintech Trading Tool Update**
*   **Context:** Introducing a new risk-assessment dashboard for high-frequency traders.
*   **Input:** Traders' need for split-second execution.
*   **Application:** Host **Office Hours** specifically during market close when traders are winding down. Perform a **Dress Rehearsal** simulating a flash crash to see if the UI remains readable when every alert is firing simultaneously.
*   **Output:** Discovery that the color-coding system was too distracting during high-volatility events, leading to a "High Contrast" emergency mode.

---

## Common Pitfalls

- **Ignoring the "Pause":** Reacting immediately to a stakeholder's frustration. Instead, practice *equanimity*—pause, listen to the vent, and extract the root cause of the friction without becoming defensive.
- **Calling it "User Testing":** Experts often feel they are being tested rather than helped. Labeling sessions as "Working Sessions" changes the power dynamic to a collaborative partnership.
- **PM-Only Discovery:** Excluding engineers from live observations. This results in "broken telephone" where the PM tries to explain the user's pain, but the engineer doesn't feel the urgency of the fix.
- **Over-Scheduling Experts:** Forgetting that their primary job (e.g., reporting news) is more important than your product feedback. Lack of "chaos buffers" in your project plan will lead to missed deadlines.