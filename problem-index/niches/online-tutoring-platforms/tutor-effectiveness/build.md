# Build: An Effectiveness Signal the Marketplace Can Use

**Niche:** [[niches/online-tutoring-platforms/tutor-effectiveness/profile|Tutor Effectiveness & Learning Measurement]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Produce a tutor effectiveness estimate the matching system can consume, combining what happens in sessions with whatever outcome evidence the platform can actually obtain.
**Tags:** #bayesian-inference #causal-inference #large-language-models #confidence-intervals #evaluation-metrics #hypothesis-testing #transformers #revenue-impact
**Contested on:** Whether an effectiveness estimate can be made reliable enough to rank tutors on without being unfair to them.

## The Problem

Every mechanism in a tutoring marketplace consumes a quality signal, and the only signal available is satisfaction. Rebooking rate, star rating and complaint count are what the ranker sees, what the tier system uses, and what determines a tutor's income.

Satisfaction and effectiveness are correlated and far from identical. A tutor who is warm, encouraging and does most of the work for the student produces a pleasant session, a happy student, a five-star rating and a rebooking — and less learning than a tutor who makes the student struggle productively, which is uncomfortable in the moment and is what the research on learning consistently supports. The platform's data cannot tell them apart, so it rewards the first.

The consequence compounds: tutors learn what the system rewards. Preparation, diagnosis and productive difficulty cost the tutor time and rating, and the market selects against them.

## Why Nobody Has Built This

Measuring learning is genuinely harder than measuring rebooking, and that is the honest core of it. The outcome data lives with schools. The horizon is months. Attribution requires a counterfactual. Students who get tutoring differ systematically from those who do not, and students who get more tutoring are often those who are struggling more.

Underneath the difficulty sits a commercial reason that keeps it hard. A platform that measured effectiveness would learn that some of its most popular tutors are ineffective, and would then have to decide what to do about it — downrank them, and the parents who love them complain; disclose it, and the marketplace's central claim weakens. Rebooking, by contrast, is a metric where the platform's interest and the measurement agree perfectly.

## What to Build

An effectiveness estimate built from the evidence actually available, with uncertainty carried explicitly and used as a prior rather than a verdict.

**Analyse the sessions.** Transcribe and analyse recordings for the features the teaching research associates with learning: student talk ratio, question-before-explanation ordering, wait time after questions, whether errors are diagnosed or merely corrected, whether the tutor hands the work back rather than completing it, whether prior material is revisited. These are observable, they are gradeable, and they give a per-session instructional quality score computable at scale.

**Obtain outcome evidence where it exists.** Platform-administered assessments at intake and at intervals. School grades where families share them. Test score improvements where the tutoring is district-contracted, which is the segment where outcome data is contractually available and is the right place to anchor the whole model. Even a modest outcome-labelled subset is enough to calibrate the in-session score against — which is the key move, because it turns an unvalidated pedagogy score into a predictor of something real.

**Model it hierarchically with the student's situation controlled.** A tutor's effectiveness estimate must account for the students they teach — starting level, subject, frequency, age, how far behind they were. Without that, the tutors who take the hardest students score worst, which is both wrong and precisely the group a marketplace should not punish. Hierarchical modelling with student-level covariates is the standard tool and the estimate should carry a wide interval for anyone with few students.

**Use it as a prior, not a score.** Feed it into matching as one input alongside fit and availability, rather than publishing a public effectiveness rating. A published number invites gaming, misinterpretation and legal challenge; a matching input improves outcomes quietly and is far more likely to survive internal review.

**Validate honestly.** The test is whether tutors the model ranks highly produce better measured outcomes on the labelled subset, out of sample. Report it with intervals. An effectiveness measure that has not been validated against real learning is a pedagogy opinion dressed as data.

## Target Customer

Platforms selling into schools and districts, where outcome data is available, effectiveness is contractually expected, and the measurement is a competitive requirement rather than a virtue. That segment funds the model, and the consumer marketplace inherits it.

## Impact If Built

The marketplace acquires a signal that points at the thing families are buying. Matching improves toward learning instead of toward satisfaction. Preparation and diagnosis stop being unrewarded, because the measurement can finally see them. And the platform can make a claim about outcomes that is supported rather than implied.
