# Evidence Collection & Continuous Monitoring

**Parent Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Category:** High Market Share
**Contested on:** Whether continuous monitoring reports the state of the estate or the state of the integrations, and whether anyone can tell the difference.

## Profile

**Market Size:** ~$2.34B
**Share of Parent Industry:** ~26%
**Digital Adoption:** High — this is the product
**Target Buyer:** Compliance and security leadership, engineering leadership
**Automation Potential:** Very high — and largely realised

## What Makes This a Distinct Niche

This is the product the category is built on: connect to cloud providers, identity systems, device managers, ticketing and code hosts; collect evidence continuously; map it to framework controls; produce audit-ready artefacts. It works, it removed an enormous amount of screenshotting, and it is the reason the automated-certification tier exists at all.

The contest is over reliability of the signal. Continuous monitoring reports that a control is passing until an integration silently stops returning data — and then it reports that too, because a check that cannot run and a check that passed look identical unless the product was built to distinguish them. The failure mode of a monitoring system is that it stops monitoring and says nothing, and this category has that failure mode in abundance.

Every serious competitor is fighting over integration breadth, which is the visible axis, and the differentiating one is whether the evidence means what the dashboard says. A platform that could demonstrate its monitoring is actually monitoring — coverage stated, staleness surfaced, verification depth disclosed — would be selling something materially different from a longer integration list.

## Current Tools & Gaps

Integration libraries spanning cloud providers, identity, device management, ticketing, code hosting and HR systems. Continuous evidence collection with control mapping and audit artefact generation. Alerting on control failure. Evidence retention for the audit period. Manual evidence upload for what integrations cannot reach.

The gaps concentrate at the edges of what the integrations see. Staleness is under-surfaced, so a broken connector can leave controls green for weeks. Estate coverage is not reported, so a platform connected to one of three cloud accounts shows a readiness percentage over a third of the company. Manual evidence — the portion requiring a human to upload something — is the part that actually fails before audits and is the least supported. Control mapping logic is proprietary and unexplained, so nobody can see why a piece of evidence was accepted for a control. And nothing reconciles what the framework asked for against what the integration actually verified.

## Problems

- [[niches/grc-compliance-platforms/evidence-collection/build|🔨 Build: Monitoring That Knows When It Stopped]]
- [[niches/grc-compliance-platforms/evidence-collection/buy|🛒 Buy: Observability Discipline for the Compliance Pipeline]]
- [[niches/grc-compliance-platforms/evidence-collection/fix|🔧 Fix: The Connector Broke and the Dashboard Stayed Green]]
