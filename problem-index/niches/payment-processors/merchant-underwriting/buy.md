# Counterparty Credit Practice

**Niche:** [[niches/payment-processors/merchant-underwriting/profile|Merchant Underwriting]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Banks model counterparty exposure with validated models, limit frameworks and back-testing, and merchant underwriting scores by category and sets reserves from a table.
**Tags:** #gradient-boosting #logistic-regression #compliance #evaluation-metrics #confidence-intervals #survival-analysis #hypothesis-testing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to decide whether a business is safe to process for, against the same registries everyone else uses, and to learn from the outcome — and whoever closes that loop stops grading a decision against losses it never attributes back.

## The Problem
Assessing whether a counterparty will cost you money is a developed banking discipline. Exposure is modelled, limits are set from modelled loss distributions rather than from convention, models are validated independently and back-tested against realised losses, and the framework is governed. Merchant acquiring carries genuine counterparty credit exposure — the acquirer is liable if a merchant fails and chargebacks follow — and underwrites it with category tables, rules and a website review.

## What Already Exists
Counterparty credit models with exposure and loss-given-default estimation; limit frameworks derived from modelled loss; independent model validation; back-testing against realised outcomes; and portfolio-level concentration management.

## The Customization Gap
The adaptation is to a counterparty whose exposure depends on their future business behaviour. It requires: (1) exposure driven by chargeback and refund behaviour that arrives months after the transaction, so the exposure profile is a delayed liability rather than a drawn balance — modelling that tail is the substantive difference from credit exposure; (2) a merchant who can change what they sell without telling the acquirer, which has no clean credit analogue and is a real and undetected exposure; (3) decisions made in minutes for the long tail of small merchants, where credit practice assumes a review; (4) portfolio concentration by merchant category and by sector shock, which acquirers experience and rarely model; and (5) the acquirer's loss being capped by reserves it can set, which gives a control lever credit practice manages differently.

## Target Customer
Acquirer risk leadership, sponsor banks overseeing acquiring portfolios, and credit risk vendors for whom merchant acquiring is an adjacent market.

## Impact If Solved
Acquiring carries genuine counterparty credit exposure and underwrites it with a category table. The delayed chargeback liability tail and the merchant who changes what they sell are the two exposures credit practice has no clean analogue for.
