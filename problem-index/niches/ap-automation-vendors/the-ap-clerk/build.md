# Getting the Answer Without Asking

**Niche:** [[niches/ap-automation-vendors/the-ap-clerk/profile|The AP Clerk]]
**Industry:** [[industries/ap-automation-vendors|AP Automation Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Most of what the clerk emails people to ask is already in the systems the platform connects to.
**Tags:** #large-language-models #data-integration #workflow-orchestration #worker-facing #automation #evaluation-metrics #confidence-intervals #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to stop the clerk's job being email to people who do not reply — and whoever gets the answer without the chase changes what the role is.

## The Problem
The clerk emails to ask which cost centre an invoice belongs to, when the goods were received, whether the service was delivered, who raised the order, and whether a variance is acceptable. A large proportion of those answers are derivable: from the purchase order, from the receipt record, from the requester's history, from how identical invoices from the same supplier were coded for the last three years. The platform is connected to the systems holding all of it and asks a person instead.

## Why Nobody Has Built This
Exception handling was designed as a routing problem, so the product's job was considered done when the item reached a human — what happens next was outside the workflow's model. The answer sources sit across ERP, procurement and receiving systems that the platform reads selectively. Clerk time is the customer's cost rather than the vendor's. And nobody measured how the role's hours are actually spent.

## What to Build
Answer the question before it is asked. Derive the likely answer from purchase orders, receipts, contracts and coding history, and present it for confirmation rather than posing an open question, which is the core and converts a chase into a click. Rank derived answers by confidence so the clerk knows what to trust. Route to the right person automatically, since identifying who can answer is itself a significant part of the work. Chase on a schedule with escalation, because persistence rather than judgement is what most of the follow-up requires. Show who is blocking what, as visibility alone changes behaviour and nobody currently sees the aggregate. Let the approver answer in one click from wherever they are, since the reply rate is a function of effort. Learn from previous answers to the same question about the same supplier, which is the recurring case. Give the clerk a single view of everything waiting on someone else, because they currently maintain it in a spreadsheet. Surface the invoices at risk of late payment, so effort goes where the consequence is. Measure how the clerk's time divides between deciding and chasing, since that number is the case for the whole investment. And give escalation real authority, because chasing without it is the role's central frustration.

## Target Customer
Product and customer leadership, AP clerks and managers, finance leaders whose team is a correspondence function, and workflow vendors whose products stop at routing.

## Impact If Built
Exception handling was designed as routing, so the workflow considered its job done once a human received the item. Deriving the answer from purchase orders, receipts and coding history turns an open question into a confirmation.
