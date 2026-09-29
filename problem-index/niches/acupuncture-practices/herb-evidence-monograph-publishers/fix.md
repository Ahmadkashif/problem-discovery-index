# Grading Decisions Are Recorded as Letters, Not Reasoning

**Niche:** [[niches/acupuncture-practices/herb-evidence-monograph-publishers/profile|Herb & Supplement Evidence Monograph Publishers]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Fix (Pain Point)
**One-liner:** Hours of adjudication over conflicting trials resolve into a single letter grade in a database field, and the reasoning that produced it is discarded — so the next reviewer, facing the same herb three years later, starts from nothing.
**Tags:** #large-language-models #bert #transformers #evaluation-metrics #hypothesis-testing #descriptive-statistics #tacit-knowledge-ml #data-integration #worker-facing

## The Problem
Assigning an efficacy grade to a botanical for a given indication is the most consequential judgment the publisher makes and the least documented. A researcher weighs a scatter of small trials with incompatible preparations, inconsistent dosing, and mixed quality, decides how much a positive meta-analysis built on weak inputs is worth, and writes a letter into a field. Everything that mattered — which studies were discounted and why, how much the heterogeneity of preparations weighed against pooling, what would have to change for the grade to move — exists only as the researcher's reasoning at the moment of the decision. Three years later the monograph comes up for review, a different researcher inherits the letter, and has no way to tell whether it was a confident call on strong evidence or a reluctant one on thin evidence that a single decent trial would overturn. In practice inherited grades are conservative and sticky, because revisiting a decision you cannot reconstruct is expensive.

## Why It's Still Broken
The editorial systems were built to produce and version published text, and a grade is stored the way it is displayed — as a value. There is no structure for a decision record, so nothing collects it. The organizational logic reinforces this: grading rationale is not part of the subscriber deliverable, so time spent documenting it reads as overhead rather than output, and under a standing publication cadence overhead loses. The result is a publisher whose entire commercial value rests on the credibility of its grades, holding no record of how any of them were reached.

## What a Fix Looks Like
A decision record attached to every grade, captured as a by-product of the work rather than as a separate documentation task. At the moment of assignment the reviewer records which studies were weighted and which discounted, the reason for each exclusion, the confidence in the call, and — the highest-value field — what evidence would change it. That last item converts a static grade into a standing trigger: when a trial arrives matching the stated condition, the monograph surfaces itself for review automatically instead of waiting for its slot in the cycle. Across the corpus the accumulated records support things the publisher cannot currently do at all: measure inter-reviewer consistency on comparable evidence, find grades resting on a single study or on evidence now superseded, and show a subscriber not just what the grade is but on what basis it stands.

## Who Feels the Pain
Reviewers inheriting decisions they cannot reconstruct and defaulting to conservatism; the editorial director accountable for consistency across a corpus with no instrument to measure it; and subscribers — clinicians and payers making coverage decisions — who receive a letter with no visibility into its strength.

## Impact If Fixed
Converts the corpus from a set of published conclusions into a body of reasoning, which is the more defensible product. Review cycles shorten because the second reviewer starts from the first one's argument. Grade changes become explainable at the moment a subscriber challenges one, which is the moment credibility is actually tested. And the record of what would change each grade turns the whole corpus into a trigger network against incoming literature, which is exactly the surveillance capability the editorial function is otherwise trying to staff its way to.
