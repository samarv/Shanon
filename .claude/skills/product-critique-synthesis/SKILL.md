---
name: product-critique-synthesis
description: A framework for organizing and prioritizing design feedback during product reviews. Use this when a team is overwhelmed by "design by committee," when feedback is disorganized or contradictory, or when you need to align stakeholders on the most critical product improvements.
---

This framework, developed by Julie Zhuo, moves product reviews away from subjective "likes" and toward a hierarchy of user needs. It ensures that the team solves for core value before debating aesthetics or minor polish.

## The Hierarchy of Product Feedback

When synthesizing feedback from stakeholders, designers, or customers, categorize every observation into one of these three layers. Always address the layers in order; do not prioritize a higher layer if the one below it is broken.

### 1. Value (The Job to be Done)
This is the base layer. If this isn't solved, nothing else matters.
- **Goal:** Validate if the product actually solves the core problem for the target audience.
- **Key Questions:** Is this thing actually valuable? Does it fulfill the "Job to be Done"? Does it address the core pain point?
- **Action:** If feedback suggests the value proposition is unclear or the problem isn't being solved, disregard all feedback regarding UI or polish until this is fixed.

### 2. Ease of Use
Once value is confirmed, focus on accessibility and friction.
- **Goal:** Ensure users can actually access the value without getting stuck.
- **Key Questions:** Are people confused? Are they hitting wrong pathways? Is it too slow (e.g., 10-second load times)? Is the flow logical?
- **Action:** Fix "hang-ups" and performance issues before moving to delight.

### 3. Delight (Joyful/Pleasurable)
The top layer of the pyramid.
- **Goal:** Exceed expectations and create an emotional connection.
- **Key Questions:** Is it joyful to use? Is the aesthetic appropriate? Are the animations delightful?
- **Action:** Use this layer for debates about colors, micro-interactions, and "wow" moments.

## The Review Protocol

To get the most out of a critique session, follow these steps to manage the room and the output:

### Set the Stage (The "Where We Are" Check)
Start every review by explicitly stating the current fidelity and the type of feedback you need.
- **Early Stage:** "We are validating **Value**. Please don't give feedback on colors or button placement; tell us if this solves the user's primary problem."
- **Middle Stage:** "The value is validated. We are now focusing on **Ease of Use**. Is the navigation clear?"
- **Late Stage:** "The flow works. Now we are looking for **Delight** and polish."

### Focus on the Problem, Not the Solution
When stakeholders give feedback, they often jump to solutions (e.g., "Make the button purple"). Force a shift back to the problem:
1. **Identify the Problem:** Ask the reviewer, "What is the problem you are trying to solve with that suggestion?"
2. **State the Reason:** Instead of "I don't like the yellow," say "The yellow makes this warning look less urgent, which might lead to user error."
3. **Empower the Designer:** Once the problem is agreed upon, let the designer (the person closest to the problem) explore the best solution rather than dictating the change in the meeting.

## Examples

**Example 1: High-Level Value Conflict**
*   **Context:** A review for a new analytics dashboard. Stakeholders are debating if the "Export to PDF" button should be blue or gray.
*   **Input:** "I think the export button should be more prominent."
*   **Application:** The facilitator realizes the team hasn't confirmed if users even *want* to export PDFs.
*   **Output:** "Before we decide on the button color, let's look at the **Value** layer. Do we have conviction that PDF export is the primary job the user is trying to do here? If not, we should pause on the UI discussion."

**Example 2: Shifting from Solution to Problem**
*   **Context:** A PM is reviewing a mobile onboarding flow.
*   **Input:** "Move step 3 to the beginning and make the text larger."
*   **Application:** The facilitator asks for the "Why."
*   **Output:** "It sounds like the **Problem** is that users might miss the value prop if it's hidden in step 3. Let's align on that problem. [Designer], now that we know the goal is to surface the value prop earlier, do you think moving step 3 is the best way, or is there a better UI solution?"

## Common Pitfalls
- **Seeking Consensus:** Do not try to get everyone to agree on a design. Use the feedback to inform a decision, but someone (the PM or Lead Designer) must ultimately make the call based on the hierarchy.
- **Jumping to Solutions:** PMs and founders often prescribe UI changes. This takes power away from the designer and often ignores the root cause of the issue.
- **Mixing Fidelities:** Reviewing "Delight" (colors/fonts) on a low-fidelity wireframe designed to test "Value." This wastes time and confuses stakeholders.
- **Ignoring the "Job":** Polishing a feature that doesn't actually solve a problem. No amount of delight can save a product that provides no value.