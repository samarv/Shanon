---
name: forward-deployed-iteration-loop
description: Rapidly solve complex enterprise problems by embedding technical talent directly into customer environments. Use this when launching high-stakes enterprise pilots, solving "messy" real-world data problems, or trying to bridge the gap between core product and custom customer needs.
---

# The Forward Deployed Iteration Loop

The Forward Deployed Engineer (FDE) model is designed to solve high-stakes, "messy" real-world problems by embedding builders directly with users. Instead of traditional "customer interviews," the goal is to live the customer's problems and execute 4-5 rapid iteration cycles per week to build software that achieves specific business outcomes (e.g., increasing factory production or finding fraud).

## The Weekly FDE Rhythm

Follow this specific schedule to maximize trust and iteration speed:

1.  **Monday (On-Site Integration):** Arrive at the customer's office. Get a desk inside their building. Attend their internal meetings. Identify the "burning problem" that the CEO or COO cares about most.
2.  **Monday Night (The Build):** Stay late to build a prototype or feature that addresses a specific pain point discovered during the day.
3.  **Tuesday (The Feedback Loop):** Show the build to the actual users (e.g., factory floor managers or analysts). Observe them using it.
4.  **Tuesday Night (The Iteration):** Refine the code based on the day's feedback.
5.  **Wednesday - Thursday:** Repeat the Cycle. By Thursday afternoon, you should have executed 4 full iterations before leaving the site.
6.  **Friday (Core Synthesis):** Return to the home office. Synthesize what you built into a generalizable product feature.

## The Murder Board Ritual

Before starting or pivoting a major project, conduct a "Murder Board" to stress-test the strategy:

1.  **Prepare the Doc:** Write a 2-page plan including the vision, goals, and specific tactics for the next three months.
2.  **Define Principles:** Include 2-3 principles that are *disagreeable*. (Avoid "Move Fast"; use something like "Prioritize data ingestion over UI polish").
3.  **Invite the Killers:** Bring in 3-4 smart peers who have no context on the project.
4.  **The Session:** Their sole job is to "tear apart" the plan, questioning every assumption, frame, and tactic. 
5.  **Outcome:** Refine the plan based on the holes they poked, or abandon the project if the core logic fails.

## Mapping the "Ontology" (Alien to Human)

Large organizations often store data in "alien language" (e.g., SAP table `S3_F1_Z`). Your job is to translate these into a human-legible "Ontology":

1.  **Identify the Core Concepts:** What are the 3-5 things the business actually talks about? (e.g., "Aircraft," "Part," "Work Order," "Oil Well").
2.  **Extract and Join:** Pull the raw, messy tables from the client's disparate systems.
3.  **Map to Humans:** Create a layer where the user can query "Where is Aircraft 79?" instead of joining 15 tables with cryptic names.
4.  **Build UI on Top:** Only build UI once the data mapping (the "Ontology") reflects the real-world operation.

## Examples

**Example 1: Manufacturing Production**
*   **Context:** A plane manufacturer needs to ramp up production from 4 to 16 planes per month.
*   **Application:** The FDE embeds in the factory, identifies that "work order carryover" is the bottleneck. They map the SAP data for "parts" and "stations" into a unified dashboard.
*   **Output:** A "Project Management" tool (similar to Asana for planes) that allows station managers to see exactly what work is remaining and where the parts are physically located.

**Example 2: Public Health Response**
*   **Context:** A government agency needs to coordinate vaccine distribution during a pandemic.
*   **Application:** The FDE sits with civil servants and clinicians. They build a data adapter that pulls real-time inventory from thousands of pharmacies into a single "Source of Truth."
*   **Output:** A supply chain visibility platform that allows the agency to reallocate doses based on daily demand spikes.

## Common Pitfalls

*   **Acting as a "Solutions Architect":** FDEs must be empowered to write code and ship new products. If the person is only "listening" and "architecting" without building, the loop breaks.
*   **Solving the Wrong Problem:** Customers often ask for "better data infrastructure." Usually, they actually need a specific business outcome (e.g., "lower wait times"). Always anchor to the outcome, not the tech stack.
*   **Remote Disconnection:** Trust is built over dinners and shared desks. Attempting this model via Zoom loses the "vibe check" and the ability to see the non-verbal frustrations of the users.
*   **Generic Principles:** Using principles like "Move Fast" during a Murder Board. If no one can reasonably disagree with your principle, it isn't a principle; it's a platitude.