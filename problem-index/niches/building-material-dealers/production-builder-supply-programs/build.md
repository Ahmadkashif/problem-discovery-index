# Per-Plan Margin Watched Against the Market

**Niche:** [[niches/building-material-dealers/production-builder-supply-programs/profile|Production Builder Supply Programmes]]
**Industry:** [[industries/building-material-dealers|Building Material Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A dealer agrees per-plan prices for a quarter and only learns which plans lost money when the quarter closes.
**Tags:** #time-series-forecasting #gradient-boosting #feature-engineering #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to supply every start of a production builder's plans complete and on the builder's schedule at the per-plan price agreed for the period, and whoever runs the fewest short, late or variance-PO starts per hundred at that price takes the account.

## The Problem
Each plan's price bundles lumber, panels, trusses, windows and installation at a moment in the market. When OSB or framing lumber moves, some plans go underwater, and the builder releases more of the cheapest plans in a downturn.

## Why Nobody Has Built This
Plan-level bills of materials sit in takeoff files, prices in the programme agreement, costs in the ERP and starts in the portal; no system joins them.

## What to Build
A plan-margin model: each plan's bill of materials costed weekly at replacement cost (from licensed assessments and the dealer's own buys), multiplied by the builder's forecast starts from schedule releases, showing margin at risk by plan, division and builder, with suggested repricing triggers for the next negotiation. A two-week demo works on synthetic plans and a public price index.

## Target Customer
Builder-account leaders and pricing teams at dealers serving production builders.

## Impact If Built
On a ~$50M builder programme (estimate), catching a 5% cost move a month earlier on the most exposed plans protects ~$200,000–$400,000 of margin per market swing (estimate), and gives the next negotiation evidence for indexed terms.
