# Example Opportunity Solution Trees

Real-world examples to illustrate good OST structure.

## Example 1: SaaS Project Management Tool

### Outcome
**Increase trial-to-paid conversion from 12% to 18% by Q2**

### Experience Map
1. Sign-up & First Session
2. Setup & Configuration
3. Daily Task Management
4. Team Collaboration
5. Progress Tracking

### Opportunities (Selected Examples)

#### Phase 1: Sign-up & First Session

**Opportunity 1.1**: "I don't know what to do first after signing up"
- Evidence: "I created an account but then just stared at an empty screen. I didn't know if I should create a project first or invite my team or what." - Interview #4
- Confidence: High (9/12 trial users mentioned this)
- Status: Pursuing

**Solutions**:
1. **Interactive onboarding tour**
   - Assumptions: Users want guided experience, 3-minute tour holds attention, showing features creates understanding
   - Status: Testing

2. **Pre-populated demo project**
   - Assumptions: Users learn by exploring example data, they'll delete demo project after, seeing populated project shows value faster
   - Status: Idea

3. **Quick-win first task**
   - Assumptions: Single simple task is less overwhelming, completing one task creates momentum, users know what task to create
   - Status: Idea

**Active Test**: A/B test onboarding tour vs. control (100 users each)
- Success: 60%+ complete tour AND create first project
- Results pending

#### Phase 2: Setup & Configuration

**Opportunity 2.1**: "I can't import my existing work from other tools"
- Evidence: "I have 50 tasks in Asana. Starting over in a new tool feels like going backwards." - Interview #7
- Confidence: Medium (5/12 mentioned, but expressed strongly)
- Status: Exploring

**Solutions**:
1. **CSV import**
   - Assumptions: Users can export CSV from current tool, they'll map fields correctly, CSV is sufficient format
   - Status: Validated (via fake door - 67% clicked "Import")

2. **Direct integrations** (Asana, Trello, etc.)
   - Assumptions: 3-4 tools cover 80% of users, users trust us with their account access, read-only access is sufficient
   - Status: Testing (surveying which tools)

3. **Manual migration assistant**
   - Assumptions: Users will pay for migration help, 2-hour async service acceptable, maintaining momentum worth the cost
   - Status: Idea

#### Phase 3: Daily Task Management

**Opportunity 3.1**: "I can't see all my tasks across projects in one view"
- Evidence: "I work on 4 different projects. I have to click into each one to see what's due today. By the time I've checked all 4, I've already wasted 5 minutes." - Interview #2
- Confidence: High (10/12 mentioned)
- Status: Pursuing

**Sub-opportunity 3.1.1**: "I can't tell which tasks are most urgent across projects"
- Evidence: "I see all my tasks but I don't know which fire to fight first." - Interview #2 follow-up
- Confidence: Medium (3/12 specifically mentioned)
- Status: Exploring

**Solutions for 3.1**:
1. **Master task list view**
   - Assumptions: Users want ALL tasks visible, they'll filter manually as needed, single long list is manageable
   - Status: Shipped (and now measuring adoption)

2. **Smart "Today" view**
   - Assumptions: Users want system to prioritize for them, due date + priority + project context = good prioritization, 20 tasks per day is the right limit
   - Status: Testing (prototype with 10 users)

3. **Customizable dashboard**
   - Assumptions: Users know how they want to see their work, they'll invest time customizing, personalization improves retention
   - Status: Idea

4. **Search-first interface**
   - Assumptions: Users can articulate what they're looking for, search is faster than browsing, natural language search works
   - Status: Idea

**Active Tests**:
- Smart "Today" view prototype: Do users complete tasks from this view? (In progress, 10 users)
- Adoption of shipped "Master task list": 45% of active users tried it, but only 12% use it weekly (below target)

**Learning**: Master task list not sticky because it's overwhelming without prioritization → validates need for "Smart Today" solution

---

## Example 2: E-Commerce Fashion Retailer

### Outcome
**Reduce cart abandonment from 68% to 55% by end of quarter**

### Experience Map
1. Product Discovery
2. Product Evaluation
3. Cart & Checkout
4. Post-Purchase

### Opportunities (Selected Examples)

#### Phase 3: Cart & Checkout

**Opportunity 3.1**: "I don't know if this will fit me"
- Evidence: "I had 3 dresses in my cart but didn't buy any because I have no idea what 'size M' means for this brand. Last time I ordered a medium somewhere it was huge." - Interview #18
- Confidence: High (23/30 mentioned fit uncertainty)
- Status: Pursuing

