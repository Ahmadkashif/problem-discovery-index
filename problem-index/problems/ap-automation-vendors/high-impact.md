# The Exception Queue Nobody Studies

**Industry:** [[ap-automation-vendors|AP Automation Vendors]]
**Type:** High Impact
**One-liner:** Automation handles the invoices that were already easy and routes the rest to a person, whose resolution of each exception is recorded as a status change rather than as the labelled example it is.
**Tags:** #bert #large-language-models #gradient-boosting #k-nearest-neighbors #graph-neural-networks #evaluation-metrics #feature-engineering #automation

## The Problem
An invoice arrives. Extraction reads it, matching compares it to a purchase order and a receipt, and if everything agrees it posts and pays without human involvement. A large share of invoices clear this way and that share is what the category markets.

The remainder does not clear, for a set of reasons that repeat endlessly. The quantity received differs from the quantity invoiced. The price differs from the purchase order by a small amount. There is no purchase order because the spend was a service nobody raised one for. The vendor on the invoice is a subsidiary of the vendor in the master file, or a renamed entity, or simply spelled differently. The tax is computed on a different basis. A freight charge appears that the purchase order did not contemplate. The invoice references a purchase order that was closed. It looks like a duplicate of one paid last month, and may or may not be.

Each goes to a queue. A clerk investigates: opens the purchase order, emails the requisitioner, emails the vendor, waits, gets an answer, adjusts something, releases the invoice. Days elapse. Early payment discounts lapse. Vendors call to ask where the money is.

The resolution is the valuable part and is thrown away. The system records that the exception was cleared and by whom. It does not record that the cause was a partial delivery, that the fix was a receipt adjustment, that this vendor's invoices systematically arrive before the goods, or that this requisitioner never closes purchase orders. The next occurrence is investigated from scratch.

Because the causes repeat, so does the work. A large proportion of a given company's exceptions trace to a handful of root causes — one vendor's invoicing practice, one buyer's purchase order habits, one category where purchase orders are never raised — and nobody computes that distribution, so the remedy is always more clerks rather than a fix upstream.

## Why It's Unsolved
The category's marketing metric is the touchless rate, and the exception queue is where the touchless rate is not. Improving extraction accuracy from ninety-four to ninety-six percent is a demonstrable product improvement; reducing exceptions by changing how a customer's buyers raise purchase orders is a consulting outcome that does not fit a software roadmap.

Resolution data is unstructured by construction. The work happens in email, in the ERP, and in conversation, and the platform sees a status transition. Capturing what was actually wrong requires either asking the clerk — which adds a step to a queue already under pressure — or inferring it from the ERP changes that accompanied resolution, which nobody does.

Root causes live outside AP. Purchase order discipline belongs to procurement, receiving accuracy to the warehouse, vendor invoicing practice to the vendor. The AP team absorbs the consequences of all three and has authority over none, so even a perfect diagnosis lands on a team that cannot act on it.

And the matching itself is more rigid than it needs to be. Three-way matching with tolerance bands is a deterministic rule from an era of paper. Whether an invoice line corresponds to a purchase order line is a matching problem with real semantics — descriptions that differ, units that differ, partial shipments, substitutions — and it is implemented as string and number comparison.

## What a Solution Looks Like
Capture resolution as a first-class object. Cause, action taken, party responsible, time to resolve. Some of it can be inferred from the accompanying ERP changes; the rest requires a single structured field the clerk selects. That one field is the difference between a queue and a dataset.

Root cause analytics on top of it. The distribution of exception causes by vendor, buyer, category and requisitioner tells a customer exactly where its exceptions come from, and the fix for the top few is usually a process change rather than more headcount. Nobody currently gives a customer this report.

Semantic matching instead of tolerance bands. Matching invoice lines to purchase order lines across differing descriptions, units, partial deliveries and substitutions is a learnable problem, and the historical matched pairs in the customer's ERP are the training data.

Predicted resolution attached to the exception. The clerk should open an exception that already says this looks like a short delivery, here are the three most similar past cases, here is who resolved them and how, here is a drafted email to the requisitioner.

Prediction at receipt. Many exceptions are foreseeable from the invoice and the vendor's history before the match is attempted, which allows pre-emptive routing rather than a failed match followed by investigation.

## Impact If Solved
Exception handling is the entire remaining labour cost of accounts payable, it is where discounts are lost and vendor relationships are strained, and it is the one part of the workflow that generates no data despite producing thousands of expert judgements a month. Capturing resolutions, analysing root causes and matching semantically attacks the cost at its source rather than shaving another point off an extraction benchmark.
