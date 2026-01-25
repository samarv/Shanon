---
name: gtm-agent-engineering
description: Build and deploy internal AI agents to automate go-to-market workflows and extract deal insights. Use this skill when your sales team spends too much time on rote research/admin tasks, when you need to diagnose systemic deal losses, or when scaling your SDR function with limited headcount.
---

# GTM Agent Engineering

The GTM Engineering framework treats the sales process like a software product. By hiring or repurposing technical "Go-To-Market Engineers," you can build internal AI agents that automate repetitive prospecting and analyze deal transcripts to find the "bugs" in your sales process. This approach shifts human effort from 30% selling time to 70% selling time.

## 1. The GTM Engineering Profile
Hiring the right person is critical for building effective agents.
*   **Ideal Profile:** Technical Sales Engineers (SEs) or individuals with Computer Science degrees who have worked in sales.
*   **Key Advantage:** They understand the "art of the sale" (discovery, objection handling) but have the technical ability to encode that workflow into an agent.

## 2. Deploying the "Lead Agent" (Prospecting Automation)
Automate the top-of-funnel research and outreach that typically consumes SDR time.

### The Implementation Workflow
1.  **Shadow Top Performers:** Identify the 7–10 browser tabs your best SDR opens when researching a lead (LinkedIn, CRM, company website, financial reports).
2.  **Map the Logic:** Define the deterministic steps. If the company is a marketplace, the agent should mention "Product X"; if they are B2C, mention "Product Y."
3.  **Build the "Mad Libs" Template:** Create email templates where 80% is fixed and 20% is a "fill-in-the-blank" section populated by the AI agent’s research.
4.  **Human-in-the-Loop (HITL):** Initially, have the agent draft the response and a human perform the final QA and hit "Send."
5.  **Monitor KPIs:** Track Lead-to-Opportunity conversion rates. Once the agent matches human performance, reduce the human headcount per agent.

## 3. The "Deal-Bot" (Transcript & Sentiment Analysis)
Use agents to provide an objective layer of truth that humans often miss in CRM entries.

### Audit Lost Opportunities
Run an agent over Gong transcripts, Slack channels, and emails for all lost deals in a quarter.
*   **The Prompt:** "Identify the root cause of this loss. Ignore the AE's CRM notes. Look for silence from the buyer, missed mentions of competitors, or failure to reach an economic buyer."
*   **Outcome:** Use this to identify if "lost on price" was actually "lost on value demonstration."

### Real-Time Deal Coaching
Connect the agent to live Slack deal channels to provide proactive alerts.
*   **Signals to Trigger:** 
    *   "You are 50% through the sales process but haven't identified an economic buyer."
    *   "The prospect mentioned [Competitor Name] on the last call; send them the comparison guide for [Feature X]."
    *   "The prospect's sentiment shifted to negative when discussing implementation timelines."

## 4. The "GTM Sprint" (Process Debugging)
Treat sales objections and friction points like software bugs.
1.  **Weekly Huddle:** Review agent-generated insights from the week's calls.
2.  **Identify "Bugs":** Locate where prospects are consistently getting stuck or where AEs are failing to handle new objections.
3.  **Deploy Fixes:** Update the objection-handling guide, adjust the demo flow, or create new marketing content by the following week.

## Examples

**Example 1: Inbound Lead Qualification**
*   **Context:** A high-growth startup receives 500 inbound leads weekly.
*   **Input:** Lead website URL and "Contact Sales" form submission.
*   **Application:** The Lead Agent scrapes the site to identify the company's business model (e.g., e-commerce) and traffic volume (Crux score). It drafts a personalized email: "I noticed your site traffic is peaking on weekends; here is how our infrastructure handles auto-scaling for e-commerce."
*   **Output:** A qualified opportunity routed to an AE with a 50% faster response time than a human SDR.

**Example 2: Diagnosing "Lost on Price"**
*   **Context:** Leadership notices a 20% spike in deals marked "Lost on Price" in the CRM.
*   **Input:** Gong transcripts for the 50 lost deals.
*   **Application:** The Deal-Bot analyzes the calls and finds that in 40 of those deals, the salesperson never presented a Total Cost of Ownership (TCO) analysis to the Finance lead.
*   **Output:** A strategic pivot to mandate TCO training for all AEs, rather than lowering the product price.

## Common Pitfalls
*   **Automating Chaos:** Do not build an agent for a process that isn't already documented and working manually. You must have a "playbook" before you can have an agent.
*   **Removing Humans Too Early:** AI can hallucinate "vibe-based" research. Keep a human QA step until the "Acceptance Rate" of the agent's drafts exceeds 90%.
*   **Focusing on Features over Pain:** Agents (and founders) often default to talking about "the art of the possible." Ensure your agents are tuned to identify 80% of buyers' motivation: **risk reduction and pain avoidance.**