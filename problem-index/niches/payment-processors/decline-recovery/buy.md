# Collections Timing Practice

**Niche:** [[niches/payment-processors/decline-recovery/profile|Decline Recovery]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Collections has optimised contact timing and channel against payment probability for decades, and payment retry uses a fixed schedule.
**Tags:** #survival-analysis #gradient-boosting #confidence-intervals #evaluation-metrics #time-series-forecasting #monte-carlo-methods #revenue-impact #optimization-fundamentals
**Contested on:** Every serious competitor in this niche is fighting to know which declines are worth retrying, from which issuer, on what schedule — and whoever learns that from settlement outcomes recovers revenue everyone else abandons.

## The Problem
Deciding when to attempt collection, how often, through which channel and when to stop is a developed quantitative practice in consumer collections. Payment probability is modelled from account characteristics and behaviour, contact timing is optimised against pay cycles, channel and intensity are matched to the segment, and the decision to stop pursuing is made on expected recovery against cost. The industry is heavily regulated and heavily modelled. Payment retry is structurally the same problem — repeated attempts against an uncertain payer — and runs on a schedule.

## What Already Exists
Payment probability models; contact timing optimisation against income cycles; channel and intensity segmentation; expected recovery against cost of pursuit; and regulated contact frequency constraints.

## The Customization Gap
The adaptation is to an automated attempt against an issuer rather than a contact with a person. It requires: (1) the counterparty being an issuer's decision system rather than a debtor, so the modelling is about the issuer's behaviour as much as the cardholder's — a dimension collections does not have and is where the processor's cross-merchant view is decisive; (2) attempts that cost fractions of a currency unit rather than a phone call, which shifts the economics toward more attempts and makes the stopping rule finer; (3) outcomes in days rather than months, giving a far faster learning loop than collections ever enjoys; (4) a customer relationship the merchant wants to preserve, so an aggressive recovery policy has a cost collections practice weighs differently; and (5) network rules constraining retry frequency, which are hard limits rather than regulatory guidance on tone.

## Target Customer
Processor product teams, subscription and recurring revenue businesses, and collections analytics practitioners for whom payment retry is an unserved adjacent problem.

## Impact If Solved
Collections models payment probability and optimises timing against pay cycles, and payment retry uses a schedule. The issuer's decision system as the counterparty is a dimension collections lacks, and outcomes in days give a far faster learning loop.
