# Buy: Benchmark Governance From Machine Learning and Testing

**Niche:** Performance Evaluation & Benchmarking
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Machine learning built shared benchmarks that drove a decade of progress, and standardised testing built the governance that keeps a benchmark honest, and trust and safety has neither.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #descriptive-statistics #data-integration
**Contested on:** Whether two products can be compared at all.

## The Problem

Shared benchmarks are how machine learning made progress measurable. A held-out test set, a common metric, a public leaderboard and a submission protocol turned subjective claims into comparable results, and the effect on the rate of improvement in several fields is well documented.

The governance that keeps a benchmark meaningful is equally well understood. Held-out test data prevents training on the evaluation. Submission-based evaluation prevents the test set leaking. Periodic refresh addresses overfitting to a static set. Disaggregated reporting prevents an aggregate concealing failure modes. And a custodian with no stake in the results is what makes the whole thing trustworthy.

Standardised testing — educational and professional examination — contributes the other half: secure item banks, controlled administration, equating across forms, and the institutional structures that prevent a test's integrity being compromised by the parties it measures.

Trust and safety has no benchmark and therefore no governance question to answer, which is the wrong end of the problem to be at.

## What Already Exists

Machine learning benchmarks: the established pattern of held-out test sets, leaderboards and submission protocols, with a well-documented effect on measurable progress and a well-documented set of failure modes.

Benchmark governance: submission-based evaluation, periodic refresh, and the substantial literature on benchmark overfitting and what to do about it.

Standardised testing: secure item banks, controlled administration, and the institutional apparatus that protects a test's integrity.

Restricted-data evaluation: the models used in medical and genomic research for evaluating against data that cannot leave its custodian, which is directly relevant to the categories here that cannot be held generally.

Trust and safety: vendor self-reported figures.

## The Customization Gap

**The data cannot always move, which is the distinguishing constraint.** Medical research solved evaluation against data that cannot leave its holder — federated evaluation and analysis conducted inside the custodian — and this is the model the restricted categories here require.

**Policy dependence has no analogue.** A benchmark for image classification has an objective label. Whether content violates a harassment policy depends on the policy, which means the benchmark must evaluate against stated policies rather than a universal ground truth.

**The custodian must be credible to adversaries.** Machine learning benchmarks are held by research institutions that participants accept. Here the participants would rather not be measured, which raises the bar on the custodian's independence.

**Labelling cost is high and the labelling is harmful.** Producing a labelled test set in these categories means people looking at the material, which is the annotation problem and makes the benchmark expensive in a way no image benchmark is.

**Refresh matters more.** Harms evolve, so a static benchmark decays faster here than in a stable domain, which makes the institution's ongoing funding the binding question.

**Participation must be compelled.** Machine learning benchmark participation is voluntary because researchers want the comparison. Commercial vendors leading on unverifiable claims do not, which means buyers or regulators must require it.

## Target Customer

Research institutions and standards bodies, as custodians — the role is established in machine learning and the credibility requirement is the same.

Existing lawful custodians of restricted material, who are the only bodies that can host evaluation in the categories where the data cannot move, and whose participation would unlock the hardest part.

Large platform buyers and regulators, who are the parties able to make participation a requirement, which is the difference between this benchmark existing and not.

## Impact If Solved

The benchmark pattern that made progress measurable in machine learning applies directly, and its governance questions are already answered.

Federated evaluation inside an existing custodian is the established answer for data that cannot move, and it is what makes the legally restricted categories addressable rather than permanently excluded.

And requiring participation is the element with no precedent in voluntary research benchmarking — it must come from buyers or regulators, and it is the difference between a benchmark that measures the willing and one that measures the market.
