# Secondary Marketing & Pipeline Risk

**Parent Industry:** [[industries/mortgage-lenders|Mortgage Lenders]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to forecast which locked loans will fund and to sell each one at its best execution, and whoever earns the most margin per locked loan net of hedge cost and lock concessions takes the account.

## Profile
**Market Size:** ~$900M a year in pricing-engine subscriptions, hedge advisory fees, loan-trading platforms and secondary desk tooling (estimate)
**Share of Parent Industry:** ~7–8% of mortgage lenders' technology, data and outsourced-service spend (estimate)
**Digital Adoption:** High — prices, locks, commitments and TBA trades are electronic; extension and renegotiation decisions still run by email and judgement
**Target Buyer:** EVP or Head of Capital Markets
**Automation Potential:** High for rate sheets and best-execution; medium for hedge strategy

## What Makes This a Distinct Niche
A lender carries interest-rate risk from the moment it locks a borrower's rate until it sells the loan, which a broker never does. Lenders selling on a mandatory basis hedge the locked pipeline with forward TBA trades, sized to the share of locks they expect to fund; they then choose for each closed loan between an agency cash window, pooling into MBS, or selling to an aggregator. Freddie Mac lists 16 integrated secondary market advisors and pricing engines, which says how much of this work is bought rather than built. Margin is won or lost in basis points: the pricing margin on the rate sheet, the hedge result, the cost of extensions and renegotiations, and the execution price.

## Current Tools & Gaps
Optimal Blue (PPE, CompassPoint hedging, Resitrader), Polly, ICE PPE and LoanPASS price and lock; MCT, MIAC, Vice Capital Markets and ALM First advise on hedges and best execution; MCT's write-back integration with Dark Matter's Empower moves loan-sale data back into the loan file. The gaps: pull-through is still estimated from stage-based tables; lock extensions and renegotiations are approved outside any system and never priced against fallout; and gain on sale is reported in total, not attributed to the decisions that made or lost it.

## Problems
- [[niches/mortgage-lenders/secondary-marketing-pipeline-risk/build|🔨 Build: Lock-Change Pricing From Modelled Fallout]]
- [[niches/mortgage-lenders/secondary-marketing-pipeline-risk/buy|🛒 Buy: Gain-on-Sale Attribution in a Generic BI Stack]]
- [[niches/mortgage-lenders/secondary-marketing-pipeline-risk/fix|🔧 Fix: The Rate Sheet Built by Hand Every Morning]]
