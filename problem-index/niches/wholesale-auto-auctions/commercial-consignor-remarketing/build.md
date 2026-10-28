# Net-to-MMR Counterfactual for Every Commercial Unit

**Niche:** [[niches/wholesale-auto-auctions/commercial-consignor-remarketing/profile|Commercial Consignor Remarketing]]
**Industry:** [[industries/wholesale-auto-auctions|Wholesale Auto Auctions]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Consignors see what each unit netted in the channel it sold through, and never what it would have netted in the channels it skipped, so channel strategy is argued from anecdotes.
**Tags:** #causal-inference #gradient-boosting #time-series-forecasting #evaluation-metrics #revenue-impact #ai-platform
**Contested on:** Every serious competitor in this niche is fighting to sell a commercial consignor's off-lease, rental, fleet and repossessed units for the most money after fees and transport, and whoever returns the highest net proceeds as a share of MMR takes the account.

## The Problem
A remarketing director at a captive decides, for tens of thousands of lease returns a year, how long to hold each car in the grounding window and how long in the upstream private-label sale before releasing it to open auction, and at which physical location. Each step trades price against time, transport and depreciation, which ran faster than usual in September 2026. The auction reports net proceeds against MMR for what sold. It cannot say what the same car would have brought had it been released to open digital sale a week earlier, or shipped to a lane 300 miles away.

## Why Nobody Has Built This
The auctions hold the outcome data but sell the channel. An auction that showed a consignor its own lanes underperforming would be arming its competitor. Consignors hold only their own results and cannot see the market's. And channel choice is confounded, because the best cars sell upstream and the rest flow down, so naive comparisons always flatter upstream.

## What to Build
A causal model of net proceeds against MMR by channel and timing, trained on the consignor's own history across every channel it uses. It adjusts for condition grade, mileage, region and the selection that sends better cars upstream, using propensity weighting and doubly robust estimation. Each unit gets a recommended channel, hold period and floor with an expected net-to-MMR and a range. A monthly report shows realised against counterfactual net by channel. It should be sold to the consignor, not the auction, so its neutrality is the product.

## Target Customer
Remarketing directors at captives, bank lessors, rental companies and fleet lessors running 20,000+ units a year across more than one channel.

## Impact If Built
At an average in-lane price of $13,800, lifting net proceeds by half a percentage point of MMR is ~$70 a unit, or $1.4M a year on 20,000 units (estimate). It would also give consignors evidence when renegotiating fees.
