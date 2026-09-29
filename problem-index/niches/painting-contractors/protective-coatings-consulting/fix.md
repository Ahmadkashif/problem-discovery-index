# Remaining Service Life Is the Deliverable and Is Never Scored

**Niche:** [[niches/painting-contractors/protective-coatings-consulting/profile|Protective Coatings Consulting & Failure Analysis]]
**Industry:** [[industries/painting-contractors|Painting Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** The firm tells owners how many years a coating has left, the owner comes back in five years, and nobody checks the last answer.
**Tags:** #evaluation-metrics #confidence-intervals #causal-inference #tacit-knowledge-ml #automation

## The Problem
The sentence that matters in a condition survey is the one that says how long the coating has left and when the owner should budget to recoat. It determines the client's capital plan, and it is a professional judgment made by an experienced engineer looking at condition data, exposure, and the structure's history.

Those engineers are often very good. Nobody knows how good, because the prediction is never scored.

The information to score it exists and is unusually clean. Many clients are repeat clients on a survey cycle, so the firm returns to the same asset. A prediction was made; a subsequent survey observed the outcome. The firm holds both. Nothing joins them.

The consequences compound. Systematic bias goes undetected — a firm that has been conservative for a decade, recommending recoating earlier than necessary, has no way to discover it, and neither does the client. Differences between engineers go undetected. And the tacit knowledge that makes the senior people good — the thing they notice about a specific exposure or a specific substrate that adjusts the estimate — is never separated from the formal condition data, so it retires with them. Pass 1 records exactly this failure mode a layer below, in painting contractors whose differentiation is preparation judgement that lives only in the crew.

## Why It's Still Broken
Recoating decisions are slow. Five to ten years pass between a prediction and its test, which is longer than most engagement records are kept in a form anyone can find, and longer than the tenure of the person who made the call.

Interventions confound the record. If the firm recommends recoating in three years and the owner recoats in three years, the prediction is untestable. The clean signal comes from assets where the owner deferred, which happens constantly and is not systematically recorded as a deferral.

And the incentive runs the wrong way. A consultancy that measured its own predictions would create a discoverable record of when it was wrong, in a field where the reports are used in litigation over premature coating failure.

## What a Fix Looks Like
**Record predictions as data.** Every survey emits a remaining-life estimate; store it as a structured field on the asset — value, date, engineer, and the condition state it was based on — rather than only as a sentence in a report.

**Join to what the next survey found.** For every asset resurveyed, compare the predicted condition trajectory to the observed one. Report bias and spread by exposure class, coating type, and engineer.

**Track deferrals explicitly.** An owner who defers a recommended recoating is running an experiment on the firm's behalf. Recording deferral and its outcome turns a client's budget constraint into the firm's most valuable evidence.

**Elicit the adjustment, not just the number.** When a senior engineer overrides what the condition data alone would suggest, capture why in a structured way. That reason is the tacit knowledge, and it is the part that currently cannot be transferred.

**Use it internally first.** Calibration reporting has real litigation exposure. The value is available without publishing: an engineer who knows their own historical bias makes better estimates, and a firm that knows its spread can say something specific to a client about the confidence around a recommendation.

## Who Feels the Pain
The consultancy's principal engineers, who carry the estimate personally with no feedback on it; the junior engineers who cannot learn a judgment nobody scores; and the asset owners, who receive a number with no stated uncertainty and build a capital programme on it.

## Impact If Fixed
Calibrated remaining-life estimates with honest intervals, the ability to distinguish a good estimator from a confident one, and a mechanism for moving senior judgment into a form that survives a retirement — in a profession where the senior people are the product.
