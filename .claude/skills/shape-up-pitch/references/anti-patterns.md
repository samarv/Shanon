# Shape Up Anti-Patterns

Common failure modes when teams adopt Shape Up cycles without the necessary rigor in shaping.

## The "Blurry Figma"

**What it looks like**: Providing "fat marker sketches" that are actually just vague wireframes without clear logic.

**Why it fails**: If the artifact doesn't tell the engineer *what* to build, it isn't shaped - it's a guess. The team will discover unknowns during the build phase, blowing timelines.

**The fix**: Breadboards must show *logic and flow*, not just boxes. If an engineer can't look at it and say "I know exactly what to build," it needs more shaping.

---

## The Detailed Spec (Water-scrum-fall)

**What it looks like**: Providing high-fidelity Figma files and detailed PRDs without engineering involvement in shaping.

**Why it fails**: The UI implies backend logic the designer didn't consider. A "simple" dropdown might require three new API endpoints. The team hits a "reality check" explosion when they discover the disconnect.

**The fix**: A senior engineer must be in the shaping room. They don't code - they validate. Ask: "Is there electricity in the wall for this lamp?"

---

## The "10 Pounds in a 5 Pound Bag"

**What it looks like**: Throwing a massive, unshaped problem at a team ("Build a newsletter builder"), giving them six weeks, and telling them to "figure it out."

**Why it fails**: This is an abdication of leadership responsibility. The team burns out trying to shape AND build simultaneously, with no clear success criteria.

**The fix**: Shaping happens BEFORE the cycle starts. If you can't describe the solution in under 10 moving pieces, it's too big. Split or reshape.

---

## Cutting Scope at the Deadline

**What it looks like**: Reaching week six, realizing the project won't finish, and slashing features to "ship something."

**Why it fails**: Destroys morale. The team knows they're shipping a half-baked version of what was promised. Sets up the next cycle for "finishing" work that should have been scoped properly.

**The fix**: Shaping defines what can be cut BEFORE the cycle starts. The "Nice-to-Haves" section in the pitch is the dial teams turn - not a surprise negotiation at the deadline.

---

## No Engineering in Shaping

**What it looks like**: PM and Designer shape alone, then "hand off" to engineering.

**Why it fails**: Shapers design a "lamp on the wall" without checking if there's "electricity in the wall." Technical feasibility questions surface during the build, when it's too late.

**The fix**: Include a senior engineer who "knows where the bodies are buried" in the codebase. They're not there to code - they're there to say "that onboarding step actually branches into three different integrations."

---

## Infinite Appetite

**What it looks like**: "Take as long as you need." Or estimating first, then calling it "appetite."

**Why it fails**: Defeats the entire purpose of Shape Up. Without a fixed time constraint, scope expands to fill available time. The discipline of shaping-to-fit disappears.

**The fix**: Set appetite FIRST, based on how much the problem is worth solving. Then shape the solution to fit that budget. If it doesn't fit, change the approach - not the time.

---

## Skipping the Circuit Breaker

**What it looks like**: A project runs over, but leadership extends the timeline "just another week or two."

**Why it fails**: The sunk cost fallacy takes over. The team keeps reinvesting in a project they don't truly understand. Other work gets delayed. Trust in the process erodes.

**The fix**: Enforce the circuit breaker ruthlessly. If it's not done at the end of the appetite, either cancel it or pull it back to the shaping table. No extensions.

---

## Summary Table

| Anti-Pattern | Root Cause | Prevention |
|--------------|------------|------------|
| Blurry Figma | Confusing sketches with shaping | Breadboards show logic, not just layout |
| Detailed Spec | Engineering excluded from shaping | Senior engineer in every shaping session |
| 10 Pounds / 5 Pounds | Skipping shaping entirely | Shape until describable in <10 pieces |
| Deadline Scope Cuts | No pre-defined flexibility | Nice-to-Haves section in every pitch |
| No Eng in Shaping | "Handoff" mentality | Engineer validates feasibility upfront |
| Infinite Appetite | Estimate-first mindset | Set appetite before shaping |
| Skipping Circuit Breaker | Sunk cost aversion | Enforce hard stops, no extensions |
