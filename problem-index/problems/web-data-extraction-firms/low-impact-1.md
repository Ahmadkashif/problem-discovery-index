# Collection Governance and Permission Tracking

**Industry:** [[web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Robots parsers, rate limiters and legal review processes all exist, and no firm maintains a continuous, queryable record of what it is collecting from where, under what permission, for whose stated purpose.
**Tags:** #large-language-models #bert #transformers #word-embeddings #change-point-detection #evaluation-metrics #compliance

## The Problem
A collection request arrives: this customer wants these fields from these sites for this purpose. Somebody assesses it. Are the pages publicly accessible without authentication. What do the site's terms say. What does robots.txt permit. Does the content include personal data. Is it copyrighted. Is the stated purpose consistent with what the customer will actually do.

That assessment happens once, at onboarding, and is recorded as an approval in a ticket. Then the collection runs, sometimes for years.

Everything underneath it moves. Sites update their terms. Robots directives change. A site adds a login wall to a section. The customer's use evolves from price monitoring to training a model. Privacy law changes what may be collected about individuals. Litigation clarifies — or unsettles — what is permissible.

None of this triggers re-review, because there is no system holding the original assessment alongside the live collection. The approval is in a ticket and the collection is in a scheduler, and nothing connects them.

The exposure has grown sharply as web-collected data has become model training input, which is a materially different use from the price comparison the original assessment contemplated.

## What Already Exists
Robots.txt parsers are standard and every reputable firm honours directives. Rate limiting and politeness controls are mature. Legal review processes exist at the established firms and are genuinely taken seriously. Terms of service are public documents. Privacy compliance tooling exists for structured data. Some firms publish acceptable use policies and refuse categories of request.

## The Customisation Gap
The gap is continuity, not capability. Each control exists as a point check and none is maintained as a live state. Robots is parsed at request time and its history is not tracked, so a directive change that newly prohibits a path is honoured going forward and nobody notices that collection was permitted yesterday and is not today.

Terms of service monitoring is absent. Terms change, they are public documents, and detecting a change that newly addresses automated access is a document monitoring problem on a corpus that is entirely available.

Purpose binding is the sharpest gap. The permission assessment was made for a stated purpose, the purpose is recorded in prose in a ticket, and nothing checks whether the customer's actual use has drifted. Given how much the training-data question has changed the risk calculus, purpose drift is now the most consequential unmonitored variable.

Personal data detection within collected content is the fourth. Whether a scraped page contains personal data determines which regimes apply, is detectable automatically at reasonable accuracy, and is generally assessed by category rather than by content.

## Impact If Solved
The sector's commercial risk is concentrated in the gap between what was assessed at onboarding and what is happening now. Maintaining permission as live state — monitored against terms changes, robots changes and purpose drift — turns a one-time review into a standing position, and it is built from documents and records the firms already have.
