# Rate Lock Timing Optimization

**Industry:** [[mortgage-brokers|Mortgage Brokers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Rate lock decisions are already made every day — they're just made by gut feel and morning rate sheet emails instead of a model that knows the pipeline.
**Tags:** #lstms-and-grus #time-series-forecasting #rnns #backpropagation #gradient-descent #loss-functions #evaluation-metrics #expectation-variance-covariance #revenue-impact

## The Problem
Mortgage brokers must decide when to lock a borrower's interest rate with the wholesale lender. Lock too early and you commit to a rate that might improve; lock too late and rates spike, forcing a worse rate or losing the deal. A typical brokerage locks 30-80 loans per month, and each basis point on a $400K loan is $40/year to the borrower — aggregate across a pipeline and bad timing costs tens of thousands in lost competitive positioning. Most brokers lock reflexively when the borrower says "go" rather than strategically timing the lock around market conditions and pipeline dynamics.

## What Already Exists
Bloomberg, MBS Live, and Mortgage News Daily provide real-time rate movement data and commentary. Some LOS platforms show current lender pricing. Float-down options exist but cost 12.5-25 bps upfront. None of these tools integrate borrower-specific pipeline data (expected close date, rate sensitivity, borrower risk of walking) with market signals to produce an actionable lock/float recommendation for each loan in the pipeline.

## The Customisation Gap
The missing layer is a pipeline-aware forecasting model that combines macro rate signals (10-year Treasury, MBS spreads, Fed commentary sentiment) with loan-level context: how rate-sensitive is this borrower, how far out is closing, what is the lender's lock expiration policy, and what is the probability this borrower comparison-shops if the rate worsens. The model must output not just a directional forecast but a loan-specific lock/float recommendation with a confidence score and a "regret cost" estimate for each decision.

## Impact If Solved
A 5-10 bps average improvement in lock timing across a pipeline translates to $200-400 per loan in borrower savings, making the broker more competitive on rate. For a 500-loan/year brokerage, this is $100K-200K in aggregate borrower value that drives referrals and retention.
