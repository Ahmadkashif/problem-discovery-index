# Buy: Field Experiment Methodology Adapted to an Employer's Own Pipeline

**Niche:** [[niches/recruiting-tech-vendors/counterfactual-evidence/profile|Counterfactual Evidence]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Labour economists have run field experiments in hiring for decades; they study employers from outside, and this design requires the employer to run it on itself.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #monte-carlo-methods #evaluation-metrics #compliance #survival-analysis #bayesian-inference
**Contested on:** Whether experimental methodology developed to study employers can be operated by an employer on its own process.

## The Problem

Field experimentation in hiring is an established research tradition. Audit studies sending matched applications, resume correspondence studies, and randomised evaluations of labour market interventions have produced a substantial body of evidence, with well-developed designs, power analysis, ethical review practice and publication standards.

Almost all of it studies employers from the outside, without their participation, and mostly asks about discrimination rather than about screening validity. The design needed here inverts that: the employer runs the experiment on its own pipeline, with the intervention inside its own process, measuring its own screen.

## What Already Exists

The field experiment literature in labour economics and its designs. Power analysis and randomisation tooling. Regression discontinuity methodology, directly applicable to threshold-based screening. IRB and research ethics practice. Experimentation platforms from the technology sector. Survival and panel analysis for long-horizon outcomes.

## The Customization Gap

**The experimenter is the decision-maker and has an interest in the result.** An academic studying an employer is independent. An employer studying itself is not, which means the analysis needs external verification, pre-registration of the design and the outcome measures, and a commitment to report the result regardless — none of which the methodology supplies and all of which determines whether the finding is believed.

**The intervention is inside an operational process at volume.** The randomisation has to happen in the applicant tracking system, silently, reliably, without disrupting the workflow or being overridden by a recruiter who notices. That is an engineering integration that the research tradition, which sends applications from outside, has never had to build.

**The ethical frame has no precedent in this shape.** Randomising who advances, upward only, inside a live process, without the candidate's knowledge or with disclosure — the arguments differ, and the research ethics tradition's frameworks were built for research subjects rather than for job applicants in a commercial process. Writing the framework is a genuine piece of work.

**The horizon is years and the analysis must run continuously.** Research designs conclude. This needs to be a standing programme with interim analyses, sequential testing to avoid overclaiming early, and a reporting cadence that survives leadership changes.

**Regression discontinuity is available immediately and underused.** The screening threshold already exists in historical data, which supports a discontinuity analysis without any randomisation at all. It is weaker and it is free, and every employer with a threshold could run one this quarter.

## Target Customer

Large employers' people analytics and research functions, and the academic labour economists who would partner with them — the partnership is the natural structure, because it supplies independence and methodology to an employer with data and access. Also regulators and foundations, for whom funding such a programme would produce evidence no disclosure requirement can compel.

## Impact If Solved

The field experiment designs, discontinuity methodology, power analysis and ethical review practice get reused, and the self-experimentation independence, operational randomisation, applicant-specific ethics, standing-programme analysis and immediate discontinuity work get built. Concretely: an employer can run the study that would tell them whether their screen is worth anything.
