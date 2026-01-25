# Shannon Examples

Real-world use cases showing Shannon's frameworks in action.

---

## Strategic Email Drafting

### Scenario: Roadmap Update to VP

**Request:**
> "Draft an email to my VP updating her on Q1 roadmap changes. We're cutting the social sharing feature to focus on core analytics."

**Shannon Response:**

```
I'll use the CRAFT method (Sam Lessin's framework) for executive communication.

---

Subject: Q1 Roadmap Shift: Analytics First

Sarah,

Quick heads-up on Q1 roadmap change:

**Catch (The Why):**
Our activation data shows 73% of new users churn before completing first report. 
Analytics clarity is the bottleneck, not social features.

**Reasoning (The Trade-off):**
We're cutting social sharing (3 eng-weeks) to double-down on analytics:
- Guided report builder (reduces time-to-first-value by 50%)
- Automated insights (addresses #1 user request from research)

Trade-off: Social launch moves to Q2. Based on usage data, this affects 
<5% of current users vs. 100% of new users benefiting from analytics improvements.

**Ask (What I Need):**
Your approval to communicate the change at Friday's all-hands.

**Follow-up (Next Steps):**
If approved, I'll:
1. Update eng team by EOD today
2. Draft all-hands messaging for your review Thursday
3. Update board materials to reflect new priorities

**Timebox:**
Need your go/no-go by EOD Wednesday (1/24) to stay on schedule.

Best,
[Your name]

---

✓ Applied CRAFT framework
✓ Passed quality gates:
  - Customer value clear (activation improvement)
  - Trade-offs explicit (Q2 delay, <5% impact)
  - Metrics quantified (73% churn, 50% improvement)
  - Stakeholder can act (clear ask + deadline)
```

**What Shannon Did:**
- Detected executive communication → activated `email-drafter` skill
- Applied CRAFT method automatically
- Structured as concentric circles (most important first)
- Validated with quality gates
- Attributed framework to Sam Lessin

---

## Meeting Summarization

### Scenario: Leadership Sync Transcript

**Request:**
> "Summarize this 1-hour leadership meeting" [paste transcript]

**Shannon Response:**

```
Activating meeting-summarizer agent. Analyzing 47-minute transcript 
with 4 speakers (Sarah, Mike, Lisa, You)...

---

## Leadership Sync Summary
**Date:** Jan 24, 2026 | **Duration:** 47 min | **Attendees:** 4

### Key Decisions

**1. Q1 Revenue Target Increased to $2.3M**
- **Decision:** Raise Q1 target from $2M to $2.3M
- **Rationale:** Enterprise pipeline accelerated, 3 deals closing early
- **Owner:** Sarah (CEO) committed to board
- **Impact:** Marketing needs $50K budget increase (Lisa to submit)
- **Dissent:** Mike (CTO) noted eng capacity risk if deals require custom work

**2. Hiring Freeze Lifted for Revenue-Critical Roles**
- **Decision:** Unfreeze sales engineering and CSM roles only
- **Rationale:** Deal velocity constrained by support capacity
- **Owner:** Sarah approved, HR to post by Friday
- **Impact:** +2 headcount, $300K annualized cost
- **Condition:** Freeze continues for all other departments

### Action Items

| Owner | Action | Deadline | Status |
|-------|--------|----------|--------|
| Lisa | Submit $50K marketing budget increase | 1/26 | Open |
| You | Update Q1 roadmap to prioritize enterprise features | 1/27 | Open |
| Mike | Assess eng capacity for 3 incoming enterprise deals | 1/28 | Open |
| Sarah | Communicate target change to board | 1/31 | Open |

### Open Questions

**1. What if enterprise deals require custom dev work?**
- **Raised by:** Mike (CTO)
- **Context:** Current pipeline assumes standard features
- **Next step:** Sales to qualify scope before final signatures
- **Deadline:** Before close (ongoing)

**2. How does marketing budget increase affect Q2 planning?**
- **Raised by:** Lisa (CMO)
- **Context:** $50K from Q2 budget or net-new?
- **Next step:** Sarah + Lisa offline discussion
- **Deadline:** Before Friday board update (1/26)

### Topics Discussed (No Decision)

- Q2 planning kickoff timeline (pushed to next meeting)
- New office space options (still evaluating)
- Team offsite planning (Lisa to send survey)

### Meeting Health Check

✓ Clear decisions with owners
✓ Action items have deadlines
⚠ 2 open questions need resolution before Friday
⚠ Mike's capacity concern not fully addressed

**Recommended Follow-up:**
Schedule 30-min with Mike + You to assess enterprise deal impact 
on eng roadmap before finalizing commitments.

---

Applied meeting protocols:
- Ambiguity detection: Flagged 2 unresolved questions
- Attribution: All decisions/concerns linked to speakers
- Action bias: Every decision has owner + deadline
```

