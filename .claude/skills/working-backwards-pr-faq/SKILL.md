---
name: working-backwards-pr-faq
description: Define new products and features by starting with the customer experience instead of technical constraints. Use this when starting a zero-to-one product, deciding which feature to prioritize next, or seeking executive alignment on a complex proposal.
---

The "Working Backwards" process centers on the PR/FAQ: a mock Press Release and a list of Frequently Asked Questions. It forces clarity of thought by requiring you to describe a finished product and its benefits before a single line of code is written.

## The Working Backwards Framework

### 1. The Press Release (PR)
The PR is a one-page document written for the customer. It describes the product as if it were launching today. It must be factual and data-rich, avoiding marketing hyperbole.

**The Three "Money Paragraphs":**
*   **The Summary:** A short description of the product and what the core benefit is.
*   **The Problem:** A crisp definition of the specific customer problem this product solves. Quantify the problem with data or customer insights.
*   **The Solution:** A description of how the product elegantly solves that problem.

**Essential PR Elements:**
*   **Hypothetical Launch Date:** Choose a date that signals the expected complexity (e.g., next month vs. next year).
*   **The "Target Customer":** Avoid broad categories. Be specific about who this is for (e.g., "high-volume professional sellers in urban areas" instead of "all merchants").
*   **Customer Quote:** A hypothetical quote from a customer explaining how the product changed their life or business.

### 2. The Frequently Asked Questions (FAQ)
The FAQ is a multi-page document that addresses the "behind the scenes" details. It is divided into two sections:
*   **External (Customer) FAQ:** Questions a customer would actually ask. "How much does it cost?" "How do I switch from my current provider?" "What happens if my internet goes out?"
*   **Internal (Stakeholder) FAQ:** Difficult questions from leadership or engineering. "Why shouldn't we just use a third-party API?" "What is the fatal flaw in this logic?" "What are the specific engineering risks?"

### 3. The Concentric Circle Review
Do not write a PR/FAQ in a vacuum. Use a "product funnel" approach:
1.  **Author Draft:** Write and self-edit. If the idea looks bad on paper, discard it immediately.
2.  **Small Group Review:** Share with immediate peers for feedback.
3.  **Leadership Review:** Present to senior stakeholders to test the logic and "disagree and commit."
4.  **Iterate:** Most successful products go through multiple versions of the PR/FAQ before being approved for development.

## Examples

**Example 1: A New Delivery Tracking Feature**
*   **Context:** Improving customer satisfaction with shipping.
*   **Input:** "We want to improve tracking."
*   **Working Backwards Application:**
    *   **PR Headline:** "Amazon Announces Real-Time Map Tracking for All Deliveries."
    *   **Problem Statement:** Customers currently only know their package is "out for delivery," forcing them to stay home all day to avoid theft.
    *   **Solution:** A live GPS map showing exactly how many stops away the driver is.
*   **Output:** A document that forces the team to solve the privacy and GPS-latency engineering hurdles before committing resources.

**Example 2: A Specialized B2B Search Tool**
*   **Context:** Choosing between "Search for Everyone" vs. "Search for Engineers."
*   **Input:** "Our search is mediocre."
*   **Working Backwards Application:**
    *   **Customer Definition:** Instead of "all users," the PR focuses on "Technical Leads looking for deprecated API documentation."
    *   **PR Focus:** A specialized filter for version-specific syntax.
*   **Output:** Realization in the FAQ that the "all users" approach would obfuscate the most valuable data for the highest-paying customers.

## Common Pitfalls
*   **Working Backwards from Revenue:** Never start with "How do we hit our $10M goal?" Start with "What does the customer need that would result in $10M of value?"
*   **The "Product Tunnel":** Assuming every PR/FAQ must be built. The goal of the process is to kill bad ideas early. A successful PR/FAQ process should result in many discarded documents.
*   **Marketing Hyperbole:** Using words like "revolutionary" or "game-changing." Stick to factual descriptions: "The service reduces load times from 5 seconds to 200 milliseconds."
*   **Ignoring the Fatal Flaw:** Using the FAQ to hide risks instead of exposing them. A good FAQ proactively addresses why the project might fail.
*   **Starting with Constraints:** Focusing on "We only have three engineers" during the PR phase. Write the ideal customer experience first, then solve the resource constraints in the Internal FAQ.