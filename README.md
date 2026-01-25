# Shannon

**The PM frameworks you already know—applied to your work automatically.**

---

## The Problem I Had

I was explaining the same frameworks to AI every single day.

"Use April Dunford's positioning method." "Apply Shreyas Doshi's LNO prioritization." "Follow the CRAFT email structure." Every conversation started from zero. Generic AI doesn't know the difference between a Working Backwards PRD and a pitch deck. It doesn't know that Radical Candor feedback requires both caring personally and challenging directly.

**I was re-teaching proven methodologies to a tool that should already know them.**

Worse: My outputs were inconsistent. Sometimes I'd remember to apply a framework. Most times I wouldn't. The quality of my work depended on whether I had the mental energy to prompt-engineer that day.

So I built Shannon—a PM system that knows 350+ frameworks from the product leaders I already follow, and applies them without me asking.

---

## What Shannon Does

Shannon is AI pre-loaded with proven PM methodologies. When you draft an email, **CRAFT method** structures it. When you create a PRD, **Working Backwards PR/FAQ** guides you. When you position a product, **April Dunford's 5-step process** applies automatically.

You tell Shannon: **"Use the appropriate skill"** and it selects the right framework for your work.

**No more explaining methodologies. No more inconsistent outputs.**

Your work improves. You notice it first. Then stakeholders start asking what changed.

---

## Who This Is For

You're a product leader. You've read the books—*Inspired*, *Continuous Discovery Habits*, *Obviously Awesome*, *Empowered*. You follow Shreyas Doshi, Teresa Torres, Lenny Rachitsky, Elena Verna.

**You know good product work when you see it.** You just can't produce it consistently under pressure.

Shannon raises your floor. The "quick email to your VP" becomes CRAFT-structured and executive-ready. The "rough positioning doc" follows April Dunford's playbook without you forcing it. The feedback you give your designer applies Radical Candor principles naturally.

**Single-player value first:** Shannon makes *your* work better immediately. Later, you can elevate your entire team. But it starts with you producing consistently excellent output.

---

## Shannon in 30 Seconds

**You:** "Use the appropriate skill to draft an email to my CEO about delaying the Q2 launch"

**Shannon:**
```
Applying CRAFT method for executive communication...

Subject: Q2 Launch → Q3 (Customer Research Gap)

Maya,

**Catch:** We have 47 signups but zero validated use cases. 
If we launch now, we're guessing.

**Reasoning:** Delaying 6 weeks to run discovery sprints with 
10 target customers. Trade-off: Q2 revenue miss, but we avoid 
building the wrong thing.

**Ask:** Your approval to communicate the shift at Friday's 
all-hands.

**Follow-up:** If approved, I'll have revised roadmap and 
customer research plan on your desk Wednesday.

**Timebox:** Need go/no-go by EOD Tuesday to keep eng team 
aligned.
```

✓ Executive-ready. First draft. No second-guessing.

---

## How It Works

### 1. Core Quality Standards (Always On)

Shannon applies product leadership rigor to every output:
- **First principles:** Start with "why" before "what"
- **Trade-off clarity:** Make every decision's cost explicit
- **Outcome focus:** Measure by impact, not activity
- **Stakeholder clarity:** Every output has a clear next action

You get the "senior PM review" automatically.

### 2. 350+ Proven Frameworks (On-Demand)

Shannon knows methodologies from the PMs you already learn from:

**Strategy & Planning:**
- Three Pillar Strategy (vision, bets, roadmap)
- Opportunity Solution Trees (Teresa Torres)
- Jobs-to-be-Done Analysis
- OKRs with Radical Focus 

**Execution & Delivery:**
- Shape Up Pitches (Ryan Singer/Basecamp)
- Working Backwards PR/FAQ (Amazon)
- Now/Next/Later Roadmapping
- Trade-off Sliders

**Product-Led Growth:**
- PLG Activation Funnels 
- First Mile Experience (Lazy/Vain/Selfish)
- Retention Mechanics & Habit Loops
- North Star Metric Frameworks

**Communication:**
- CRAFT Method (Concise Executive Emails)
- Radical Candor Feedback 
- Strategic Narrative Framework
- Eigenquestions 
**Go-to-Market:**
- Product Positioning 
- Crossing the Chasm 
- Category Design
- Beachhead Market Selection

**Discovery & Research:**
- Continuous Discovery Habits (Teresa Torres)
- Customer Interview Best Practices
- Hypothesis-Driven Validation
- Jobs-to-be-Done Research

*Full list: [Browse 350+ skills](.claude/skills/)*

