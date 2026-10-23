# Demurrage & Detention Billing and Disputes

**Parent Industry:** [[industries/ocean-shipping-carriers|Ocean Shipping Carriers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to bill every chargeable container day inside the FMC's 30-day window on an invoice that survives dispute, and whoever collects the highest share of billed demurrage and detention without waiver takes the account.

## Profile
**Market Size:** ~$300M global spend on D&D billing, dispute handling and evidence tooling at ocean carriers and NVOCCs, ~$90M of it in US trades (estimate); terminal demurrage billing by marine terminal operators is left to the queued port-terminal-operators industry
**Share of Parent Industry:** ~2% of carrier shore-side spend (estimate)
**Digital Adoption:** Medium — container events are digital; free-time terms, terminal conditions and disputes are spread across systems and inboxes
**Target Buyer:** Head of Billing / Director of Equipment and D&D
**Automation Potential:** Very high — clock reconstruction, invoice assembly and dispute triage are rule-bound

## What Makes This a Distinct Niche
Demurrage and detention are charges for keeping containers in the terminal or out of the carrier's equipment pool past free time, and they became a regulatory issue after the 2020–22 congestion. OSRA 2022 (recalled) and the FMC's billing rule (46 CFR 541, effective 28 May 2024) now require invoices within 30 days of the last chargeable day, a fixed set of data elements and certifications, and a 30-day dispute and resolution process. An invoice that is late or incomplete need not be paid. The work is mechanical once the clock is right, and the clock is the hard part. See [[problems/ocean-shipping-carriers/low-impact-2|Demurrage and Detention Invoices Under the FMC Rule]]. Importers' own D&D tracking is analysed at [[niches/freight-tech-platforms/ocean-intermodal-visibility/profile|Ocean & Intermodal — Milestone Reconciliation]].

## Current Tools & Gaps
Carrier and terminal billing modules, visibility feeds (project44, Portcast, Vizion), ERP receivables. Gaps: free-time clocks rebuilt by hand when terminals close or appointments are unavailable, certification evidence not assembled, and disputes answered from scratch.

## Problems
- [[niches/ocean-shipping-carriers/demurrage-detention-billing/build|🔨 Build: A Free-Time Clock Rebuilt From Every Source]]
- [[niches/ocean-shipping-carriers/demurrage-detention-billing/buy|🛒 Buy: Receivables Dispute Software Adapted to 46 CFR 541]]
- [[niches/ocean-shipping-carriers/demurrage-detention-billing/fix|🔧 Fix: Invoices Issued on Day 31]]
