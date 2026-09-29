# Fix: Attribution Is Narrative and Cannot Be Checked

**Niche:** The Intelligence Analyst
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** An attribution rests on several specific inferences, is published as a narrative, and when it turns out to be wrong nobody can say which inference failed.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #graph-theory #worker-facing #bayesian-inference
**Contested on:** Whether an analyst can ever learn whether their judgement was right.

## The Problem

An attribution assessment rests on a set of distinct inferences. The infrastructure overlaps with previously attributed activity. The tooling resembles a known family. The targeting matches the group's established pattern. The operational hours suggest a particular timezone. The code contains artefacts consistent with a known developer.

Each is a separate inference with its own reliability. Infrastructure overlap can be strong evidence or an artefact of shared hosting. Tooling similarity may reflect a shared builder used by several groups. Targeting patterns overlap between actors. Timezone inference is famously weak.

The assessment combines them into a narrative with an overall confidence. The narrative is well written and the individual inferences are described and weighted in prose.

When the attribution turns out to be wrong — which happens, and is occasionally very public — nobody can identify which inference failed. The reasoning was not recorded in a form that separates the load-bearing claims, so the correction is a general lesson about caution rather than a specific finding that this kind of inference is less reliable than the team assumed.

So the practice does not learn. The same inference types are used with the same implicit weights, indefinitely.

## Why It's Still Broken

**Narrative is how the tradition writes.** Intelligence assessment is a written form, and a good analyst communicates reasoning through prose. Structuring it feels like reducing craft to a form.

**Weights are implicit and would be uncomfortable to state.** Analysts weigh evidence intuitively. Making the weights explicit invites challenge from colleagues and customers, and reveals disagreement within a team that currently stays hidden.

**Recording the reasoning takes time under deadline.** The structured version is extra work at the moment the report is due.

**Refutation is rare and slow.** With few attributions ever clearly refuted, there is little immediate return on structuring the reasoning, and the payoff arrives years later.

**The customer wants a conclusion.** Reporting is consumed as an answer. A structured breakdown of competing inferences is more honest and harder to act on, which pushes toward confident narrative.

**Nobody aggregates across assessments.** Even where reasoning is described, it is not extracted into a form that would let a practice see which inference types it relies on most and how they have performed.

## What a Fix Looks Like

**Record the inferences separately, with their individual strength.** Infrastructure, tooling, targeting, tradecraft, timing — each as a claim with a stated evidential weight, alongside the narrative rather than replacing it. Five minutes per assessment and it makes the reasoning inspectable.

**State what would refute each one.** For the load-bearing inferences, what evidence would undermine them. This is a key-assumptions check by another name, it is cheap, and it identifies the fragile parts of an assessment before publication.

**Apply competing hypotheses on major calls.** Which other actors could produce this evidence, and why they are less likely. This is a documented technique that demonstrably reduces bias and is skipped under deadline on precisely the assessments where it matters most.

**Track which inference types the practice relies on.** Across assessments, which evidence categories carry the weight. A practice discovering it attributes primarily on infrastructure overlap has learned something important about its own exposure.

**Revisit when contradicting evidence arrives.** With structured inferences recorded, a later contradiction identifies the specific claim that failed — which is how a practice learns that a particular inference type is weaker than assumed.

**Publish the reasoning structure to customers.** A customer who can see which inferences support an attribution can weigh it against their own knowledge, which is a better product than a confident conclusion.

**Separate the cluster from the name.** Much attribution confusion comes from conflating an activity cluster with a named group. Recording them as distinct claims — this activity forms a cluster, and this cluster is the group known as X — makes the weaker second claim visible as a separate judgement.

## Who Feels the Pain

The analyst, who cannot learn from being wrong because the record does not identify what was wrong.

The practice, which repeats the same implicit weighting of evidence types indefinitely with no mechanism to discover that one of them is unreliable.

The customer, who receives a conclusion and cannot assess how much weight it deserves or which part of it is fragile.

And the field, where attribution disputes between vendors are frequently disputes about a specific inference that neither side has stated separately.

## Impact If Fixed

Recording inferences separately costs five minutes per assessment and makes the reasoning inspectable, correctable and — crucially — learnable from when it fails.

Separating the activity cluster from the group name would resolve a large share of the attribution confusion in this field, because the two claims have very different evidential strength and are routinely presented as one.

And tracking which inference types a practice depends on would reveal its own methodological exposure, which is a question no intelligence practice has ever been able to ask about itself.
