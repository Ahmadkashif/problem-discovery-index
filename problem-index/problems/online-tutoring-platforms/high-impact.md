# Matching and Ranking Decide the Income, and Learning Is Never Measured

**Industry:** [[online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** High Impact
**One-liner:** The platform ranks tutors by rating and rebooking, takes a commission it sets unilaterally, and has no idea which of its tutors actually help students learn.
**Tags:** #hidden-markov-models #bayesian-inference #gradient-boosting #confidence-intervals #causal-inference #evaluation-metrics #worker-facing #transformers

## The Problem
A student or parent searching for a tutor sees a ranked list ordered by some combination of rating, response rate, booking volume, price and platform-determined relevance. Being high in that list is the difference between a full schedule and an empty one, and the ranking's inputs and weights are not disclosed.

The signal underneath it all is rebooking. A student who returns is counted as a success, and rebooking is a reasonable proxy for satisfaction and a poor one for learning. A tutor who is encouraging, patient and does the student's homework with them rebooks extremely well. A tutor who insists on the student doing difficult work independently, which is what produces learning, may rebook less. The platform's ranking rewards the first.

Nothing measures the outcome. Whether the student's grades improved, whether they passed the exam they were preparing for, whether they can now do the thing they could not — none of it is collected, even though families report it readily when asked and it is the entire reason they are paying.

The commission structure compounds the asymmetry. The platform sets the rate, adjusts it unilaterally, and tutors learn about changes when they take effect. Several platforms in this sector have increased commission or restructured tutor pay in ways that materially reduced earnings, and a tutor's only response is to leave — abandoning the student relationships they built, which the platform's terms usually prohibit them from taking with them.

## Why It's Unsolved
Learning is genuinely hard to measure. A student's grade improvement depends on the tutoring, on their school, on their own effort, on their starting point and on regression to the mean — a student is usually referred for tutoring when doing badly, which is the point at which improvement is most likely regardless. Naive before-and-after measurement will flatter every tutor.

The data required is outside the platform. Grades, test scores and teacher assessments belong to the school and the family, and collecting them requires asking, consent and handling minors' educational data — which carries real regulatory obligations and a legitimate reluctance.

The commercial incentive is weak. Rebooking is what the platform monetises, and it is measurable today; learning outcomes are harder, slower, and would likely reduce the ranking of some highly-rated tutors, which is a customer-satisfaction problem. A platform is not obviously better off knowing.

And the relationship lock-in is a deliberate design rather than an oversight. Off-platform prohibition protects the platform's revenue from the disintermediation that would otherwise follow every successful match, and it is the mechanism that leaves tutors with no leverage over commission changes.

## What a Solution Looks Like
Measure what can be measured properly. Self-reported grades and exam outcomes, collected with consent from families who are generally willing to share them, plus platform-administered diagnostic assessments at the start and after a period of tutoring, give a defensible signal — provided the analysis compares against expected trajectories rather than simple before-and-after, since students enter tutoring at their worst.

Model the confound explicitly. Regression to the mean is the dominant statistical artefact here and any measurement that ignores it will produce uniformly positive results that mean nothing. Comparing against matched students and modelling expected improvement from the starting point is the minimum honest approach.

Rank on learning where it is measurable and say so where it is not. A ranking that incorporates outcome evidence, with the evidence's strength stated, is a different product from one ranked on rebooking — and it would reward the tutors whose students actually improve, which is the alignment the market currently lacks.

Make the commission structure transparent and stable. Advance notice of changes, a stated rationale, and a tutor's own earnings history presented clearly, are basic conditions for a working relationship with a contractor workforce whose alternatives are limited by the platform's own terms.

And give tutors their outcome record. A tutor who can show that their students improved has something portable and meaningful, which is both fair and — given the lock-in — the only professional capital the arrangement currently permits them.

## Impact If Solved
This market allocates work by satisfaction and sells learning, and the two diverge in exactly the way that matters. Outcome measurement done honestly — with regression to the mean modelled rather than ignored — would change which tutors get work and reward the preparation and rigour that the current signal penalises. For families it would answer the only question they have. For tutors it would create a professional record in a relationship where they currently accumulate nothing they can keep.
