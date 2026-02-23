# Shannon

**PM Best Practices applied automatically.**

330+ frameworks from Lenny's Podcast, Teresa Torres, and April Dunford. Practical skills for decks, docs, and code. A system that learns your context and scales with your team.

| What's Included | Examples |
|-----------------|----------|
| **PM Frameworks** | CRAFT emails, Radical Candor, Working Backwards PRDs, LNO prioritization |
| **Practical Skills** | PowerPoint generation, GitHub code search, PDF/Excel processing |
| **Extensibility** | Skill Creator for custom frameworks, Sub-Agent Creator for workflows |
| **Memory** | Brains that track decisions, personal context that persists |

Shannon isn't a prompt library. It's bundled PM best practices that adapt to how you work.

---

## What You Get

You tell Shannon what you need. Shannon applies the right framework.

| Your Request | Shannon Applies |
|--------------|-----------------|
| "Create a leadership review deck for Q1. Use appropriate skills" | PPTX skill → branded PowerPoint with executive narrative structure |
| "I have 23 tasks this week. What should I focus on? Use appropriate skills" | LNO framework → Leverage, Neutral, Overhead prioritization |
| "Find how authentication works across our repos. Use appropriate skills" | GitHub Code Context skill → searches code across repositories |
| "Draft an email to my CEO about delaying launch. Use appropriate skills" | CRAFT method → executive-ready communication |
| "Synthesize these 40 customer quotes into insights. Use appropriate skills" | Jobs-to-be-Done analysis + opportunity framing |

**No prompt engineering. No re-explaining frameworks. Just results.**

---

## The Problem Shannon Solves

You know what good PM work looks like. You've read the books, listened to the podcasts, saved the frameworks.

But when it's 4pm and you need to send that exec update, you don't pull out April Dunford's positioning template. You just write something and hope it lands.

**Best practices exist. They just don't get applied.**

Generic AI makes this worse. It doesn't know that CRAFT emails lead with the ask. It doesn't know Radical Candor requires caring personally *and* challenging directly. It treats every PRD like a feature list.

Shannon fixes this. 330+ best practices from the PM leaders you already follow—pre-loaded and auto-selected based on your request.

---

## How It Works

You say: **"Use the appropriate skill"**

Shannon reads your request, selects the right methodology from 330+ options, and applies it. You don't memorize frameworks. You don't prompt-engineer. You get senior PM-quality output on the first draft.

---

## Works With Your AI Coding Tool

Shannon works with any AI coding assistant that supports markdown context files:

| Tool | Setup Complexity | Notes |
|------|------------------|-------|
| **Cursor** | Medium | Enable CLAUDE.md in settings, create symlinks |
| **Claude Code** | Easy | Native `.claude/` support, no extra config |
| **VS Code + Claude** | Medium | Configure extension settings |
| **Windsurf** | Medium | Similar to Cursor setup |
| **Google Project IDX** | Medium | Configure workspace settings |
| **Zed** | Medium | Configure assistant settings |

**The core workflow is identical across all tools:**
1. Add your content files to the chat context
2. Reference the skills folder so Shannon can auto-select frameworks
3. Tell Shannon what you need
4. Review and keep (or undo) the generated output

