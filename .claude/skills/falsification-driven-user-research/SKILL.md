---
name: falsification-driven-user-research
description: Shift user research from "performative validation" to strategic learning. Use this when you are tempted to ask for a "quick study to validate assumptions," when research feels like it's slowing down shipping, or when you need to understand the "why" behind an A/B test result.
---

# Falsification-Driven User Research

Traditional user research often falls into "user-centered performance"—the act of conducting studies to signal customer obsession without actually intending to change a decision. To drive real business impact, research must shift from seeking **validation** (looking for proof you are right) to **falsification** (actively looking to be proven wrong).

## The Three Altitudes of Research

Align your research requests to one of these three levels to avoid "middle-range" research that is interesting but un-actionable.

1.  **Macro Research:** Strategic, forward-looking, and business-focused. Use this for annual planning, identifying TAM (Total Addressable Market), or "concept car" projects looking 3-5 years out.
2.  **Micro Research:** Tactical, high-precision usability and optimization. Use this for A/B test "why" analysis, perfecting CTA language, or fixing specific friction points in a funnel.
3.  **Middle-Range Research (The "Danger Zone"):** General questions about "how users feel" that aren't pointed at a specific business problem. Avoid this unless it is explicitly tied to a conversion funnel or a specific strategic pivot.

## How to Move from Performance to Impact

### 1. Adopt the Falsification Mindset
Stop asking, "Can you validate this design?" instead ask, "What evidence would prove this approach is the wrong way to solve the user's problem?" 
- **Goal:** Expose blind spots and biases in your intuition.
- **Success Metric:** You shouldn't want to hold a decision-making meeting without your research partner present because their insights are critical to the "go/no-go" choice.

### 2. Connect Research to Profit
Researchers must speak the language of the business to be impactful.
- **Quarterly Alignment:** Read the latest quarterly report and shareholder calls. Align research questions with the current OKRs and conversion funnel.
- **Unified Metrics:** The PM, Designer, and Researcher should share the exact same metrics for success. Research is not a separate workstream; it is a component of the product's success.

### 3. Deploy the "Five Tools"
A high-impact researcher (or a PM doing their own research) should utilize these five technical tools:
- **Formative/Generative:** Ethnographic field work to find new opportunities.
- **Evaluative:** Rapid usability testing to find functional bugs.
- **Survey Design:** Rigorous, unbiased scaling of user feedback (prefer CSAT over NPS).
- **Applied Statistics:** Understanding significance in the context of A/B testing.
- **Data Querying:** Using SQL, dashboards, or AI prompting to pull your own behavioral data.

## Metrics to Use (And What to Avoid)
- **Use CSAT (Customer Satisfaction):** Ask "Overall, how satisfied are you with [Experience]?" It has better data properties and correlates more strongly with business outcomes.
- **Avoid NPS (Net Promoter Score):** The "likelihood to recommend" question is often irrelevant to the product (e.g., enterprise software) and the 11-point scale is statistically noisy and prone to formatting bias on mobile.

## Examples

**Example 1: Micro-Research (The Multi-Million Dollar Button)**
- **Context:** An Airbnb checkout button had low conversion. PMs suspected the UI was ugly.
- **Application:** Evaluative research showed users were *afraid* the button would charge them immediately.
- **Output:** Changed the text (7 characters) to clarify it was just the "next step." This drove a 1% lift in conversion, worth millions in revenue, in under 48 hours.

**Example 2: Falsifying Intuition (The "Super-Hider")**
- **Context:** Facebook engineers assumed that "hiding a post" was a signal of low quality. They planned to deprioritize all hidden posts.
- **Application:** Formative research (think-aloud study) observed a power user who hid *every* post she liked.
- **Output:** Researchers discovered she used "Hide" as an "Inbox Zero" marker. The team falsified the "Hide = Bad" assumption and saved the feed from a broken ranking algorithm.

## Common Pitfalls to Avoid

*   **Treating Research as a Service:** Calling a researcher at the end of a project to "bless" a design. This is 97% performance and 3% learning.
*   **Relying on "Post-hoc" Logic:** Saying "we knew that already" after a study. This is hindsight bias. Acknowledge that while it seems obvious now, you didn't have the conviction to act until the data arrived.
*   **The "Henry Ford" Trap:** Avoiding research because "users don't know what they want." Great researchers don't ask users what they want; they observe behavior to identify latent needs.
*   **A/B Test Speculation:** Seeing a stat-sig drop in a test and guessing why. Use a 48-hour qualitative study to get the "why" instead of running three more "guess-and-check" experiments.
*   **Biased Walkthroughs:** Dogfooding your own product and assuming your experience is universal. You are not the user; you lack their constraints, priorities, and technical limitations.