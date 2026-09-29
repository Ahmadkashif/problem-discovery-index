# One Wet Signature Puts the Whole Package on Paper

**Niche:** [[niches/esignature-document-workflow/regulated-industry-signing/profile|Regulated Industry Signing]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Fix (Pain Point)
**One-liner:** A package of ninety documents contains two that require a physical formality, and organisations respond by printing all ninety, because nothing is built to run a hybrid package.
**Tags:** #logistic-regression #bert #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #quick-win
**Contested on:** Every serious competitor here is fighting to finish a regulated transaction without a room — and that contest splits by transaction type rather than by regulation, which is why this niche is not terminal and is decomposed below.

## The Problem
A transaction package has ninety documents. Eighty-eight can be signed electronically today with no legal question at all. Two require a notary or a witness or a wet original. The organisation prints ninety, because the workflow is all-or-nothing, because tracking which documents are in which channel is error-prone and nobody wants to be the person who loses a piece, and because the safe answer under time pressure is paper. Every efficiency the category promised is lost to two documents out of ninety.

## Why It's Still Broken
Hybrid packages are an orchestration problem and the products are built around a single execution channel. Tracking partial completion across two channels needs a state model nobody implemented. Risk aversion compounds it: the person assembling the package is judged on whether the transaction closed cleanly and not on whether it closed efficiently, so paper is the rational individual choice even when it is the wrong organisational one. And the classification step — knowing which of the ninety documents actually require a formality — is done by memory, so people over-apply the requirement rather than risk under-applying it.

## What a Fix Looks Like
Run the package as a package with mixed channels. Classify every document by its required execution channel, which is a document classification problem over standard instrument types and is the step that makes everything else possible — and doing it properly will reveal that the wet-ink set is smaller than the organisation assumed, because over-application is the norm. Track completion across channels in one state model, so the transaction has a single status regardless of how each piece is being executed. Sequence deliberately: run the electronic majority first and in parallel, so the physical minority is the only thing left and the room, if still needed, is fifteen minutes rather than two hours. Make the physical piece trackable — courier, scan-back, receipt confirmation — as a first-class part of the package rather than a gap in the record. And report the composition: how many documents per package actually require a formality, and how many were printed anyway, which is a number no organisation has and which is the argument for changing the practice.

## Who Feels the Pain
Closing coordinators, transaction assistants and compliance staff assembling packages by hand; the customers who take a half-day off for a signing that could have been fifteen minutes; and organisations paying for a signature platform they route around whenever it matters.

## Impact If Fixed
The formality genuinely applies to a small minority of documents and the all-or-nothing response is a workflow limitation rather than a legal requirement. Classification plus a mixed-channel state model is ordinary engineering, and the composition report alone would show most organisations they are printing far more than they must.
