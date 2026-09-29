# Build: Tiered by What They Actually Touch

**Niche:** Vendor & Third-Party Risk
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Derive each supplier's actual data access and system reach from the organisation's own systems, tier the assessment programme accordingly, and monitor the top tier continuously.
**Tags:** #graph-theory #gradient-boosting #evaluation-metrics #confidence-intervals #change-point-detection #compliance #automation #data-integration
**Contested on:** Whether supplier assessment is scaled to what each supplier actually touches, or applied near-uniformly across hundreds of them.

## The Problem

A vendor risk team of four covers eight hundred suppliers. The arithmetic permits about two hours each per year, which buys a questionnaire sent, a response filed and a certificate collected. Everything is assessed and nothing is assessed properly.

The distribution of actual risk across those eight hundred is extremely skewed. A small number have persistent access to production systems or customer data. A somewhat larger number process data in a bounded way. The majority touch nothing sensitive at all. A well-allocated programme would spend most of its effort on the first group and almost none on the last, and would be dramatically more effective with the same headcount.

The reason it does not is that the tiering input is missing. Asking a supplier what data they access produces their own characterisation. Asking the internal owner produces a guess. So tiering is done from contract value or from a self-reported category, neither of which correlates well with actual access.

The information exists inside the organisation. Identity systems know which external identities exist and what they can reach. Cloud logs show which third-party integrations call which APIs. Data platforms record which external destinations receive data. Expense and procurement systems reveal suppliers nobody registered. The organisation can observe what its suppliers actually touch and instead asks them.

## Why Nobody Has Built This

**Vendor risk platforms sit outside the organisation's systems.** They manage questionnaires and documents. Deriving access from identity, cloud and data systems means integrating deeply into the customer's estate, which is a different product with a different sales motion.

**Access data is fragmented.** Identity providers, cloud platforms, data pipelines, SaaS integrations and API gateways each hold part of it, with no common notion of which supplier an external identity belongs to. Resolving identities to vendors is the substantive work.

**Coverage of the supplier list is the measured objective.** Programmes are assessed on whether every supplier was assessed, which penalises concentration. A programme that did four suppliers thoroughly and two hundred not at all would fail its own audit, however much better the risk outcome.

**Tiering down is a liability position.** Deciding a supplier warrants light assessment is a judgement that will be examined if that supplier causes an incident. Uniform treatment is defensible in a way that deliberate prioritisation is not.

**Shadow suppliers are the largest gap and nobody wants to open it.** Discovering the hundreds of unregistered tools teams have adopted expands the programme's scope enormously, which is the correct finding and an unwelcome one.

## What to Build

**Derive access from internal systems.** External identities and their permissions from the identity provider; third-party integrations and their API scopes from cloud platforms; data flows to external destinations from the data platform; OAuth grants across SaaS applications. Resolve these to suppliers, and produce an observed access profile per vendor.

**Tier on observed access, not self-report.** Persistent production access, bounded data processing, no sensitive access — derived and evidenced. This is the input the whole programme needs and currently does not have.

**Find the unregistered suppliers.** Expense data, OAuth grants, DNS and egress traffic, and SaaS discovery tooling reveal the tools in use that no procurement record covers. Shadow suppliers are frequently a large fraction of the real population and are entirely absent from the programme.

**Monitor the top tier continuously.** For the small number that matter, watch for change: expanded permissions, new subprocessors, acquisition, breach disclosure, certificate lapse, external posture degradation. Annual assessment is the wrong cadence for the suppliers where cadence matters.

**Assess proportionately and say so.** Deep assessment for tier one, standard for tier two, registration and monitoring only for tier three — with the tiering rationale documented and evidenced, which is what makes the deliberate prioritisation defensible rather than negligent.

**Track access drift.** A supplier onboarded for a narrow purpose whose permissions have expanded is a risk the annual cycle will not catch, and the identity data shows it immediately.

**Map fourth parties where possible.** Which subprocessors the critical suppliers depend on, from their own disclosures and from observable infrastructure. Concentration on a shared upstream provider is a real exposure that almost no programme models.

## Target Customer

Vendor risk and security leadership at organisations with several hundred suppliers and a small team, which is the great majority of them — the pitch is better risk reduction from the same headcount rather than more coverage.

The compliance platforms, for whom this extends an existing integration footprint into a large adjacent market they already partially serve.

Cloud security posture vendors are natural adapters, already holding much of the access data and currently using it for internal risk only.

## Impact If Built

Effort concentrates where the exposure is. A programme that assesses four hundred low-risk suppliers annually and monitors none of the critical ones continuously has its resources exactly backwards, and the fix is an allocation change rather than a headcount one.

Shadow supplier discovery would reveal the part of the supply chain the programme does not know exists, which is consistently where the uncontrolled data access lives.

And tiering on observed rather than self-reported access replaces the weakest input in the whole programme with an evidenced one derived from systems the organisation already runs.
