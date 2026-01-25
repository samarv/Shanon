---
name: conclusive-failure-experimentation
description: A framework for designing experiments that fail definitively to prevent "zombie" ideas from recurring. Use this when testing high-risk strategic hypotheses, launching in low-traffic (B2B) environments, or evaluating a tactic that a company repeatedly tries without success.
---

The goal of this skill is to ensure that when a product experiment fails, it does so "conclusively." By maximizing the treatment effect, you eliminate the ambiguity of whether an idea failed due to a poor hypothesis or just poor execution, allowing the team to move on or iterate with confidence.

## The Conclusive Design Principles

In environments where you lack massive scale (common in B2B or early-stage startups), you cannot rely on a large sample size ($N$) to detect small improvements. Instead, you must maximize the **Treatment Effect**.

### 1. Maximize the Treatment Effect
If you have a hypothesis, do not test the "minimum" version. Throw every possible tactic and resource at the experiment to give it the best possible chance of success. 
- **Rationale:** If it fails in its most "expensive," high-effort, and polished version, you can be certain the hypothesis is wrong.
- **Action:** If it works, you can "cost-rationalize" later by stripping away the parts that didn't matter.

### 2. Solve for the "Zombie Idea"
A "Zombie Idea" is a project that fails, is killed, but then is resurrected a year later because "maybe we didn't do it right last time."
- **Action:** Design the test so that you can tell future stakeholders: "We tried every lever (design, copy, trigger, and personalization) simultaneously, and it still didn't move the needle."

## Step-by-Step Workflow

1.  **Define the Strategic Hypothesis:** Move beyond tactical changes (e.g., "Change the button color") to strategic bets (e.g., "Personalized outreach to C-level executives drives conversion").
2.  **Apply the "Kitchen Sink" Treatment:** Instead of testing one variable, combine all intuitive levers:
    *   **Content:** Full copy rewrite.
    *   **Design:** Professional visual refresh.
    *   **Context:** Change the trigger or timing of the intervention.
    *   **Social Proof:** Add testimonials or badges.
3.  **Run the Conclusive Test:** Compare this "Maximized Version" against your control group.
4.  **Evaluate and Pivot:**
    *   **If it fails:** Kill the strategy permanently. Document the high-effort attempt to prevent future repeats.
    *   **If it works:** Run a follow-up "Optimization" test to see which 20% of the tactics drove 80% of the results.

## Examples

**Example 1: B2B Account-Based Marketing (ABM)**
*   **Context:** A team wants to know if high-touch marketing works for a set of target accounts.
*   **Input:** Previous attempts used only automated LinkedIn ads and failed.
*   **Application:** Maximize the treatment. For the test group, the team sends physical gift boxes, runs custom-tailored webinars, executes personalized executive email sequences, and buys targeted billboards near the prospect's office.
*   **Output:** The test fails. The PM concludes that the problem isn't the "touchpoint," it's the value proposition itself. The strategy is killed conclusively.

**Example 2: Feature Adoption via Gamification**
*   **Context:** A team wants to test if "Badges" increase user retention.
*   **Input:** A previous "lean" test gave a badge for signing up, which did nothing.
*   **Application:** Maximize the treatment. Create 10 different collectible badges, add a "Trophy Case" to the user profile, create a leaderboard, and trigger a celebratory animation upon earning.
*   **Output:** Retention increases by 15%. The team then tests a "lite" version to see if the Trophy Case is actually necessary or if the animation alone drives the behavior.

## Common Pitfalls

*   **Testing Incrementally on Low Volume:** Trying to test a small subject line change when you only have 1,000 users. You will never reach statistical significance. In low-volume scenarios, you must go big or don't test.
*   **The "Lame Badge" Error:** Shipping a Minimum Viable Experiment (MVE) that is so stripped down it lacks the core psychological triggers required for the hypothesis to work.
*   **Failing to Dogfood:** Running experiments without the team actually using the product. If the team uses the "Maximized Treatment" and finds it annoying or useless, the experiment will likely fail for users too.
*   **Ignoring Unit Economics:** Scaling a "Maximized Treatment" that can never be profitable. Always ask: "If this works, is there a path to making the costs work at scale?"