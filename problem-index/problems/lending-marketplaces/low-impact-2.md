# Lead Quality Scoring and Consent Compliance

**Industry:** [[lending-marketplaces|Lending Marketplaces]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Leads are priced on source and profile and sold before anyone knows whether they convert, while the consent record that makes contacting them lawful is the single largest litigation exposure in the business.
**Tags:** #gradient-boosting #logistic-regression #bert #k-means-clustering #evaluation-metrics #feature-engineering #compliance #data-integration

## The Problem
A lead is a consumer who submitted a form. Its value depends on whether that consumer will actually take a loan, which is unknown at the moment of sale. Pricing is therefore by proxy: traffic source, credit band, loan amount, state, time of day.

The proxies are weak and the sources vary enormously. The same nominal credit band converts at very different rates depending on whether the consumer arrived from organic search, a comparison affiliate, a display retargeting campaign or a co-registration path where they may not fully realise they submitted anything. Affiliate traffic in particular ranges from excellent to fabricated, and fraudulent lead generation — invented or scraped profiles submitted for payment — is a persistent problem the industry manages rather than solves.

Then there is consent. Contacting a consumer by phone or text requires documented prior express consent under the TCPA, and the record must show what disclosure was displayed, when, and to whom. Consent obtained through a chain of affiliates is only as good as the weakest link, and the marketplace is exposed to the conduct of partners it does not control. Class action litigation in this area is routine and expensive, and the 2024–25 regulatory changes around consent scope and revocation tightened the requirements further.

Lead resale multiplies both problems. A lead sold to several lenders generates several contact attempts under one consent record, and the consumer experiences it as being hunted.

## What Already Exists
Lead scoring systems exist at every marketplace. TrustedForm and Jornaya certify consent capture with a replayable record. Suppression lists and DNC scrubbing are standard. Ping-tree infrastructure handles routing and resale. Fraud detection on lead submission exists in basic form.

## The Customisation Gap
Conversion prediction at submission is coarse. The marketplace holds a large history of leads with their eventual funding outcomes and the full behavioural context of submission — session behaviour, form completion pattern, device, time to complete, field revision — and prices on source and credit band. The behavioural signal distinguishes a genuine applicant from a fabricated one far better than the source label does.

Source quality is monitored on aggregate conversion and drifts before the aggregate moves. A partner whose lead behaviour profile has shifted — faster completions, less field revision, different device mix — has usually changed something upstream, and detecting that early is the difference between a bad week and a bad quarter.

Consent chain validation is document-level rather than semantic. Whether the disclosure a consumer actually saw covers the parties who will contact them, in the language the rules require, is a comparison between a captured page and a legal requirement, and it is performed by sampling.

And nothing models contact burden. The number of calls a consumer receives after one submission is knowable, is the single largest driver of complaints and of litigation risk, and is not a variable anyone optimises.

## Impact If Solved
Lead quality determines lender relationships and consent quality determines legal exposure, and both are managed with proxies while the underlying behavioural and document evidence sits unused. Predicting conversion from submission behaviour, detecting source drift early and validating consent chains semantically address the commercial and the legal problem with the same data.