**What Shannon Did:**
- Detected meeting content → activated `meeting-summarizer` agent
- Extracted decisions with full context (rationale, dissent, impact)
- Identified action items with owners and deadlines
- Flagged unresolved ambiguities (open questions)
- Provided meeting health assessment
- Recommended next steps

---

## PRD Creation with Eigenquestions

### Scenario: New Feature PRD

**Request:**
> "Create a PRD for adding collaboration features to our analytics platform"

**Shannon Response:**

```
I'll use eigenquestion-context to gather high-leverage information 
before building the PRD.

---

To create the best PRD for collaboration features, I need to understand 
one thing:

**Is this collaboration primarily about teams working together in 
real-time (like Figma), or about asynchronous review and feedback 
(like Google Docs comments)?**

This determines:
- Technical architecture (WebSocket vs. REST API)
- UX model (live cursors vs. comment threads)
- Pricing tier (team feature vs. enterprise feature)
- Timeline (real-time is 3-4x more complex)

[User responds: "Async review - users want to share reports and get 
feedback from stakeholders"]

---

Perfect. That unlocks 20+ downstream decisions. Building PRD now...

# Analytics Sharing & Feedback - PRD

**Owner:** [Your name]
**Status:** Draft
**Last Updated:** Jan 24, 2026

---

## Problem Statement

**Who:** Analytics power users (20% of user base, 80% of usage)

**What:** Users create reports but can't get stakeholder feedback 
without screenshots + email chains. No audit trail of decisions.

**Why it matters:**
- Business: Blocks enterprise sales (collaboration is #2 deal requirement)
- Users: 73% of surveyed users export to slides just to share internally
- Activation: Feedback loop currently takes 2-3 days, slows adoption

### Success Metrics
- **Primary:** 40% of reports shared within 7 days of creation
- **Secondary:** Average feedback loop time < 4 hours (from 2-3 days)
- **Business:** Unblocks 8 enterprise deals worth $1.2M ARR

---

## Proposed Solution

**Async sharing + threaded feedback on analytics reports**

### Key Features

**1. Share Report (with permissions)**
- Generate shareable link with view/comment/edit permissions
- Email notification with context ("Sarah shared Q4 Revenue Dashboard")
- User benefit: Stakeholders see live data, not static screenshots
- Success criteria: 60% of shared reports use "view-only" permission

**2. Threaded Comments**
- Comment on specific data points or visualizations
- @-mentions for notifications
- Resolve/unresolve workflow
- User benefit: Async feedback with context, no email chains
- Success criteria: Average 3+ comments per shared report

**3. Activity Feed**
- See all comments, shares, edits in one timeline
- Filter by report or user
- User benefit: Audit trail for decision-making
- Success criteria: 80% of users check feed before meetings

---

## Trade-offs

| Option | Pros | Cons | Recommendation |
|--------|------|------|----------------|
| **Async only** (proposed) | Simpler (8 weeks), covers 90% of use cases, enterprise-ready | No real-time for power users | ✅ YES - start here, real-time in Phase 2 if data shows need |
| **Real-time collab** | Competitive with Figma/Notion, "wow" factor | 24+ weeks, requires WebSocket infra, overkill for use case | ❌ NO - not validated by research |
| **Email-only** | Zero eng work, instant | Doesn't solve feedback loop problem, no audit trail | ❌ NO - doesn't move metrics |

**Chosen approach:** Async-only for Phase 1. Real-time cursors/editing 
in Phase 2 if enterprise customers request (currently 0 requests).

**Rationale:** User research shows "I need feedback from my VP" (async) 
not "I need to edit together in real-time." Starting with async unblocks 
enterprise deals and gives us 16 weeks back.

---

## Open Questions

**1. Do shared reports count against workspace seat limits?**
- **Impact:** Pricing model, sales messaging
- **Owner:** You + Sarah (CEO)
- **Deadline:** Before eng kickoff (2/1)

**2. Should view-only users see full data or summary?**
- **Impact:** Data security, enterprise requirements
- **Owner:** Mike (CTO) + compliance team
- **Deadline:** Before enterprise demo (2/5)

---

## Rollout Plan

### Phase 1: Core Sharing (Weeks 1-4)
- Share link generation
- Permission models
- Email notifications

### Phase 2: Comments (Weeks 5-7)
- Threaded comments
- @-mentions
- Resolve workflow

### Phase 3: Activity Feed (Week 8)
- Timeline view
- Filters
- Polish + launch

**Target Launch:** End of Q1 (March 28)

---

✓ Applied eigenquestion framework (real-time vs. async)
✓ Passed quality gates:
  - Customer value clear (unblock feedback loop)
  - Trade-offs explicit (async-only, real-time deferred)
  - Success metrics quantified (40% share rate, <4hr feedback)
  - Stakeholders can act (open questions have owners)
  - Executive-worthy (ties to $1.2M in deals)
```

