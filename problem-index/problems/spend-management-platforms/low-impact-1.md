# ERP Integration and GL Coding

**Industry:** [[spend-management-platforms|Spend Management Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every transaction must be coded to an account, department, class and project in a chart of accounts unique to each customer, and the coding model is rebuilt per customer from scratch.
**Tags:** #bert #large-language-models #gradient-boosting #k-nearest-neighbors #word-embeddings #evaluation-metrics #data-integration #workflow-orchestration

## The Problem
A card transaction becomes a journal entry. That requires a general ledger account, usually a department or cost centre, often a class, location, project or customer for companies that track profitability at that grain, and correct tax treatment.

The chart of accounts is idiosyncratic per company. One customer has fourteen expense accounts, another four hundred. Account names range from standard to internal shorthand that means nothing outside the company. Departments change with reorganisations. Projects are created weekly.

Rules-based coding covers the obvious cases — this merchant maps to that account — and breaks on everything else. The same merchant can be several things: a hardware store purchase is office supplies, or facilities maintenance, or a capitalised project cost, depending on what was bought and why. An airline charge might be travel, or cost of goods sold if the employee was travelling for a billable engagement.

So a controller codes the remainder by hand, at month end, from memory and context. Their coding is consistent because one person does it, and when they leave the consistency goes with them.

Implementation carries the same problem at the start. Mapping a new customer's chart of accounts, dimensions and approval structure into the platform is the bulk of onboarding and is done by a solutions consultant in workshops.

## What Already Exists
Every platform ships ERP connectors for NetSuite, QuickBooks, Intacct, Xero and Dynamics. Merchant category codes provide a coarse default. Rules engines map merchants and categories to accounts. Some platforms learn from corrections at a basic level. Accounting automation — accruals, amortisation, prepaid schedules — is where the category is competing hardest.

## The Customisation Gap
Learning from a customer's own history is shallower than it should be. Every company has months or years of correctly coded transactions in its ERP before the platform arrives, which is a directly supervised training set for that company's specific conventions, and most platforms start from rules and learn slowly from corrections instead.

Cross-customer transfer is unexploited. Charts of accounts differ in naming and structure and not in underlying semantics; an account called "Software & Subscriptions" at one company and "IT Tools" at another are the same thing. Aligning charts semantically would let a new customer start with a model informed by thousands of similar companies rather than from zero.

Ambiguity is not surfaced. The right output for a genuinely ambiguous transaction is a question — what was this for — asked of the employee at the moment of spend, when they remember, rather than a guess corrected by a controller at month end when they do not.

And nothing captures the reasoning. When a controller recodes a transaction, why they did so is not recorded, so the correction teaches the system what but never why, which is the part that generalises.

## Impact If Solved
Coding is the largest recurring manual task in the product's core workflow and the largest component of implementation. Training on the customer's own ERP history, transferring across semantically aligned charts of accounts and asking the employee when genuinely ambiguous removes most of a controller's month-end and most of an onboarding.
