# Sourcing Analyst Running Evaluations

**Industry:** [[data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Worker Life Changing
**One-liner:** Data sourcing analysts spend their quarters running bespoke evaluations of sample files against internal benchmarks, building the same comparison harness repeatedly because the market provides no basis for comparison.
**Tags:** #hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #k-nearest-neighbors #cross-validation #workflow-orchestration #worker-facing

## The Problem
A sourcing analyst at a bank, an insurer or a data-heavy enterprise is asked to find the best available dataset for a use case. Several providers claim to serve it.

The evaluation is theirs to build. Obtain samples, which requires sales conversations and non-disclosure agreements. Load each into an environment. Write comparison logic — coverage against an internal reference list, field population rates, accuracy on the subset where truth is known, freshness, overlap with existing holdings. Normalise the differing schemas enough that comparison is meaningful. Assemble a recommendation.

It takes weeks and it is rebuilt every time, because the harness is specific to the entity type, the fields and the internal benchmark used.

The samples make it worse. They are curated, so measured quality overstates production quality, and the analyst knows it and cannot quantify the gap. Their recommendation carries an asterisk they cannot remove.

Then a purchase is made, production data arrives, and it differs from the sample in ways that require the evaluation to be redone against reality.

## Why It Matters to the Worker
Sourcing analysts are commercially astute people doing data engineering. The valuable part of the role — understanding what the business actually needs, negotiating terms, managing the provider relationship — competes with harness construction.

The credibility exposure is the specific pressure. The analyst recommends a purchase worth six or seven figures on evidence they know is compromised by sample curation, and if the dataset underperforms, the recommendation is theirs.

The work is also unshareable. Each evaluation is bespoke, so nothing accumulates. An analyst who has assessed forty firmographic providers has real knowledge of the market and no artefact expressing it, and when they leave it goes with them.

And the negotiating position is weak. Without measured comparison the analyst cannot credibly say a competitor offers better coverage at a lower price, which is exactly the leverage the role exists to apply.

## What a Solution Looks Like
A reusable evaluation framework rather than a bespoke harness. Coverage, population, freshness, overlap and accuracy-where-checkable are standard measurements, and the harness differs only in the entity type and the reference — which makes it configurable rather than rewritten.

Privacy-preserving overlap measurement against internal reference data, so coverage of the buyer's actual population can be established before purchase without disclosing the reference list.

Sample representativeness testing. Whether a sample is drawn from the same distribution as the full dataset is testable in several ways — checking a provided sample against a differently-drawn one, or against known population statistics — and would put a number on the asterisk.

Accumulated evaluation history as an internal asset. Every assessment the organisation has run, on which provider, with what result, retained and comparable, which is the market knowledge that currently lives in an analyst's head.

Continuous re-evaluation after purchase, because datasets degrade and nobody currently checks whether the dataset they bought is still the dataset they are receiving.

## Impact If Solved
Data purchasing decisions are large, recurring and made on evidence the buyer builds by hand from curated samples. A reusable measurement framework converts weeks of harness construction into a configuration, and it gives the sourcing function the comparative evidence that is its entire source of negotiating leverage.
