# Invoice Reconciliation Against Tariffs That Change Every Year

**Niche:** [[niches/last-mile-delivery/parcel-audit-contract-negotiation/profile|Parcel Audit & Contract Negotiation Firms]]
**Industry:** [[industries/last-mile-delivery|Last-Mile Delivery]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Auditing a parcel invoice means recomputing the carrier's own rating engine, and the rules change annually and mid-year.
**Tags:** #data-integration #workflow-orchestration #anomaly-detection #automation #compliance

## The Problem
A parcel charge is the output of a rating computation: base rate by zone and weight, dimensional weight if it applies, a stack of accessorials — residential, delivery area, fuel, peak, additional handling, oversize — each with its own applicability rules, then the shipper's contract discounts applied in a specific order with minimums and tiers.

To audit it, the firm must recompute the same thing independently and compare. That means maintaining an accurate model of each carrier's published tariff and each client's contract, across every version in effect during the period being audited. Carriers publish a general rate increase annually, adjust fuel weekly, add surcharges mid-year, and change applicability rules with limited notice.

Getting the model wrong in either direction is expensive: a missed discrepancy is an unrecovered refund, and a false one is a claim that gets denied and costs credibility with the carrier.

## What Already Exists
Invoice audit and reconciliation platforms exist across procurement and telecoms. Rules engines, ETL tooling, and exception workflow are all mature commodity categories.

## The Customization Gap
The generic tools assume a stable rate structure and a stable definition of correct.

**Tariffs are versioned, temporal, and adversarially complex.** The correct charge depends on the tariff version and contract amendment in force on the ship date, and audits run months later. Every rule needs an effective-date dimension and full reconstructability, which no generic rules engine treats as central.

**Contracts arrive as documents.** Client agreements are PDFs with negotiated tiers, minimums, waivers, and bespoke language. Turning them into an executable rate model is a document extraction and formalization problem that must be exactly right, and it is currently done by hand for every new client.

**Discrepancy classification drives everything downstream.** A charge that differs from the model may be a carrier billing error, a contract term the firm modelled wrong, a service failure eligible for refund, or a legitimate charge under a rule nobody had encoded. These have entirely different actions, and distinguishing them is where analyst time goes.

**Refund claim windows are short and per-carrier.** Service failure refunds must be claimed within days. Prioritization has to be driven by expiry and expected value, not by invoice arrival order.

**Model drift must be detectable.** When the firm's rate model diverges from a carrier's actual behaviour — because a rule changed quietly — the symptom is a spike in unexplained discrepancies across many clients at once. Detecting that pattern is the control that prevents thousands of bad claims.

## Target Customer
Chief Technology Officer or VP of Operations at a parcel audit firm, where rate model maintenance is the recurring engineering burden and claim accuracy is the carrier relationship.

## Impact If Solved
Rate model accuracy determines both recovery and credibility, and it is maintained against carriers who change the rules on their own schedule. Versioned, reconstructable rate modelling with automated contract extraction shortens client onboarding from weeks to days and catches quiet rule changes before they become a wave of denied claims.
