# Nobody Knows Which Customers a New Law Actually Breaks

**Niche:** [[niches/hr-consultants/employment-law-content-publishers/profile|Employment Law Compliance Content Publishers]]
**Industry:** [[industries/hr-consultants|HR Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The publisher knows a city just passed a sick leave ordinance and knows which of its customers operate there, and it sends the same alert to everyone.
**Tags:** #graph-ml #large-language-models #text-classification #named-entity-recognition #compliance

## The Problem
Pass 1 states the gap in one sentence: compliance tools provide legal update feeds but do not map changes to specific client configurations. That is exactly right, and it is the whole opportunity.

An HR consultant with thirty SMB clients across a dozen states receives a stream of alerts — a state minimum wage change, a new local paid leave ordinance, an amended notice requirement, a threshold change that only bites above fifty employees. Each alert describes a change in the law. None of them says which of the thirty clients is affected, which of their policies now conflicts, or what has to be edited by when.

So the consultant does it by hand, from memory, for thirty clients, every time — the compliance treadmill Pass 1 describes, where changes pile up faster than any one person can track. And they do it badly, not from incompetence but because the mapping is a cross product of thirty clients against dozens of jurisdictions against hundreds of policy provisions.

The publisher already holds both halves. It maintains the jurisdictional rules and it hosts the customers' handbooks and configurations. It has never joined them.

## Why Nobody Has Built This
The business grew as publishing. The organizing unit is a piece of content — a policy template, an alert, a guidance article — and content is authored for a jurisdiction and a topic, not for a customer. A customer relationship is a subscription, not a modelled entity with locations, headcount, and policies. Joining them means representing the customer, which is a different product architecture than the one a content business builds.

There is also a professional caution, and it is real: telling a customer "your handbook is now non-compliant" edges toward legal advice, which a publisher is careful not to give. The distinction that resolves it is available and simply has not been drawn — identifying that a provision conflicts with a rule that took effect is a factual comparison, not an opinion about what they should do.

## What to Build
A rules-to-configuration mapping layer over content the publisher already has.

**Structure the rules.** Each requirement as a machine-readable object: jurisdiction, applicability thresholds (headcount, industry, employee classification), effective date, and the policy provisions it touches. This is a representation change to content that already exists in prose, and it is the substantial piece of work.

**Model the customer.** Locations, headcount by location, employee classifications, and the policies in force. Most of this is already in the customer's handbook or configuration; some needs to be asked once and maintained.

**Compute the intersection.** For every rule change, which customers are in scope, which of their provisions conflict, and what the deadline is. Not an alert about the law — a list of affected customers with the specific text at issue.

**Rank by exposure.** A consultant with thirty clients and a dozen changes needs an order of work. Penalty exposure, employee count affected, and deadline proximity give one.

**Suggest the amended language.** The publisher already writes compliant policy text for every jurisdiction. Presenting the specific redline for this customer's handbook is assembly, not authorship.

## Target Customer
Chief Product Officer or VP of Content at an employment law compliance publisher. The commercial case is retention and pricing: a legal update feed is a commodity that renews on price, and a system that tells a consultant which of their thirty clients has a problem this month is not.

## Impact If Built
The multi-client compliance treadmill is the highest-impact problem in Pass 1 for this industry, and it is unsolvable at the consultant's altitude — the required rule corpus is exactly what a fractional HR consultant cannot maintain. The publisher already maintains it. What is missing is the join, and everything needed for it is already inside the company.
