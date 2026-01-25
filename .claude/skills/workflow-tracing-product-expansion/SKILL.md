---
name: workflow-tracing-product-expansion
description: A strategic framework for identifying and launching new product lines by mapping the user's end-to-end journey. Use this when your core product is mature, when users are "hacking" your current tool for unintended use cases, or when you need to expand your TAM without bloating your primary interface.
---

# Workflow-Tracing Product Expansion

This framework shifts the focus from "Total Addressable Market (TAM) chasing" to "Workflow Completion." Instead of building what looks biggest on paper, you build what naturally comes before or after your core product in the user’s daily life. This ensures high retention and a seamless ecosystem.

## The Workflow Tracing Process

### 1. Identify "Adjacency Hacks"
Observe how users are misusing your core product. Look for patterns where users are forcing your tool to do something it wasn't built for.
- **Identify the friction:** Where is the UI becoming "clunky" because of these hacks?
- **Quantify the behavior:** Is this a niche use case or a widespread workaround?
- *Figma Example:* Users were using Figma Design for brainstorming and presentations, even though the tool was optimized for high-fidelity vectors.

### 2. Map the "Idea-to-Product" Journey
Trace the entire lifecycle of a project in your domain. Identify every stage a user goes through and mark where your company is currently absent.
- **Ideation/Brainstorming** (FigJam)
- **Presentation/Pitching** (Figma Slides)
- **High-Fidelity Design** (Figma Design)
- **Developer Handoff/Implementation** (Dev Mode / Dev Mode MCP)
- **Publishing/Shipping** (Figma Sites)

### 3. Make the "Surface vs. Feature" Decision
Decide if the new use case should be a feature inside the current product or a brand-new product surface.
- **When to create a new surface:**
    - The new use case requires a different mental model (e.g., freeform vs. structured).
    - Adding it to the core product would create "Swiss minimalism" bloat.
    - The target persona is different (e.g., Marketing/Brand vs. Product Designers).
- **When to keep it as a feature:**
    - It directly enhances the core loop without adding significant UI complexity.
    - The context-switching cost for the user is too high.

### 4. Inject a "Soul" Differentiator
A new product in a crowded space needs a specific "vibe" or soul to gain traction. Avoid "good enough" or "table stakes" only.
- **Define a non-functional differentiator:** Is it fun? Is it exceptionally fast? Is it highly collaborative?
- *Figma Example:* For FigJam, the differentiator was "Fun" (cursor chat, stamps, high energy) to break the isolation of remote work during COVID.

## Application Examples

### Example 1: Expansion into Presentations
- **Context:** A design tool team notices users creating "slide decks" by manually drawing rectangles and using arrows to navigate.
- **Input:** Observation of high-volume "Presentation" tags in file names.
- **Application:** Instead of adding a "Slide Mode" to the vector tool, create a dedicated surface (Slides) that handles transitions and presenter notes, but allows "Round-tripping" back to the design tool for high-fidelity edits.
- **Output:** A new revenue stream that captures PMs and Executives who never learned the complex design tool.

### Example 2: Bridging to Development
- **Context:** Designers are finished with their work, but developers are struggling to find CSS values and assets.
- **Input:** "View-only" users (developers) are the fastest-growing segment but have the lowest engagement.
- **Application:** Trace the workflow from "Design" to "Code." Build "Dev Mode"—a specialized surface that hides design tools and highlights implementation details (MCPs, API context).
- **Output:** Reduced friction in the handoff process and increased seat expansion within engineering teams.

## Common Pitfalls

- **Sorting by TAM:** Don't just build what has the biggest market on paper (e.g., "We should build a CRM because it's a huge market"). If it doesn't trace the user's existing workflow, the friction of adoption will be too high.
- **Ignoring Tech Debt during Expansion:** Expanding to a second product is the hardest leap. If your core infrastructure is brittle, "moving fast" to launch Product B will grind both products to a halt.
- **The "Good Enough" Trap:** In a mature market, "good enough" is mediocre. If your new expansion doesn't have a "differentiator through craft," users will stick to their existing fragmented tools.
- **Failing to "Detach":** When the mission changes (e.g., from one product to a multi-product platform), ensure the team is re-aligned. Give people the option to opt-out if they aren't interested in the new, high-pace "startup" mode required for expansion.