Setup instructions for each tool are in the [Setup Guide](#setup-guide) below.

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

### 2. 330+ Proven Frameworks (On-Demand)

Shannon knows methodologies from the PM leaders you already learn from:

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

*Full list: [Browse 330+ skills](.claude/skills/)*

**The key:** You don't choose frameworks manually. You tell Shannon **"use the appropriate skill"** and it selects the right methodology for your request.

### 3. Personal Context Layer

Shannon learns your context once (2-minute setup):
- Your name, role, product
- Your team structure and stakeholders
- Communication preferences
- Company terminology

Stored in `CLAUDE.local.md` (gitignored for privacy).

Every response uses your context. No re-explaining who your CEO is or what product you work on.

### 4. Living Brain Memory

Each major project gets its own Brain -- a knowledge context that actively accumulates and connects information:

```
Brains/
└── enterprise-tier/
    ├── CLAUDE.md          # Auto-maintained: decisions, timeline, blockers, connections
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

## Setup Guide

**Time required:** 15-20 minutes

### Prerequisites

- An AI coding assistant (Cursor, Claude Code, VS Code + Claude, Windsurf, etc.)
- GitHub account (optional—only needed for team collaboration)

### Step 1: Download Shannon

**Option A: Download ZIP (Recommended for beginners)**
1. Go to the repository page
2. Click the green "Code" button
3. Select "Download ZIP"
4. Extract to your projects folder (e.g., `~/Projects/shannon`)

**Option B: Git Clone**
```bash
git clone https://github.com/samarv/shannon.git shannon
cd shannon
```

### Step 2: Open in Your AI Coding Tool

| Tool | How to Open |
|------|-------------|
| **Cursor** | File → Open Folder → Select shannon folder |
| **Claude Code** | `cd shannon && claude` |
| **VS Code** | File → Open Folder → Select shannon folder |
| **Windsurf** | File → Open Folder → Select shannon folder |

### Step 3: Enable CLAUDE.md Context (Tool-Specific)

**Cursor:**
1. Open Cursor → Settings → Cursor Settings
2. Navigate to "Rules and Commands"
3. Enable "Include CLAUDE.md in context"
4. (Recommended) Go to Agents → Set "Run everything in sandbox" to "Auto run in sandbox"

**Claude Code:**
- No action needed. Claude Code natively supports `.claude/` folders.

**VS Code + Claude Extension:**
- Configure the Claude extension to include workspace context files.

**Other Tools:**
- Check your tool's documentation for markdown context file support.

### Step 4: Create Symlinks (Cursor and Some Tools)

Some tools require files at the repository root level. Run these commands in your terminal:

```bash
# Navigate to shannon folder first
cd /path/to/shannon

# Create symlinks
ln -s .claude/CLAUDE.md CLAUDE.md
ln -s .claude/CLAUDE.local.md CLAUDE.local.md
```

Two new files will appear at root level. These are shortcuts that help your tool find Shannon's configuration.

**Note:** Claude Code users can skip this step—it reads from `.claude/` directly.

### Step 5: Create Your Personal Context

1. Copy the example file:
   ```bash
   cp .claude/claude.local.md .claude/CLAUDE.local.md
   ```

2. Open `.claude/CLAUDE.local.md` and fill in:
   - Your name and role
   - Your team and manager
   - Your product/company
   - Communication preferences

3. Save the file (Cmd+S / Ctrl+S)

This file is gitignored—your personal details stay private.

### Step 6: Verify Your Setup

In your AI assistant's chat, ask:

> "What is my name and role according to CLAUDE.local.md?"

If Shannon responds with your information, setup is complete.

**Optional:** Check if Python is installed (enables PDF/Word processing):
> "Do I have Python installed?"

### Step 7: Make Your First Request

```
Use the appropriate skill to draft an email about Q1 roadmap 
priorities to my leadership team
```

Shannon will select the CRAFT email framework and generate an executive-ready email.

---

## How to Use Shannon

### Adding Context to Your Request

Shannon only knows what you explicitly add to the conversation context:

1. **Add your content files:** Drag files from the sidebar into the chat context area (don't rely on search—it may not find all files)
2. **Add the skills folder:** Include `.claude/skills/` so Shannon can auto-select the right framework
3. **Write your request:** Be specific about what you need

**Important:** Files don't auto-sync. You must add them to context each time you start a new conversation.

### Choosing a Mode

Most AI coding tools offer different interaction modes:

| Mode | When to Use |
|------|-------------|
| **Plan Mode** | Complex tasks where you want to review what Shannon will do before it executes. Recommended for PRDs, strategy docs, and multi-step work. |
| **Agent Mode** | Straightforward tasks where you want immediate execution. Good for quick emails, feedback scripts, prioritization. |
| **Ask Mode** | When you want to explore or ask questions without Shannon making changes. |

**Recommendation:** Start with Plan mode until you're comfortable with Shannon's outputs.

### Choosing a Model

| Model | Quality | Cost/Limits | Best For |
|-------|---------|-------------|----------|
| **Claude Opus** | Highest | Usage limits apply | High-stakes strategy docs, board decks |
| **Claude Sonnet** | High | Fewer limits | Daily work (recommended default) |
| **Auto** | Variable | No limits | Quick tasks, exploration |

### Reviewing Output

After Shannon generates content:

1. **Review the output carefully.** Shannon applies frameworks, but you own the final quality.
2. Click **"Keep"** to save the file, or **"Undo"** to discard it.
3. If you click Undo, the file disappears—it's not saved anywhere.

**Critical:** Always validate outputs before building on them. Small errors compound quickly when you iterate on unreviewed content.

### Quality Validation Checklist

Before clicking "Keep," verify:
- [ ] Output makes sense given your inputs
- [ ] Content aligns with your source documents
- [ ] No hallucinated facts or filled-in assumptions
- [ ] Framework was applied correctly (check structure)
- [ ] Would pass review by your stakeholders

---

## Working with Content

### File Format Support

| Format | Support | Notes |
|--------|---------|-------|
| **Markdown (.md)** | Best | Native support, no processing needed |
| **Plain text (.txt)** | Best | Native support |
| **PDF** | Works | Requires Python installed |
| **Word (.docx)** | Works | Requires Python installed |
| **PowerPoint (.pptx)** | Works | Requires Python installed |
| **Excel (.xlsx)** | Works | Requires Python installed |
| **Raw transcripts** | Avoid | Too noisy—synthesize into notes first |

**Recommendation:** When possible, convert or extract content to markdown before adding to Shannon. This produces the most reliable results.

### Context Size Best Practices

- **Keep files under 2,000 lines** when possible. Very large files (measured in KB) should be broken down or summarized first.
- **Synthesize before analyzing:** Meeting notes outperform raw transcripts. Shannon works better with smaller, focused inputs.
- **One topic per conversation:** For complex projects, break work into focused sessions rather than overloading a single context.

### Where Files Get Saved

- **Default location:** `output/` folder
- **Specify location in prompt:** "Save to Brains/my-project/"
- **Move after generation:** You can always move files manually after clicking "Keep"

### Adding Company Knowledge

Store your company's reference material in `input/`:
- User research summaries
- Product vision documents
- Analytics dashboards (exported)
- Competitive analysis
- Customer quotes and feedback

Shannon discovers and uses this content when you add it to your conversation context.

---

## Customizing Shannon for Your Company

Shannon ships with 330+ universal PM frameworks. But your company has its own SOPs, templates, and standards.

**Shannon is fully customizable:**

### Add Your Company's Content

Add to the `input/` folder:
- **Templates**: Your PRD template, roadmap format, OKR structure
- **Brand Voice**: Your company's writing style and terminology
- **Org Data**: Colleague names, team structure, stakeholder map
- **Quality Standards**: Your company's definition of "good enough"

Shannon discovers and applies these automatically. Input *extends* core frameworks—it doesn't replace them.

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
2. `input/` (your input pack)
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
- Create shared `input/` pack with company templates
- Team members clone and customize
- Collective PM practice improves

### Phase 4: Standard Operating System (Month 3+)
- Shannon becomes how your team works
- New PMs onboard faster (frameworks built-in)
- Entire team speaks the same methodological language
- You're known as the PM who elevated the practice

**But it starts with you.** Get better first. Prove it works. Then scale.

---

## Realistic Timeline Expectations

Shannon saves time long-term, but expect an investment period where you're learning the system and validating outputs.

| Phase | Time | What Happens |
|-------|------|--------------|
| **Initial setup** | 1-2 hours | Repository configured, personal context created, first request made |
| **First value** | Day 1 | Use existing skills for emails, feedback, prioritization |
| **Learning curve** | Week 1 | Understand how to add context, when to use Plan vs Agent mode |
| **Skill validation** | Weeks 1-2 | Test which skills produce quality output for your specific context |
| **Custom skills** | Weeks to months | Build and validate company-specific frameworks |
| **Full proficiency** | 2-3 months | Shannon becomes a natural extension of your workflow |

### Why Validation Takes Time

- **Every output needs review.** Shannon applies frameworks, but you're responsible for final quality.
- **Context matters.** A skill that works great for one PM's use case might need adjustment for yours.
- **Errors compound.** If you iterate on unvalidated outputs, small mistakes become big problems.

### How to Measure Success

Track these indicators to know Shannon is working:
1. **Fewer iterations needed** to get acceptable output
2. **Less editing required** when stakeholders review your documents
3. **Consistent quality** across different types of work
4. **Time saved** on framework application (you're not re-explaining methodologies)

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

## Understanding Skills and Agents

Shannon includes two types of reusable components: **Skills** and **Agents**. Understanding the difference helps you use the right tool for each task.

### Skills (Single-Task Frameworks)

A **skill** is one reusable prompt that applies a specific methodology to your work.

- **Examples:** CRAFT email method, April Dunford positioning, Radical Candor feedback, Shape Up pitches
- **Location:** `.claude/skills/`
- **How to use:** Add the skills folder to your context, then say "use the appropriate skill"
- **When to use:** Single-step tasks like drafting an email, giving feedback, positioning a feature

Shannon reads the name and description of each skill (not the full content) and selects the most appropriate one for your request.

### Agents (Multi-Step Workflows)

An **agent** is a collection of skills orchestrated to accomplish a larger workflow.

- **Examples:** Meeting Analyzer (transcribe → extract decisions → route to Brains), Growth Experiment Designer (research → hypothesis → test plan)
- **Location:** `.claude/agents/`
- **How to use:** Reference the specific agent folder in your context
- **When to use:** Complex multi-step processes where multiple frameworks need to work together

### Which Should You Use?

| Task Type | Use |
|-----------|-----|
| Draft an email | Skill |
| Give feedback | Skill |
| Position a product | Skill |
| Analyze a meeting and update all relevant Brains | Agent |
| Design an experiment with research, hypothesis, and test plan | Agent |
| Synthesize user research across multiple sources | Agent |

**Start with skills.** They're simpler and cover most PM tasks. Graduate to agents once you're comfortable with how skills work.

---

## Common Questions

### Setup & Requirements

**Q: Do I need GitHub?**
No—not for individual use. GitHub is only necessary if you want to share your setup with teammates or sync across multiple computers. For solo use, everything stays on your local machine.

**Q: Do I need to know how to code?**
No. While Shannon uses technical tools like Git and terminal commands during setup, you don't need coding skills. The system is designed for product managers to use natural language.

**Q: Which AI coding tool should I use?**
Any tool that supports markdown context files works. Cursor and Claude Code are the most tested. Choose based on your preference—the core Shannon workflow is identical across tools.

### Using Shannon

**Q: Do I have to memorize 330 frameworks?**
No. Tell Shannon **"use the appropriate skill"** and it selects the right one for your request. You benefit from frameworks without studying them.

**Q: Can I still choose a specific framework?**
Yes. Say *"Use Radical Candor to draft feedback"* or *"Apply April Dunford's positioning framework"*. Shannon gives you control when you want it.

**Q: Should I use Plan mode or Agent mode?**
Use **Plan mode** for complex tasks where you want to review what Shannon will do before it executes. Use **Agent mode** for straightforward tasks where you want immediate execution. When in doubt, start with Plan mode.

**Q: How does Shannon choose which skill to use?**
When you add the skills folder to your context, Shannon reads the name and description of each skill (not the full content) and selects the most appropriate one based on your prompt. Make your request specific to get better skill selection.

### Files & Output

**Q: Where do generated files get saved?**
By default, files save to the `output/` folder. You can specify a different location in your prompt ("Save to Brains/my-project/") or move files manually after generation.

**Q: What happens if I click Undo?**
The file is not saved and disappears. Use Undo when the output isn't what you wanted. Only click Keep when you're satisfied with the result.

**Q: Do files automatically sync into Shannon's knowledge?**
No. Files only become part of Shannon's context when you explicitly add them to the conversation. If you add files to the input folder, you must add them to your chat context to use them.

**Q: What file formats work best?**
Markdown (.md) is best because it's plain text. PDFs and Word documents work but require Python installed. When possible, convert or extract content to markdown first.

### Quality & Validation

**Q: How do I know if a skill was applied correctly?**
Validate by reviewing the output. Check if it matches your expectations, uses the right framework structure, and includes the information you wanted. If not, refine your prompt or explicitly name the skill you want.

**Q: How do I prevent errors from accumulating?**
Always review and validate outputs before saving. Sample-check generated content against source material. Don't let multiple iterations build on unverified outputs—errors compound quickly.

### Customization & Sharing

**Q: What if my company uses different terminology?**
Customize `input/` with your company's templates, voice, and standards. Shannon adapts to your organization's language.

**Q: What gets shared if I commit this to git?**
Everything except `.claude/CLAUDE.local.md` (personal context is gitignored). Share core frameworks, keep personal details private.

**Q: How do I add my company's proprietary frameworks?**
Use `.claude/skills/skill-creator` to create your new skill and document your process. Shannon discovers it automatically. [Guide in CONTRIBUTING.md](Shanon-Docs/CONTRIBUTING.md)

**Q: Is this just fancy prompt engineering?**
No. Shannon is a systematic framework application system with quality gates, living Brain memory, auto-selection logic, and 330+ validated methodologies. Prompts give suggestions. Shannon applies proven processes.

---

## What's Included

📚 **Core PM Philosophy** (Always Active)
- Shreyas Doshi's first principles thinking
- Five quality gates
- Trade-off analysis framework
- Eigenquestion context gathering

🎯 **330+ Proven Frameworks** (Auto-Select)
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
- Brain auto-tracking (decisions, timeline, blockers)
- Context persistence across conversations
- Decision rationale capture

🎨 **Customization System**
- Company content packs (templates, voice, standards)
- Custom skill creation
- Organizational adaptation

---

## Troubleshooting

### CLAUDE.md Not Being Read

**Symptoms:** Shannon doesn't know your context, asks for information you've already provided in CLAUDE.local.md.

**Solutions:**
1. **Check settings:** In Cursor, verify "Include CLAUDE.md in context" is enabled
2. **Check symlinks:** Run `ls -la` at root level—you should see `CLAUDE.md -> .claude/CLAUDE.md`
3. **Recreate symlinks:** If missing, run the symlink commands from [Step 4](#step-4-create-symlinks-cursor-and-some-tools)

### Can't Find Files When Adding Context

**Symptoms:** Search doesn't show your files when you try to add them to context.

**Solution:** Drag and drop files from the left sidebar directly into the chat context area. Don't rely on the search function—it may not index all files.

### Output Quality Is Inconsistent

**Symptoms:** Some outputs are great, others miss the mark or seem generic.

**Solutions:**
1. **Reduce context size:** Too much information confuses Shannon. Keep files under 2,000 lines.
2. **Be more specific:** Instead of "write a PRD," try "use the appropriate skill to write a PRD for [specific feature] targeting [specific user]"
3. **Synthesize inputs first:** Don't feed raw transcripts—create meeting notes first, then analyze the notes.
4. **Add the skills folder:** Make sure `.claude/skills/` is in your context so Shannon can select frameworks.

### Skills Not Being Selected

**Symptoms:** Shannon gives generic responses instead of applying a specific framework.

**Solutions:**
1. **Add skills folder to context:** You must include `.claude/skills/` in your conversation
2. **Use the magic phrase:** Include "use the appropriate skill" in your request
3. **Be explicit:** If auto-selection isn't working, name the skill: "Use the CRAFT email skill"

### PDF/Word Files Not Processing

**Symptoms:** Error messages when trying to read PDF, Word, or PowerPoint files.

**Solution:** Install Python. Ask Shannon: "Do I have Python installed?" and follow the instructions to install it.

### Generated Files Disappearing

**Symptoms:** Files you thought you saved aren't in your project.

**Explanation:** You likely clicked "Undo" instead of "Keep." When you click Undo, the file is discarded—it's not saved anywhere. Always click "Keep" to save generated content.

---

## Learn More

**📚 Browse Frameworks**
Explore [`.claude/skills/`](.claude/skills/) to see all 330+ methodologies with application protocols and examples.

**🏗️ Advanced Customization**
[ADVANCED.md](Shanon-Docs/ADVANCED.md) covers content packs, custom skills, team collaboration, and organizational adaptation.

**🔧 Technical Architecture**
[ARCHITECTURE.md](Shanon-Docs/ARCHITECTURE.md) explains Shannon's framework selection, quality gates, and content resolution system.

**🤝 Contribute New Frameworks**
[CONTRIBUTING.md](Shanon-Docs/CONTRIBUTING.md) shows how to document and share new PM methodologies.

---

## License

MIT License - See [LICENSE](LICENSE)

**Framework Attribution:** Every skill credits its original creator. Shannon applies methodologies—it doesn't claim to invent them. See [Attribution.md](Shanon-Docs/Attribution.md) for full credits.

---

**Ready to raise your bar?**

```bash
git clone https://github.com/samarv/shannon.git shannon
cd shannon
cursor .
```

Ask Shannon: *"Use the appropriate skill"* and watch proven frameworks activate.
