# Account Data Hygiene

**Parent Industry:** [[industries/crm-platforms|CRM Platforms]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in account data is fighting to keep the relationships between accounts correct — parent, subsidiary, duplicate, acquired — rather than the fields inside them, and whoever holds the hierarchy right takes the account.

## Profile
**Market Size:** ~$2.3B US spend on data enrichment, deduplication and account data management
**Share of Parent Industry:** ~7% of CRM revenue
**Digital Adoption:** Medium — enrichment is widely bought and structure is not addressed
**Target Buyer:** Revenue and data operations leaders; enrichment vendors as the incumbent suppliers
**Automation Potential:** Very High — this is entity resolution with commercial reference data available

## What Makes This a Distinct Niche
The enrichment industry solved the wrong half of the problem very well. Firmographics — employee count, revenue, industry, technology stack, contact details — are available for essentially any company from several vendors and are kept reasonably current. What no vendor maintains is the structure: which of the four records named after the same company are the same account, which is the parent and which is a subsidiary, which entity was acquired last year and now belongs under a different parent, and which division of a global customer is contracted separately. That structure determines whether a global account's total value can be stated, whether a territory assignment is correct, whether a duplicate is created for the fifth time, and whether a customer who exists in three regions is treated as one relationship. It is the foundation under territory design, account planning, revenue reporting and every enterprise account strategy, and it is maintained by whoever last cared enough to merge two records.

## Current Tools & Gaps
ZoomInfo, Clearbit, Apollo, Dun & Bradstreet and the enrichment category supply firmographics with broad coverage; Dun & Bradstreet in particular maintains corporate linkage that is used less than it should be. Deduplication tooling exists in and around every CRM. The gaps: merges are performed manually and destructively, so the history of what was merged is lost and the duplicate reappears; hierarchy is a field that someone populates rather than a maintained structure, and it decays immediately as companies reorganise and are acquired; corporate events — acquisitions, divestitures, rebrands, subsidiary formations — are not monitored, so the structure is correct on the day it is built and degrades continuously; and nobody measures structural accuracy, so an organisation cannot tell how much of its account graph is right.

## Problems
- [[niches/crm-platforms/account-data-hygiene/build|🔨 Build: The Account Hierarchy as a Maintained Structure]]
- [[niches/crm-platforms/account-data-hygiene/buy|🛒 Buy: Corporate Linkage and Event Data Already Sold]]
- [[niches/crm-platforms/account-data-hygiene/fix|🔧 Fix: The Merge That Destroys the Evidence]]
