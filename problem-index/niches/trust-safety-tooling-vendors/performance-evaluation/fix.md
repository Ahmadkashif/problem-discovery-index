# Fix: Every Buyer Runs Their Own Evaluation Badly

**Niche:** Performance Evaluation & Benchmarking
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** In the absence of a benchmark every platform runs its own proof of concept, without a methodology, and two buyers evaluating the same two products reach opposite conclusions.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #compliance #workflow-orchestration
**Contested on:** Whether two products can be compared at all.

## The Problem

A platform evaluates two classifiers. They assemble a sample of their own content, label some of it, run both products, and compare.

The evaluation is not methodologically sound, through no fault of the team. The sample was drawn from what was convenient rather than from a defined population. The labels were produced by whoever was available, with no agreement measurement, against a policy definition that was not written down precisely. Both products were run at default thresholds, which are not comparable. The categories were compared in aggregate. And the sample was too small to distinguish the products on anything but a large difference.

The result is a conclusion that feels evidenced and rests on an evaluation that would not survive examination. And another platform, running the same comparison on their own content with their own labels and their own thresholds, reaches a different answer.

So the absence of a shared benchmark does not merely prevent comparison — it produces a large amount of duplicated, methodologically weak evaluation effort, at every buyer, with inconsistent results.

Each evaluation costs a platform weeks. Across the market it is an enormous duplicated expense producing conclusions that do not aggregate to anything.

## Why It's Still Broken

**No benchmark exists, so the proof of concept is the only option.** Every buyer must evaluate because nobody else has.

**No methodology standard exists either.** Even a sound self-evaluation requires a protocol — sampling, labelling, agreement measurement, threshold matching — and nobody has published one.

**Threshold comparison is the most common error.** Running two products at their default thresholds compares two different operating points, which is the single most frequent methodological mistake and produces meaningless results.

**Labelling is the expensive part and is done cheaply.** Proper labels need multiple annotators, a written policy definition and agreement measurement. Most proof of concepts use one person and an informal understanding.

**Sample sizes are too small.** Distinguishing two products that differ by a few percentage points requires more labelled data than a proof of concept usually produces.

**Results are not shared.** Every platform's evaluation stays internal, so the market accumulates no comparative knowledge despite enormous spending on it.

## What a Fix Looks Like

**Publish an evaluation methodology.** A protocol covering sampling, policy definition, labelling with agreement measurement, threshold matching and sample size. This is a document, costs a working group a few months, and would improve every proof of concept in the market immediately.

**Match operating points, not defaults.** Compare products at equal false positive rates rather than at their default thresholds. This single correction fixes the most common error in these evaluations.

**Label properly on a smaller sample.** Multiple annotators with a written definition on a thousand items is worth more than one annotator on ten thousand, and most teams do the reverse.

**Report disaggregated.** By language and content type, because the aggregate comparison conceals exactly what the platform needs to know for its own markets.

**Share results where possible.** Even anonymised, aggregated comparative results across buyers would build the comparative knowledge the market lacks, and a buyer consortium could do this without any vendor agreeing.

**Reuse the evaluation set.** A platform's labelled evaluation set is reusable for every future vendor evaluation and for monitoring the incumbent, and is frequently discarded after the proof of concept.

**Measure the incumbent too.** Most platforms evaluate candidates and never re-evaluate what they are running, so the comparison is against an unmeasured baseline.

## Who Feels the Pain

The platform, spending weeks on an evaluation that does not support the conclusion drawn from it, and choosing a vendor on a weak basis.

The trust and safety engineer running the proof of concept, who is not an evaluation methodologist and has no protocol to follow.

Vendors with genuinely better products, who lose evaluations run at mismatched thresholds on small samples with inconsistent labels.

And the market, which spends an enormous aggregate amount on duplicated evaluation and accumulates no comparable knowledge from any of it.

## Impact If Fixed

A published evaluation methodology is a document that would improve every proof of concept in the market and is well within the capability of a buyer working group.

Matching operating points rather than comparing defaults corrects the most common single error in these evaluations and costs nothing.

And reusing the labelled evaluation set for ongoing monitoring of the incumbent would convert a one-off proof of concept into a standing measurement — which is what a platform actually needs and almost none maintain.
