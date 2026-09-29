# Learning From a Million Resolutions

**Niche:** [[niches/ap-automation-vendors/invoice-exception-handling/profile|Invoice Exception Handling]]
**Industry:** [[industries/ap-automation-vendors|AP Automation Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every exception has been resolved by a person who knew exactly what was wrong, and none of that was written down as data.
**Tags:** #large-language-models #gradient-boosting #evaluation-metrics #confidence-intervals #automation #workflow-orchestration #transfer-learning #data-integration
**Contested on:** Every serious competitor in this niche is fighting to resolve the fifteen to thirty percent of invoices that survive automation — and whoever learns from how humans resolved the last million of them automates the part the category has never touched.

## The Problem
An exception arrives. A clerk determines that the quantity difference is a partial shipment, or that the vendor name variant is the same supplier, or that the tax line reflects a different jurisdiction's rounding, and resolves it. The system records that the invoice moved from exception to approved. What was actually wrong, what evidence settled it, and what would prevent it recurring are all in the clerk's head and in an email thread. Across a customer base that is millions of resolved cases, every one a labelled example of a problem and its fix.

## Why Nobody Has Built This
Workflow systems record state transitions, so the resolution was captured as a status rather than as a reason — the data model had no field for what happened and nobody added one. Product effort went to capture accuracy, which demos well. Exception handling is where implementation and support revenue lives. And nobody measured the cost of the queue, so its size never became a product priority.

## What to Build
Capture the reason, then learn from it. Record the resolution reason and the evidence in a structured vocabulary, which is the core and is a small change that makes everything after it possible. Classify incoming exceptions by predicted cause, since most fall into a handful of recurring types and classification alone routes them correctly. Resolve the recurring ones automatically where the evidence is unambiguous, because a vendor whose invoices always except for the same reason should stop excepting. Transfer knowledge across customers where the pattern is general, as tax rounding and partial shipment logic are not company-specific. Predict at capture which invoices will except, so the problem can be addressed before it reaches a queue. Attribute exceptions to root causes — this vendor, this purchase order practice, this master data record — since a large share trace to a few sources that could simply be fixed. Assemble the evidence an exception needs before routing it, because the clerk currently spends their time gathering rather than deciding. Measure exception rate, resolution time and cost per exception, which the category reports in none of its metrics. Feed the root causes back to the customer as recommendations, which is the product. Keep the clerk deciding the genuinely ambiguous, as those exist and matter. And report what proportion of exceptions were eliminated rather than merely processed faster.

## Target Customer
Product and operations leadership, AP managers whose teams live in the queue, finance leaders paying for automation that covers the easy cases, and workflow vendors recording status transitions.

## Impact If Built
Workflow systems record state transitions, so the data model had no field for what actually happened and nobody added one. Structuring the resolution reason turns millions of human fixes into the training data for the part automation never reached.
