# Enrolment Is the Product and Learning Is Unmeasured

**Industry:** [[online-course-platforms|Online Course Platforms]]
**Type:** High Impact
**One-liner:** The platform records every pause, rewind and quiz attempt of millions of learners and cannot say whether any of them can now do the thing the course was about.
**Tags:** #bayesian-inference #hidden-markov-models #survival-analysis #gradient-boosting #confidence-intervals #evaluation-metrics #transformers #tacit-knowledge-ml

## The Problem
A learner enrols, watches some videos, attempts a few quizzes, and either finishes or does not. The platform records all of it. What it reports is progress — percentage of material viewed — and at the end issues a certificate for having viewed it.

Nothing in that chain measures capability. Multiple choice quizzes at the end of a section test recognition shortly after exposure, which is the weakest possible evidence of durable learning and is well understood to be so in the education research literature. Projects, where they exist, are self-assessed or peer-reviewed by other learners with no calibration. The certificate therefore certifies attendance, which employers have worked out, which is why these credentials carry limited weight in hiring.

The consequence for the learner is that they cannot tell whether they learned. They watched the course, they felt they understood it, and the feeling of understanding while watching a clear explanation is famously unreliable — it is the well-documented fluency illusion, and video delivery maximises it. Months later they attempt the task and discover the gap.

The consequence for the platform is that it has no signal to improve on. It knows which courses get enrolled in and rated highly; it does not know which produce competence, so its recommendations, its rankings and its instructional design guidance all optimise satisfaction. A course that feels great and teaches little outranks one that is difficult and works.

And the sector-wide numbers make the problem impossible to dismiss. Completion in the single digits on open courses is not a marketing problem; it is the product telling everyone something about itself for a decade, unanswered.

## Why It's Unsolved
Measuring learning properly costs the learner effort, and effort reduces the metrics the business runs on. Retrieval practice, spaced review and genuinely difficult assessment produce better learning and worse completion rates, lower satisfaction scores and more refund requests. Every incentive in a consumer education marketplace points away from them. This is not a technical barrier; it is a direct conflict between what works and what sells, and the category has resolved it the same way every time.

Grading real work is the second barrier. Assessment that demonstrates capability means open-ended work — code, a design, an analysis, a piece of writing — which is expensive to evaluate. Peer review was the scalable answer and is unreliable. This is the constraint that has genuinely shifted, since evaluating open-ended work against a rubric is now substantially automatable, and the category has mostly deployed that capability as a chatbot that answers questions rather than as an assessor.

The outcome data is the third. Whether someone got the job, passed the certification, or shipped the project happens outside the platform. Some learners report it; the reporting is self-selected and sparse. Nobody has built the follow-up loop, partly because it is awkward and partly because the answer might be unflattering.

And there is a measurement-theory difficulty that is real. Learning is latent, assessments are noisy, and estimating what a learner knows from sparse interaction data requires a model rather than an average — a well-studied problem with decades of literature that consumer platforms have largely ignored in favour of progress bars.

## What a Solution Looks Like
Estimate the learner's state rather than their progress. Knowledge tracing — modelling mastery of specific skills as a latent state updated by each interaction — is a mature problem with established approaches, and the interaction data these platforms hold is far richer than what the research literature was developed on. Replacing the progress bar with a per-skill mastery estimate, with uncertainty, changes what the product is.

Assess with open-ended work, graded automatically against a rubric, with the reasoning shown. This is the capability that recently became feasible and it is the one that matters most: a learner who submits work and receives specific, evidenced feedback is in a fundamentally different relationship with the material than one who ticks a box. Calibration against expert graders is the requirement that makes it trustworthy, and it must be measured and published, not assumed.

Build in retrieval and spacing deliberately, and measure the trade. Courses designed around recall and spaced review will show worse completion and better capability, and a platform willing to run that experiment honestly — and to report both numbers — would produce the first real evidence in the category.

Close the outcome loop. Follow-up at three and six months, asking whether the skill was used and what happened, is unglamorous, achievable, and would give the platform the first genuine outcome signal it has ever had. Even a self-selected sample, honestly labelled, beats nothing.

## Impact If Solved
The category's core asset — recorded explanation — is being commoditised by tools that explain on demand, for free, interactively. What survives is assessment, practice and a credential somebody trusts, and none of those exist in credible form today. A platform that can say with evidence that a learner has reached a level of capability holds something a video library cannot replicate, and the data required to build it has been accumulating, unused, for fifteen years.
