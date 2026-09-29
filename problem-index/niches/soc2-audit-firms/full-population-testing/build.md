# Build: The Population, Extracted and Tested

**Niche:** Full-Population Testing
**Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A reusable extraction and rule-evaluation layer that pulls each control's complete population from the client's own systems, tests every item, and states what the extraction covered.
**Tags:** #evaluation-metrics #confidence-intervals #compliance #data-integration #automation #workflow-orchestration #descriptive-statistics
**Contested on:** Whether an auditor examines every item in a control's population, now that the population is sitting in a platform the client already runs.

## The Problem

An associate tests change management. They request a list of changes, receive an export, select a sample, and for each selected change request the approval evidence, receive it, and check it.

Elapsed time: several days, most of it waiting for the client to respond to evidence requests, and a meaningful share of an associate's engagement hours.

The same test as a query: extract every change from the ticketing system with its approval status and approver, evaluate the rule that a change must have an approval from someone other than the requester, and report the exceptions. Minutes, once the connector exists, over the entire population rather than twenty-five items.

The barrier is that nobody has built the connectors. Each engagement's evidence collection is bespoke, so the work of extracting a population is paid for once per engagement and thrown away, which makes it look expensive. Built once as a reusable library across a client base using the same platforms, it is paid for once and amortised over hundreds of engagements.

The second barrier is completeness. A population extracted from a compliance platform covers what the platform sees, and a platform connected to two of three cloud accounts produces a population missing a third of the changes. Testing everything in an incomplete population is not the same as testing everything.

## Why Nobody Has Built This

**Engagement economics are per-engagement.** Fixed-fee work with utilisation targets does not fund a reusable capability whose payback is across the client base rather than within one job.

**More testing finds more exceptions.** A firm that tests everything qualifies more reports, which is professionally correct and commercially uncomfortable in a market where the purchaser wants a clean one.

**The report cannot express the benefit.** Without the reporting change, exhaustive testing produces the same opinion as sampling, so the investment buys nothing the client can see.

**Completeness verification is real work.** Establishing what an extraction actually covers requires reconciling against an independent source, which is the same coverage problem the compliance platforms have not solved for themselves.

**Audit firms are not software organisations.** Building and maintaining a connector library is an engineering function most attestation firms do not have.

**Client data access needs a framework.** Direct system access for extraction is a different arrangement from receiving evidence exports and needs contractual and security groundwork.

## What to Build

**A reusable connector library across the common platforms.** The compliance platforms, cloud providers, identity providers, ticketing systems and code hosts that most clients use. Built once, maintained centrally, used on every engagement.

**Express control tests as rules over populations.** Each control's test written as a rule that evaluates every item — a change must have an independent approval, an access review must have occurred within ninety days with a named reviewer, a departure must have deprovisioning within one business day. This is the methodological artefact and it is reusable across clients.

**Verify the extraction's completeness.** Reconcile the extracted population against an independent count — the cloud provider's own record, the identity system, the ticketing system's totals — and report the coverage. An extraction presented as complete when it covers sixty per cent is the same failure as everything else in this cluster.

**Report exceptions with rates.** Not a pass or fail but the exception count over the population, with the exceptions themselves available for examination. This is a far more informative test result and it requires the full population.

**Escalate automatically.** An exception triggers examination of related items and of the surrounding period, which is a query rather than an expanded sample.

**Test continuously rather than at year end.** With connectors in place, controls can be tested throughout the period rather than in a concentrated fieldwork window, which spreads the work and catches failures while they can still be remediated.

**Handle mixed availability honestly.** Where a population is not extractable, sample it and record that. A test record distinguishing exhaustive from sampled is the foundation for the reporting change.

## Target Customer

Attestation firms with technology investment capacity, for whom a connector library is a durable asset that lowers cost per engagement and is the only defensible efficiency play in a price-competitive market.

Audit technology vendors, for whom a control-testing layer over compliance platform data is an obvious product and does not exist.

Compliance platform vendors, who hold the populations and could offer an auditor-facing extraction and testing interface — and who would gain from their customers' audits being cheaper and faster.

## Impact If Built

Testing moves from a sample to a population for the controls where the data exists, which is most of them for most clients, and the inference becomes far stronger.

Continuous testing throughout the period rather than at year end catches control failures while they can still be remediated, which is better for the client as well as for the audit.

And a reusable connector library makes full-population testing cheaper than sampling after the first engagements, which removes the cost argument that has kept the method in place.
