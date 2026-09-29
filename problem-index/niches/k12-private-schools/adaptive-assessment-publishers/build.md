# Growth Norms Describe the Past and Are Used as Targets

**Niche:** [[niches/k12-private-schools/adaptive-assessment-publishers/profile|Adaptive Assessment Publishers]]
**Industry:** [[industries/k12-private-schools|K-12 Private Schools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Schools set goals against a growth norm that says what students like this did, not what this student could do.
**Tags:** #tabular-ml #gradient-boosting #causal-inference #survival-analysis #evaluation-metrics

## The Problem
The publisher's growth norms are the sector's shared yardstick: given a student's starting score, grade, and subject, how much did comparable students gain over a year. Schools set targets against them, teachers are evaluated partly on them, and a school's account of its own effectiveness rests on them.

They are descriptive. A norm is the average observed gain for a cohort, which makes it a statement about what happened under whatever instruction those students received — including the ineffective instruction. Used as a target, it encodes the status quo as the expectation.

The corpus could answer a far more useful question. With longitudinal records on tens of millions of students, and enormous variation in outcomes among students with identical starting points, the publisher can estimate the distribution of achievable growth rather than its mean — and identify where in that distribution a given student sits and what separates the students who exceeded expectation from those who did not.

## Why Nobody Has Built This
Norms are a measurement product and the organization is a measurement institution. Producing a defensible, representative, well-documented norm is a real technical achievement, and the profession's standards are about representativeness and stability, not about usefulness as a goal.

There is also a firm and correct reluctance to make causal claims. The publisher measures; it does not control what schools do, and asserting that a given practice causes growth is beyond what an observational corpus supports. That caution has been applied too broadly — quantifying the spread of achievable outcomes and identifying student-level factors that predict divergence from the norm requires no causal claim at all.

And the customer asks for norms. Schools want to know how they compare, districts want it for reporting, and nobody has requested something better.

## What to Build
Move from average growth to predicted growth with an honest interval.

**Predict individual growth distributions.** Given starting score, grade, subject, prior growth trajectory, and testing context, what is the full distribution of likely outcomes for this student? A target set at the median of that distribution is a very different instrument from one set at a cohort average.

**Quantify how much of growth is predictable.** A large share of measured growth is measurement error and regression to the mean, and schools routinely act on both as if they were signal. Reporting the predictable component honestly would change how the entire sector reads its own data.

**Separate real movement from statistical artefact at the student level.** A student who scored low in autumn and high in winter has probably regressed to their mean, and the intervention credited with it did nothing. Flagging that is unglamorous and would prevent an enormous amount of misdirected effort.

**Identify divergence, not causes.** Students and schools that consistently exceed their predicted distribution are worth attention, and saying so is a description, not a causal claim. It is also the beginning of any useful research programme in the field.

## Target Customer
Chief Research Officer or VP of Psychometrics at an assessment publisher. The pressure is that assessment is increasingly asked to justify its instructional time, and a product that tells a teacher what this student is likely to do, with uncertainty, is defensible in a way that a cohort average is not.

## Impact If Built
Growth norms shape goal setting, intervention decisions, and teacher evaluation for tens of millions of students. Replacing a descriptive average with a predicted distribution — and stating plainly how much of observed growth is noise — would improve the quality of a very large number of instructional decisions, using data the publisher already holds.
