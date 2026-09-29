# Buy: Program Evaluation Methodology Adapted to Per-Tutor Attribution

**Niche:** [[niches/online-tutoring-platforms/learning-gain-attribution/profile|Learning Gain Attribution]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Education research has a well-developed apparatus for evaluating whether a programme works; the question here is whether a named individual works, on eleven students, with no control group.
**Tags:** #causal-inference #hypothesis-testing #bayesian-inference #confidence-intervals #evaluation-metrics #compliance #descriptive-statistics #data-integration
**Contested on:** Whether programme evaluation methodology survives being pushed down to the individual practitioner.

## The Problem

Evaluating educational interventions is a mature discipline with established methods, experienced practitioners, independent evaluators and a clear standard of evidence. Randomised trials, quasi-experimental designs, regression discontinuity and difference-in-differences are all routinely applied, and the tutoring literature specifically is among the better-evidenced areas in education research.

All of that operates at the programme level: does high-dosage tutoring, as a category, improve outcomes. The marketplace question is different in kind — does this tutor improve outcomes — and the methodology degrades sharply when pushed to a unit of analysis with a dozen students and no assignment mechanism.

## What Already Exists

Education research methodology and the evaluation firms that apply it. Value-added and teacher-effectiveness modelling with its substantial literature, including a well-documented critique of exactly this kind of individual-level inference. Assessment instruments and item banks. Statistical software and causal inference libraries. IRB and research ethics infrastructure. District data-sharing agreements as a legal template.

## The Customization Gap

**The unit of analysis has an order of magnitude too little data.** Programme evaluation pools thousands of students. A tutor estimate rests on a handful. Every method has to be reformulated with shrinkage toward a population mean as the default and separation as the exception, which changes what can honestly be said about any individual — and is the single most important adaptation.

**There is no assignment mechanism to exploit.** Trials randomise; districts phase in; here families choose their tutor from a ranked list, which is about as selected as assignment gets. The natural experiments that do exist — availability constraints, cancellations, waitlists, rollout timing — have to be found and defended, and that is bespoke work per platform.

**The dosage is small and variable.** Evaluation designs assume a defined treatment. Here it is four hours or forty, spread irregularly, alongside school instruction that dominates. Modelling dose-response rather than a binary treatment is necessary and is not how these designs are usually specified.

**The measured party has commercial consequences.** Programme evaluation informs a purchasing decision. Individual attribution affects a person's income, which brings the fairness, transparency and appeal considerations that the teacher value-added debate documented painfully — and the tutors here have none of the protections teachers had in that debate.

**The data-sharing agreements are the hard part.** Student data involving minors, held by schools, under FERPA and state law, shared with a commercial platform. The legal template exists in the district contracting world and is the practical gate on everything else. It is procurement work, not data science, and it should start a year before anyone writes a model.

## Target Customer

Platforms selling into districts, who need the evaluation apparatus and the data agreements to compete for contracts. Education evaluation firms, for whom marketplace tutoring is a new client category. And district procurement offices, who are commissioning this work and mostly receiving programme-level answers to a provider-level question.

## Impact If Solved

The established evaluation methodology and legal templates get reused, with the individual-level shrinkage, the found natural experiments, the dose-response specification and the fairness apparatus built deliberately. The practical result is an attribution that is defensible about what it does not know, which is the only kind that will survive contact with the people it measures.
