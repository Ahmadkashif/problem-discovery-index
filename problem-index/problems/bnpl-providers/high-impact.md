# Underwriting Blind to Accumulation

**Industry:** [[bnpl-providers|BNPL Providers]]
**Type:** High Impact
**One-liner:** Every provider underwrites as if it were the consumer's only lender, because the sector's partial furnishing makes concurrent plans across providers invisible to all of them at once.
**Tags:** #gradient-boosting #logistic-regression #survival-analysis #causal-inference #confidence-intervals #evaluation-metrics #feature-engineering #compliance #revenue-impact

## The Problem
A consumer is at a checkout. The provider has a few hundred milliseconds, an email address, a phone number, a debit card, a shipping address, and whatever device and behavioural signal it can gather. It may have a thin bureau file or none. It may have its own history with this consumer, which is the strongest signal it has and exists only for returning customers.

It approves or declines a $180 purchase in four payments.

What it cannot see is that the same consumer opened three other plans this week at three other providers, and has two more outstanding from last month. Pay-in-four tradelines are furnished to the bureaus inconsistently and, where furnished, often in formats and on timelines that make them useless for a real-time decision. There is no equivalent of the credit card industry's shared visibility.

So each provider underwrites a consumer it models as having one obligation, and the consumer has six. Each individual decision looks defensible. The aggregate is not, and no participant can see the aggregate.

The second blindness is temporal. The provider learns whether the plan repaid over six weeks. It learns whether the consumer came back. It does not learn what happened to them — whether the instalments were paid by taking another plan, whether an overdraft fee was triggered at the bank when the auto-debit hit, whether a different provider's payment failed the same day. The consumer's actual financial state is the thing underwriting is trying to estimate, and the observable outcome is a much narrower thing: did this specific plan repay.

The cost of the gap falls in two directions. The provider takes credit losses on accumulation it could not see. And the consumers who accumulate are, in the sector's own data, disproportionately those with the least capacity to absorb it — which is the version of this problem that gets written about, and is the same problem.

## Why It's Unsolved
There is no shared infrastructure and no strong incentive to build one. Furnishing repayment data makes a provider's good customers visible to competitors, who will then market to them. The competitive logic runs directly against the prudential logic, which is exactly the situation that produced mandatory bureau reporting in traditional credit and has not yet produced an equivalent here.

The bureau infrastructure is also a poor fit. It was built for monthly tradelines on accounts that persist. A pay-in-four plan lives six weeks, involves four payments, and a consumer may open and close forty of them in a year. Reporting each as a tradeline damages the consumer's own score through account count and utilisation effects that the model was never calibrated for, which is a real argument against furnishing that is not merely self-interested.

Regulatory status was unsettled for most of the sector's growth. The CFPB's 2024 interpretive rule brought pay-in-four under Regulation Z's dispute and refund provisions, which settled some questions and not the furnishing one.

And the labels are genuinely thin. A consumer with no bureau file, on their first plan, generates one binary outcome in six weeks. That is a small amount of information on which to build a capacity estimate, and providers compensate with device, behavioural and cashflow signals whose relationship to repayment is empirical rather than causal, and which drift.

## What a Solution Looks Like
Cashflow underwriting as the primary signal rather than a supplement. A consumer who connects a bank account exposes the thing that actually determines repayment — income timing and amount, recurring obligations, balance troughs, overdraft history, and critically the auto-debits of every other instalment plan they hold. Connected-account coverage is the single highest-leverage lever the sector has, because it solves the accumulation problem from the consumer's side without requiring competitors to cooperate. It costs conversion, which is why it is not default, and that tradeoff should be measured rather than assumed.

Accumulation inference from what is already visible. Other providers' auto-debits are identifiable in a connected bank feed by descriptor. Even without a connection, repeated small instalment-shaped debits are inferable from the card's own behaviour where the provider has a relationship. This is estimation rather than observation, and it is far better than the current assumption of zero.

Outcome definition beyond plan repayment. A plan that repaid because the consumer overdrafted is not a success, and the provider can see that in a connected feed. Modelling toward consumer-level outcomes rather than plan-level ones changes what the model learns and is the difference between a risk function and an affordability function.

Shared infrastructure, honestly. A sector-level accumulation signal — a real-time count of concurrent plans without disclosing which provider or what was bought — is technically straightforward, competitively neutral in the way credit bureaus are, and requires collective action nobody has yet organised.

## Impact If Solved
The sector's central risk is invisible to the sector by construction, and every participant's losses and every critic's complaint trace back to the same gap. Cashflow-primary underwriting and inferred accumulation are available to a single provider unilaterally and would materially improve both loss rates and the outcomes of the consumers who are currently being approved into obligations nobody is counting. The alternative is that the number gets established by a regulator, from worse data, with the remedy attached.
