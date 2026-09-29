# Lineage: Threat Intelligence Vendors

**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**The tool:** STIX — Structured Threat Information eXpression, the language for describing an indicator, the observable it matches and the campaign or actor behind it so that a machine can ingest it, carried between organisations by its companion transport, TAXII
**Builder:** MITRE
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Threat intelligence used to arrive as prose.

An analyst at one organisation saw an attack, wrote down the IP addresses, domains and file hashes involved, and sent them to peers. The STIX whitepaper describes the state of the art bluntly: most indicator sharing was "human-to-human exchanges of unstructured or semi-structured descriptions of potential indicators, conducted via web-based portals or encrypted email."

That had a specific cost. **Every indicator had to be read by a person and re-keyed into a detection tool, by every recipient.** And because each sender used its own layout, there was no way to carry the context that says what an indicator *means* — which campaign, which technique, what to do about it — in a form a machine could act on.

## What Got Built

STIX: a structured language, first expressed as XML Schema, for cyber threat information. Version 1.1 of the whitepaper names eight core constructs — **Observable, Indicator, Incident, TTP, ExploitTarget, CourseOfAction, Campaign and ThreatActor** — with observables themselves expressed in a sister language, CybOX.

The design choice that matters is the split between an *observable* (this domain was seen) and an *indicator* (this pattern of observables means this threat). It let one document carry both the raw fact and the analyst's claim about it, linked to the actor and campaign and to a recommended course of action.

TAXII, the Trusted Automated eXchange of Indicator Information, was the transport: the whitepaper calls it the DHS implementation for automated exchange of STIX content.

STIX 1.x ran through versions 1.0 to 1.2. Under OASIS the language was rebuilt for version 2.0 as JSON — the committee maintains a tool to convert STIX 1.2 XML to STIX 2.0 JSON — and STIX 2.1 became an OASIS Standard on 10 June 2021.

## Who Built It, And Why Them

MITRE wrote it; the US government paid for it; the problem was the government's first.

The whitepaper traces STIX to the IDXWG email list, "established by members of US-CERT and CERT.org in 2010 to discuss automated data exchange for cyber incidents." Its author, Sean Barnum, published it under MITRE copyright with the Department of Homeland Security as sponsor.

**That is why it was MITRE and not a vendor.** A sharing format is worthless if owned by one seller, because every competitor must adopt it. DHS needed critical-infrastructure operators, government agencies and vendors to exchange indicators with each other, and a federally funded non-profit could write a neutral schema that no vendor would refuse on commercial grounds. MITRE had done it before: it has run CVE, the public vulnerability identifier, since September 1999, through the DHS-funded research centre HS-SEDI — the same body the whitepaper names as STIX's community moderator.

In July 2015 DHS transitioned STIX, TAXII and CybOX to the OASIS Cyber Threat Intelligence Technical Committee. The committee's charter describes them as "developed and contributed to the TC by U.S. Department of Homeland Security." MITRE staff still chair and edit: the 2.1 standard lists Richard Struse of MITRE as co-chair and Rich Piazza of MITRE as an editor.

## What It Cost

**STIX made indicators cheap to move, not cheap to judge.** Once a feed could be ingested automatically, nothing slowed an indicator between a vendor's collection and a customer's detection rule.

In STIX 2.1 an Indicator's `valid_from` is required; `valid_until` is optional, and "if the valid_until property is omitted, then there is no constraint on the latest time for which the Indicator is valid." The format can express decay. It does not demand it. An address flagged two years ago arrives looking exactly as current as one flagged this morning.

## What You Still Touch

A SOC analyst's alert that says "matched threat feed" is a STIX indicator crossing a TAXII collection into a SIEM rule, usually with no expiry.

- [[problems/threat-intelligence-vendors/low-impact-2|🟡 Indicator Decay and Feed Precision]] — the optional `valid_until`, in production
- [[problems/threat-intelligence-vendors/worker-life-2|🟢 The Defender Whose Alert Queue Is Someone Else's Feed]]
- [[niches/threat-intelligence-vendors/indicator-lifecycle/profile|Indicator Lifecycle & Decay]]
- [[niches/threat-intelligence-vendors/precision-verification/profile|Precision Verification]]
- [[niches/threat-intelligence-vendors/enrichment-and-integration/profile|Enrichment & Integration]]

**Sources:** WebSearch was unavailable this session (session cap reached); research was by direct fetch. Sean Barnum, *Standardizing Cyber Threat Intelligence Information with the Structured Threat Information eXpression (STIX)*, v1.1 rev 1, 20 Feb 2014, MITRE, at stixproject.github.io (IDXWG origin, 2010, US-CERT/CERT.org, DHS sponsor, HS-SEDI moderator, eight constructs, CybOX, TAXII, the human-to-human quotation); stixproject.github.io/about (MITRE copyright; versions 1.0–1.2; now maintained by OASIS CTI TC); OASIS CTI TC home page and charter (July 2015 transition headlines; "developed and contributed… by U.S. Department of Homeland Security"; Call for Participation May 2015); *STIX Version 2.1*, OASIS Standard, 10 June 2021 (chairs and editors; `valid_from`/`valid_until` text; Confidence Scales appendix); OASIS cti-documentation (STIX 1.2 XML → 2.0 JSON elevator). ⚠️ **Not established:** the release date of STIX 1.0 — not stated on any page fetched. CVE date and HS-SEDI role from Wikipedia, *Common Vulnerabilities and Exposures*. Keyed `MITRE` as designer and copyright holder; `US Department of Homeland Security` as sponsor and contributor to OASIS has an arguable claim to the key.
