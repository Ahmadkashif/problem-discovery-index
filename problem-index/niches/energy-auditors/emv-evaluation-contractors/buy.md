# Billing Analysis Adapted to Programme Attribution

**Niche:** [[niches/energy-auditors/emv-evaluation-contractors/profile|Efficiency Programme Evaluation Contractors]]
**Industry:** [[industries/energy-auditors|Energy Auditors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Statistical packages estimate treatment effects competently; the hard part is that the treatment group self-selected, the comparison group is contaminated by the same programme, and the regulator will litigate whichever choice is made.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #gradient-boosting #time-series-forecasting #evaluation-metrics #cross-validation #feature-engineering #automation #compliance

## The Problem
The core analysis is estimating how much energy a programme caused participants to save, from billing data, when participation is voluntary. Participants differ systematically from non-participants, weather varies, and the obvious comparison group frequently contains people who took the same measures without the rebate. Evaluators handle this with matched comparison designs, billing regression, and net-to-gross surveys, each requiring dozens of specification choices — matching variables, weather normalization approach, outlier handling, model form — that materially move the answer and are made afresh in each study by whoever is assigned.

## What Already Exists
The statistical toolkit is complete and free. R and Python cover every estimator involved; the causal inference libraries handle matching, weighting, and difference-in-differences with good diagnostics; open-source weather normalization implementations are standard in the field and widely used.

## The Customization Gap
What is missing is not method but discipline and domain structure. No available tooling encodes the specific analytical shape of this work — programme participation as the treatment, weather normalization as a required pre-step with its own conventions, self-selection as the central threat, and a regulator as the audience who will examine the specification. The adaptation is an evaluation-specific analysis framework where the pipeline is a first-class object: matching and specification choices declared before the analysis rather than selected after seeing results, sensitivity across the reasonable specification space computed and reported by default rather than on request, and every study emitting a reproducible record that can be re-executed by an intervenor. Comparison group construction should draw on the pooled archive to identify contamination risk that a single study's data cannot reveal. And because the regulator is the audience, the output has to be a defensible narrative with the specification decisions visible, not a coefficient table.

## Target Customer
Methodology leads and practice principals at evaluation firms, and the commission staff who receive these studies and currently have no efficient way to test whether a different reasonable specification would have produced a different answer.

## Impact If Solved
Makes the most contested part of the work defensible by construction. Reporting specification sensitivity by default also pre-empts the most common intervenor challenge, which is that the evaluator chose the specification that suited the client.
