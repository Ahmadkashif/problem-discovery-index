# Test Coverage and Assurance Case Practice

**Niche:** [[niches/ai-red-teaming-firms/coverage-measurement/profile|Coverage Measurement]]
**Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Safety-critical engineering built assurance cases to argue that a system is acceptably safe with the evidence and its limits stated, and AI assessments produce a findings list.
**Tags:** #compliance #evaluation-metrics #confidence-intervals #hypothesis-testing #graph-theory #descriptive-statistics #monte-carlo-methods #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to say what fraction of a system's risk surface an assessment examined — and whoever does that takes the market, because without it a clean report is an assertion and with it it is evidence.

## The Problem
Arguing that a system is acceptably safe, when exhaustive testing is impossible, is the founding problem of safety-critical engineering. The answer is an assurance case: a structured argument connecting claims to evidence, with assumptions and gaps stated explicitly, reviewed by a party who did not build it. Aviation, rail, medical devices and nuclear all run on this. AI assessment produces a list of findings and a conclusion, with the argument connecting them left implicit.

## What Already Exists
Structured assurance and safety case notations with claims, arguments and evidence; hazard analysis methods including systematic identification techniques; test coverage criteria for cases where exhaustive testing is impossible; independent safety assessment as an institutional role; and the practice of stating assumptions and residual risk explicitly.

## The Customization Gap
The adaptation is to a system whose hazards are behavioural and whose adversary is adaptive. It requires: (1) hazard identification adapted to model behaviour, where the systematic techniques from process safety supply the discipline and the hazard vocabulary has to be rebuilt — this is where the domain taxonomy work connects; (2) evidence that is statistical rather than deductive, since the argument cannot be that a failure is impossible but that it was sought competently and not found, which is a weaker and still valuable claim the assurance case notation can express and a findings list cannot; (3) an adaptive adversary in the argument, which safety cases do not model and security assurance does, making the useful form a hybrid of both traditions; (4) explicit residual risk and assumptions, which is standard practice in assurance cases and absent here, and which is the single most transferable element; and (5) independent review of the argument rather than only of the findings, which is how the safety-critical world catches a plausible argument resting on a weak assumption.

## Target Customer
Assessment firms, regulated deployers, regulators writing requirements, and the safety assurance profession for whom AI systems are a live and unsettled application.

## Impact If Solved
Safety-critical engineering answered exactly this question with structured assurance cases and this field produces a findings list. Explicit statement of assumptions and residual risk is the most transferable element, and a hybrid of safety and security assurance is what an adaptive adversary requires.
