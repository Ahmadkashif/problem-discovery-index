# Payer Fee Schedules Modelled in a Spreadsheet

**Industry:** [[physician-practices|Physician Practices]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Contract management modules check whether a claim paid what the table says; none of them tells a practice what a payer's renewal offer is worth against its own procedure mix and next year's Medicare fee schedule.
**Tags:** #linear-regression #descriptive-statistics #monte-carlo-methods #feature-engineering #data-integration #revenue-impact #quick-win

## The Problem
Most commercial contracts with physician groups pay a percentage of Medicare's fee schedule, sometimes pegged to a named year, sometimes with carve-outs for high-volume codes, and with escalators every one to three years. When a payer sends a renewal ("115% of 2026 Medicare, evergreen"), the practice administrator must decide whether to sign. They do it in a spreadsheet: last year's top 50 CPT codes, a guess at volumes, and the current Medicare rate.

The CY2026 fee schedule shows why that guess breaks. The conversion factor rose 3.26% to $33.40, but 2.5% of that is a one-year statutory bump, and CMS cut work RVUs 2.5% on non-time-based services while exempting E/M and care management (CMS-1832-F). A primary care group and a gastroenterology group can therefore see opposite effects from the same "percent of Medicare" offer. Office practices also gained relative to facility-based ones through a practice-expense change.

## What Already Exists
RCM contract management modules (athenaCollector's expected-payment tables, Experian Health Contract Manager, Waystar) and point tools such as MDClarity load fee schedules and flag underpaid claims. Consultancies negotiate for larger groups, and price transparency data from Turquoise Health and Serif Health shows competitors' negotiated rates. Medicare publishes RVUs, GPCIs and the conversion factor every year.

## The Customisation Gap
Underpayment detection looks backward at claims. The practice needs a forward model that:

- prices every CPT and modifier the group bills, by place of service, under the offer's exact terms (named-year peg, carve-outs, multiple-procedure and bilateral rules, -25 and -59 modifier behaviour);
- re-prices it under next year's proposed and final Medicare rules, including the efficiency adjustment and the expiry of the one-year bump;
- shows the effect of mix shifts such as a new physician, an added procedure line or a move from hospital outpatient to the office;
- compares the offer with published negotiated rates for the same payer and market.

## Impact If Solved
A group that models offers properly avoids signing contracts that quietly lose 2%–4% of commercial revenue to a pegged year or to RVU cuts on its main procedures (estimate). For a 20-physician specialty group with ~$40M in commercial collections, that is ~$0.8M–$1.6M a year. Renewal analysis would take hours instead of the weeks of spreadsheet work it takes now.
