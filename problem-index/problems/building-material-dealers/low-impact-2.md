# Lumber Quotes Held Against a Moving Market

**Industry:** [[building-material-dealers|Building Material Dealers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Price optimisation tools set customer prices from segments and elasticity; a lumber package needs a price indexed to this week's framing and panel market, a hold period the builder accepts, tariff changes passed through, and a sweep of every open quote when the market moves.
**Tags:** #time-series-forecasting #exponential-smoothing #gradient-boosting #feature-engineering #revenue-impact #automation #data-integration

## The Problem
Lumber and sheet goods are about a quarter of a pro dealer's sales (Builders FirstSource reported $3.9B, 25.5%, in 2025), and their cost moves every week. Mills and wholesalers price framing lumber and panels off weekly assessments such as the Random Lengths composites, which weight 15 framing lumber prices and 11 panel items; CME's lumber futures exist but are thin beside the physical trade (total open interest of ~8,900 contracts in a February 2026 snapshot, search summary of a CME bulletin). Duties move too: Canadian softwood carried 35.16% anti-dumping and countervailing duties for most producers plus a 10% Section 232 tariff from 14 October 2025, and Commerce announced lower seventh-review rates (24.75% combined) on 14 October 2026.

The dealer quotes a builder a package today for delivery in ~4–12 weeks (estimate), often against inventory bought at another price. Each quote carries a hold period — a day for a counter price, a week for a custom-home package, a monthly or quarterly price sheet for a production builder (estimate) — and every package that ships after its hold should be repriced. In practice a commodity buyer watches the market and a few salespeople reprice what they remember. Open quotes are rarely swept when OSB jumps, so packages ship below replacement cost in a rising market, and in a falling one stale high quotes lose bids to a competitor who repriced.

## What Already Exists
Price optimisation software (Zilliant, PROS, Pricefx and others) sets customer-specific prices from segment, elasticity and margin targets; LBM ERPs apply matrix pricing, cost updates and quote expiry dates; Fastmarkets' Random Lengths service and other price reports give the market; a few large dealers hedge with futures or buy forward.

## The Customisation Gap
A lumber price has to be built bottom-up from a market reference: replacement cost by species, grade, size and length off the latest assessment or mill quote, plus freight, tariff and duty pass-through for Canadian product, plus a margin that differs between a counter sale and a production builder's programme. Quotes need explicit hold periods by customer and quote type, escalation language in long packages, and a daily sweep that flags every open quote, unreleased package and builder price sheet whose margin has fallen below floor since the market moved, with the replacement cost shown. Generic optimisers treat lumber as a product class with a stable cost and a demand curve; for a dealer its cost is the variable, and the customer's tolerance for repricing is the constraint.

## Impact If Solved
Holding commodity margin through a market swing protects a category worth ~$10–30M a year at a mid-size dealer (estimate), and replaces one buyer's memory with a rule applied to every quote, branch and salesperson. The electrical analogue, repricing wire to COMEX copper, is mapped at [[electrical-distributors|Electrical Distributors]].
