# Verifying Private Fund Fees and Carry Against the LPA

**Industry:** [[pension-funds|Pension Funds]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every public pension with a private markets programme must report each fund's fees, expenses and carried interest, and the data arrives in a different shape from every GP, with nobody recomputing it from the partnership agreement.
**Tags:** #large-language-models #transformers #seq2seq #feature-engineering #evaluation-metrics #compliance #data-integration #automation

## The Problem
A large public plan has a few hundred private fund interests. Each quarter it receives capital account statements, capital call and distribution notices and, increasingly, an ILPA-format fee template. California's Government Code 7514.7 requires public funds to obtain each fund's fees and expenses, the plan's share of fees paid to the manager and related parties, its share of carried interest, and portfolio-company fees, and to present them at least once a year in an open meeting. ILPA's updated Reporting Template, released in January 2025, applies from Q1 2026 reporting and splits out internal chargebacks and partnership expenses in more detail.

The plan's real question is not whether the GP filled in the template. It is whether the numbers are right under the limited partnership agreement and the side letter. Is the management fee charged on the right basis now that the investment period has ended? Have transaction and monitoring fees been offset at the agreed percentage? Is the fund charging organisational expenses above the cap? Is carry being taken before the hurdle and catch-up are met? Most plans have one or two people reconciling this by spreadsheet, and the annual board report is assembled from what GPs supply.

## What Already Exists
Private markets monitoring platforms (MSCI's Burgiss, FactSet's Cobalt, Chronograph, Nasdaq's Solovis, Colmore) collect and extract GP documents and present cash flows, NAVs and fees. Custodians offer private markets accounting services. Fund administrators produce ILPA templates on the GP side. Consultants assemble the annual fee report for some clients. Generic contract-analysis tools read LPAs.

## The Customisation Gap
The tools collect what GPs report; they do not recompute it. The missing layer is pension-specific. Each LPA and side letter must be turned into executable terms: fee basis by period, step-downs, offset percentages, expense caps, hurdle, catch-up, clawback and most-favoured-nation elections. Those terms must be recomputed against each quarter's statement, with differences flagged in dollars. And the result must produce the statutory disclosure fields in the form the board and the public records officer will see. The terms vary fund by fund, and the obligation (an annual public report) is specific to public plans.

## Impact If Solved
Fee and carry verification moves from an annual compilation exercise to a quarterly check, catching overcharges while they can still be raised at the LPAC. It gives the one analyst who owns the 7514.7 report a defensible, recomputed number for every fund instead of the GP's own.