**Solutions**:
1. **Size guide with measurements**
   - Assumptions: Users have measuring tape, they'll measure themselves, they can interpret measurements, measurements predict fit accurately
   - Status: Shipped (no impact on conversion - users didn't use it)

2. **Virtual try-on (AR)**
   - Assumptions: Users have compatible phones, they'll grant camera access, AR accurately represents fit, tech is reliable
   - Status: Invalidated (prototype tested - too clunky, users didn't trust accuracy)

3. **Size recommendation quiz**
   - Assumptions: Users will answer 5 questions, our algorithm is accurate, users trust recommendations, one-time setup is acceptable
   - Status: Testing

4. **Fit photos from real customers**
   - Assumptions: Customers will submit photos, photos represent variety of body types, seeing real people builds confidence, privacy concerns manageable
   - Status: Validated (ran test with 20 products - 34% increase in conversion)

**Active Work**: Scaling "Fit photos" feature to more products (building)

**Learning**: The winning solution wasn't the most technically sophisticated one - it was the one that built confidence through social proof.

---

## Example 3: Mobile Fitness App

### Outcome
**Increase 30-day retention from 22% to 35%**

### Experience Map
1. Goal Setting
2. First Workout
3. Building Habit (Days 2-14)
4. Sustaining Practice (Days 15-30)
5. Progress Review

### Opportunities (Selected Examples)

#### Phase 3: Building Habit (Days 2-14)

**Opportunity 3.1**: "I don't work out because I don't have time"
- Evidence: "I downloaded the app with good intentions, did one workout, then life happened. I don't have 45 minutes for a workout most days." - Interview #9
- Confidence: High (18/20 mentioned time as barrier)
- Status: Pursuing

**Sub-opportunity 3.1.1**: "I don't think short workouts count"
- Evidence: "If I only have 15 minutes, I feel like 'what's the point?' so I do nothing instead." - Interview #12
- Confidence: Medium (7/20 mentioned)
- Status: Exploring

**Solutions for 3.1**:
1. **10-minute workout library**
   - Assumptions: Users will find 10 minutes, 10 minutes provides value, users trust that short workouts work, quality > duration messaging resonates
   - Status: Testing

2. **Micro-workouts throughout day**
   - Assumptions: Users can do 3x 5-minute sessions, notifications won't annoy, fragmented workouts are effective, users remember to do them
   - Status: Idea

3. **Flexible workout plans**
   - Assumptions: Users will plan workout duration each day, system can adapt plans intelligently, "time available" is the right input parameter
   - Status: Idea

**Active Test**: 10-minute workout promotion
- Method: Featured collection of 10-minute workouts
- Success: 40% of new users try at least one, 20% do 3+ per week
- Status: Running (week 2 of 4)

**Opportunity 3.2**: "I lose motivation when I skip a day"
- Evidence: "I was doing great for 5 days, then I missed Saturday. After that I felt like I'd failed and didn't want to open the app." - Interview #14
- Confidence: High (15/20 mentioned)
- Status: Pursuing

**Solutions**:
1. **Remove streak counter**
   - Assumptions: Streaks cause anxiety, removing them reduces pressure, alternative metric can motivate, users won't miss streaks
   - Status: Invalidated (tested with 50 users - complained about losing feature)

2. **Flexible streak** (allows 1 skip per week)
   - Assumptions: 1 skip feels achievable, users won't game the system, flexibility reduces anxiety, streak remains motivating
   - Status: Validated (A/B test showed 18% retention improvement)

3. **Highlight consistency over streaks**
   - Assumptions: "5 workouts in 7 days" more motivating than "5 day streak", flexible framing reduces all-or-nothing thinking
   - Status: Pursuing (building based on test results)

**Learning**: Removing friction (flexible streak) more effective than adding features (new workout types).

---

## What Makes These Examples Good OSTs

### 1. Opportunities are clearly needs, not solutions
- "I don't know what to do first" (need)
- NOT "Users need an onboarding tour" (solution)

### 2. Specific and concrete
- "I can't see all my tasks across projects in one view"
- NOT "Task management is hard"

### 3. Grounded in customer evidence
Every opportunity cites actual interview quotes and counts

### 4. Multiple diverse solutions per opportunity
Each opportunity has 3-4 different approaches, not just one obvious solution

### 5. Explicit assumptions
Every solution lists what must be true for it to work

### 6. Active testing
Each tree shows tests in progress and results from completed tests

### 7. Learnings drive iteration
Failed tests lead to new solutions or refined opportunities

### 8. Vertical depth where needed
Example 1 shows Opportunity 3.1 decomposed into 3.1.1 when needed

### 9. Living documents
These trees show shipped solutions, invalidated ideas, and ongoing work

### 10. Connected to outcome
Each opportunity clearly impacts the stated metric

## Anti-Pattern Examples (Don't Do This)

### Bad Opportunity Framing
- "Users need better navigation" (solution, not need)
- "Improve performance" (too vague)
- "Users want dark mode" (assumes solution)

### Single Solution
- Opportunity: "I can't find products I like"
  - Solution: "Add AI recommendations"
  - (No alternatives considered = high risk)

### No Evidence
- "Users want X" with no interview citation
- Confidence levels with no basis

### No Tests
- Solutions marked "Pursuing" with no validation
- Building without assumption testing

### Stale Tree
- No updates in months
- No active tests
- All opportunities "In progress" indefinitely

## Tree Evolution Example

**Week 1**: Opportunity 3.1 added from interview #2

**Week 3**: Three solutions proposed for 3.1

**Week 5**: Master task list shipped for 3.1

**Week 7**: Adoption data shows low usage - learning captured

**Week 9**: Sub-opportunity 3.1.1 identified (prioritization problem)

**Week 11**: Smart Today view solution designed and prototyping

**Week 13**: Prototype test with 10 users shows promise

**Week 15**: Full build begins on Smart Today view

This shows continuous evolution based on learning.
