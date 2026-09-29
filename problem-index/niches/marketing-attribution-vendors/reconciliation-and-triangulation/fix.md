# Averaging Two Overconfident Numbers

**Niche:** [[niches/marketing-attribution-vendors/reconciliation-and-triangulation/profile|Reconciliation & Triangulation]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Two estimates that each understate their own uncertainty are averaged, and the result is presented with more confidence than either, which is exactly backwards.
**Tags:** #confidence-intervals #bayesian-inference #hypothesis-testing #evaluation-metrics #monte-carlo-methods #quick-win #descriptive-statistics #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to combine three methods with unknown biases into one defensible number — and whoever does that properly replaces an instruction to triangulate that nobody can execute.

## The Problem
Vendor A says a channel contributed twelve percent. Vendor B says twenty-four. The measurement lead reports eighteen. That average is treated as more reliable than either input, on an intuition borrowed from averaging repeated measurements of the same quantity with independent random error. These are not that. They are two estimates with systematic biases of unknown sign and magnitude, possibly correlated, each already presented with an interval that understates its true uncertainty. Averaging them produces a number that is not more likely to be right than either and is presented with more confidence than both, which is the opposite of what the disagreement should have caused.

## Why It's Still Broken
Averaging feels rigorous and produces a single number, which is what the meeting needs — the practice survives because it resolves a social problem rather than a statistical one. The distinction between random and systematic error is not intuitive to non-statisticians. Each vendor's interval already understates uncertainty, so the inputs are misleading before the combination. And nobody owns the combination step.

## What a Fix Looks Like
Let the disagreement widen the interval rather than disappear. Report a range spanning both estimates rather than their midpoint, which is the fix, is more honest, and is a better basis for a decision than a false point — a decision robust across the range needs no further resolution, and one that is not should trigger an experiment. Treat method disagreement as the dominant uncertainty term, because it is larger than the within-method intervals and is currently the only one discarded. State plainly that averaging systematic biases does not cancel them, which is the specific misconception and takes one sentence to correct. Identify decisions that are insensitive to the disagreement, since many are and resolving the number is then unnecessary. Trigger an experiment where the decision is sensitive, which is the efficient use of a measurement budget and turns an argument into a question. Ask each vendor to state their expected bias direction, which is uncomfortable and highly informative. Report the disagreement as a standing metric, since a business whose methods disagree by a factor of two should know that is its measurement reality. Avoid weighting by preference or by relationship, which is what happens in the absence of a stated method. Document the combination reasoning so it can be reviewed. And escalate persistent disagreement as a finding rather than smoothing it, because it is the clearest signal the category produces about its own state.

## Who Feels the Pain
Measurement leads producing a number they cannot defend; businesses allocating on a midpoint with no standing; and the category, whose central weakness is resolved by an arithmetic operation that does not apply.

## Impact If Fixed
Averaging survives because it resolves a social problem rather than a statistical one, and systematic biases do not cancel. Reporting the range and treating method disagreement as the dominant uncertainty term turns a false point estimate into a decision that can be tested where it matters.
