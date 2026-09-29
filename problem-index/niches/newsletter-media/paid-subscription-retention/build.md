# Knowing Who Will Pay and Who Will Leave

**Niche:** [[niches/newsletter-media/paid-subscription-retention/profile|Paid Subscription & Retention]]
**Industry:** [[industries/newsletter-media|Newsletter Media]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The publisher has years of reading behaviour per person and asks everybody to subscribe with the same message at the same moment.
**Tags:** #logistic-regression #survival-analysis #gradient-boosting #evaluation-metrics #confidence-intervals #revenue-impact #causal-inference #automation
**Contested on:** Every serious competitor in this niche is fighting to convert free readers to paid and keep them past the first renewal — and whoever knows which reader will pay and which will lapse stops running the paid tier on hope.

## The Problem
A newsletter publisher knows, for every subscriber, exactly which issues they opened, which links they clicked, how long they have been reading, which topics they engage with and how that has changed. That is a far richer behavioural record than most subscription businesses have. It is used to send everyone the same appeal at the same time, to price a single tier chosen by intuition, and to discover churn after the payment fails.

## Why Nobody Has Built This
The paid tier was added to an advertising business rather than designed as one, so it inherited no subscription discipline — a revenue line bolted on to an existing product does not arrive with its own operating model. Behavioural data sits in the sending platform and billing in another. Publishers are small and have no analytics function. And churn is treated as a fact of the category.

## What to Build
Model the two decisions. Predict conversion propensity from reading behaviour, which is the core and lets the appeal go to the readers who are close rather than to everyone equally. Time the ask to behaviour rather than to a calendar, since a reader in a period of high engagement is a different prospect from one drifting away. Test pricing and tier structure properly, as the price was almost certainly set by intuition and has never been examined. Predict churn before the renewal from engagement decay, because a subscriber who stopped reading two months ago is already gone and can sometimes be recovered. Collect cancellation reasons in a structured form, since they are the clearest product feedback available and are currently a free-text box nobody reads. Segment the paid base, as treating a founding subscriber and a three-week trial identically wastes both. Model what the paid product would have to be for the readers who declined, using their behaviour, which is the product question underneath the conversion question. Report contribution per subscriber against acquisition cost, so the tier's economics are known. Support the gift, group and institutional cases, which are underexploited and require little. And measure conversion and retention as operating metrics rather than as a periodic surprise.

## Target Customer
Publisher leadership, subscription platform vendors serving publishers, advertisers whose inventory competes with the paywall, and readers who would have paid and were never asked well.

## Impact If Built
A revenue line bolted on to an existing product does not arrive with its own operating model, so the paid tier inherited no subscription discipline. The reading record is richer than most subscription businesses ever have and it drives none of the decisions.
