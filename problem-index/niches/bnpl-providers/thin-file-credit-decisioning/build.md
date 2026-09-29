# Judging Capacity Without a File

**Niche:** [[niches/bnpl-providers/thin-file-credit-decisioning/profile|Thin-File Credit Decisioning]]
**Industry:** [[industries/bnpl-providers|BNPL Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The bureau has nothing to say about a large share of applicants, and the provider must decide anyway from a device, a basket and a few hundred milliseconds of behaviour.
**Tags:** #gradient-boosting #logistic-regression #survival-analysis #confidence-intervals #evaluation-metrics #feature-engineering #causal-inference #compliance
**Contested on:** Every serious competitor in this niche is fighting to infer capacity from device, behaviour, basket and their own history when the bureau has nothing to say — and whoever does that best approves the people competitors decline and still gets repaid.

## The Problem
The applicant has no credit history worth the name. What exists is a device with an age and a history, an email address of some vintage, a basket with a value and a category, a merchant with its own customer profile, the time of day, how the person moved through the checkout, and whether this provider has seen them before. Each of those carries information about capacity and willingness. Most providers use a subset, weighted by a model built once, validated on the population it approved, and rarely revisited against a six-week outcome that arrives faster than in any other consumer credit product.

## Why Nobody Has Built This
The sector grew fast and the decisioning stack was built to be fast rather than to be right, because latency was the visible constraint and accuracy was not measurable in the first years — the engineering problem was solved and the credit problem inherited its shape. Alternative data features are easy to add and hard to validate, so they accumulate without evidence. Reject inference is standard practice in credit and unusual here. And the outcome loop's speed, which is the sector's great advantage, is not used for continuous model improvement.

## What to Build
Exploit the evidence and the fast loop. Engineer features from the whole checkout interaction rather than from a handful of identity signals, since how a person completes a purchase carries information and most providers capture a fraction of it. Use the provider's own repeat history properly, because a returning customer's repayment record is the strongest available signal and is frequently used as a simple flag rather than as a model. Perform reject inference, since the model is trained on the approved population and the declined population is where growth is — this is standard credit practice and its absence here is the fix note's subject. Validate continuously against the six-week outcome, which is feasible here and is impossible in conventional credit, and turn that advantage into a faster improvement cycle than anyone else can run. Model the payment schedule rather than a single default event, since missing the third of four payments is a different outcome from never paying and the product's structure gives a richer target. Predict affordability separately from willingness, because they have different signals and different remedies. Handle fairness deliberately, since alternative data features can encode protected characteristics indirectly and the sector's regulatory scrutiny is increasing. Measure the declined-but-good population explicitly, by approving a sample near the threshold. Segment by merchant and category, since the same consumer is a different risk buying different things. And report the model's accuracy at the six-week horizon continuously, because a sector with this feedback speed should be improving visibly and mostly is not.

## Target Customer
Credit risk and data science leadership at instalment providers, the alternative data vendors serving them, and the consumers whose thin file is currently read as absence of creditworthiness.

## Impact If Built
Latency was the visible constraint and accuracy was not measurable early, so the credit problem inherited the engineering problem's shape. A six-week outcome loop permits a faster improvement cycle than any other consumer credit product and the sector does not use it.