**What Shannon Did:**
- Detected PRD request → activated `eigenquestion-context` skill
- Asked ONE discriminating question (real-time vs. async)
- User's answer eliminated 20+ follow-up questions
- Applied PRD framework with quality gates
- Trade-off analysis explicit (why not real-time)
- Quantified success metrics and business impact
- Flagged open questions with owners

---

## TODO Prioritization

### Scenario: Overwhelmed by Tasks

**Request:**
> "I have 15 things on my plate. Help me prioritize what to focus on this week."

**Shannon Response:**

```
Activating updating-todos agent. I'll use the LNO framework 
(Leverage, Neutral, Overhead) to prioritize.

First, let me ask: What's your #1 objective this quarter?

[User responds: "Ship enterprise collaboration features to close 
Q1 deals"]

---

Perfect. Prioritizing your 15 tasks through the LNO lens:

## Your Prioritized TODO List

### 🚀 LEVERAGE (Do These First - 20% of effort, 80% of impact)

**L1. Finalize enterprise sharing PRD**
- Why: Unblocks eng team, they're waiting (8 eng-weeks at stake)
- Impact: Without this, Q1 launch slips
- Time: 2 hours
- Do: Today before 2pm standup

**L2. Demo collab features to VP**
- Why: Her approval unblocks $1.2M in deals
- Impact: Direct line to Q1 revenue target
- Time: 30 min prep + 30 min meeting
- Do: Schedule for Friday this week

**L3. Resolve "view-only permissions" open question**
- Why: Blocker for 3 enterprise deals (data security concern)
- Impact: Deals won't close without clarity
- Time: 1 hour with Mike (CTO)
- Do: Tomorrow morning

### ⚖️ NEUTRAL (Important but not urgent - do after Leverage items)

**N1. Update Q2 roadmap draft**
- Why: Planning cycle starts next week
- Impact: Medium - directional only at this stage
- Time: 3 hours
- Do: Next week, before planning kickoff

**N2. Interview user for case study**
- Why: Marketing needs customer story
- Impact: Medium - helps sales, not blocking
- Time: 1 hour
- Do: Next week

**N3. Review designer's mockups for sharing flow**
- Why: Designer is waiting, but not blocking eng yet
- Impact: Medium - quality improvement
- Time: 30 min
- Do: Friday afternoon

[... 6 more Neutral tasks ...]

### 🔻 OVERHEAD (Delegate or defer - busy work that feels urgent but isn't)

**O1. Reorganize Confluence documentation**
- Why: Nice-to-have, doesn't move Q1 metrics
- Impact: Low - no one blocked
- Action: Defer to Q2 or delegate to junior PM

**O2. Attend "PM Best Practices" lunch & learn**
- Why: Professional development, not urgent
- Impact: Low - no immediate business need
- Action: Skip this month, focus on Q1 execution

**O3. Update 47 Jira tickets with new labels**
- Why: Process overhead, no customer impact
- Impact: Low - busy work
- Action: Delegate to intern or skip

---

## This Week's Focus (LNO-Prioritized)

**Monday:**
- Morning: L1 (PRD) - 2 hours
- Afternoon: L3 (Permissions decision with CTO) - 1 hour

**Tuesday:**
- Morning: L2 prep (Demo prep) - 30 min
- Afternoon: N3 (Design review) - 30 min
- Rest: N1 (Q2 roadmap draft) - 2 hours

**Wednesday-Thursday:**
- Neutral tasks as time allows
- Protect Friday for VP demo

**Friday:**
- L2 (VP Demo) - critical
- Wrap remaining Neutral items

**What to drop:**
- All Overhead tasks - defer or delegate

---

✓ Applied LNO framework (Lenny Rachitsky)
✓ Prioritized by impact on Q1 objective
✓ Time-boxed each item
✓ Flagged Overhead as delegate/defer
✓ Actionable: You know exactly what to do Monday morning
```

