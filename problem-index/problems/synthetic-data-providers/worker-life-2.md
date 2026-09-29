# Privacy Officer Signing Off

**Industry:** [[synthetic-data-providers|Synthetic Data Providers]]
**Type:** Worker Life Changing
**One-liner:** A privacy officer is asked to approve the release of synthetic data on the basis of an epsilon value and a set of attack results, and to accept personal accountability for a guarantee the field itself has not settled.
**Tags:** #bayesian-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #entropy-cross-entropy-kl-divergence #mutual-information #compliance #worker-facing

## The Problem
Before synthetic data leaves an organisation, someone signs. That someone is a privacy officer, a data protection officer or a compliance lead, and their signature carries real personal and organisational exposure.

What they receive is a vendor report. It contains a differential privacy epsilon, possibly a delta, the results of a membership inference attack, a nearest-neighbour distance analysis, and a statement that the data contains no real records.

Interpreting that requires understanding what epsilon bounds, under what adversary model, with what auxiliary information assumed — questions on which the research community itself does not fully agree, and on which the practical guidance is genuinely thin. The officer is not a cryptographer. They are being asked to convert a technical artefact into a regulatory judgement about whether the output is personal data under GDPR, HIPAA or state privacy law, when regulators have not clearly answered that question either.

So the decision gets made on institutional comfort. Has anyone else done this. Does the vendor have other customers in our sector. Would this survive an audit. None of which is a privacy analysis.

## Why It Matters to the Worker
This is accountability without the means to exercise it. The officer carries the consequence of a wrong call — regulatory action, breach notification, personal exposure in some regimes — and the information available does not support the judgement they are being asked to make.

The asymmetry is uncomfortable. The vendor has every incentive to present the strongest reading, the internal team wants the project approved, and the officer is the only party whose role is to say no, with a technical basis they cannot fully evaluate.

The regulatory ambiguity makes it worse rather than easier. If synthetic data were clearly outside the scope of privacy law, the decision would be simple. Because its status is contested, the officer is making a bet on how a regulator will eventually interpret it, years from now, possibly after an incident.

Many officers respond by refusing or by imposing conditions that destroy the utility, which is a rational response to being asked to guarantee something nobody can guarantee, and it is a significant brake on adoption.

## What a Solution Looks Like
Reports written for the decision being made rather than for a machine learning audience. What was assumed about the adversary, what auxiliary information they were assumed to hold, what the empirical attack results mean in plain terms, and — critically — what the report does not establish.

Record-level risk rather than a dataset-level score. An officer can act on "these two hundred synthetic records sit unusually close to real outliers and have been suppressed" in a way they cannot act on an epsilon.

Comparison against alternatives. The relevant question is rarely whether synthetic data is perfectly safe but whether it is safer than the redaction or aggregation the organisation would otherwise use, and that comparison is computable and never presented.

An independent evaluation option. A privacy assessment produced by someone other than the vendor selling the data would change the nature of the sign-off entirely, and no such service currently exists at scale.

## Impact If Solved
Privacy sign-off is the binding constraint on synthetic data adoption in exactly the sectors where it would do most good. Giving officers evidence calibrated to their decision, rather than to a research paper, is what would let them approve confidently or refuse for good reasons — and either is better than deciding on institutional comfort.
