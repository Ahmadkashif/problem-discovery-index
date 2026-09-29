# Build: Causal Attribution of Learning Gains to Tutors

**Niche:** [[niches/online-tutoring-platforms/learning-gain-attribution/profile|Learning Gain Attribution]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Acquire outcome evidence from outside the platform and attribute the gain to the tutor, with the selection and the counterfactual handled honestly.
**Tags:** #causal-inference #bayesian-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #survival-analysis #compliance #data-integration
**Contested on:** Whether an individual tutor's contribution can be separated from the student's trajectory, the school's teaching and the family's engagement.

## The Problem

Families buy tutoring to produce a result and nobody tells them whether it did. Districts buy it with public money and can usually say only that the programme as a whole was associated with some gain. Neither can say whether the particular tutor delivered anything.

The attribution problem is genuinely hard and is routinely underestimated. Students who receive tutoring differ from those who do not. Students who receive more tutoring are often those who were struggling most, or those whose families are most engaged, and these pull in opposite directions. Improvement over a semester happens for many reasons. And the tutor's contribution is a small share of a student's total instruction.

That difficulty is real. It is also not a reason to measure nothing, which is the current state of the consumer segment.

## Why Nobody Has Built This

The outcome data is outside the platform. Acquiring it means persuading families to share grades and test scores, or contracting with districts who hold them — a relationship and consent problem that platform product teams are not staffed to solve and that has no obvious owner.

The causal work then requires real methodological care, and doing it badly is worse than not doing it, because a naive comparison will show that tutored students underperform — since they were behind to begin with — and produce a headline nobody can use.

And the result is dangerous to the marketplace. Attribution at the tutor level means some named tutors are found to produce nothing measurable. Acting on that means removing or downranking people who are well-rated and well-liked; not acting on it means holding the finding while continuing to charge for their sessions. Both are uncomfortable, and not measuring avoids the choice.

## What to Build

An outcome evidence pipeline and an attribution model, with the design honest about what it can and cannot claim.

**Acquire the outcome data.** Three routes, in decreasing order of quality. District contracts, where assessment data is available under agreement and the population is defined — this is the anchor and should be pursued first. Family-shared evidence, where a parent uploads a report card or score report in exchange for a progress report that is worth having, which is a fair exchange and gets meaningful uptake when the report is genuinely useful. And platform-administered diagnostics at intake and intervals, which are weaker as external evidence but fully controlled and consistent.

**Handle selection explicitly.** Students choosing tutoring are not random. Where possible, exploit variation that is close to random — waitlist timing, tutor availability, a district's rollout order, a session cancelled for scheduling reasons. Where not, model the selection with the covariates available and state the assumption plainly. Difference-in-differences against a student's own prior trajectory is the workhorse here and is considerably better than a cross-sectional comparison.

**Attribute hierarchically with heavy shrinkage.** A tutor with eleven students over a year has a gain estimate with an enormous interval, and presenting it as a number is misleading. The model should produce a posterior that is mostly prior for most tutors and separates only the clearly strong and clearly weak. Being honest about this is what makes the output usable rather than litigable.

**Calibrate the cheap signals against it.** The most valuable output may not be the tutor estimates themselves but the answer to which observable proxies — rebooking, in-session instructional measures, session frequency, tutor experience — predict measured gain. Those proxies can then be computed for every tutor, continuously, without outcome data. This is the route by which a small outcome-labelled sample improves the entire marketplace.

**Decide in advance what a finding triggers.** Before running it, agree what happens if a tutor's estimate is clearly poor: coaching first, matching de-weighting second, and disclosure to families only under a stated standard of evidence. Deciding this afterwards, case by case, under pressure, is how the whole programme gets shut down.

## Target Customer

Districts and schools procuring tutoring, who increasingly must demonstrate impact on public spending and for whom this is a purchasing requirement. Platforms selling into that market, for whom it is a competitive necessity. And, eventually, families — though consumer demand for outcome evidence in this market has historically been weaker than one would expect.

## Impact If Built

The industry acquires, for the first time, evidence about whether individual tutoring works and for whom. Districts can buy on demonstrated impact rather than on price and availability. And the cheap in-session and behavioural proxies get calibrated against real learning, which is what lets the whole marketplace be pointed at outcomes instead of satisfaction.
