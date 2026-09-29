# Buy: Attack Surface Management Pointed at the Quote

**Niche:** Engagement Scoping & Estimation
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Attack surface management continuously discovers what an organisation actually exposes, is sold to defenders, and is exactly what a testing firm needs before it writes a quote.
**Tags:** #graph-theory #gradient-boosting #evaluation-metrics #confidence-intervals #data-integration #automation #workflow-orchestration
**Contested on:** Whether an engagement's size is set by what the attack surface actually contains, or by an asset list the client compiled by asking around.

## The Problem

Discovering what an organisation exposes to the internet — domains, subdomains, hosts, services, applications, cloud assets, third-party dependencies, shadow IT — is a mature commercial capability. Attack surface management platforms do it continuously, at scale, from outside the perimeter, and they routinely find substantially more than their customers' own inventories contain. That gap is their entire value proposition and it is well evidenced.

Testing firms scope engagements from a questionnaire the client fills in from memory. They have the same problem ASM solves, at the exact moment when solving it would matter most, and they do not use the tooling — because ASM is sold as a security product to a defender, on a subscription, for their own estate, and nobody has packaged it as a scoping instrument for a firm assessing many estates.

The capability and the need are one repackaging apart.

## What Already Exists

Attack surface management: Randori, Censys, Bishop Fox Cosmos, Detectify, Palo Alto's Cortex Xpanse, Microsoft Defender EASM, Group-IB and the ASM modules inside the larger security platforms. Continuous external discovery with asset attribution, service fingerprinting and change detection.

Reconnaissance data sources: certificate transparency logs, passive DNS, internet-wide scan data from Shodan and Censys, and the open-source reconnaissance toolchain — Amass, subfinder, httpx — which most testers already use manually during the first days of an engagement.

Cloud posture: Wiz, Orca and the CSPM category, enumerating cloud assets comprehensively where access is granted.

API discovery: Salt, Noname and Traceable, enumerating live endpoints from traffic, which is a far better application scoping input than a specification document.

Proposal and estimation: the professional services quoting tools firms use for the document, with no connection to any of the above.

## The Customization Gap

**Tenancy, again.** ASM products are subscriptions for an organisation monitoring itself. A testing firm needs many prospect and client estates, each scoped and time-boxed, some pre-contract, under one firm account — a completely different commercial and access model that no ASM vendor offers.

**Pre-contract use needs a consent framework.** Running discovery on a prospect before an agreement exists is the sensitive part. ASM vendors have never had to design for it because their customer is always the asset owner. A packaged consent and authorisation flow is as much of the product as the technology.

**Output is a monitoring dashboard, not a scope.** ASM presents a continuously updated asset inventory with risk signals. Scoping needs a bounded snapshot, structured as testable units with complexity attributes, exported into a proposal. Different artefact entirely.

**No effort model anywhere.** Discovery tells you what exists. Nothing in the category estimates how long testing it would take, which is the actual question a scoper has to answer, and which requires the firm's own historical data rather than anything a vendor holds.

**Reconciliation against a declared list is not a feature.** The valuable scoping output is the difference between what the client says they have and what discovery finds. ASM products compare against an internal CMDB for their own customer; comparing against a prospect's questionnaire answers is a small feature with a large commercial effect.

**Internal and authenticated surface stays invisible.** External discovery covers one part of most estates. The scoping model has to combine it with declared internal counts and state the uncertainty, rather than implying the external view is the whole picture.

## Target Customer

Randori and Bishop Fox are the most natural adapters, both having testing heritage and an existing relationship with the offensive security world — a scoping edition sold to firms extends their reach into every engagement those firms quote.

The open-source reconnaissance toolchain is the alternative foundation for a specialist entrant, since most of the discovery capability is freely available and the product is the packaging, the consent model, the reconciliation and the estimate.

Buyers are testing firm commercial and delivery leadership.

## Impact If Solved

A commodity capability reaches the moment it would matter most. Discovery before the quote is the difference between an engagement sized against the estate and one sized against a guess.

The reconciliation output doubles as the strongest sales instrument in this industry — showing a prospect assets they did not know they had, before any contract, makes the case for testing better than any proposal.

And bringing external discovery into scoping would eliminate the most common and least visible failure in the industry: an engagement that never tests the thing nobody remembered to list.
