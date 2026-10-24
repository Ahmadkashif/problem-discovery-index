# A Molecule Ledger From Filing to Price Floor

**Niche:** [[niches/pharmaceutical-manufacturers/generic-oral-solid-dose-portfolios/profile|Generic Oral Solid Dose Portfolios]]
**Industry:** [[industries/pharmaceutical-manufacturers|Pharmaceutical Manufacturers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A generic maker forecasts every molecule when it decides to file and never compares the forecast with what the molecule earned, so portfolio selection does not learn.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #feature-engineering #evaluation-metrics #revenue-impact #data-integration
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to earn money on a molecule after the brand's exclusivity ends, but first-to-file launches and mature-molecule supply reward different things: a launch is won by whoever is first lawfully on the market with exclusivity, a mature molecule by whoever keeps shipping an awarded contract at an eroded price without a failure-to-supply penalty. Decomposed into contested sub-niches below.

## The Problem
Portfolio teams pick molecules years ahead: expected entry date, number of competitors, price erosion curve, API cost, development and litigation spend. The forecast justifies the filing and is then set aside. By the time the molecule launches, the team that chose it has moved on, and the actual entry count, price path and supply problems are tracked in separate finance, commercial and supply systems. Nobody can say which kinds of selection call (competitor counts, erosion assumptions, API sourcing choices) the team tends to get wrong.

## Why Nobody Has Built This
Pipeline databases sell forward-looking data, not a grading of the customer's own calls. Finance tracks product P&L, not the decision that created it. The horizon is long (five to ten years from selection to mature price), so feedback arrives after the people have changed.

## What to Build
A ledger attached to every molecule decision: the forecast as made, joined to the public record of what followed (FDA approvals and entrant counts, Paragraph IV outcomes, shortage events) and the firm's own launch timing, prices and margins. Survival models of time to each new entrant and erosion models by dosage form and market structure, calibrated against the firm's history, then used to score new candidates and flag molecules whose margin no longer covers their quality and supply cost.

## Target Customer
Heads of portfolio strategy and US generics finance at the top 15 generic makers selling in the US.

## Impact If Built
A portfolio that learns from its own record could cut failed or unprofitable filings by two or three a year, each a multi-million-dollar development and litigation cost (estimate), and would show which mature molecules to exit before they become shortages.
