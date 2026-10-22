# Institutional Custody & Asset Servicing

**Parent Industry:** [[industries/trust-companies|Trust Companies]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to deliver each client's positions, cash and corporate-action entitlements without breaks before the client's own NAV and settlement cutoffs, and whoever has the fewest unresolved breaks at the cutoff takes the account.

## Profile
**Market Size:** ~$3B a year in operations technology, data and outsourced services inside custody and asset servicing (estimate), against ~$18.0B of gross custody and safekeeping fiduciary income at FDIC-insured institutions in 2025
**Share of Parent Industry:** ~32% of FDIC-reported fiduciary income ($18.0B of $55.6B)
**Digital Adoption:** High — straight-through processing for most trades and income; exceptions still worked by email and spreadsheets
**Target Buyer:** Head of Asset Servicing Operations / COO, Securities Services
**Automation Potential:** High for break resolution and corporate actions processing

## What Makes This a Distinct Niche
A handful of banks hold most institutional assets: BNY ($59.3T in assets under custody or administration at end-2025), State Street (~$53.8T), JPMorgan Chase, Citi and Northern Trust (~$18.7T). Their clients — pension funds, asset managers, insurers, sovereign funds — need positions, cash and entitlements right before their own deadlines: the fund's daily NAV strike, the shortened US settlement cycle, an election deadline on a tender offer. The work is reconciliation across custodian, investment manager, fund accountant and depository, and the processing of income, corporate actions and tax. Competitors are the custody banks themselves and the technology vendors they buy from (Broadridge, SS&C, Duco); clients choose and keep custodians largely on servicing quality once fees converge.

## Current Tools & Gaps
Proprietary custody platforms, SWIFT messaging, depository interfaces, reconciliation engines and corporate-actions data from vendors. The gaps: breaks are found after they occur rather than predicted; root causes are coded inconsistently, so recurring causes are not fixed upstream; voluntary corporate-action elections still arrive as free-text messages; and the context of how a break was last resolved sits with the analyst who resolved it.

## Problems
- [[niches/trust-companies/institutional-custody-asset-servicing/build|🔨 Build: Break Prediction Before the Cutoff]]
- [[niches/trust-companies/institutional-custody-asset-servicing/buy|🛒 Buy: Reconciliation Platforms Taught Corporate Actions]]
- [[niches/trust-companies/institutional-custody-asset-servicing/fix|🔧 Fix: The Voluntary Election That Arrived as an Email]]
