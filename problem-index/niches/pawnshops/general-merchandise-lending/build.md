# Store-Level Resale Comparables From the Operator's Own Sales

**Niche:** [[niches/pawnshops/general-merchandise-lending/profile|General Merchandise Lending]]
**Industry:** [[industries/pawnshops|Pawnshops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Clerks price used goods off national marketplace listings when the operator's own sales history already says what each model sells for in this town and how long it takes.
**Tags:** #gradient-boosting #k-nearest-neighbors #survival-analysis #bayesian-inference #feature-engineering #evaluation-metrics #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to price a used branded item — a drill kit, a games console, a guitar, a laptop — from its exact model and condition against what that model actually resells for locally, in seconds at the counter, and whoever prices it closest to its realised resale takes the account.

## The Problem
A national sold price is the wrong number for a pawn loan. It ignores shipping, marketplace fees, the condition the item will actually be in, local demand and the weeks the item may sit on a shelf. Yet it is what clerks use, because the operator's own history — thousands of forfeited and purchased items sold in its stores — is buried in POS tables nobody queries at the counter.

## Why Nobody Has Built This
Item descriptions are free text, so matching "DEWALT 20V DRILL KIT 2BAT" across tickets requires normalisation nobody has done. Single-store operators have too few sales per model; chains have the volume but treat the data as accounting, not pricing.

## What to Build
A comparables service that normalises descriptions to models, joins each to realised sale prices and days on shelf by store and region, fits depreciation curves by model age and product-cycle events, adjusts for the condition grade captured at intake, and returns to the clerk a range, a median days-to-sell and the count of comparables behind it. Pool thin models across similar ones and nearby stores, and show uncertainty when the history is thin.

## Target Customer
Directors of lending and merchandising at chains and regional groups; POS vendors who could offer pooled comparables to independents.

## Impact If Built
Loans on general merchandise are set against what the item will actually fetch, in seconds, and the forfeits that sell below the loan become rarer — while clerks lend more confidently on items the store sells well.
