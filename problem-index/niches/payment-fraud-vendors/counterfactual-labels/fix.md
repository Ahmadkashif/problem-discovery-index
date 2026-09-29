# The Experiment Nobody Will Fund

**Niche:** [[niches/payment-fraud-vendors/counterfactual-labels/profile|Counterfactual Label Acquisition]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The data science team has proposed the randomised holdout three times and it has been declined three times on cost.
**Tags:** #quick-win #evaluation-metrics #confidence-intervals #descriptive-statistics #revenue-impact #hypothesis-testing #compliance #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to obtain honest outcomes for the transactions the model declines — and whoever pays the visible short-term cost of that experiment first can say something about its own accuracy that no competitor can contradict or match.

## The Problem
Inside most fraud vendors and large merchants, someone has already proposed this. The proposal describes approving a small random sample of declines to measure false positives. It is rejected because it will cost money and because approving known-bad transactions sounds indefensible in a meeting. The proposal is never costed properly, the sample size is never computed, and the value of the information is never quantified — so the decision is made on the word "fraud" rather than on the numbers.

## Why It's Still Broken
The proposal arrives as a technical request rather than as an investment case, so it is evaluated on its cost alone — a request with a quantified cost and an unquantified benefit will always lose. Nobody computes the required sample size, so the cost sounds larger than it is. The downside is emotionally vivid and the upside is statistical. And no peer has done it, which makes it feel reckless rather than overdue.

## What a Fix Looks Like
Make the investment case properly. Compute the required sample size and the actual expected cost, which is the fix and will usually show a number far smaller than the room assumed. Quantify the value of the information — what a one percent threshold improvement is worth across the book — since that is the other side of the ledger and is currently blank. Bound the exposure by capping transaction value and excluding the highest-risk bands, because a bounded downside is approvable where an open one is not. Start with one merchant who wants the answer, as a willing participant removes the internal objection entirely. Run it on low-value transactions first, since the cost per label is lowest there and the statistical lesson transfers. Present it as measurement rather than as approving fraud, because the framing is most of the objection. Log propensities from today regardless, as it costs nothing and enables everything later. Report the result whatever it shows, which is what makes the exercise credible. Compare against the known industry estimates of false decline cost, so the asymmetry is visible. And bring the merchant into the decision, since it is their revenue on both sides.

## Who Feels the Pain
Data scientists who know the answer and cannot get the data; merchants whose lost revenue is unmeasured; risk leaders defending numbers they cannot verify; and an industry that has known its central defect for a decade.

## Impact If Fixed
A request with a quantified cost and an unquantified benefit will always lose, so the proposal keeps being rejected on the cost alone. Computing the sample size, bounding the exposure and valuing the information turns a rejected request into an obvious investment.
