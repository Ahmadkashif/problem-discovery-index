# History: IT Managed Services

**Industry:** [[industries/it-managed-services|IT Managed Services]]
**Primary Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**Secondary Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**Origin Parent:** Native birth — no origin parent. See below.
**Episode Tier:** 1
**Transferable Pattern:** An industry can professionalise entirely through a labour-and-billing innovation, with no new algorithm anywhere in it — and the same aggregation that makes the new model viable, one vendor's tooling reaching thousands of endpoints, becomes the single point of failure that can hurt all of them at once.

> **Template note.** This file uses the absence rule twice. There is no founding event and no competitive duel here, and rather than manufacture either, this file names what actually stands in their place: a gradual, multi-vendor shift in billing model, and a real security incident that stands in for a graveyard no company's failure otherwise supplies.
>
> **Origin Parent — there genuinely is none.** MSPs did not descend from a pre-computer industry. They exist to service the client-server estate — Windows domains, on-premise Exchange, small-business servers — that [[series/eras/wave-04-client-server-erp|Wave 4]] put in every office that could afford one, and later moved their own delivery model onto Wave 6's economics. That makes this industry's ancestry a *wave*, not a *parent business*.

## Before

An IT services relationship in the 1990s and early 2000s was overwhelmingly **break-fix**: a business called a local technician when something stopped working, was billed by the hour for the call, and had no ongoing visibility into the health of its own network between visits. The incentive this created was structurally perverse and rarely discussed as such — a vendor paid only when something broke had no financial reason to prevent breakage, and a business with no monitoring had no way to know a problem was forming until it had already stopped work. This is the direct client-side legacy of Wave 4: the client-server infrastructure it put in every small business — a server room, a domain controller, a handful of workstations — is exactly what needed a truck roll every time it failed.

## The Origin Event — There Isn't One

No single company or product marks the start of managed services the way a founding date marks other files in this vault. What is dateable is the tooling that made the billing shift possible: **Kaseya, founded in 2000** in California by Mark Sutherland and Paul Wong, built remote monitoring and management (RMM) software letting a technician see the state of many clients' devices continuously rather than being told about a failure after the fact. Competing RMM and professional-services-automation (PSA) tools — ConnectWise, N-able, and Autotask (founded 2001, later merged into Datto) — emerged across the same rough window, none of them displacing the others outright. This is the same shape of finding this vault's own research has already logged for pharma CROs and telecom carriers: a gradual, multi-vendor category formation with no credible single founding battle, and the honest move is to say so rather than invent one to fit the template.

## What Became Cheap

**Knowing the state of a client's network without a technician driving to the site.** An RMM agent installed on a workstation or server reports continuously to a dashboard the MSP can watch from anywhere, and once that dashboard itself became a cloud-hosted subscription rather than software the MSP had to run and maintain on its own infrastructure — Wave 6's mechanism, one layer removed from the end customer — monitoring shifted from an occasional, billable site visit to a background service running for a flat monthly fee.

## How It Was Actually Solved

The mechanism that let break-fix become managed services was not predictive or particularly sophisticated: an RMM agent detects a condition (disk filling up, a service stopped, a patch missing) and opens a ticket in the PSA system automatically, before the client notices anything is wrong. This converted the vendor's core risk from "unknown, unbounded, billed after the fact" to "monitored, bounded, priceable in advance" — which is the entire reason a flat per-device or per-user monthly contract became something an MSP could offer without going broke on the bad months. No model was built here in the sense this vault otherwise means; the innovation was operational and financial, not statistical, and the category has proceeded largely on that footing since.

## The Contest — There Isn't One, Only a Slow Roll-Up

