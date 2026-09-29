# Panel Data Practice

**Niche:** [[niches/payment-processors/network-outcome-intelligence/profile|Network Outcome Intelligence]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Econometrics has a mature toolkit for panels of many units observed repeatedly, and the largest transaction panel in existence is used to produce invoices.
**Tags:** #causal-inference #hypothesis-testing #gradient-boosting #confidence-intervals #evaluation-metrics #bayesian-inference #descriptive-statistics #monte-carlo-methods
**Contested on:** Every serious competitor in this niche is fighting to turn a network-scale record of approvals, declines and settlements into knowledge no issuer and no merchant can have — and whoever does that owns the empirical basis for questions the industry answers with folklore.

## The Problem
Panel data — many units observed repeatedly over time — is one of the best-served structures in applied statistics. Fixed and random effects, hierarchical models, difference-in-differences over policy changes, and the identification strategies that come with them are mature, and economists build careers on far smaller panels than a payment processor generates in an hour. The processor's data is a panel of issuers, merchants and cardholders observed continuously with outcomes attached, and it is aggregated into invoices.

## What Already Exists
Panel data econometrics with fixed and random effects; hierarchical modelling across nested units; event study designs around rule changes; instrumental variable identification; and clustered inference.

## The Customization Gap
The adaptation is to a panel the analyst can also experiment on. It requires: (1) the ability to randomise, since the processor controls the routing and retry decisions and can therefore run experiments rather than relying solely on identification strategies — this turns an observational panel into an experimental one and is an advantage econometrics rarely has; (2) units that are commercial counterparties whose behaviour responds to the processor's own actions, so the panel is not passive; (3) scale that makes computation rather than inference the binding constraint, inverting the usual situation; (4) governance constraints on cross-merchant analysis that are legal and contractual rather than methodological; and (5) results that must drive a real-time decision rather than a published estimate, changing what form the output takes.

## Target Customer
Processor data science teams, the orchestration and optimisation vendors without network position, and applied econometricians for whom this is an unusually rich unexploited panel.

## Impact If Solved
Economists build careers on far smaller panels than a processor generates in an hour, and this one produces invoices. The ability to randomise turns an observational panel into an experimental one, which is an advantage the econometric toolkit rarely gets to assume.
