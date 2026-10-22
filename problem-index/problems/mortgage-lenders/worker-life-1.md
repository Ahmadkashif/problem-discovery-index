# The Lock Desk Before the Rate Sheet Goes Out

**Industry:** [[mortgage-lenders|Mortgage Lenders]]
**Type:** Worker Life Changing
**One-liner:** A secondary marketing analyst publishes the morning rate sheet, reprices it whenever MBS prices move, and spends the rest of the day deciding lock extensions and renegotiations one email at a time, with the lender's margin on every call.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #large-language-models #worker-facing #workflow-orchestration #revenue-impact

## The Problem
The lock desk's day starts before the market opens. The analyst loads the morning's MBS prices, the hedge advisor's coverage report and the investor price sheets, builds the rate sheet for every product the lender offers, checks it against the pricing engine, and releases it to loan officers. If MBS prices move by more than the lender's tolerance during the day, the sheet is pulled and reissued, and every loan officer who quoted a borrower an hour earlier calls to ask why. Locks taken just before a reprice are reviewed one by one.

Then the exceptions arrive. A loan will not close inside its lock because the appraisal is late, so the loan officer asks for a free extension. Rates have fallen since the borrower locked, a competitor is quoting lower, and the loan officer wants a renegotiation or the borrower walks. A lock was taken on the wrong product and must be re-priced. Each request comes by email or chat with a story attached, and the analyst decides from the lender's policy, the loan officer's history and their own sense of whether the borrower will really leave. Every concession comes out of the margin the hedge was protecting.

## Why It Matters to the Worker
The analyst carries the lender's interest-rate risk at a desk with no one to share it. A reprice released late, or a misplaced decimal on a rate sheet, can lock dozens of loans below cost before anyone notices, and the analyst is the person who answers for it in the capital markets meeting. The job is also a stream of negotiation with loan officers who outrank them commercially, and saying no to a top producer's extension request has consequences that policy documents do not cover.

The hours follow the market, not the clock. Volatile days mean multiple reprices and a flood of lock changes. Month-end means commitment deliveries, pair-offs and pipeline reconciliation with the hedge advisor. In a refinance boom the volume doubles with no new staff, and in a bust the desk is cut to one person.

## What a Solution Looks Like
A rate sheet built and checked automatically from the morning's inputs, with every changed price explained against yesterday's, and a reprice drafted the moment MBS prices cross the tolerance. Lock-change requests arrive structured rather than as emails: the loan's status, reason for delay, days needed, the borrower's likelihood of leaving at the current market (from a pull-through model, not a guess), the loan officer's history of requests, and the cost of each option to the hedge. The analyst approves or declines with a recorded reason, and the policy learns from what renegotiations actually kept loans that would otherwise have walked.

## Impact If Solved
Automating sheet production and reprices returns one to two hours each morning (estimate) and removes the most error-prone manual step on the desk. Pricing lock changes against modelled fallout rather than negotiation stops margin leaking in five- and ten-basis-point concessions, and gives the analyst a defensible answer for the top producer.
