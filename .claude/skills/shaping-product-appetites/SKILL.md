---
name: shaping-product-appetites
description: A framework for defining product features within a fixed time budget (appetite). Use this when projects are consistently dragging, when there is a "wall" between design and engineering, or when you want to replace dense PRDs and high-fidelity mockups with actionable, de-risked concepts.
---

# Shaping Product Appetites

This framework shifts product development from "estimating how long a feature will take" to "deciding how much time we are willing to spend" (the Appetite). It ensures that by the time a project reaches the build phase, the major "rabbit holes" and "time bombs" have been cleared by a collaborative triad of Product, Design, and Engineering.

## Core Principles
- **Fixed Time, Variable Scope**: You commit to a time box (usually 2, 4, or 6 weeks) and adjust the feature's complexity to fit that box.
- **The Triad**: Shaping must involve Product (business context), Design (user flow), and Engineering (technical feasibility) simultaneously.
- **Fat Marker Fidelity**: Ideas are sketched at a level that is "sharp enough to understand, but fuzzy enough to leave room for the builders' creativity."

## The Shaping Workflow

### 1. Frame the Problem
Narrow the scope to a specific, valuable problem rather than a generic feature.
- **Bad Frame**: "Build a calendar."
- **Good Frame**: "Users need to see empty spaces to book appointments because the current agenda view only shows scheduled items."

### 2. Set the Appetite
Determine the "budget" for the solution.
- **Small Batch**: 1–2 weeks for minor improvements.
- **Big Batch**: 4–6 weeks for significant features.
- *Constraint*: If it takes longer than 6 weeks, it cannot be "seen from the beginning." Break it down into smaller, independently shippable shaped pieces.

### 3. Conduct the Shaping Session
Bring the triad (PM, Designer, Senior Engineer) into a room with a whiteboard (physical or digital).
- **Identify Rabbit Holes**: The "grumpy old plumber" (Engineer) should look at the code/infrastructure during the session to identify hidden complexities.
- **Breadboarding**: Map out the flow using only text and arrows (e.g., [Button: Create Event] -> [Form: Event Details] -> [Success Message]).
- **Fat Marker Sketching**: Use thick lines to draw the UI. If you can't draw the idea with a "fat marker," you are getting too detailed and micromanaging the build team.

### 4. Define the Moving Parts
A well-shaped project should have **fewer than 10 moving pieces**. 
- Example: "1. Two-month dot grid, 2. Scrolling agenda view, 3. 'New' button, 4. Event creation modal."

### 5. The Build Kickoff: Nine Boxes
When handing off to the build team, have them perform the "Nine Boxes" exercise:
1. Draw a 3x3 grid.
2. The team must identify the ~9 major "scopes" of work required to finish the project.
3. If it requires significantly more than 9 boxes, the project is likely over-scoped or under-shaped.

## Examples

### Example 1: The Calendar Update
- **Context**: Users complain they can't see when they are free.
- **Appetite**: 6 weeks.
- **Shaping Output**: Instead of a full Google Calendar clone, the team shapes a "Dot Grid" view.
    - **Concept**: A two-month view where days with events have dots.
    - **Interaction**: Tapping a day slides an agenda view underneath.
    - **Technical Check**: Engineer confirms the existing API supports "dots per day" without a new database schema.
- **Result**: The team ships a functional, high-value "empty space finder" within the 6-week appetite.

### Example 2: FinTech Onboarding Optimization
- **Context**: High churn on the "Bank Info" step of a funnel.
- **Appetite**: 3 weeks.
- **Shaping Session**: The PM suggests piping data from a partner API to skip the step.
- **The Rabbit Hole**: The Engineer opens the code and finds three different branching paths for different bank integrations.
- **The Trade-off**: The triad decides to shape the solution for the top 80% of users (Bank A and B) and leave the old flow for Bank C to fit the 3-week appetite.

## Common Pitfalls
- **Shaping in Isolation**: PMs writing PRDs or Designers making high-fidelity Figmas without Engineering input. This leads to "time bombs" discovered in week 4 of a 6-week cycle.
- **The Paper Shredder**: Breaking a shaped idea into 100 tiny Jira tickets. This destroys the team's ability to see the "whole castle" and make creative trade-offs.
- **Estimating vs. Appetite**: Asking "How long will this take?" instead of "What is the best version of this we can build in 4 weeks?"
- **The "Over-easy" Hand-off**: Giving a team a fuzzy goal (e.g., "Improve the dashboard") without shaping the boundaries. This causes the team to spin in circles.