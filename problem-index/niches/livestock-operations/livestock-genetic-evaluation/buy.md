# Performance Data From Producers Who Report What Flatters Them

**Niche:** [[niches/livestock-operations/livestock-genetic-evaluation/profile|Livestock Genetic Evaluation Programmes]]
**Industry:** [[industries/livestock-operations|Livestock Operations]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The evaluation is only as good as the weights and scores members submit, and members are selling the animals being evaluated.
**Tags:** #anomaly-detection #tabular-ml #data-integration #evaluation-metrics #automation

## The Problem
Genetic evaluation runs on member-submitted performance records: birth weights, weaning and yearling weights, calving ease scores, udder and foot scores, and increasingly genomic samples. The submissions are voluntary, unaudited, and made by producers who will later sell the animals the evaluation describes.

The failure modes follow. Producers report the calves that did well and omit the ones that did not. Contemporary groups — the comparison sets that make records meaningful — are split by producers in ways that flatter particular animals. Weights are estimated rather than measured. Subjective scores drift by scorer. A herd changes management and its records shift for reasons that have nothing to do with genetics.

Statistical safeguards exist — contemporary grouping rules, edits, outlier checks — and analysts who know their member herds catch a great deal more. That last part is entirely in people.

## What Already Exists
Data quality platforms handle validation, distributional monitoring, and stewardship queues well. Statistical genetics software includes standard edit and outlier procedures. Both are mature.

## The Customization Gap
Generic quality tooling assumes an indifferent data source. Here the source has a direct financial interest in the output.

**Selective reporting is the central problem and it is invisible per record.** Every submitted weight can be plausible while the set is biased by omission. Detecting under-reporting requires reasoning about what should have been submitted — expected calf crops from recorded breedings — which no generic tool frames.

**Contemporary group integrity is the load-bearing assumption.** The entire evaluation rests on animals being compared within genuinely comparable management groups, and group definition is partly under the producer's control. Detecting strategic group splitting is a specific, checkable pattern nobody monitors systematically.

**Herd-relative baselines.** A record's plausibility is a question about this herd's own history, its management, and its region — not about the breed distribution. That requires maintained herd profiles, which no generic platform models.

**Influence-weighted triage, down to the animal.** An erroneous record on a widely used sire's progeny moves that sire's evaluation and therefore thousands of breeding decisions. Prioritization should follow effect on published predictions, which is a computation about the evaluation rather than about the record.

**Corrections must be reconstructable.** Evaluations are published, animals are sold on them, and disputes happen. Every edit and exclusion needs an audit trail years later.

## Target Customer
Director of Data Operations at a breed association or evaluation body, where a small analyst team validates growing submission volume against fixed evaluation run dates.

## Impact If Solved
The evaluation's credibility is the association's entire franchise, and it rests on unaudited data submitted by interested parties. Detecting selective reporting and strategic contemporary grouping — neither of which any current control addresses systematically — protects the one product the whole industry transacts on.
