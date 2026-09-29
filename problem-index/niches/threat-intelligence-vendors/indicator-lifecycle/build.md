# Build: Modelled Decay and Automatic Retirement

**Niche:** Indicator Lifecycle & Decay
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A decay model per indicator type and context, driven by observed infrastructure change, that retires content automatically rather than waiting for someone to notice.
**Tags:** #survival-analysis #change-point-detection #gradient-boosting #evaluation-metrics #confidence-intervals #time-series-forecasting #automation #data-integration
**Contested on:** Whether an indicator is retired when it stops describing reality, or accumulates indefinitely.

## The Problem

Indicators decay at wildly different rates and are treated as though they do not decay at all.

A file hash remains valid permanently — that file is that file. A domain registered by an actor may remain theirs for years or be seized next week. An address on a dedicated host may be theirs for months; an address on a cloud provider may be reassigned in hours. A URL path may stop resolving immediately. A certificate has an expiry date printed on it.

Feeds ship all of these with a first-seen date and no expiry, and retirement happens when an analyst notices a problem. So the feed accumulates, and the proportion of it describing infrastructure that has moved on grows continuously.

The customer absorbs this as false positives. A cloud address flagged four months ago now serves a supplier's application, and the analyst investigating the match cannot tell from the alert that the indicator is four months old and sits on a provider that reassigns addresses daily.

The information to model this is available. Vendors see, across their customer base, when indicators stop matching and when they start matching high-volume ordinary traffic. Public data shows when addresses are reassigned, when domains change registrant, when certificates are revoked and which domains are sinkholed. None of it is used.

## Why Nobody Has Built This

**Removal requires a decision, retention does not.** The default is accumulation, and nobody is accountable for a feed containing stale content.

**Volume is what procurement compares.** Retiring aggressively shrinks the indicator count, which is the number in the comparison table.

**Retiring something that was still valid is visible.** An indicator removed and later implicated in an incident is a specific, attributable error. Leaving stale content produces diffuse false positives nobody attributes to anyone.

**Decay rates are genuinely context-dependent.** How fast an address decays depends on the hosting type, the actor's tradecraft and the campaign. A single expiry rule would be wrong in both directions, and doing it properly is a modelling problem.

**Vendors have historically valued their archive.** The historical corpus has real research value, which is an argument for retaining it internally and not for shipping it as current.

**Customers can filter by age and mostly do not.** The capability exists downstream, requires configuration, and is rarely used, which leaves the problem with the party least equipped to solve it.

## What to Build

**Model decay per indicator type and context.** Survival modelling on the vendor's own observation data: how long indicators of this type, on this infrastructure type, from this collection source, continue to match meaningfully. This is a well-posed problem on data already held.

**Use observed match behaviour as the decay signal.** An indicator that stops matching anywhere, or that starts matching high-volume traffic at many organisations, has almost certainly gone stale. Vendors with telemetry can see this directly and it is the strongest available signal.

**Detect reallocation and re-registration from public data.** Address reassignment, domain registrant change, certificate revocation and sinkhole adoption are all observable. Each is a hard retirement signal and none is systematically monitored.

**Ship a confidence that declines with age.** Rather than a binary retirement, a decaying score reflecting the modelled probability that the indicator still describes actor-controlled infrastructure. This lets a customer set their own threshold and is a better structure than a cliff.

**Retire automatically with an audit trail.** Indicators removed when the model crosses a threshold, with the reason recorded and the content retained internally for research. Retirement should be a default behaviour, not a decision someone must make.

**Publish the feed's age distribution.** A customer should be able to see the age profile of what they receive. Vendors that retire properly would benefit from the comparison, which is what would make retirement a competitive attribute.

**Treat hashes differently and say so.** Hashes do not decay the way network indicators do. Applying a single lifecycle policy across types is a category error that shows up as either premature hash retirement or indefinite address retention.

## Target Customer

Vendors with telemetry, who can observe decay directly and for whom a modelled lifecycle is a quality claim supported by evidence.

Threat intelligence platform vendors, who sit across multiple feeds and could apply decay modelling as a layer above all of them — arguably a better position, since it improves every feed the customer holds.

Security operations leadership as the beneficiary, since stale indicators are the largest single contributor to the false positive load their analysts carry.

## Impact If Built

The largest driver of false positives in this industry is addressable with modelling on data vendors already hold, which makes it an unusually tractable improvement.

Detecting reallocation and sinkholing from public data would retire the specific indicators that most reliably produce harmful false positives — including the ones that cause legitimate services to be blocked.

And a declining confidence score is a better structure than a binary expiry, because it lets a customer blocking on high confidence and hunting on low confidence use the same feed appropriately.