This vault's H2 research already flagged that not every origin produces a duel; this industry does not produce a duel either, at any point in its history to date. Kaseya, ConnectWise, Datto/Autotask and N-able have coexisted as a fragmented, multi-vendor RMM/PSA market for two decades, and the most significant structural move among them was **Kaseya's acquisition of Datto in 2022 for $6.2 billion** — a merger between two established players, not a case of one company defeating the other in the market. The more consequential competitive dynamic in this industry today is not between tool vendors at all. It is the ongoing, private-equity-backed **roll-up of the MSPs themselves** — a widely reported trend in trade press, consistent with the fact that this vault already carries dedicated niches (`msp-ma-brokerage`, `msp-rollup-corporate-development`) for exactly this activity. I could not independently verify specific deal-count or deal-value figures for the roll-up wave in this session, and this file does not attach a number to it that it cannot source.

## The Graveyard — Not a Company, an Incident

No MSP tooling vendor in this category has failed the way Wirecard failed. What this industry's history does supply is a real, dated demonstration of the structural risk its own business model creates. **On 2 July 2021, the REvil ransomware group exploited unpatched vulnerabilities in Kaseya's VSA software**, compromising roughly 60 Kaseya MSP customers directly and, through them, as many as 1,500 downstream small and medium businesses that had never bought anything from Kaseya themselves. Kaseya began restoring service around 23 July, using a universal decryptor obtained from a third party.

This is the industry's genuine failure-class case, and it is not a competitor dying — it is the exact aggregation that makes flat-rate managed services economical (one vendor's agent, reaching thousands of endpoints across hundreds of client businesses) turning into a single point of failure with a blast radius none of those downstream businesses had any visibility into or control over. It is a more honest "graveyard" for this file than reaching for a bankruptcy that did not happen.

## The Binding Constraint

The binding constraint on this industry, now as at its founding, is **labour**, not technology. This vault's own hub note for the industry states that 60–70% of inbound tickets are low-skill, repetitive L1 issues — password resets, printer failures, basic connectivity problems — consuming technician hours without requiring real expertise. That figure is consistent with the kind of numbers MSP trade publications and RMM vendors self-report, but I could not verify it against an external, citable study in this session, and it should be read as this vault's own working figure rather than an independently audited one. What is not in question is the shape of the constraint: an MSP's margin is set by how many technician-hours a fixed contract can be delivered within, and by the wage and turnover economics of the technicians doing that work — a labour-market limit, not an algorithmic one, and no model this vault could propose changes what a technician costs to hire and retain.

## What's Still Open

- [[problems/it-managed-services/high-impact|🔴 Ticket Triage, Routing, and Automated Resolution for L1 Issues]] — automating the 60–70% that consumes technician hours without needing technician judgement
- [[niches/it-managed-services/l1-ticket-automation/profile|L1 Ticket Automation]]
- [[niches/it-managed-services/billing-reconciliation/profile|Billing Reconciliation]] — the PSA/RMM data-matching gap that leaks revenue quietly
- [[niches/it-managed-services/msp-rollup-corporate-development/profile|MSP Roll-Up & Corporate Development]] — the consolidation this file names in place of a contest
- [[niches/it-managed-services/cyber-insurance-smb-underwriting/profile|Cyber Insurance & SMB Underwriting]] — pricing the exact concentration risk the Kaseya incident demonstrated

## The Transferable Pattern

> **An industry does not need a technical breakthrough to professionalise — a change in who bears risk and when they get paid can be enough on its own. But look for where that same industry concentrated its risk to make the new model work, because that concentration is where the next real incident comes from, not from a competitor.**

An FDE arriving at an MSP-shaped business should not look for a model to build first. The constraint is who is doing the work and how much of it is being done more than once for no reason — and the biggest documented risk in the category's history came not from a rival but from the very tool that made the business model possible in the first place.

**Sources:** Wikipedia, *Kaseya*; this vault's `industries/it-managed-services.md`; this vault's `series/_plan.md` §5, "Structural finding from H2" (precedent for gradual, multi-vendor category formation with no founding duel). MSP market-size figures ($300B global, $100B North America, ~40,000 US MSPs) and the 60–70% L1-ticket figure are carried from this vault's own hub note and were not independently re-verified against an external source in this session; flagged here rather than re-asserted as newly confirmed.
