# Annotator Performance as a Measured Routing System

**Niche:** [[niches/data-analytics-consultants/data-annotation-providers/profile|Data Annotation & Evaluation Providers]]
**Industry:** [[industries/data-analytics-consultants|Data Analytics Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Quality is managed by sampling completed work and removing people who fail, when the far larger gain is routing each task to the annotators whose judgment is demonstrably good on that kind of task.
**Tags:** #gradient-boosting #bayesian-inference #evaluation-metrics #confidence-intervals #probability-distributions #feature-engineering #optimization-fundamentals #cross-validation #data-integration #revenue-impact

## The Problem
As the deliverable shifted from bulk labelling toward expert evaluation, annotator judgment became the product and the quality system did not keep up. Quality is managed with gold-standard tasks, review sampling, and consensus, all of which detect bad work after it is produced. What is not modelled is competence as a graded, task-specific property: an annotator can be excellent on factual verification and weak on nuanced preference judgment, strong in one domain and unreliable in another, and reliable early in a session and degraded late. Routing largely ignores all of it — tasks go to whoever is available and qualified at a coarse level — so the highest-judgment work is distributed without regard to who is actually good at it, and the review layer absorbs the consequences.

## Why Nobody Has Built This
Annotation platforms were built for volume throughput, where interchangeability is the design assumption and quality is a filter. Measuring competence per task type requires enough observations per annotator per type, which the routing system itself prevents by spreading work broadly. Ground truth is also scarce for exactly the judgment tasks that matter most — if the correct answer were known the task would not need a human — so competence has to be inferred from agreement structure and from the subset where review provides an answer. And project-based delivery means annotator history is often reset between programmes rather than carried forward.

## What to Build
A competence model estimating each annotator's reliability by task type, domain, and difficulty, inferred from agreement with peers weighted by their own estimated competence, from review outcomes where available, and from gold tasks embedded naturally in the flow. The model must be honest about uncertainty, since a new annotator's competence is unknown rather than average, and routing should explore deliberately to learn it rather than assuming. Routing then allocates by expected quality per task rather than by availability, sending genuinely ambiguous work to the annotators who handle ambiguity well and straightforward work to those who are fast and accurate on it. Consensus requirements become adaptive — a task where two high-competence annotators agree needs no third opinion, and one where they diverge needs escalation — which is where most of the cost saving lives. And annotator development becomes targeted, because the model says what each person is weak on rather than only whether they passed.

## Target Customer
Heads of quality science and operations at annotation and evaluation providers running workforces in the thousands, and the model teams at client organizations who currently receive judgments with no per-item confidence attached.

## Impact If Built
Improves quality and reduces redundant labour simultaneously, which is rare — adaptive consensus alone changes the unit economics of the highest-value work. It also lets the provider deliver something no competitor offers: per-item confidence on delivered judgments, which is what a model team actually needs to weight the data they are training on.
