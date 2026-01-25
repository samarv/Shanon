---
name: retention-streak-mechanic-design
description: A framework for building and optimizing a "streak" feature to drive long-term user retention. Use this when designing habit-forming products, increasing Daily Active Users (DAU), or leveraging loss aversion to prevent churn.
---

## Overview
A streak tracks how many consecutive periods (usually days) a user performs a core action. When designed correctly, streaks leverage human psychology—specifically loss aversion—to turn a casual user into a power user. This skill focuses on the "bend, don't break" philosophy used to scale Duolingo to 9 million+ users with year-long streaks.

## Core Principles
- **Identify the "Unit of Use":** Define the smallest, most comprehensible action that counts as engagement. (e.g., Doing one lesson, not earning 50 points).
- **The Seven-Day Threshold:** Focus disproportionately on getting users from Day 0 to Day 7. Loss aversion significantly peaks after one week of consistency.
- **Sanctity vs. Flexibility:** Balance "Streak Freezes" (insurance) with "Perfect Streaks" (rewards for zero freezes) to keep the mechanic meaningful.

## Implementation Workflow

### 1. Define the Action and the Cycle
Identify the specific behavior you want to habituate.
- **Set the frequency:** Match the natural frequency of the value proposition. While Duolingo uses daily, a fitness app might use weekly streaks.
- **Simplify the requirement:** Avoid complex goals early on. Move from "Reach a specific XP goal" to "Complete one unit of content."

### 2. Optimize the First 7 Days
Focus experimentation on the "New User" experience to trigger loss aversion.
- **Goal Setting:** Ask users to commit to a specific streak length (e.g., 7, 14, or 30 days) during onboarding.
- **Intentionality:** Use CTAs that require commitment. Change generic buttons like "Continue" to "Commit to my Goal."
- **Visual Clarity:** Use a calendar view to show progress. The more it looks like a standard calendar, the more users understand the daily requirement.

### 3. Build the "Bend, Don't Break" System
Provide ways to preserve the streak during life's inevitable interruptions.
- **Strategic Flexibility:** Give new users 2 "Streak Freezes" immediately. It is easier to restart a 1-day streak than a 10-day streak; the freezes prevent early churn.
- **The "Earn Back" Mechanic:** If a streak is lost, allow the user to repair it by performing extra work (e.g., "Complete 2 lessons now to save your streak") rather than just paying for it.
- **23.5 Hour Reminders:** Send practice reminders 23.5 hours after the last session. This assumes the user is free at the same time they were yesterday.

### 4. Protect the "Sanctity" of the Streak
Prevent the mechanic from feeling "cheap" or unearned.
- **Perfect Streaks:** Celebrate users who don't use freezes. Turn the streak icon gold or add unique animations for users with a "Perfect Week."
- **Late-Night "Streak Saver" Notifications:** Send a high-urgency notification at 10:00 PM or 11:00 PM only if the user hasn't completed their action. Users perceive this as helpful "life-saving" rather than spam.

## Examples

**Example 1: Fitness App Streak**
- **Context:** A workout app trying to move users from 2 days/week to 5 days/week.
- **Input:** User finishes their second workout.
- **Application:**
    1. Display a "Streak Goal" screen: "Users with a 14-day streak are 5x more likely to hit their weight goal. Can you commit?"
    2. Provide 3 options: 7 days, 14 days, 30 days.
    3. If they miss Day 4, offer an "Earn Back": "Do a 5-minute stretch now to keep your 3-day streak alive."
- **Output:** Increased Day-14 retention and higher session frequency.

**Example 2: SaaS Writing Tool**
- **Context:** A tool like Grammarly or Jasper wanting daily usage.
- **Input:** User writes 100 words.
- **Application:** 
    1. Show a "Writing Streak" flame in the UI.
    2. Change the "Save" button to "Commit to Daily Goal" after the first 100 words.
    3. At 10:00 PM, send a push: "Don't let your 5-day writing streak go cold! Write just 10 words to save it."
- **Output:** User returns at 10:05 PM to maintain the streak, reinforcing the daily habit.

## Common Pitfalls
- **Over-complicating the V1:** Don't build a complex gem economy or social leaderboard immediately. Test if a simple counter moves the needle first.
- **Dumbing down the unit too much:** If you make the requirement too easy (e.g., "Just open the app"), the streak loses its connection to the value of the product. 
- **The "One-Way Door" of Cheapening:** Once you give away too much flexibility (e.g., unlimited freezes), you cannot easily take it back without an "extinction level event" for user trust.
- **Ignoring Cultural Context:** Not all icons (like a flame) mean "streak" or "consistency" globally. Use clear numbers and calendar iconography for international users.