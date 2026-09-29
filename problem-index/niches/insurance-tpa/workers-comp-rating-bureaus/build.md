# The Experience Mod Is Individualized and Nobody Measures Whether It Predicts

**Niche:** [[niches/insurance-tpa/workers-comp-rating-bureaus/profile|Workers' Compensation Rating Bureaus]]
**Industry:** [[industries/insurance-tpa|Insurance Third-Party Administrators (TPAs)]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every employer in America gets a personalized risk multiplier computed by a formula fixed decades ago, and the bureau has never asked how well it works.
**Tags:** #gradient-boosting #tabular-ml #evaluation-metrics #causal-inference #hypothesis-testing

## The Problem
The experience modification factor is close to unique in insurance: a published, individualized rating of one employer's loss record that directly multiplies their premium. A mod of 1.35 means paying 35% more than the class rate; below 1.00 means a discount. In construction and many other trades it also gates work, because general contractors and public owners refuse bidders above a threshold.

The formula is a credibility-weighted comparison of the employer's actual losses to their expected losses, with primary and excess loss splits and caps. It is transparent, filed, and structurally the same as it has been for a very long time.

What has never been established is how well it predicts. The bureau holds every policy and every claim at unit level across its states — the data required to ask whether an employer's mod this year actually forecasts their loss ratio next year, whether it predicts equally well for a 12-employee roofer and a 4,000-employee manufacturer, and whether the primary-excess split is set anywhere near optimally. Those are answerable questions on the bureau's own data and they are not asked.

## Why Nobody Has Built This
The mod is a filed rating procedure, approved by regulators, embedded in every carrier's rating system and in thousands of contract requirements. Changing it is a regulatory undertaking, so the institutional answer has always been that the formula is settled.

That answer conflates two things: whether the formula should change, and whether anyone should know how it performs. The second requires no filing and no approval and has never been done.

There is also no owner. Actuarial capacity is consumed by the filing calendar — loss costs for every class in every state, every cycle — and experience rating research is nobody's deliverable.

## What to Build
A standing performance evaluation of the rating plan.

**Measure predictive accuracy directly.** For every employer, does the mod computed from years one to three predict loss experience in year four? Report discrimination and calibration, segmented by employer size, class, and state. Nobody publishes this, and the segmentation is where the finding will be.

**Test the credibility weighting empirically.** Credibility is a function of expected losses, set by formula. The right weighting is an estimation question the bureau's data can answer, and the current answer is a convention.

**Test the primary-excess split.** Splitting each claim so frequency counts more than severity is the plan's central design choice, and the split point is a filed constant. Whether it sits where it maximizes predictive power is measurable.

**Look for systematic bias by employer size.** Small employers' mods swing violently on one claim, which is arithmetically inevitable and may be materially unfair given how the mod is used to gate contract eligibility. Quantifying that is the most consequential single output here.

**Model the claim-reporting response.** Employers manage their mod by managing claims — deductibles, aggressive return-to-work, and sometimes suppression. Where reported frequency responds to the incentive rather than to injury rates, the plan is measuring behaviour as well as risk, and the bureau's data can reveal it.

## Target Customer
Chief Actuary or Chief Data Officer at a workers' compensation rating organization. The pressure is real: large carriers increasingly deviate with their own schedule rating and predictive models, and the advisory plan's authority rests on being demonstrably good rather than merely long-established.

## Impact If Built
This number sets premium and gates contract eligibility for essentially every employer in the country, and its accuracy has never been published. Small employers in particular are rated on a formula that may be far noisier for them than for large ones, with consequences well beyond insurance pricing. Measuring it is the necessary first step, and the bureau is the only party that can.
