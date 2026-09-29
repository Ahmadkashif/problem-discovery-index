# Buy: Infrastructure Change Data, Already Public

**Niche:** Indicator Lifecycle & Decay
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Address reassignment, domain re-registration, certificate revocation and sinkhole adoption are all publicly observable, and no feed monitors them to retire its own content.
**Tags:** #change-point-detection #graph-theory #evaluation-metrics #gradient-boosting #data-integration #automation #confidence-intervals
**Contested on:** Whether an indicator is retired when it stops describing reality, or accumulates indefinitely.

## The Problem

The events that invalidate an indicator are, almost without exception, public.

An address is reassigned — visible in routing data, in passive DNS, in reverse lookup changes and in internet-wide scan results showing different services. A domain changes hands — visible in registration records, in nameserver changes and in certificate issuance. A domain is seized or sinkholed — visible in the resolution pointing to a well-known sinkhole operator. A certificate is revoked — visible in the revocation infrastructure. A host stops serving the malicious content — visible in scan data.

The data sources are established, commercially available and widely used for other purposes. Passive DNS, certificate transparency, internet-wide scan data and routing information are all standard inputs for security research.

They are used to discover new infrastructure and almost never to retire old. A vendor's collection pipeline is oriented entirely toward finding, and the same sources that reveal that an address became malicious would reveal that it stopped being so.

## What Already Exists

Passive DNS: historical resolution data from several commercial providers, showing what resolved where and when.

Certificate transparency: the public log of issued certificates, with revocation infrastructure alongside.

Internet-wide scanning: Shodan, Censys and similar, showing what is running on every address over time.

Routing and allocation: BGP data, regional registry allocation records, and the data showing when address space changes hands.

Domain registration: registrar records and their change history, with expiry and re-registration observable.

Sinkhole infrastructure: well-known sinkhole operators whose nameservers and addresses are largely enumerable.

## The Customization Gap

**Collection pipelines are one-directional.** They are built to find and enrich, not to monitor existing content for invalidating change. Adding a retirement watch over the existing corpus is a pipeline addition nobody has made.

**Sinkhole detection is the cheapest available win.** Sinkholed domains are a well-defined, largely enumerable category producing guaranteed false positives, and detecting them is a resolution check against a known list. Some vendors do this; many do not.

**Reallocation detection needs joining several sources.** Establishing that an address has changed hands requires combining routing, allocation, passive DNS and scan data — each individually available and rarely combined for this purpose.

**Re-registration is a strong signal and is unmonitored.** A domain that expired and was re-registered by a different party is almost certainly no longer malicious, and registration change data makes this directly observable.

**The data costs money and the retirement saves none.** Monitoring the corpus against commercial data sources is an ongoing cost with no revenue attached, which is why it loses to collection.

**Nobody publishes retirement metrics.** A vendor retiring diligently has no way to demonstrate it, so there is no competitive return on the investment.

## Target Customer

Vendors with existing pipelines into these data sources, for whom pointing them at the corpus is an incremental addition rather than a new capability.

Threat intelligence platform vendors, who could apply retirement checks across every feed a customer holds and thereby improve all of them at once — a stronger position than any single feed vendor has.

Security operations teams, who could run sinkhole and age checks on their own ingested indicators today and would remove a meaningful share of their false positives.

## Impact If Solved

The data that would retire stale indicators is the same data used to discover them, already flowing into every vendor's pipeline, pointed in one direction only.

Sinkhole detection alone is a resolution check against a known list and removes a category of indicator that produces guaranteed false positives — the single cheapest improvement available in this industry.

And a platform-level retirement layer would improve every feed a customer holds simultaneously, which is a better intervention point than persuading each vendor individually.
