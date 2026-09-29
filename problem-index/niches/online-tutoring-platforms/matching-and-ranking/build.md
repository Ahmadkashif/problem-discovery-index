# Build: Compatibility-Aware Matching

**Niche:** [[niches/online-tutoring-platforms/matching-and-ranking/profile|Matching & Tutor Ranking]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Model which tutors work well with which kinds of student, rather than which tutors are generally popular, and rank on the interaction.
**Tags:** #matrix-decompositions #gradient-boosting #bayesian-inference #confidence-intervals #evaluation-metrics #k-nearest-neighbors #revenue-impact #tacit-knowledge-ml
**Contested on:** Whether tutor-student compatibility is learnable from the platform's own repeat-engagement record.

## The Problem

Ranking treats tutor quality as a scalar. A tutor is good or less good, and the list is sorted accordingly. That model is wrong about the thing being matched.

Tutoring effectiveness is substantially interactional. The tutor who is patient and warm is right for the student who has given up and wrong for the one who needs pushing. The tutor whose strength is drilling exam technique is wrong for a conceptual gap. The tutor who works well with a fourteen-year-old boy who will not talk is a specific skill, not a general one. Families know this — it is why the first question in every parent forum is about fit rather than quality — and the platform has no representation of it.

The consequence is that first matches fail more often than they should, and a failed first match is the largest churn event in this business: a family who tries tutoring, has a poor experience, and concludes tutoring does not work.

## Why Nobody Has Built This

Interaction effects need more data than main effects, and the platform's per-student data is thin — a student may take six sessions. The signal exists in the aggregate, though: tens of thousands of tutor-student pairs with observable outcomes, where the same tutors recur with many students and student characteristics recur across tutors. That is exactly the structure collaborative filtering was built for and nobody has applied it here.

Student characterisation is also missing. Matching is done on subject and level, and the attributes that would drive compatibility — confidence, the specific misconception, learning preference, how far behind, what has been tried — are not collected, because the intake form was designed to get to checkout quickly.

And the objective is wrong upstream. A ranker optimised for first-session conversion has no reason to prefer a better fit, since a worse fit converts equally well at booking time and fails later.

## What to Build

An interaction model over the platform's repeat-engagement record, fed by a real intake.

**Characterise the student properly at intake.** Not just subject and level, but goal, current grade, what specifically is hard, what has been tried, confidence, and preference for pace and style. A well-designed intake of eight questions is a large improvement over the current three, and this is the input the whole model depends on. Some of it can also be inferred later from session behaviour and tutor notes.

**Learn compatibility as an interaction.** A latent-factor model over tutor-student pairs with observed outcomes — continued engagement, session count, satisfaction and, where available, measured gain — with student and tutor attributes as side information to handle the cold start. The useful output is a predicted fit for this pair rather than a general score for this tutor.

**Choose the right target.** Not first-session booking. Sustained engagement past a threshold, or measured gain where available, or at minimum the third session — which is when a family has decided the match works. Retraining the ranker on this target alone, with no interaction modelling, is likely to be a meaningful improvement and is the cheapest step.

**Handle new tutors with an informative prior.** A new tutor's compatibility profile can be initialised from their stated approach, subject specialisms, their own education, and the in-session instructional measures from their first few sessions. Combined with a bounded exploration allocation, this gives them a route to their first students that does not run through underpricing.

**Explain the match.** Families respond to a reason — this tutor works well with students who have lost confidence in maths — and the reason is both a conversion feature and an honest description of what the model believes. It also lets the family correct the model when it is wrong about their child.

## Target Customer

Platform marketplace leadership, where the business case is first-match retention, which is measurable now and is the largest single churn driver. Also the premium and district segments, where human matching is currently used precisely because the automated version does not do this.

## Impact If Built

First matches succeed more often, which addresses the most expensive failure in this business — a family who tries tutoring once and concludes it does not work for their child. The ranking starts optimising a relationship rather than a transaction. And new tutors get a path to their first students that runs on fit rather than on price.
