# A Catalogue That Goes Stale Silently

**Niche:** [[niches/ai-red-teaming-firms/automated-probing-platforms/profile|Automated Probing Platforms]]
**Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Automated suites provide breadth cheaply and go stale as models are updated against known attacks, and nothing in the product tells a customer how current the catalogue they are being tested against actually is.
**Tags:** #evaluation-metrics #change-point-detection #automation #descriptive-statistics #confidence-intervals #compliance #time-series-forecasting #hypothesis-testing
**Contested on:** Every serious competitor in this sub-niche is fighting to cover broad ground cheaply and stay current as models are updated against known techniques — and whoever does that takes the account, because the alternative is a public dataset that goes stale.

## The Problem
A platform runs a suite against a customer's deployed assistants every week and reports clean. The suite is built on a public dataset last updated nine months ago, against which every major model has since been hardened. The clean result is close to guaranteed and close to meaningless — it demonstrates that the models were updated against known attacks, which everyone already knew. The customer's compliance function files the report. The platform's value depends entirely on catalogue currency and the product reports nothing about it, which means a diligent vendor and a negligent one produce identical-looking reassurance.

## Why Nobody Has Built This
Maintaining currency is ongoing research work with an ongoing cost, while a static suite has none — and the output looks the same to the customer either way. Reporting catalogue age invites the question of what a clean result is worth. New techniques come from the research community and from engagement work, and wiring those into a product is a pipeline nobody built. And the customer cannot evaluate currency, so it is not priced.

## What to Build
Make currency the product. Report catalogue version and age with every result, and report per-technique effectiveness trend, so a customer can see that a technique has stopped working everywhere and that their clean result on it means nothing — this disclosure is the fix and it differentiates immediately. Retire techniques that no longer succeed against any current model, since running them inflates apparent coverage while testing nothing. Ingest new techniques continuously from the research literature and from the firm's own engagement work, with a stated lag, which is the operational commitment this business is actually selling. Report effective coverage — techniques that currently work against something — rather than a raw catalogue count, which is the number that grows without meaning. Adapt the suite to the system under test, skipping categories irrelevant to a deployment and concentrating on those that are, since uniform sweeps waste most of their budget. Report success rates rather than pass or fail, which the fix note develops. Distinguish clearly between what the automated ground covers and what it cannot, so a customer does not read breadth as completeness — this honesty is what lets the automated product coexist with expert assessment rather than being mistaken for it. And publish catalogue currency as a competitive metric, since it is the axis this business should be competing on and nobody currently reports.

## Target Customer
Engineering and security teams running many deployed systems, compliance functions filing the reports, and the platform vendors whose differentiation is currently invisible.

## Impact If Built
Catalogue currency is the entire value of this product and nothing reports it, so a diligent vendor and a negligent one look the same. Reporting effective coverage — techniques that currently work against something — replaces a count that grows without meaning.
