# Build: The Severity Reference

**Niche:** Severity Calibration
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A cross-programme severity distribution per finding class and context, built from the platform's own corpus, so a rating can be compared against how the market values the same thing.
**Tags:** #bayesian-inference #gradient-boosting #evaluation-metrics #confidence-intervals #hypothesis-testing #expectation-variance-covariance #k-means-clustering #data-integration
**Contested on:** Whether a finding's severity can be referenced against how comparable findings were rated across the whole market, or remains one programme's private judgement.

## The Problem

Severity determines payment, and severity is assigned by one person at one programme with no reference to anything.

The same authorisation bypass is rated critical at one organisation and medium at another. Sometimes that reflects a real difference — one is on a payment path, one is on an internal tool. Frequently it reflects the programme's remaining budget this quarter, the triager's disposition, or a policy written by someone who left. Neither the researcher nor the programme can tell which, because there is no distribution to compare against.

The researcher's position is the worse one. They cannot predict what a finding will earn, cannot choose between programmes on expected value, and cannot argue a rating except by assertion. The most common grievance in this community is not that payments are low but that they are unpredictable, and unpredictability is what drives capable people to spend their time elsewhere.

The platform holds the entire answer. Millions of severity assignments across thousands of programmes, with finding class, asset type, sector and outcome attached. It computes reputation scores from this data and does not compute the one statistic both sides most need.

## Why Nobody Has Built This

**The paying side would be measured.** A distribution makes systematic under-raters visible. The platform's customers are the programmes, and publishing a statistic that embarrasses some of them is a commercial decision no product manager takes lightly.

**Context genuinely matters and is hard to encode.** The payment-system-versus-marketing-site difference is real, and a reference that ignores it produces wrong comparisons that programmes will reject immediately and correctly. Encoding enough context to compare like with like is the substantive work.

**Finding classification is inconsistent.** Comparing ratings requires a consistent taxonomy, and submissions are classified loosely, differently across platforms, and sometimes not at all. The taxonomy has to be applied or inferred consistently before any comparison is possible.

**Severity and payout are entangled.** Programmes with small budgets rate lower partly because the band determines the payment. Separating the assessment of severity from the willingness to pay requires reporting both, which exposes a relationship most programmes would rather leave implicit.

**A reference becomes a de facto standard.** Whoever publishes it acquires influence over how the whole market prices, which is a responsibility as much as an opportunity, and attracts criticism from every programme that sits below the line.

## What to Build

**Normalise the taxonomy first.** Every finding classified consistently — CWE or an equivalent — inferred from the submission text and evidence where it was not supplied. Without this nothing downstream is possible, and it is a well-posed text classification problem over a corpus the platform already holds.

**Model context explicitly.** Asset type, data sensitivity, authentication requirement, exposure, sector and regulatory character as covariates. The output is not a single distribution per class but a distribution conditional on context, which is what makes the comparison defensible.

**Report distributions, not verdicts.** For a given class in a given context: the distribution of severities and payouts assigned across the market, with sample size and uncertainty. Never a prescribed rating — a reference. Programmes retain their judgement and acquire a mirror.

**Surface it to the triager at the moment of assessment.** When a triager assigns a severity that sits well outside the conditional distribution, show them. Most will reconsider or record a reason, and both outcomes are improvements. This is the highest-value placement and it is non-confrontational, because it is information rather than enforcement.

**Capture divergence reasons.** When a programme rates away from the reference, a recorded reason — compensating control, deprecated asset, regulated data, higher business impact. This preserves legitimate variation and makes the unexplained variation visible, which is the whole point.

**Show researchers the expected value before they choose.** Typical payout by class for programmes of this shape, visible at programme selection. Researchers currently allocate their scarcest resource with no price information at all.

**Publish per-programme divergence.** Each programme's rating distribution relative to the conditional reference. This is the accountability mechanism, and it rewards the programmes that rate fairly — which currently get no benefit from doing so.

## Target Customer

The platforms, and the honest argument is researcher supply rather than programme satisfaction. Supply is the binding constraint on the marketplace, unpredictable pricing is the main thing suppressing it, and no competitor can replicate the corpus.

Programme managers who rate fairly are a genuine constituency, because a reference lets them demonstrate it.

An industry body or researcher organisation would be a more credible publisher than any single platform, and a cross-platform reference would be better still — though the corpora are proprietary, which makes this the likely limit.

## Impact If Built

Pricing becomes predictable, which is the condition every functioning labour market requires and this one lacks. Researchers can allocate effort on expected value rather than on hope.

Showing a triager where their assessment sits relative to the market is a light-touch intervention that would reduce arbitrary variation substantially without anyone adjudicating anything.

And separating justified context from unexplained divergence is what would let the market reward fair programmes — which is the only mechanism that improves behaviour without rules.
