# Screening Rules as Executable Content Per Jurisdiction

**Niche:** [[niches/proptech-platforms/screening-compliance-content/profile|Screening Compliance Content]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** What a landlord may lawfully consider now varies by city, the platform knows every property's address, and the criteria are still a configuration screen filled in by a regional manager with a national default in front of them.
**Tags:** #large-language-models #bert #transformers #evaluation-metrics #confidence-intervals #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor in tenant screening is fighting to apply the criteria that are lawful in this specific city, for this specific property, at the moment of application — and whoever keeps that rule set correct takes the account.

## The Problem
A property in a city with a fair chance ordinance applies a blanket criminal history exclusion because that is what the criteria template said and nobody changed it. A property in a source-of-income jurisdiction has an income multiple criterion applied to voucher holders in a way the ordinance prohibits. A third charges an application fee above a local cap. Each is applied automatically to every applicant, consistently, hundreds of times — which makes each one a documented pattern rather than an isolated error, and patterns are what enforcement actions are built from. Nobody in the operator's organisation is aware.

## Why Nobody Has Built This
Screening providers supply data and have structured their business to leave the decision criteria with the operator, which is a considered legal position and also means nobody owns the correctness of the criteria. The content itself is genuinely hard to maintain — local ordinances are published inconsistently, amended frequently, and interact with state law in ways that require interpretation rather than extraction. And a vendor that asserts what is lawful takes on a role its counsel will resist, which is the same dynamic that keeps small landlord tools shipping templates and disclaimers.

## What to Build
Jurisdiction-scoped screening rules as maintained, versioned, executable content. Each property resolves to its jurisdiction stack — state, county, municipality — and the applicable constraints are composed: which record types may be considered and over what lookback, whether individualised assessment is required and what it must consist of, whether income criteria may be applied to subsidised rent portions, fee caps, sequencing requirements, and adverse action content and timing. Configured criteria are validated against that stack continuously, not only at setup, so a property becomes non-compliant the day an ordinance takes effect and is told. Where a rule requires judgement, the product routes to a human with the provision cited rather than deciding. Every applied decision is logged with the rule version that governed it, which is the evidentiary record an operator needs and currently cannot produce.

## Target Customer
Screening providers, platform vendors, large operators with multi-jurisdiction portfolios, and — with a different framing — housing agencies and legal aid organisations who monitor screening practice.

## Impact If Built
The exposure this addresses is asymmetric: a misconfigured criterion is applied uniformly and therefore creates the pattern that enforcement looks for. It also matters to applicants, who are denied housing by criteria that are unlawful where they are being applied and who will almost never know. Jurisdiction-correct screening is the rare capability where the operator's legal interest and the applicant's interest point the same way.
