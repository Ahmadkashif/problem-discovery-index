# The Declines Nobody Ever Grades

**Industry:** [[payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** High Impact
**One-liner:** Fraud models are trained and evaluated on chargebacks, which only exist for approved transactions, so the decisions the model is least certain about are the ones it never receives a label for.
**Tags:** #logistic-regression #gradient-boosting #causal-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #feature-engineering #revenue-impact

## The Problem
A transaction is scored and declined. Nothing further happens. The customer either abandons, retries with a different card, buys from a competitor, or was in fact a fraudster who moves on. None of those outcomes returns to the vendor as a label.

Approved transactions do generate labels. If a chargeback arrives in the following weeks, the transaction was fraud, or at least was disputed as such. If none arrives, it is treated as legitimate. Models are trained on this.

The consequence is textbook and consequential. The training set consists entirely of transactions the current system chose to approve, which means the model learns the fraud patterns visible among approvals and is blind to whatever it has been successfully filtering. Over time this narrows: the model becomes confident about a region of the space it sees and increasingly uninformed about the region it declines. Thresholds drift on evidence that cannot speak to them.

Meanwhile false declines are the larger commercial harm and are essentially unmeasured. Industry estimates place their value well above actual fraud losses in card-not-present commerce, and those estimates are derived from surveys and modelling rather than from measurement, because nobody is measuring. A merchant sees approval rate and chargeback rate; the number that matters — how many good customers were turned away — appears in neither.

The label itself is unreliable even where it exists. A chargeback may be fraud, or a customer who did not recognise a descriptor, or a dispute about delivery, or first-party misuse where the cardholder did authorise the purchase and later denied it. These have different causes and different remedies, and the model receives them as one binary.

And the incentive alignment is subtle. A chargeback guarantee provider bears the fraud loss and therefore has a genuine incentive to approve, which is better than a pure scoring vendor. But it does not bear the cost of a declined good customer's lifetime value, so its optimum and the merchant's are close rather than identical.

## Why It's Unsolved
The fix is experimental and the experiment costs money visibly. Approving a randomised sample of transactions the model would decline produces unbiased labels exactly where they are missing. It also approves some fraud, and that loss lands in a specific month on a specific line, while the bias it corrects is invisible and diffuse. No product manager is rewarded for the trade.

Merchants resist randomisation on revenue-bearing traffic even when the expected value is positive, because the downside is concrete and attributable and the upside is statistical.

Attribution is genuinely hard. A declined customer who buys elsewhere leaves no trace with the merchant, so even measuring the cost of a decline requires either a holdout or a cross-merchant network view that vendors have and rarely apply to this question.

And there is a competitive incentive not to know. A vendor that measured its own false decline rate would hold a number no competitor publishes, which is an advantage only if the number is good. Most of the industry has chosen not to find out.

## What a Solution Looks Like
A permanent randomised approval allowance in the decline region. A small fraction of transactions the model would decline, approved deliberately, produces unbiased outcome data in the region where the model is weakest. Concentrated near the decision boundary and stratified by score band, the cost is modest and bounded, and the information gain is the only source of truth available about the half of the decision surface currently unobserved.

Propensity correction for everything else. Where randomisation is not permitted, the selection mechanism is at least known — the scoring model is the propensity function — and inverse weighting or doubly robust estimation gives a defensible correction rather than pretending the sample is random.

False decline measurement as a first-class metric, reported to merchants alongside approval and chargeback rate. Even an estimate with an interval is infinitely more useful than the current silence.

Chargeback reason disaggregation. True fraud, friendly fraud, descriptor confusion and delivery disputes have different signals and different remedies, and collapsing them into one label costs real accuracy.

Lifetime value in the objective. The cost of declining a customer is not the order margin; it is the margin on every future order they will now place elsewhere, and merchants can supply that number where vendors ask for it. Almost none do.

## Impact If Solved
This is the defining measurement failure of a multi-billion dollar category, and the correction is a bounded experiment rather than a research programme. A vendor that runs a continuous randomised allowance obtains the only unbiased estimate of decline accuracy in the industry, can state its false decline rate with evidence, and gains a model that is no longer trained exclusively on the population it selected — a combination no competitor can match without making the same visible trade.
