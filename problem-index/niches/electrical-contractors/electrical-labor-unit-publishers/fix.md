# Every Line Item Is a Number Without Its Basis

**Niche:** [[niches/electrical-contractors/electrical-labor-unit-publishers/profile|Electrical Labour Unit & Estimating Database Publishers]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** A researcher sets a labour unit after weighing time studies, field observation, and judgment about conditions, and the database stores the number — so a challenged figure is defended from memory and a retirement takes thousands of entries with it.
**Tags:** #tacit-knowledge-ml #large-language-models #bert #transformers #descriptive-statistics #confidence-intervals #evaluation-metrics #data-integration #worker-facing #workflow-orchestration

## The Problem
Electrical contractors bid multi-million dollar jobs against these units and occasionally argue about them in front of an owner or an arbitrator. The units' authority rests on the rigour of their derivation, which is not stored. A researcher determines that a task takes a given time by combining time study data, field observation, an assessment of how the task changes in a finished renovation versus new construction, and experience with how crews actually sequence the work. Then they write a number. When a subscriber challenges it, the response is reconstructed. When the researcher retires, the basis for a large section of the database becomes unavailable, and their successor inherits numbers they cannot interrogate — which means they leave them alone, because revising a figure you cannot reconstruct is risky.

## Why It's Still Broken
The system was built to publish a database and databases store values. The volume argues against documentation, since a researcher maintaining tens of thousands of entries under a release deadline treats each extra keystroke as cost. And the field has treated estimating research as craft, with the corollary — that the knowledge is uninspectable and untransferable — accepted rather than examined, in an industry whose Pass 1 analysis identifies exactly this as its defining crisis one layer down.

## What a Fix Looks Like
A derivation record attached to each unit, captured as the work is done: sources consulted with dates, the conditions assumed, the judgments applied and their basis, the researcher's confidence, and what would cause the figure to change. That last field turns a static number into a standing trigger — when a code provision moves or a product method changes, the units whose derivations depend on it surface for review rather than waiting for the next sweep. Across the database the records support what is impossible today: finding units resting on a single stale study, measuring consistency between researchers on comparable tasks, and answering a subscriber challenge with an account rather than an assertion. Most importantly it makes maintenance transferable, which is the succession problem every estimating publisher has and none has solved.

## Who Feels the Pain
Researchers inheriting entries they cannot interrogate and therefore never revise; the content director with no instrument to measure consistency across a database whose value is consistency; contractors whose disputed bids rest on figures the publisher can only defend from memory; and the business, whose most senior expertise is unrecorded and retiring on the same demographic curve as the trade it serves.

## Impact If Fixed
Turns a collection of numbers into a body of evidence, which is both the more defensible product and the more valuable one when a figure is actually tested. It also unblocks the rest — outcome validation and dependency-driven maintenance both require knowing why a unit is what it is before anything can be said about whether it is right.
