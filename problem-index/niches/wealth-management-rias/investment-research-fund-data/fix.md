# The Analyst's Conviction Is the Product and It Ships as a Medal

**Niche:** [[niches/wealth-management-rias/investment-research-fund-data/profile|Investment Research & Fund Data Providers]]
**Industry:** [[industries/wealth-management-rias|Wealth Management RIAs]]
**Type:** Fix (Pain Point)
**One-liner:** An analyst spends months on a fund's people, process and parent, and the output is a rating grade with a few paragraphs and no record of what would change it.
**Tags:** #tacit-knowledge-ml #evaluation-metrics #hypothesis-testing #compliance #worker-facing

## The Problem
The qualitative research is the part of this business that quantitative data cannot replicate. An analyst covers a strategy over years: meets the managers, tracks turnover in the investment team, assesses whether the stated process is the process actually followed, watches how the parent firm behaves toward the fund, and forms a view.

That view is published as a rating grade and a written report. What is not captured in structured form is the reasoning: which specific factors drove the grade, how they were weighted, what the analyst was uncertain about, and — most valuable of all — what observable event would cause an upgrade or a downgrade.

Three consequences. Consistency is unmeasured: two analysts covering comparable strategies in different asset classes may weight team stability, fee level or capacity differently, and nothing surfaces the divergence because there is no structured record of weighting. Rating changes cannot be attributed: when a fund is downgraded, whether the analyst's view changed or the fund did is not recoverable from the file. And when an analyst leaves — coverage handovers are frequent in this business — the successor inherits reports rather than reasoning, and the rating's continuity becomes a fiction.

It also blocks the measurement above. Scoring ratings as forecasts requires knowing what they were forecasting; without recorded expectations, a rating that was right for the wrong reason is indistinguishable from one that was right.

## Why It's Still Broken
The published artefact is a grade because a grade is what fits in a fund screen, a fact sheet and an adviser's committee memo. Every downstream consumer is satisfied by it, so nothing in the pipeline demands more.

Coverage load is heavy and reports are on a cycle. Structured capture is time taken from the next fund.

And there is real caution about recording internal deliberation at a firm whose ratings move flows and are read by the managers being rated. A written record of an analyst's private doubts about a strategy is a document that could surface in a dispute with that manager — which is exactly why the discipline of writing down what would change the view has never been imposed.

## What a Fix Looks Like
**Record the drivers, weighted.** For each rating: the pillar assessments, the specific factors that moved the grade, and the analyst's confidence. This is largely formalising what the written report already argues.

**Capture the falsifier.** One field — what would cause me to change this rating — is the highest-value item in the whole record. It makes the rating a testable statement, gives the monitoring process something specific to watch for, and gives a successor analyst the thread.

**Attribute every rating change.** Whether the change was driven by a fund event, a performance outcome, an analyst view revision or a methodology update. Without this, the rating history is uninterpretable as a forecast record.

**Measure inter-analyst consistency deliberately.** Route the same fund to two analysts periodically and compare. Uncomfortable, and the only way to know whether a grade means the same thing across the coverage universe.

**Make prior reasoning retrievable.** Analysts reason from comparable situations — a manager departure, a capacity constraint, a fee change — and a searchable record of how those were assessed before is useful immediately, which is what determines whether the capture habit survives.

**Settle the disclosure posture first.** Decide with counsel what is retained and in what form. Recording nothing is not neutral: it leaves the firm unable to demonstrate that its most commercially important judgments are made consistently, at a moment when that is exactly what the market is questioning.

## Who Feels the Pain
Senior analysts, whose accumulated judgment is the differentiated product and is stored as prose; junior analysts, who inherit coverage without the reasoning behind it; advisers, who receive a grade with no visible basis and no statement of what would change it; and the firm, whose analytical franchise is under fee and passive pressure and cannot demonstrate its own consistency.

## Impact If Fixed
Qualitative research is the part of this business that a competitor cannot replicate from public data, and it is the part whose quality has never been measured. Recording the drivers and the falsifiers makes ratings testable statements rather than opinions, makes consistency demonstrable, and creates the labelled record without which no honest accounting of the ratings' predictive value is even possible.
