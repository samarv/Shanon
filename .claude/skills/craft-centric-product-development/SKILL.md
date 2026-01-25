---
name: craft-centric-product-development
description: A framework for building high-quality, opinionated software by prioritizing taste, "Main Quests," and direct user empathy over metrics and A/B testing. Use this when entering a crowded market where design is a differentiator, or when restructuring teams to increase individual agency and output quality.
---

# Craft-Centric Product Development

In crowded markets, design and craft are the primary differentiators. This framework replaces traditional metrics-driven management with a focus on "taste," opinionated defaults, and high-agency project teams. It treats software quality as a retention and trust mechanism rather than a conversion optimization problem.

## The Strategic Framework

### 1. Identify the "Main Quest"
Maintain ruthless focus by categorizing every potential task as either a **Main Quest** or a **Side Quest**.
- **Main Quest:** Tasks that directly progress the core product value and solve primary customer problems.
- **Side Quest:** Tasks that feel productive but don't move the needle (e.g., custom swag, prematurely optimizing legal/security docs, unnecessary process meetings).
- **Rule:** If a task does not progress the Main Quest, ignore it or defer it.

### 2. Build Opinionated Software
Avoid the "flexible software" trap which forces users to spend time configuring tools rather than doing work.
- **Design for someone, not everyone:** Generalized solutions are weak. 
- **Set strong defaults:** Choose one optimized workflow and build the product around it.
- **Reduce choice architecture:** Minimize settings and configuration options to reduce user friction.

### 3. Balance "Magic and Science"
- **The Science:** Constant user empathy. Everyone (including engineers and CEOs) must answer customer Slack messages and support tickets to build a deep, intuitive understanding of the problem space.
- **The Magic:** Using that intuition to make decisions. Avoid using A/B tests or data to "make the choice for you." If the data says one thing but your product intuition says another, trust the intuition and be willing to fix mistakes later.

## Execution Workflow

### Project Team Structure
Discard durable, cross-functional teams in favor of fluid, project-based units.
- **Composition:** Small teams (typically 1-3 people) consisting only of Engineering and Design.
- **Leadership:** Assign a "Project Lead" (can be an Engineer or Designer) responsible for scoping, communication, and timelines.
- **The "Overlapping Skills" Rule:** Hire "T-shaped" individuals. Engineers must have product sense; Designers must understand technical constraints. Avoid specialists who say, "That's not my job."

### The "Internal-to-Public" Shipping Cycle
Instead of perfecting a design in isolation, move into production immediately.
1.  **Production Prototype (Week 1):** Get a rough version into the live app, visible only to the internal team.
2.  **Customer Opt-in:** Release to 1-10 "co-creation" customers who are willing to use a janky version in exchange for early access.
3.  **Intuitive Review:** The CEO or Lead Designer tests the feature manually. Look for "paper cuts" (janky animations, misaligned scrolling, friction points).
4.  **General Release:** Polish the craft (UI/UX details) only after the core concept is proven in the internal/opt-in phases.

### Automated Cycles
Use "Cycles" instead of "Sprints."
- **Automation:** Cycles should start and end on a fixed, automated schedule (e.g., every 1 or 2 weeks).
- **No Manual Setup:** Remove the overhead of "planning meetings."
- **Focus:** The cycle is a boundary. Once it starts, the team focuses only on the selected tasks, ignoring the infinite backlog.

## Examples

**Example 1: Feature Ownership**
*   **Context:** Improving the navigation of a complex sub-menu system.
*   **Input:** A standard vertical list of menu items.
*   **Application:** An engineer notices that users often "miss" sub-menus because they don't move their mouse in a perfect horizontal line. Instead of waiting for a PM ticket, the engineer implements "dynamic safe zones" (triangular hover areas) that allow for diagonal mouse movement.
*   **Output:** A high-quality "invisible" feature that makes the app feel "smooth" and "expensive."

**Example 2: Scoping a New Feature (Project Updates)**
*   **Context:** Users need a way to communicate project status (Red/Yellow/Green).
*   **Input:** A request for a robust reporting suite with search, filters, and automated emails.
*   **Application:** The team applies "Opinionated Software" principles. They launch a simple text field with a status color picker inside the existing project view. They defer the "Side Quests" (search/filtering/email digests) until they see if users actually adopt the core status-update behavior.
*   **Output:** A 2-week build that solves the immediate need without bloating the codebase.

## Common Pitfalls

- **Using Data as a Crutch:** Using metrics to avoid making a hard decision. If you find yourself saying, "Let's wait for the data," you are likely lacking enough user empathy to make an intuitive choice.
- **The "Everything for Everyone" Trap:** Trying to win a deal by adding a feature that violates your product's core opinions. It is better to lose a customer who doesn't fit your workflow than to ruin the workflow for everyone else.
- **Over-Specialization:** Hiring PMs or Managers too early who "manage the tool" instead of building the product. This creates a disconnect between decision-making and execution.
- **Polishing Too Early:** Spending weeks on UI mocks before seeing how the feature feels in a live production environment. Quality comes from iterating on the *feel* of the software, not the *look* of a static design.