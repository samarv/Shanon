# Eigenquestion Examples & Case Studies

Deep-dive examples of eigenquestion methodology from Shishir Mehrotra and PM-specific applications.

## Table of Contents

1. [The Modern Family Case Study](#the-modern-family-case-study)
2. [The Coda Decision](#the-coda-decision)
3. [The Teleporter Framework](#the-teleporter-framework)
4. [PM-Specific Eigenquestions](#pm-specific-eigenquestions)

---

## The Modern Family Case Study

From Shishir Mehrotra's time leading YouTube (2008).

### The Gridlock

Users searched for "Modern Family" on YouTube, which YouTube didn't host.

**Product View**: Link users to ABC.com to satisfy user intent ("do the right thing").

**Business View**: Don't link out—it discourages partners from uploading to YouTube ("protect the ecosystem").

This debate created endless meetings. The choice was framed as "User Experience vs. Business Strategy"—an impossible tradeoff to reconcile tactically.

### The Eigenquestion

Mehrotra reframed by asking:

> "In a decade, is the online video market more likely to value **consistency** or **comprehensiveness**?"

### The Cascade

The team concluded: **consistency**.

This single decision answered all downstream questions:

| Tactical Question | Answer (from Eigenquestion) |
|------------------|----------------------------|
| Should we link out to ABC? | No—creates inconsistent experience |
| Should we use embedded players? | No—different ad models, inconsistent |
| Should we let Apple build our iPhone app? | No—take it back, even with zero installs |

**Key insight**: One strategic question eliminated dozens of tactical debates.

---

## The Coda Decision

### The Fork in the Road

Coda faced a fundamental choice between two visions:
- "Make a doc as powerful as an app"
- "Make an app as easy as a doc"

### The Eigenquestion

> "Are we more committed to being a **doc** or being an **app**?"

### The Answer

**A Doc.** (Hence "Coda"—"Doc" spelled mostly backward.)

### The Cascade

This prevented constant feature re-litigation:

| Feature Request | Decision |
|-----------------|----------|
| "Add a native mobile app shell" | Does it break the doc metaphor? If yes, don't do it. |
| "Let users build custom UIs" | Does it feel like editing a doc? If not, reconsider. |
| "Add real-time collaboration" | Docs have this. Yes. |

**Key insight**: Identity questions ("what are we?") unlock product strategy.

---

## The Teleporter Framework

A practice exercise from Mehrotra for developing eigenquestion intuition.

### The Scenario

Scientists invented a teleporter. You're the PM. They'll only answer **two questions** before you must build a go-to-market plan.

### Bad Questions (Information-Gathering)

- "How big is it?"
- "What color is it?"
- "How much does it weigh?"

These provide data but don't discriminate strategy.

### Good Questions (Eigenquestions)

1. **Is it safe for humans?**
2. **Is it expensive to buy (CapEx) or expensive to run (OpEx)?**

### The Decision Matrix

| Safe? | Cost Structure | Strategy |
|-------|---------------|----------|
| Yes | High CapEx, Low OpEx | Replace airports (hub-and-spoke) |
| Yes | Low CapEx, High OpEx | Treat like fax machines (ubiquitous) |
| No | Either | Focus on cargo and logistics |

Two questions → complete GTM framework.

---

## PM-Specific Eigenquestions

### Product Strategy

| Situation | Eigenquestion |
|-----------|--------------|
| Feature prioritization deadlock | "If this product could only do ONE thing perfectly, what would it be?" |
| Platform vs. point solution | "Do we win by being the best at X, or by connecting X to Y and Z?" |
| Build vs. buy vs. partner | "Is this capability core to our differentiation, or table stakes?" |
| Market positioning | "Are we competing on [dimension A] or [dimension B]?" |

### User/Customer Focus

| Situation | Eigenquestion |
|-----------|--------------|
| Conflicting user needs | "If we could only delight ONE persona, which creates the most downstream value?" |
| Enterprise vs. consumer | "Does our growth come from more users or more value per user?" |
| New vs. existing users | "Is our constraint acquisition or retention?" |

### Timeline/Resource

| Situation | Eigenquestion |
|-----------|--------------|
| Scope creep | "If we had to ship in half the time, what's the irreducible core?" |
| Quality vs. speed | "Is a delayed, polished launch better than an early, rough one for THIS product?" |
| Team allocation | "Is the bottleneck ideas, execution, or distribution?" |

### Architecture/Technical

| Situation | Eigenquestion |
|-----------|--------------|
| Monolith vs. microservices | "Do we need to scale parts independently, or is unified deployment simpler?" |
| Build custom vs. use platform | "Is the differentiation in the infrastructure or the experience layer?" |
| Data model decisions | "Is this data more like [structured/relational] or [flexible/document]?" |

---

## Forma Board-Specific Examples

### Example 1: Collaboration Model

**Context**: Adding collaboration to Forma Board.

**Eigenquestion**:
> "Is Board collaboration about **synchronous co-creation** (two architects sketching together) or **asynchronous review** (stakeholder leaving comments for later)?"

**Cascade**:
- Synchronous → Real-time cursors, presence, conflict resolution
- Asynchronous → Comments, @mentions, notification system

### Example 2: Integration Depth

**Context**: Integrating Board with Forma Design.

**Eigenquestion**:
> "Should Board **embed inside** Forma Design, or **link to** Forma Design?"

**Cascade**:
- Embed → Deep technical integration, shared context, complex dependencies
- Link → Loose coupling, faster development, separate upgrade paths

### Example 3: Global Launch Scope

**Context**: Scope pressure for April 2026 Global Launch.

**Eigenquestion**:
> "Is Global Launch the **beginning** of Board's story (MVP to iterate on) or the **coming out party** (polished showcase)?"

**Cascade**:
- Beginning → Ship core loop, accept rough edges, plan fast follow
- Coming out → Delay if needed, polish matters, first impression critical

---

## Identifying Your Own Eigenquestions

### The Process

1. **List all the questions you want to ask** (brain dump)
2. **For each question, ask**: "If I knew this, what other questions would it answer?"
3. **Rank by leverage**: Which question eliminates the most downstream questions?
4. **Validate**: Is this truly discriminating, or just important?

### Signs You've Found an Eigenquestion

- Answering it feels like it "unlocks" the problem
- You can immediately see how each answer leads to different strategies
- It's uncomfortable—both answers seem reasonable
- It's strategic, not operational

### Signs You Haven't

- It's a "what" question instead of a "which" question
- The answer is obvious once you think about it
- It only affects one downstream decision
- It's asking for information you could look up
