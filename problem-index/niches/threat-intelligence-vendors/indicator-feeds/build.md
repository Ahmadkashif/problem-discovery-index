# Build: Shipping Less, Selected Better

**Niche:** Indicator Feeds
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A feed that selects for each customer — by stack, sector, exposure and observed match behaviour — and states what each indicator is for, instead of shipping everything collected.
**Tags:** #gradient-boosting #k-means-clustering #evaluation-metrics #confidence-intervals #bayesian-inference #graph-theory #automation #data-integration
**Contested on:** Whether a feed delivers what a particular customer should act on, or everything the vendor collected with the filtering left to the buyer.

## The Problem

A customer receives several million indicators. Their environment is a specific technology stack in a specific sector in a specific geography, exposed to a specific set of adversaries. The overwhelming majority of the feed is irrelevant to them — infrastructure associated with malware families targeting platforms they do not run, campaigns aimed at sectors they are not in, and regions where they have no presence.

The filtering is left to them. They receive sector tags, which are coarse enough to be nearly useless — financial services covers a global bank and a payments startup with nothing in common.

So a security team that is already the binding constraint spends its capacity deciding what to ignore, and the usual resolution is to ingest everything into the matching engine and let the alert queue absorb the consequence. Which it does, as described in [[niches/threat-intelligence-vendors/the-soc-analyst/profile|🟣 The SOC Analyst Receiving the Alerts]].

The vendor is better placed to do this selection than the customer. They know which adversaries target which sectors and which malware families run on which platforms. They see, across their installed base, which indicators actually match at organisations of which shape. And they ship everything anyway, because volume is what procurement compares and selection would mean sending less.

## Why Nobody Has Built This

**Selling less is commercially counterintuitive.** A vendor offering a smaller feed is offering a worse-looking product in a comparison built on indicator counts.

**Selection requires knowing the customer's environment.** Tailoring by stack means the vendor knows what the customer runs, which requires either disclosure or telemetry access, and many customers are reluctant.

**Wrong selection is a serious failure.** Withholding an indicator that would have mattered is worse than sending noise, and that asymmetry pushes every vendor toward shipping everything.

**Demonstrating selection quality needs the measurement.** A vendor claiming better selection has no way to prove it without the match rate and precision data the category does not publish.

**Sector tagging looks like it solves the problem.** Coarse tags create the impression that relevance is addressed, which reduces pressure to do it properly.

**Customers ask for completeness.** Buyers, aware they might miss something, ask for everything, which vendors reasonably supply.

## What to Build

**Model relevance from the customer's actual environment.** Technology stack, exposed services, geography, sector, supply chain and — where telemetry access exists — the traffic they actually see. Score each indicator's relevance to that profile rather than assigning it a sector bucket.

**Learn from observed match behaviour across the base.** Which indicators match at organisations resembling this customer is a strong predictor, computable from the installed base, and is the best available relevance signal.

**State what each indicator is for.** Block, alert, hunt or context. These require completely different precision — an indicator good enough to hunt on is not good enough to block on — and shipping them undifferentiated forces the customer to make a judgement they lack the information to make. This is the cheapest and most useful change available.

**Ship tiers, and let the customer choose their own risk posture.** A small high-confidence set suitable for blocking, a broader alerting set, and a wide context set for hunting and enrichment. Customers can then take the completeness they want at the tier where it belongs.

**Report what was withheld and why.** Selection is only acceptable if it is transparent. A customer should be able to see what was filtered out and on what basis, and to override it. This addresses the missed-indicator fear directly.

**Deliver uniqueness information.** Which indicators in this feed are not in the customer's other subscriptions. This helps the customer and is a genuine differentiator for a vendor confident in their unique collection.

**Prove the selection with the measurement.** Match rate and precision for the selected set against the full set is what turns a claim into evidence, which is why this build depends on [[niches/threat-intelligence-vendors/feed-quality/profile|🔵 Feed Quality Measurement]] existing.

## Target Customer

Security operations leadership at mid-sized organisations, who feel the filtering burden most acutely because they have the same feed volume as a large enterprise and a fraction of the analysts.

Vendors with telemetry across an installed base, who can compute relevance from observed match behaviour and for whom selection is a defensible differentiator.

Detection engineering teams, who would immediately use an indicator's stated purpose because block-versus-hunt is exactly the decision they make manually today.

## Impact If Built

The filtering work moves to the party best placed to do it, which is the vendor with the cross-customer view rather than the customer with three analysts.

Stating what each indicator is for costs a field and would immediately let customers route indicators to blocking, alerting or hunting appropriately — a distinction they currently make by guessing.

And tiered delivery would let a buyer take a small high-precision set for enforcement and a broad set for context, which is what they actually want and what no feed structure currently offers.
