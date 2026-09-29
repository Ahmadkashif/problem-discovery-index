# Public Input Processing Adapted to Committee Workflow

**Niche:** [[niches/electrical-contractors/code-standards-development-bodies/profile|Electrical Code & Standards Development Bodies]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Consultation management platforms collect and route submissions; a code cycle needs to know which of five thousand inputs are substantively the same proposal arriving from twenty different people.
**Tags:** #bert #transformers #large-language-models #contrastive-learning #word-embeddings #k-means-clustering #evaluation-metrics #automation #workflow-orchestration #compliance

## The Problem
Each cycle draws thousands of public inputs and comments, submitted by manufacturers, contractors, inspectors, and interest groups, in free text of wildly varying quality. Staff sort them to panels, and panels work them individually. Much of the volume is substantively duplicative — the same substantive proposal in different words, sometimes coordinated, sometimes coincidental — and identifying that is done by reading. Panels consequently debate the same question several times under different input numbers, and the record of why a proposal was rejected in a prior cycle is available only if someone recalls that it was.

## What Already Exists
Consultation and submission management is a solved category. Regulatory comment platforms, the standards development management systems, and general case management tools all handle intake, routing, deadline tracking, status, and publication of resolutions competently.

## The Customization Gap
Those systems treat a submission as a unit of work to be routed and resolved. What the process needs is substantive clustering — grouping inputs by the change they actually propose rather than by the text they used, linking them to the provisions affected, and connecting them to prior-cycle proposals on the same question with their resolutions attached. That requires semantic comparison against the code text and against the historical proposal record, not keyword search. Coordinated submission campaigns should be visible as such, since a panel weighing consensus needs to know whether it is seeing twenty independent views or one view submitted twenty times. And routing should follow the dependency graph rather than the article number, because a proposal to change one article frequently belongs in front of a different panel than its numbering implies.

## Target Customer
Standards development staff and panel secretaries at code bodies, and the technical committee chairs who currently work an unclustered queue under a fixed cycle deadline.

## Impact If Solved
Removes duplicative committee time in a process whose bottleneck is volunteer expert attention on a fixed schedule. Linking proposals to prior-cycle resolutions also stops the same rejected idea being re-argued from scratch, which is the most common complaint of long-serving panel members.
