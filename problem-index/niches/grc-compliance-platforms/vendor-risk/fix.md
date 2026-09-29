# Fix: Assessed Once, Then Whatever Happens Happens

**Niche:** Vendor & Third-Party Risk
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A supplier is assessed at onboarding and reassessed a year later, and everything that changes in between — access, ownership, subprocessors, breaches — changes unobserved.
**Tags:** #change-point-detection #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #data-integration
**Contested on:** Whether supplier assessment is scaled to what each supplier actually touches, or applied near-uniformly across hundreds of them.

## The Problem

A supplier is onboarded. They complete a questionnaire, provide a certificate, and are approved for a defined purpose with defined access. The assessment is filed and a renewal is scheduled for twelve months later.

In those twelve months the relationship changes in ways nobody records. The integration's permissions are expanded because a new feature needed them. The supplier is acquired, and their security programme is folded into the acquirer's. They change a subprocessor, moving data to a jurisdiction the original assessment did not contemplate. They suffer a breach and disclose it in a blog post nobody at the customer reads. Their certificate lapses. Their external security posture degrades.

None of this triggers anything. The assessment is a point-in-time artefact and the process treats the intervening year as unchanged. At renewal the supplier completes a questionnaire that asks about current state, and the answer reflects whatever is true then, with no record of what happened in between.

The most common real supply chain failure is not a supplier who was badly assessed at onboarding. It is a supplier whose situation changed afterwards, in a relationship nobody was watching.

## Why It's Still Broken

**Annual is what the process specifies.** Vendor risk frameworks and auditors expect periodic reassessment, and periodic means annual. Continuous monitoring is not what the process was designed around, so it is not what gets resourced.

**The team cannot even keep up with annual.** With hundreds of suppliers and a handful of people, renewal cycles slip routinely. Adding continuous monitoring to a programme already behind on its periodic obligations is not obviously possible.

**Change signals are scattered.** Permission expansion is in the identity system, acquisitions are in the news, subprocessor changes are in a page on the supplier's website, breaches are in a disclosure nobody subscribes to. No single system sees them.

**Suppliers are not obliged to tell you much.** Contracts often require notification of material change and define it loosely, and enforcement is rare. Suppliers with many customers do not proactively inform each one of every change.

**Access expansion happens inside the customer.** A supplier's permissions growing is the customer's own doing — an engineer granted a broader scope to make something work. Vendor risk is rarely in that loop and the identity data that would show it is not connected to the vendor programme.

**Nothing bad has happened yet, visibly.** Until a supplier-related incident traces to a change that occurred after assessment, there is no internal case for changing the cadence.

## What a Fix Looks Like

**Watch permissions, not questionnaires.** Monitor the access each supplier integration actually holds, from the identity provider and cloud platforms, and alert on expansion. This is the highest-value continuous signal, it comes from the customer's own systems, and it requires no supplier cooperation at all.

**Subscribe to the cheap external signals.** Certificate expiry, breach disclosures, acquisition news, subprocessor page changes and external posture scores for the critical tier. Each is individually easy to monitor and collectively they cover most of what changes.

**Watch the subprocessor page.** Most suppliers publish their subprocessors and commit to notifying changes. Almost nobody monitors the page, and a change there is often the earliest signal of a material shift in where data goes.

**Trigger reassessment on events, not only on dates.** An acquisition, a breach, a scope expansion or a certificate lapse should trigger review regardless of where the annual cycle sits.

**Concentrate it on the tier that matters.** Continuous monitoring of eight hundred suppliers is not feasible and is not necessary. For the twenty with real access it is entirely feasible, and that is where the exposure is.

**Put change notification in the contract and actually check it.** Most contracts already require notification of material change. Almost nobody tracks whether suppliers comply, which means the clause does nothing.

## Who Feels the Pain

The organisation, whose supply chain exposure is a year out of date at any given moment, in a relationship that changes continuously.

The vendor risk team, running behind on annual renewals while knowing the annual cadence is the wrong one, with no capacity to argue for a different model.

The security team, who discover during an incident that a supplier's access had expanded substantially since the assessment on file.

And the customers downstream, who are told their vendor's supply chain is assessed, which it was, once.

## Impact If Fixed

Monitoring supplier permission expansion from the organisation's own identity data is the single highest-value change here: it needs no supplier cooperation, catches the most common real drift, and uses data the organisation already has.

Event-triggered reassessment converts a calendar-driven process into a risk-driven one at little cost, since the triggering signals are mostly cheap to watch.

And concentrating continuous monitoring on the small critical tier makes the whole thing feasible — the reason nobody does it is an implicit assumption that it would have to apply to every supplier, and it does not.
