# Capture Measured Against Outcomes Rather Than Activity

**Niche:** [[niches/crm-platforms/revenue-intelligence-capture/profile|Revenue Intelligence & Capture]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Revenue intelligence captures everything and reports activity counts and talk ratios, which are inputs, while the outcome that would say whether any of it matters sits in the same platform unjoined.
**Tags:** #gradient-boosting #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #cross-validation #revenue-impact #survival-analysis
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A dashboard reports that representatives who ask more questions have higher win rates, that talk-to-listen ratio correlates with success, and that deals with more multi-threading close more often. Each is presented as a finding. Each is also what you would expect if good representatives get good deals — a deal that is going well produces engaged customers who ask questions and involve colleagues, so the behaviour and the outcome are both downstream of the deal's quality. Coaching a representative to talk less on a dying deal does not resurrect it. The category has built a large business on correlations it presents as levers, and the data to do better is in the same system.

## Why Nobody Has Built This
Correlational dashboards are easy to build, easy to demo and easy to believe, and the customers asking for them are sales leaders who find them intuitive. Doing better requires treating coaching as an intervention to be tested rather than as advice to be given, which means running experiments inside a sales organisation — culturally difficult and rarely attempted. There is also a commercial disincentive that ought to be named: a vendor that rigorously tests its own coaching recommendations may find some of them do nothing, which is harder to sell than a dashboard that always finds a pattern.

## What to Build
Outcome-linked measurement with the confounding handled explicitly. Every captured behaviour is joined to the deal outcome, and the analysis controls for what a deal's own quality predicts — segment, deal size, competitive situation, inbound versus outbound origin, and the account's prior relationship — so that what is reported as a behavioural effect is not simply deal quality wearing a disguise. Where the organisation is willing, coaching recommendations are tested: a behaviour is introduced to a randomly assigned group of representatives and the outcome difference is measured, which is the only design that supports the causal claim the category makes. Prediction is separated from prescription and both are reported honestly: this signal predicts outcome, and we do not know whether changing it changes anything. That distinction is the product, and it is the one thing nobody in the category currently offers.

## Target Customer
Revenue intelligence vendors willing to test their own claims, large sales organisations with enough representatives to run experiments, and the enablement functions whose programmes are currently evaluated by attendance.

## Impact If Built
Sales coaching is a substantial enterprise investment evaluated almost entirely by belief. Separating prediction from prescription tells an organisation which of its signals are early warnings and which are levers, which are different things requiring different responses. The vendor that tests its own recommendations gains the only defensible claim in a category currently competing on dashboard breadth.