**What Shannon Did:**
- Detected prioritization request → activated `updating-todos` agent
- Applied LNO framework (Leverage/Neutral/Overhead)
- Asked for quarterly objective to prioritize correctly
- Categorized all 15 tasks through LNO lens
- Provided weekly schedule with specific timing
- Identified what to delegate or skip

---

## Stakeholder Communication

### Scenario: Difficult Trade-off Update

**Request:**
> "Draft an update to the leadership team. We need to cut the mobile app from Q1 to ship web features first. This will disappoint Sarah (CEO) who promised mobile to a key customer."

**Shannon Response:**

```
I'll use concentric circle messaging (start with core truth, expand 
with context) and apply the "bad news + clear path forward" framework.

---

Subject: Q1 Mobile → Q2: The Trade-off & Path Forward

Team,

**Core Decision:**
We're moving mobile app from Q1 to Q2. Web features ship as planned.

**Why (The Data):**
Our Q1 capacity analysis shows we can ship:
- Option A: Web features (80% of user requests) → 40% activation lift
- Option B: Mobile app (20% of user requests) → 15% activation lift
- Option C: Both → neither ships well, quality compromised

Option A delivers 2.6x more impact with same resources.

**The Difficult Part:**
Sarah, I know you've communicated mobile to [Customer Name]. This 
creates a customer commitment challenge.

**Proposed Path Forward:**

*For the customer:*
1. I'll call [Customer contact] this week with the update
2. Offer: Beta access to web features 4 weeks early (Feb instead of March)
3. Commit: Mobile in Q2 with their top 3 feature requests prioritized
4. Give them influence: Join our mobile beta advisory group

*For Q1:*
- Web ships March 15 (unchanged)
- Delivers 40% activation improvement
- Unblocks 8 enterprise deals worth $1.2M

*For mobile:*
- Kicks off April 1 (Q2 start)
- 4 weeks ahead vs. compressed Q1 timeline
- Higher quality because team isn't split

**What I Need:**

From Sarah: Approval to call customer, or would you prefer to make 
the call? I can draft talking points either way.

From team: Any concerns with this trade-off? Speak now before I 
communicate externally.

**Deadline:** Need your input by EOD Thursday (1/25) to stay on 
schedule and maintain customer trust.

This is the right trade-off for users and business, even though it's 
not the easy one.

[Your name]

---

✓ Applied concentric circles (core decision first)
✓ Used data to justify (2.6x impact difference)
✓ Acknowledged difficult reality (CEO commitment)
✓ Provided clear path forward (not just bad news)
✓ Made it easy for stakeholders to respond (specific asks)
✓ Showed leadership (took ownership of customer call)
```

**What Shannon Did:**
- Detected difficult stakeholder communication
- Applied concentric circle messaging (core → context → details)
- Structured as "bad news + clear path" framework
- Quantified trade-off (2.6x impact difference)
- Included specific asks with deadlines
- Maintained stakeholder relationships (offered to own customer call)

---

## Growth Strategy Analysis

### Scenario: Evaluate PLG Funnel

**Request:**
> "Analyze our PLG funnel. We're getting signups but activation is low. What should we focus on?"

**Shannon Response:**

