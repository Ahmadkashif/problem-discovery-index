# Fix: The Customer Has the Telemetry and Never Looks

**Niche:** Match Rate Measurement
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Every organisation could compute which of its threat intelligence subscriptions ever matched anything, from logs it already keeps, and almost none do.
**Tags:** #evaluation-metrics #confidence-intervals #descriptive-statistics #revenue-impact #worker-facing #data-integration
**Contested on:** Whether anyone will publish how often a feed's indicators actually fire against real telemetry.

## The Problem

An organisation subscribes to four threat intelligence feeds. At renewal, the security leader must decide which to keep.

They have the data to decide. The SIEM holds every alert with its source. The matching logs record every indicator hit. The case management system records what each alert turned out to be. Answering which feed produced matches, how many, and how they were resolved is a set of queries against systems the organisation already runs.

Nobody runs them. The renewal decision is made on whether the team found the vendor's reporting useful, whether the account manager was responsive, and whether the budget allows all four. The analytical question — did this feed ever fire in our environment — is not asked.

The reason is straightforward. Feed evaluation is nobody's objective. The security operations team is measured on incident response, the intelligence function on producing assessments, and the procurement team on price. The analysis would take an analyst a week and there is no week available for something nobody has asked for.

So organisations renew subscriptions worth substantial money on the basis of a feeling, with the evidence sitting in their own logs.

## Why It's Still Broken

**No owner.** Feed evaluation sits between security operations, the intelligence function and procurement, and belongs to none of them.

**The tooling does not report it.** Platforms show alerts and not feed performance, so the analysis requires custom queries rather than opening a dashboard.

**Provenance is lost.** Deduplication across feeds means an alert often cannot be attributed to the feed that supplied the indicator, which blocks the analysis before it starts.

**Vendors do not offer it.** A vendor could supply a per-customer match rate report and none does, because the honest version may not support the renewal.

**A low match rate has an available excuse.** A feed that never matched can be argued to have provided context and upstream prevention, which makes the finding contestable and therefore easier to not produce.

**Nobody is rewarded for cutting a subscription.** The analyst who demonstrates that a feed is inert has created work and made an enemy of an account manager, and saved money that appears in someone else's budget.

## What a Fix Looks Like

**Run the analysis once, before the next renewal.** Which feeds produced alerts, how many, what proportion of each feed's indicators ever matched, and how the resulting alerts were resolved. A week of an analyst's time, informing a decision worth far more than that, using data already held.

**Fix provenance first.** Configure the threat intelligence platform to retain which feeds supplied each indicator, even after deduplication. Without this the analysis is impossible, and it is a configuration change.

**Ask the vendor for a per-customer report.** Request the match rate for your own environment as a condition of renewal. Vendors who can produce it will, and the ones who cannot have told you something.

**Measure overlap before adding a fifth.** How much of a candidate feed is already covered by existing subscriptions. This is a set comparison and it routinely reveals substantial duplication.

**Replay history to evaluate a candidate.** Rather than a short live trial against a low base rate, match a candidate feed against retained telemetry from the last year. This produces a real match rate in days and is technically simple.

**Give someone the objective.** Feed evaluation as a named responsibility with an annual deliverable, so the analysis happens as a matter of routine rather than as an initiative someone has to champion.

## Who Feels the Pain

The security leader, renewing four subscriptions on impression with the evidence in their own logs.

The SOC analyst, working alerts from feeds nobody has evaluated, several of which may be producing nothing but noise.

The budget, which funds duplicated and inert content year after year because nothing ever tests it.

And the vendors with genuinely good feeds, who cannot be distinguished from the others by a customer who has never measured.

## Impact If Fixed

A week of analysis informs a renewal decision worth far more, using data the organisation already has — which makes this one of the clearest cost-benefit cases in security operations.

Retaining feed provenance is a configuration change that unlocks the entire analysis and is the specific technical reason most organisations cannot do it today.

And replaying historical telemetry against a candidate feed would replace the short trial — which cannot distinguish anything against a low base rate — with an evaluation that actually measures something.
