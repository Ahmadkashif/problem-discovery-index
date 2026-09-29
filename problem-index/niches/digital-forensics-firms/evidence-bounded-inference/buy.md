# Buy: Missing Data Methods From Statistics

**Niche:** Evidence-Bounded Inference
**Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Statistics has a developed theory of what can be concluded when data is missing, including when the missingness itself is informative, and forensics reasons about gaps in prose.
**Tags:** #bayesian-inference #probability-distributions #confidence-intervals #hypothesis-testing #evaluation-metrics #maximum-likelihood-estimation #expectation-maximization
**Contested on:** Whether, mid-incident, a firm can state what the surviving evidence supports as a calibrated bound rather than as a narrative.

## The Problem

Reasoning under missing data is a developed field. Statistics distinguishes data missing completely at random, missing at random and missing not at random, because the three permit very different conclusions. It has methods for bounding a quantity when the missing portion could take any value — partial identification, where the answer is an interval rather than a point. It has sensitivity analysis for showing how a conclusion depends on assumptions about the missing data. And it has a well-developed understanding of when missingness is itself informative.

Digital forensics faces exactly this problem on every engagement and reasons about it informally. Logs were not retained. The examiner considers what that permits and states a conclusion in prose. Whether the missingness is informative — whether the attacker deleted the logs, which is a very different situation from retention having expired — is discussed and not formalised.

The partial identification framework in particular maps almost exactly onto the scope problem: the quantity of interest is the number of records accessed, the evidence bounds it above and below, and the honest answer is the interval.

## What Already Exists

Missing data theory: the missingness taxonomy, multiple imputation, likelihood-based methods and the extensive literature on when each is appropriate.

Partial identification: bounding a parameter when point identification is impossible, with worked frameworks for exactly the situation where a quantity could lie anywhere in a range consistent with the observed data.

Sensitivity analysis: methods for showing how a conclusion varies with assumptions about the unobserved, standard in epidemiology and increasingly required in causal work.

Bayesian inference: priors and posteriors over quantities of interest, with the machinery for updating on partial evidence and expressing the result as a distribution.

Forensic practice: likelihood ratio frameworks in physical forensics, which are the applied version of the same reasoning.

## The Customization Gap

**The framework is not applied at all.** This is the gap — not that the methods need adapting but that the field has never reached for them. Scope conclusions are prose where an interval with stated assumptions is available.

**Informative missingness is the central case and is unformalised.** Attacker-deleted logs are missing not at random in the strongest sense, and the deletion is itself evidence. Treating it as equivalent to expired retention is a category error the field makes routinely in its informal reasoning.

**Priors are tacit and would be contested.** A Bayesian treatment needs priors on attacker behaviour — how often does an actor with this access exfiltrate — which experienced responders hold implicitly and would argue about explicitly. Making them explicit is uncomfortable and is exactly what would make the reasoning reviewable.

**The audience is legal, not statistical.** An interval with stated assumptions must be usable by counsel making a notification decision, which is a presentation problem and a real one.

**Sparse calibration data.** Statistical methods are strongest where distributions can be estimated. Here the base rates — how often exfiltration follows this kind of access — are not established, which means early work would rest on elicited priors and should say so.

**Litigation prefers point conclusions.** An interval is harder to present in court than a finding, which pushes back toward the narrative form even where the interval is more honest.

## Target Customer

Firms with expert witness practices, where the admissibility standards already favour defensible expression of uncertainty and where a bounded conclusion is easier to defend than an overstated one.

Cyber insurers, whose reserving is a quantitative exercise and who would benefit directly from scope expressed as a distribution rather than as a narrative.

Academic collaboration is the likely route for the initial work, since establishing the priors and the missingness framework properly is research before it is a product.

## Impact If Solved

A mature body of statistical method applies directly to this field's central problem and has never been reached for.

Formalising informative missingness would distinguish the case where an attacker destroyed the evidence from the case where retention expired — a distinction every responder makes intuitively and no report expresses rigorously.

And expressing scope as a bounded interval with stated assumptions is both more honest and more useful to counsel and insurers than a narrative, because it makes explicit what the conservative and the optimistic readings actually are.