```
I'll apply the PLG funnel audit framework and activation optimization 
methodology.

First, share your funnel data:
- Signup → Activation rate?
- Activation definition?
- Time to activation (median)?

[User provides: 1000 signups/week, 12% activate (complete first report), 
median time-to-activation: 4.3 days]

---

## PLG Funnel Analysis

### Current State

```
Signup: 1000/week
↓ (88% drop-off)
Activation: 120/week (completed first report)
↓
Retention: [need data]
```

**Critical Issue:** 88% drop-off before activation is a comprehension 
problem, not an effort problem.

### Applying First Mile Experience Design

Your funnel fails the "Lazy, Vain, Selfish" test:

**Lazy (Cognitive Load):**
- 4.3 days to first report = too much thinking required
- Users giving up = they don't understand what to do
- **Hypothesis:** No guided onboarding, blank slate problem

**Vain (Success Moment):**
- No quick win in first session
- Nothing to "show" colleagues until day 4+
- **Hypothesis:** Missing "10-second aha moment"

**Selfish (Value Clarity):**
- Not clear what problem you solve in first 30 seconds
- Users bouncing = "is this for me?" not answered
- **Hypothesis:** Generic onboarding, not role-specific

### Recommended Focus (Prioritized by Impact)

**🎯 Priority 1: Immersive Onboarding Wizard**

Current: Blank table + tooltips  
Problem: Users don't know what to build

**Build:**
- Wizard asks 3 questions:
  1. "What are you tracking?" (Projects/Sales/Marketing/Other)
  2. "What status columns?" (To Do/Doing/Done + custom)
  3. "Import existing data?" (CSV/Google Sheets/Start fresh)
- As they answer, show LIVE PREVIEW of their board building
- Takes 60 seconds, they enter the app with functional workspace

**Expected Impact:** 12% → 35% activation (based on Notion's case study)

**Why this works:**
- Lazy: No blank slate, reduced cognitive load
- Vain: They built something in 60 seconds (success moment)
- Selfish: Board is customized to their use case immediately

**Effort:** 3 eng-weeks  
**Test:** A/B test in week 4

---

**🎯 Priority 2: Role-Based First Report Templates**

Current: Users start from scratch  
Problem: Don't know what "good" looks like

**Build:**
- Detect role from signup (PM/Marketer/Engineer/Sales)
- Offer 3 pre-built report templates for their role
- One-click to duplicate and customize
- Examples:
  - PM: "Sprint Progress Dashboard"
  - Marketer: "Campaign Performance Tracker"
  - Engineer: "Bug Triage Board"

**Expected Impact:** Time-to-activation: 4.3 days → 1.2 days

**Why this works:**
- Lazy: Template = no blank slate problem
- Vain: Professional-looking report instantly
- Selfish: "This is made for me" (role-specific)

**Effort:** 2 eng-weeks (templates) + 1 week (role detection)  
**Test:** Sequential test after wizard ships

---

**🎯 Priority 3: "Aha Moment" Metric Tracking**

Current: You track "completed first report" (lagging indicator)  
Problem: Don't know where users get stuck

**Build:**
- Track micro-conversions:
  - Created first column (%)
  - Added first data point (%)
  - Customized view (%)
  - Shared with teammate (%)
- Identify where 88% drop off
- Instrument interventions at drop-off points

**Expected Impact:** Data to optimize Priority 1 & 2

**Effort:** 1 eng-week  
**Test:** Ship before Priority 1 to baseline

---

## Recommended Roadmap

**Week 1-2:** Priority 3 (instrumentation) - baseline data  
**Week 3-5:** Priority 1 (wizard) - biggest impact  
**Week 6:** Analyze wizard data, iterate  
**Week 7-9:** Priority 2 (templates) - compound improvement  
**Week 10:** Measure combined effect

**Success Criteria:**
- Activation: 12% → 30%+ (2.5x improvement)
- Time-to-activation: 4.3 days → <2 days
- Business impact: 1000 signups/week × 30% = 300 activated users/week 
  (vs. current 120) = 180 more customers entering funnel

---

✓ Applied PLG funnel audit framework
✓ Used First Mile Experience Design principles
✓ Prioritized by impact (not effort)
✓ Quantified expected outcomes
✓ Provided specific roadmap with timeline
✓ Tied to business metrics
```

**What Shannon Did:**
- Detected growth strategy question
- Applied PLG funnel audit + First Mile Experience Design frameworks
- Analyzed through "Lazy, Vain, Selfish" lens
- Prioritized interventions by expected impact
- Provided concrete roadmap with timeline
- Quantified success criteria and business impact
- Referenced proven case studies (Notion)

---

## More Examples

See skill-specific examples in:
- `.claude/skills/[skill-name]/references/examples.md`
- Each skill includes 2-3 detailed examples

Common skills to explore:
- `product-positioning-framework` - April Dunford's 5-step positioning
- `lno-product-prioritization` - Leverage/Neutral/Overhead framework
- `cross-functional-alignment-contract` - Stakeholder alignment
- `data-informed-product-loop` - Metrics-driven PM
- `pmf-optimization-engine` - Product-market fit assessment

---

**Shannon brings these frameworks to every request automatically.**  
You don't memorize 350 methodologies—Shannon applies them for you.
