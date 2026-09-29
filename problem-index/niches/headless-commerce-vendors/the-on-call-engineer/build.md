# Owning an Incident You Cannot See Into

**Niche:** [[niches/headless-commerce-vendors/the-on-call-engineer/profile|The On-Call Engineer]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An on-call engineer owns an incident spanning six vendors' systems on the highest-revenue day of the year, with visibility into their own integration code and nothing else.
**Tags:** #worker-facing #graph-theory #change-point-detection #evaluation-metrics #automation #confidence-intervals #data-integration #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to let the person holding the pager see across the vendors whose systems they are responsible for — and whoever does that shortens the incidents, because the engineer currently owns an outcome and can see one component of it.

## The Problem
Checkout error rates rise at nine in the evening on the busiest trading day of the year. The engineer sees failures in their own integration layer with a generic upstream error. They check six status pages, all green. They open support tickets with four vendors, three of which promise a response within a business day. They call an account manager. Ninety minutes into a revenue-critical incident they establish that the tax service is rate-limiting them because the retry storm from an unrelated timeout tripled their call volume. Every minute of that ninety was spent obtaining information that the architecture could have provided.

## Why Nobody Has Built This
Cross-vendor visibility requires every vendor to participate in tracing, which none is obliged to do and several do not support. Status pages are marketing surfaces reporting aggregate service health rather than a customer's experience. Incident response commitments are not in most contracts because nobody negotiated them. And the on-call engineer, who understands all of this precisely, is not in the procurement conversation.

## What to Build
Give the engineer the view and the standing. Instrument every vendor call from the retailer's side with tracing, latency, error and retry data, which the retailer controls entirely and which gives an attributable view of every boundary without any vendor's cooperation — this is the fix's foundation and it is available today. Build a dependency health view showing each vendor's behaviour as the retailer experiences it, rather than as the vendor reports it. Detect which boundary is failing automatically and present it at page time, so the incident starts with an attribution rather than with a search. Include the retry and backoff behaviour in the view, since retry storms are a recurring cause and are caused by the retailer's own integration code reacting to somebody else's slowness. Provide a runbook per vendor with the escalation path, the contractual response commitment and the person to call, which is a document that takes an afternoon and is missing everywhere. Negotiate incident response commitments and peak-period cover into the contracts, since an outage window on the busiest day of the year is a commercial term rather than a technical problem. Establish a single incident channel with all parties pre-arranged before peak, rather than assembling it during one. And report time-to-attribution as the metric, because that is where the ninety minutes goes.

## Target Customer
Retail engineering organisations, the on-call engineers, procurement functions negotiating the contracts, and the vendors whose incident behaviour is currently unmeasured.

## Impact If Built
Retailer-side instrumentation of every vendor call gives an attributable view of every boundary without any vendor's cooperation, and it is available today. A per-vendor runbook with the escalation path and contractual commitment takes an afternoon and is missing everywhere.