**The key:** You don't choose frameworks manually. You tell Shannon **"use the appropriate skill"** and it selects the right methodology for your request.

### 3. Personal Context Layer

Shannon learns your context once (2-minute setup):
- Your name, role, product
- Your team structure and stakeholders
- Communication preferences
- Company terminology

Stored in `.claude/CLAUDE.local.md` (gitignored for privacy).

Every response uses your context. No re-explaining who your CEO is or what product you work on.

### 4. Living Initiative Memory

Each major project gets its own folder with a `CLAUDE.md` brain that Shannon maintains automatically:

```
Initiatives/
└── enterprise-tier/
    ├── CLAUDE.md          # Auto-maintained: decisions, timeline, blockers
    ├── prd.md
    ├── positioning.md
    └── research/
```

**What Shannon tracks:**
- Decisions made and why
- Trade-offs accepted
- Documents created
- Current blockers
- Open questions

Three weeks later: *"Why did we decide on async instead of real-time collaboration?"*

Shannon reads `CLAUDE.md` and tells you exactly why—with the original reasoning, trade-offs, and data.

**You never lose context. You never rehash decisions.**

---

## Real Examples

### Draft a PRD → Working Backwards
**You:** "Use the appropriate skill to create a PRD for enterprise SSO"  
**Shannon:** Applies Amazon's PR/FAQ format—starts with customer benefit, asks clarifying questions, then writes customer-centric documentation before features.

### Prioritize Tasks → LNO Framework
**You:** "Use the appropriate skill—I have 18 tasks, what should I focus on?"  
**Shannon:** Applies Shreyas Doshi's LNO framework—categorizes into Leverage (outsized impact), Neutral (important but not urgent), and Overhead (delegate or kill). Clear priorities based on impact.

### Position Your Product → April Dunford
**You:** "Use the appropriate skill to position our API analytics tool against Datadog"  
**Shannon:** Walks through Obviously Awesome's 5 steps—competitive alternatives, unique attributes, value translation, target segment, market category. Produces differentiated positioning statement.

### Give Feedback → Radical Candor
**You:** "Use the appropriate skill to give feedback about John missing sprint commitments"  
**Shannon:** Applies Kim Scott's Radical Candor—balances caring personally with challenging directly. Creates script that's direct but respectful, builds trust while solving problems.

---

## Quick Start

```bash
# 1. Clone and open in Cursor
git clone https://github.com/samarv/shannon.git shannon
cd shannon
cursor .

# 2. Create your personal context file
cp .claude/CLAUDE.local.example.md .claude/CLAUDE.local.md
# Edit with your name, role, product, team (2 minutes)

# 3. Make your first request
"Use the appropriate skill to draft an email about Q1 roadmap 
priorities to my leadership team"

# Done. Shannon selects the right framework and applies it.
```

---

## Customizing Shannon for Your Company

Shannon ships with 350+ universal PM frameworks. But your company has its own SOPs, templates, and standards.

**Shannon is fully customizable:**

### Add Your Company's Content

Create a `content/` folder with:
- **Templates**: Your PRD template, roadmap format, OKR structure
- **Brand Voice**: Your company's writing style and terminology
- **Org Data**: Colleague names, team structure, stakeholder map
- **Quality Standards**: Your company's definition of "good enough"

Shannon discovers and applies these automatically. Company content *extends* core frameworks—it doesn't replace them.

### Add Custom Skills

Your company has proprietary frameworks? Add them:

```bash
# Create a new skill
mkdir .claude/skills/our-launch-process
touch .claude/skills/our-launch-process/SKILL.md

# Document your methodology
# Shannon discovers it automatically
```

No coding. Just document your process in markdown. Shannon applies it.

### Resolution Order

