---
name: working-backwards-product-development
description: A customer-centric framework for product discovery and validation. Use this when pitching a new product or feature, seeking executive buy-in for a major initiative, or when you suspect a team is building a solution in search of a problem.
---

The "Working Backwards" process is a mechanism to ensure that every product decision is grounded in a specific customer problem. It moves the most difficult questions to the beginning of the development cycle, preventing the "retrofitting" of problems to pre-conceived solutions.

## The Three-Question Investment Test
Before writing any documents, evaluate a potential initiative against these three criteria:
1. **Is it a big idea?** Does it have the scale to move the needle for the business?
2. **Is it something we should be doing?** Does it align with the company's core mission and strengths? (e.g., A great oil extraction technology might be a big idea, but it isn't something Amazon should do).
3. **Is there a legitimate plan to succeed?** Do we have a path to execute this given our constraints?

## The Internal Press Release (PR) Structure
The PR is a one-page document written in the future tense, imagining the day the product launches. It must be written in customer-centric language, avoiding internal jargon.

### 1. The Problem Paragraph
Clearly define the customer's pain point. If you cannot write a compelling paragraph about the problem, the product shouldn't exist.
- **Rule:** Do not skip this.
- **Red Flag:** If the problem paragraph feels like an afterthought to justify a technology, you are "working forwards."

### 2. The Solution Paragraph
Describe how the product solves the problem elegantly. Focus on the "what," not the "how." Describe the user experience in simple terms.

### 3. The Customer Quote
Write a hypothetical quote from a customer describing how this product changed their life or solved their specific frustration. This anchors the team in the human impact of the work.

## The Frequently Asked Questions (FAQ)
The FAQ is the second part of the document and handles the "Legitimate Plan to Succeed." It is split into two sections:

### External FAQ
Questions a customer or member of the press would ask:
- How much does it cost?
- How do I get started?
- What happens if [X] goes wrong?

### Internal FAQ
Questions leadership or the engineering team will ask:
- What are the biggest technical risks?
- How does this impact our current margins?
- What are the dependencies on other teams?
- What is the "fitness function" (the one metric that defines success)?

## Implementation Guidelines
- **Focus on the "Why":** A product leader’s job is to teach the mental model behind the decision, not just make the decision. Use the PR/FAQ to teach the team how to think.
- **Scale Appropriately:** While every new product needs a PR/FAQ, smaller features may only need the spirit of the process (starting with the problem) rather than the full overhead of the document.
- **Avoid "Pantry-First" Thinking:** Do not look at the "ingredients" (available APIs, existing code, spare server capacity) and try to combine them into a product. Look at the customer first.

## Examples

**Example 1: Amazon Smile**
- **The Problem:** Customers want to support charities but find the process of donating small amounts of money or tracking their impact cumbersome and expensive.
- **The PR Solution:** A version of Amazon where the company donates a percentage of every purchase to a charity of the customer's choice at no cost to the user.
- **The FAQ Focus:** How do we onboard 1M+ charities? How do we ensure the donation doesn't increase prices for customers?

**Example 2: A Tech-First Failure (The "Ingredients" Mistake)**
- **The Input:** A team realizes they have a database of product attributes and a new voting UI component. They decide to link products together based on subjective attributes (e.g., "products that feel like summer").
- **The Mistake:** They named it "ASIN to ASIN linking" (internal jargon) and retrofitted a problem to use the existing tech.
- **The Result:** The product lacked a clear customer "Why" and was eventually shut down because it didn't solve a real pain point.

## Common Pitfalls
- **Retrofitting the Problem:** Starting with a solution you’re excited about and then inventing a customer problem to justify it.
- **Skipping the Problem Paragraph:** Moving straight to features because the problem seems "obvious." This usually leads to a lack of focus.
- **Using Jargon in the PR:** Using internal project names (e.g., "The Phoenix Project") instead of customer-facing names. If a customer wouldn't say it, it doesn't belong in the PR.
- **Ignoring the FAQ:** Writing a visionary PR but failing to answer the hard internal questions about costs, risks, and technical trade-offs.