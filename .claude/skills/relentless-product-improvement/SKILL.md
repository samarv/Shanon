---
name: relentless-product-improvement
description: A framework for driving product growth by combining deep user empathy (Jobs to be Done), analytical rigor, and design clarity. Use it when troubleshooting a feature that has plateaued, launching a new "big bet" within a mature product, or diagnosing why users are abandoning a specific workflow.
---

# Relentless Product Improvement

To build products at a global scale, you must embody "productive dissatisfaction"—the refusal to tolerate mediocre user experiences and a commitment to compounding small improvements until they hit a tipping point of success. This framework guides you through the process of understanding why users "hire" your product, diagnosing failures with rigor, and shipping with extreme clarity.

## 1. Deeply Understand the "Big Hire"
Move beyond demographics to find the *causation* of why someone uses your product. Every user "hires" a product to do a job.

- **Conduct "Interrogations":** Ask users exactly where they were and what they were doing the moment they decided to use your product.
    - *BAD:* "Do you like this feature?"
    - *GOOD:* "Where were you? Were you in bed? At work? What was the exact thought that prompted you to open the app?"
- **Identify Emotional Jobs:** Recognize that users often hire products for emotional needs (e.g., feeling connected, reducing anxiety) rather than just functional utility.
- **Find the "Big Hire" Moment:** Identify the first time a user decides to use the product. The information obtained from that specific moment is more critical than any general feedback.

## 2. Apply Analytical Rigor to Root Causes
When metrics drop or a feature fails to gain traction, do not guess. Dissect the data to find the specific point of failure.

- **Perform Segmented Root Cause Analysis:** If a core metric is down, investigate if the issue is isolated to a specific region, device, demographic, or use case.
- **Measure the "Closed Loop":** For social or communication products, ensure the user's action results in a response.
    - *Example:* If a user posts a private story but has too few people on their list, the probability of a "reply" is zero, causing the user to abandon the feature.
- **Track S-Curves:** Monitor every feature's growth. When a feature hits a plateau (diminishing marginal returns), reallocate resources to first-principles bets rather than minor optimizations.

## 3. Design for Clarity over Cleverness
Avoid "differentiating" through unique UI if it compromises the user’s mental model. Standards provide leverage.

- **The Door Principle:** A door should communicate whether to push or pull through its design (a handle vs. a flat plate). Apply this to UI.
- **Use Global Icons:** Do not reinvent standard symbols. If a feature uses the camera, use a camera icon. Avoid "clever" icons that require a learning curve.
- **Leverage Spatial Thinking:** People think of apps spatially. If you add a new feature to an existing product, it must feel coherent but distinctive.
- **Complement, Don't Replace:** When building a new format (like AI Mode in Search or Stories in Instagram), design it to expand the product’s utility rather than forcing users to change existing habits.

## 4. Scaling the Breakthrough
Once you have internal conviction (the "perfect shot" moment), move from scrappy to robust.

- **Move Fast on "Live" Testing:** Use "Trusted Tester" groups of ~500 people to find where the product "sucks" before a public Labs launch.
- **Identify the Conviction Moment:** Once you see a small group of users finding intense value, invest resources to build the "best version" rather than staying in a "minimum viable" state too long.

---

**Example 1: Reviving a "Flop" Feature**
- **Context:** A private sharing feature (Close Friends) is failing to grow.
- **Input:** Data shows users are only adding 1-2 people to their list and never getting replies.
- **Application:**
    1. **Understand People:** The "job" is feeling connected. Two people isn't enough to guarantee a response.
    2. **Analytical Rigor:** Identify that users with 20+ friends on their list have high retention.
    3. **Design for Clarity:** Change the name from "Favorites" (which implies a very small number) to "Close Friends." Add a clear visual cue (e.g., a green ring) on the *outside* of the feature so users know it's unique before they click.
- **Output:** The feature loop closes, replies increase, and retention stabilizes.

**Example 2: Complementary Product Expansion**
- **Context:** A mature search engine wants to integrate generative AI without breaking the core keyword-search habit.
- **Input:** Users are starting to append "AI" to their queries because the standard results aren't answering complex questions.
- **Application:**
    1. **Identify the Gap:** Recognize that "keyword ease" is failing for multi-sentence, complex intents.
    2. **Build a Distinctive Space:** Create an "AI Mode" that is a full-page, conversational experience, rather than just a small box in the existing results.
    3. **Design for Clarity:** Name it "AI Mode" so users immediately understand the capability change.
- **Output:** Users use the core search for quick utility (phone numbers, prices) and the AI Mode for "expansionary" curiosity (planning, research).

---

## Common Pitfalls to Avoid
- **Reinventing the Wheel:** Creating a custom UI for a standard action (like a "sharing" icon) just to be "on-brand." This forces users to think, which leads to abandonment.
- **Staying Scrappy Too Long:** Holding onto a tiny team after you've found a breakthrough. This slows down the iteration cycle and allows competitors to get ahead.
- **Ignoring the "Causation" Interview:** Building features based on what users *say* they want in a survey rather than what they *did* in the moments leading up to using the product.
- **Acceptance of Mediocrity (Habituation):** Becoming like a "grown-up" who ignores the stickers on fruit that puncture the flesh. Always ask "Why does this suck?" and "How can this be better?"