Shannon always prefers your company's standards:
1. `.claude/CLAUDE.local.md` (your personal preferences)
2. `content/` (your company's content pack)
3. `.claude/defaults/` (Shannon's built-in frameworks)

**Result:** Shannon speaks your company's language while applying universal PM best practices.

---

## From Single-Player to Team Adoption

### Phase 1: You (Week 1)
- Clone Shannon
- Add personal context
- Produce better work immediately
- Stakeholders notice quality improvement

### Phase 2: Prove Value (Weeks 2-4)
- Use Shannon for high-stakes work (board decks, strategy docs)
- Share outputs with leadership
- Hear: *"This is the clearest positioning I've seen from our team"*

### Phase 3: Team Rollout (Month 2)
- Share your `.claude/` setup (not CLAUDE.local.md—that's personal)
- Create shared `content/` pack with company templates
- Team members clone and customize
- Collective PM practice improves

### Phase 4: Standard Operating System (Month 3+)
- Shannon becomes how your team works
- New PMs onboard faster (frameworks built-in)
- Entire team speaks the same methodological language
- You're known as the PM who elevated the practice

**But it starts with you.** Get better first. Prove it works. Then scale.

---

## What Makes Shannon Different

### 1. Frameworks, Not Generic Advice
Every output applies a proven methodology. You don't get "here are some ideas"—you get Teresa Torres' opportunity mapping or Kim Scott's Radical Candor applied systematically.

### 2. Quality Gates Always Active
Five-step validation before every output:
- Does it answer "Why does this matter to customers?"
- Are trade-offs explicitly stated?
- Are success metrics defined?
- Can stakeholders take clear action?
- Would this pass senior leadership review?

### 3. Context Persists
Shannon remembers your decisions, your team, your product. No re-explaining. No starting from zero every conversation.

### 4. Credibility by Association
When you apply April Dunford's positioning or Amazon's Working Backwards, stakeholders recognize best practices. Your work carries the weight of proven methodologies.

### 5. Raises the Bar for "Good"
Shannon makes excellence your default. A "quick email" becomes CRAFT-structured. A "rough draft" follows rigorous frameworks. **Your floor becomes higher than most PMs' ceiling.**

---

## Common Questions

**Q: Do I have to memorize 350 frameworks?**
No. Tell Shannon **"use the appropriate skill"** and it selects the right one for your request. You benefit from frameworks without studying them.

**Q: Can I still choose a specific framework?**
Yes. Say *"Use Radical Candor to draft feedback"* or *"Apply April Dunford's positioning framework using claude/skills"* Shannon gives you control when you want it.

**Q: What if my company uses different terminology?**
Customize `content/` with your company's templates, voice, and standards. Shannon adapts to your organization's language.

**Q: What gets shared if I commit this to git?**
Everything except `.claude/CLAUDE.local.md` (personal context is gitignored). Share core frameworks, keep personal details private.

**Q: Is this just fancy prompt engineering?**
No. Shannon is a systematic framework application system with quality gates, living initiative memory, auto-selection logic, and 350+ validated methodologies. Prompts give suggestions. Shannon applies proven processes.

**Q: How do I add my company's proprietary frameworks?**
Use .claude/skills/skill-creator to create your new skill and document your process. Shannon discovers it automatically. [Guide in CONTRIBUTING.md](CONTRIBUTING.md)

---

## What's Included

📚 **Core PM Philosophy** (Always Active)
- Shreyas Doshi's first principles thinking
- Five quality gates
- Trade-off analysis framework
- Eigenquestion context gathering

🎯 **350+ Proven Frameworks** (Auto-Select)
- Strategy: OKRs, North Star, Opportunity Solution Trees
- Execution: Shape Up, Working Backwards, Now/Next/Later
- Growth: PLG, First Mile, Retention Mechanics
- Communication: CRAFT, Radical Candor, Strategic Narratives
- GTM: Positioning, Crossing the Chasm, Category Design
- Discovery: Continuous Discovery, JTBD, Customer Interviews

🤖 **Specialized Sub-Agents**
- Marketing Copywriter (11 brand/copy frameworks)
- Product Onboarding Specialist (5 activation frameworks)
- Meeting Analyzer (transcript synthesis)
- Executive Reviewer (strategic alignment)

📖 **Living Documentation**
- Initiative auto-tracking (decisions, timeline, blockers)
- Context persistence across conversations
- Decision rationale capture

🎨 **Customization System**
- Company content packs (templates, voice, standards)
- Custom skill creation
- Organizational adaptation

---

## Learn More

**📚 Browse Frameworks**
Explore [`.claude/skills/`](.claude/skills/) to see all 350+ methodologies with application protocols and examples.


**🏗️ Advanced Customization**
[ADVANCED.md](ADVANCED.md) covers content packs, custom skills, team collaboration, and organizational adaptation.

**🔧 Technical Architecture**
[ARCHITECTURE.md](ARCHITECTURE.md) explains Shannon's framework selection, quality gates, and content resolution system.

**🤝 Contribute New Frameworks**
[CONTRIBUTING.md](CONTRIBUTING.md) shows how to document and share new PM methodologies.

---

## License

MIT License - See [LICENSE](LICENSE)

**Framework Attribution:** Every skill credits its original creator. Shannon applies methodologies—it doesn't claim to invent them. See [Attribution.md](Attribution.md) for full credits.

---

**Ready to raise your bar?**

```bash
git clone https://github.com/samarv/shannon.git shannon
cd shannon
cursor .
```

Ask Shannon: *"Use the appropriate skill"* and watch proven frameworks activate.
