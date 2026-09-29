# Lineage: Healthcare Practice Software

**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**The tool:** the NCCI procedure-to-procedure edit table — Medicare's National Correct Coding Initiative list of CPT/HCPCS code pairs that may not be paid together for one patient on one date, implemented January 1996
**Builder:** Health Care Financing Administration
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A physician's claim is a list of codes, and the payer pays each line. That is cheap to process and easy to game.

A comprehensive CPT service often includes smaller services that have their own codes — the repair after an excision, say. Bill both on the same day and a line-by-line payer pays for the same work twice, and cannot tell carelessness from intent.

Medicare's problem, by the mid-1990s, was that it paid Part B claims through regional carriers, each with its own local rules. **Checking every combination by hand was impossible, and checking them differently in each region was indefensible.** What was missing was a single machine-readable statement of which code pairs are wrong together.

## What Got Built

A table. Each row is a pair of codes: a column-one code that is paid, a column-two code that is denied when billed with it for the same beneficiary on the same date, and an indicator saying whether a modifier may override the denial.

The Office of Inspector General records that **in January 1996 Medicare implemented the Correct Coding Initiative**, "to promote correct coding of health care services by providers and to prevent Medicare payment for improperly coded services," as "automated edits used to evaluate claim submissions when a provider bills more than one service for the same beneficiary and same date of service." The policies behind the pairs were drawn from AMA CPT conventions, national and local policies, specialty society guidelines and review of actual coding practice. HCFA's own July 1996 physician fee schedule rule was already using it as a policy lever — proposing to stop separate payment for skin repairs billed with lesion excisions "through our correct coding initiative" rather than through a payment status code.

CMS later added a second kind of edit, Medically Unlikely Edits, which cap the units of one code per day. It updates both tables quarterly.

## Who Built It, And Why Them

The Health Care Financing Administration, renamed CMS in 2001. Only the largest payer had both the motive and the standing.

The motive was simple arithmetic: every unbundled pair the edits catch is a Medicare payment not made. The standing mattered more. A private insurer that published its own bundling rules would be one more private rulebook; **Medicare publishing one made it the reference everyone else copied.** CMS states it owns the programme and makes every decision about its contents.

The table's shape follows: binary, pairwise, keyed to the AMA's existing CPT codes, and public — simple enough for a carrier to apply automatically, visible enough for every physician to look up.

The contractor that has built and maintained the edit tables for CMS is not established here; see Sources.

## What It Cost

**A pairwise table cannot hold context.** Two codes that are usually redundant are sometimes both legitimate — separate lesions, separate sessions, separate sites. The answer was the modifier, and the modifier became the most argued-over field on the claim: it lets the correct claim through and lets the incorrect one through too, so it draws audits.

The second cost is that NCCI became a template. The OIG found in 2003 that eight states used a **commercial edit package** instead of Medicare's, and that 39 states' Medicaid programmes paid $54 million in 2001 for services the Medicare edits would have denied. That is where the market came from: once one payer published its logic as a table, every other payer's slightly different logic became something a vendor could sell as content.

## What You Still Touch

Practice-management claim scrubbers still start from the NCCI pair table. The public part is easy; the hard part is every commercial payer's private variant, unpublished and changing.

- [[problems/healthcare-practice-software/low-impact-1|🟡 Payer Rule Engine Maintenance]] — keeping the non-Medicare copies current
- [[problems/healthcare-practice-software/high-impact|🔴 Claim Denial Prediction & Clean-Claim Rate]]
- [[problems/healthcare-practice-software/worker-life-2|🟢 Support Engineer Repeat-Ticket Treadmill]] — the same rejection, four hundred times
- [[niches/healthcare-practice-software/payer-rule-content-vendors/profile|Payer Rule & Claim Edit Content]]
- [[niches/healthcare-practice-software/ambulatory-rcm-modules/profile|Ambulatory Revenue Cycle Modules]]

**Sources:** HHS Office of Inspector General, *Applying the National Correct Coding Initiative to Medicaid Services*, OEI-03-02-00790, October 2004 — January 1996 implementation, stated purpose, policy sources, 2003 state survey, $54 million figure; Federal Register, 2 July 1996, HCFA proposed rule *Revisions to Payment Policies Under the Physician Fee Schedule for Calendar Year 1997* (96-16744, via govinfo.gov) — the "through our correct coding initiative" passage; CMS, *National Correct Coding Initiative (NCCI) Edits* page (ownership statement, PTP and MUE definitions); Wikipedia, *National Correct Coding Initiative* (quarterly updates). This vault's `history/healthcare-practice-software.md` was read for context and is not independent corroboration. ⚠️ **WebSearch was unavailable** (session cap reached); research was by WebFetch of known URLs. **Not established:** the contractor that originally built the edit tables for HCFA — secondary recollection names AdminaStar Federal and later Correct Coding Solutions LLC, but no source fetched this session confirms either, so neither is asserted. The start year of Medically Unlikely Edits and the Affordable Care Act's extension of NCCI to Medicaid were not confirmed and are not dated here. The CMS MLN NCCI booklet and medicaid.gov NCCI page both returned 404.
