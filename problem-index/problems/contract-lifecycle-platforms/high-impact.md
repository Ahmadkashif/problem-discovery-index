# The Unstructured Back Catalogue

**Industry:** [[contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** High Impact
**One-liner:** A company's obligations live in thousands of executed agreements that nobody has read since signature, and every CLM implementation quietly begins by declaring the back catalogue out of scope — which is where the liability is.
**Tags:** #large-language-models #bert #transformers #word-embeddings #transfer-learning #confidence-intervals #evaluation-metrics #compliance #revenue-impact

## The Problem
Ask a general counsel a simple question — which of our customer contracts have most-favoured-nation pricing, or which vendors can we exit within ninety days, or how many agreements commit us to a data residency requirement — and the honest answer is that finding out means someone reading several thousand documents.

This is the problem CLM was sold to solve. In practice the implementations manage contracts going forward: new agreements are authored in the system, negotiated in it, executed from it, and their metadata is captured. The executed back catalogue is migrated as files, sometimes with basic fields extracted, and the substantive terms remain in the PDFs.

That is where the liability sits. Agreements signed three years ago are the ones currently binding, currently renewing, and currently containing the commitment nobody remembers making. The new contracts are the well-understood ones.

The consequences arrive as surprises. An acquisition's due diligence discovers change-of-control provisions nobody knew about. A pricing change is blocked by most-favoured-nation clauses discovered late. An unwanted auto-renewal. A customer invokes a service level the company had forgotten. A regulatory change requires knowing which agreements contain a particular data commitment, and answering takes six weeks of contract review.

## Why It's Unsolved
Extraction quality was genuinely inadequate until recently. Contract language is dense, heavily cross-referenced, negation-laden and highly variable across counterparties' paper, and earlier approaches produced accuracy that a legal team could not rely on. That has changed substantially, and the category's assumptions have not fully caught up.

The precision requirement is unusual. In most extraction applications a small error rate is acceptable. Here, a missed exclusivity clause or an inverted indemnity cap is a material misstatement of the company's position, and a legal team that finds two errors will discard the whole dataset. That asymmetry has justified a lot of caution.

The economics of back-catalogue processing were bad. Manual review of ten thousand contracts is a large project with no immediate deliverable, and it competes for legal budget against work with visible outcomes. So it is deferred permanently.

And nobody owns it. Legal operations owns the system, counsel owns the advice, the business owns the relationships, and the back catalogue is everybody's inheritance and nobody's project.

## What a Solution Looks Like
Extraction across the executed estate with confidence per field and per clause, and an explicit distinction between what the model is sure of and what needs review. The deliverable is not a perfect dataset but a searchable one with honest uncertainty, which is strictly better than the current state of nothing.

Prioritisation by consequence rather than by date. The clauses worth extracting first are the ones that produce surprises — change of control, exclusivity, most-favoured-nation, auto-renewal and notice, indemnity caps, data commitments, termination rights — and they are a small set.

Review targeted where it matters. High-value agreements and low-confidence extractions get human eyes; a routine NDA with high-confidence extraction does not. That triage is what makes the project affordable.

Obligation calendaring is the output that pays for it immediately: notice deadlines, renewal dates and milestone commitments turned into dated reminders assigned to owners.

And the question interface is the point. A general counsel should be able to ask which agreements contain a given commitment and get an answer with citations to the clause and the confidence attached.

## Impact If Solved
Every enterprise carries obligations it cannot enumerate, and the surprises arrive at the worst moments — in diligence, in a pricing decision, in a regulatory response. Making the back catalogue queryable is the thing CLM was bought to do and consistently does not, and extraction quality has only recently become good enough to attempt it honestly.
