# Fighting Only What Can Be Won

**Niche:** [[niches/payment-fraud-vendors/chargeback-representment/profile|Chargeback Representment]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Specialists assemble evidence by hand for disputes whose outcome was determined by the reason code before anyone opened the case.
**Tags:** #gradient-boosting #large-language-models #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to assemble the evidence a network's reason code demands, inside its deadline, only for the cases that can actually be won — and whoever predicts winnability stops spending effort on disputes that were lost before they started.

## The Problem
Representment outcomes are highly predictable from the reason code, the evidence available, the merchant's category, the transaction's characteristics and the issuer involved. Some combinations are won almost always and some almost never. Teams work the queue in arrival order, spending the same effort on both, and the aggregate recovery rate is reported without decomposition — so nobody knows how much of the team's month goes to cases that could not be won.

## Why Nobody Has Built This
Representment was staffed as an operations function and measured on a recovery rate, so effort allocation was never the question — a team judged on how much it recovers has no reason to ask what it wasted. Outcomes are recorded per case and never analysed as a dataset. Evidence lives across merchant systems the vendor reads selectively. And service pricing is often per case, which rewards volume.

## What to Build
Predict the outcome, then automate the winnable. Model win probability from reason code, evidence availability, merchant category, issuer and transaction attributes, which is the core and is straightforward supervised learning on outcomes already recorded. Retrieve the required evidence automatically from the merchant's systems, since gathering is the bulk of the effort and the required items per reason code are well defined. Encode each network's reason code requirements as structured rules, because they are published, they change, and they are currently carried in specialists' memory. Assemble and format the submission, leaving the judgement to the specialist. Rank the queue by expected recovery rather than by deadline, so effort follows value. Decline to fight cases below a threshold and say so explicitly, as that is an honest and valuable recommendation rather than a failure. Prevent the chargeback where possible by resolving with the customer first, since a refund is cheaper than a lost dispute and a cardholder contact often avoids both. Feed outcomes back continuously, which keeps the model current as network rules shift. Report recovery per hour of effort, which is the metric the function lacks. And distinguish genuine fraud chargebacks from friendly fraud and service disputes, because the strategies differ entirely and they are currently one queue.

## Target Customer
Dispute operations leadership, merchants paying for representment, fraud vendors offering guarantees, and dispute service providers pricing per case.

## Impact If Built
A team measured on total recovery has no reason to ask what it wasted, so effort allocation was never examined. Win probability is highly predictable from data already recorded, and it turns an arrival-order queue into a ranked one.
