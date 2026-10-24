# Equivalency Proposals From Catalogue Descriptions

**Niche:** [[niches/colleges-and-universities/transfer-credit-evaluation/profile|Transfer Credit Evaluation & Articulation]]
**Industry:** [[industries/colleges-and-universities|Colleges & Universities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Equivalency tables answer the common courses; everything else waits weeks for a faculty member to compare two catalogue descriptions a model could pre-match in seconds.
**Tags:** #transformers #word-embeddings #k-nearest-neighbors #large-language-models #evaluation-metrics #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn an incoming transcript into posted, degree-applicable course equivalencies, and whoever applies the largest share of incoming credit toward degree requirements takes the account.

## The Problem
A transfer evaluator at a regional university processes thousands of transcripts a year. Courses from the top feeder colleges match the equivalency table; courses from out-of-state, older or unusual sources are sent to department faculty with the description attached. Faculty answer when they can, often weeks later, and each answer becomes a table entry used by nobody else.

## Why Nobody Has Built This
Catalogue descriptions by year are scattered across institution websites and archives, transcripts arrive in many formats, and faculty are wary of automated equivalency decisions. Degree audit vendors treat equivalency as a table to maintain, not a matching problem.

## What to Build
A matcher that retrieves the sending course's description for the catalogue year, ranks the receiving institution's candidate courses by semantic similarity and by past faculty decisions on similar courses, and proposes direct, elective or no-credit with the precedents shown. High-confidence frequent cases post automatically; the rest go to faculty pre-filled, with a one-click decision.

## Target Customer
Registrars and transfer centres at public four-year universities receiving thousands of transfers a year.

## Impact If Built
Faculty review queues shrink to the genuinely new courses. If half of referred courses can be pre-matched, an evaluator team saves hundreds of hours a term and students learn their remaining requirements before registration (estimate).
