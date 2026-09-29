# Methodological Choices Decide the Result and Are Recorded as Prose

**Niche:** [[niches/energy-auditors/emv-evaluation-contractors/profile|Efficiency Programme Evaluation Contractors]]
**Industry:** [[industries/energy-auditors|Energy Auditors]]
**Type:** Fix (Pain Point)
**One-liner:** A realization rate that determines whether a utility earns tens of millions in incentive rests on a chain of analytical decisions described in a methodology section, and the chain itself is not stored anywhere it can be examined or reused.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #causal-inference #descriptive-statistics #tacit-knowledge-ml #compliance #data-integration #worker-facing #workflow-orchestration

## The Problem
Evaluations are adjudicated documents. A regulator, the utility, and intervenors all read the methodology section and argue about it, because the choices in it move the result: which participants were excluded, how free-ridership was estimated, what the comparison group was and why, how weather normalization was handled. Those choices are written as prose in a report and are not retained as structured decisions. Three consequences follow. The firm cannot measure whether its own evaluators make comparable choices on comparable studies. When a regulator accepts or rejects an approach, that ruling reaches only the team on that engagement. And when a study is challenged two years later, defending it means reconstructing reasoning from a document written for a different purpose.

## Why It's Still Broken
The deliverable is a report, so the report is what the system stores. Analysis lives in scripts where the reasoning is implicit in code. Evaluation is also a professional-judgment discipline where methodological choice is regarded as expertise rather than as process, which has left it undocumented in the same way estimating and appraisal are — and for the same reason, with the same result when someone leaves.

## What a Fix Looks Like
A decision record attached to every study, captured as the analysis is built: the choices made at each juncture, the alternatives considered, the rationale, and — the highest-value field — the regulatory or client reaction where one was received. That last item is what turns individual engagements into institutional knowledge, because the record of which approaches a given commission has accepted or rejected is currently the most valuable thing a senior evaluator knows and the least transferable. Across studies, the accumulated records make consistency measurable, surface where the firm's practice has drifted, and let a new evaluator start from how the firm has handled this situation before. They also make the pooled evidence base usable, since combining estimates across studies is only defensible when the methodological differences between them are recorded.

## Who Feels the Pain
Evaluators reconstructing choices colleagues have already worked through; practice leaders accountable for methodological consistency with no instrument; regulators receiving studies whose comparability across firms and years they cannot assess; and the firm, whose defensibility in a contested proceeding rests on a report written before the challenge existed.

## Impact If Fixed
Turns methodological judgment into institutional capital in a discipline where it is the entire product, and makes studies defensible years later on their actual basis. It is also the precondition for pooling — an evidence base of estimates is uninterpretable without the methodological differences that produced them.
