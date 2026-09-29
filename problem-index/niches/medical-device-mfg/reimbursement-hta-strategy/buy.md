# Economic Models Rebuilt in Spreadsheets Every Time

**Niche:** [[niches/medical-device-mfg/reimbursement-hta-strategy/profile|Reimbursement & Health Technology Assessment Strategy]]
**Industry:** [[industries/medical-device-mfg|Medical Device Manufacturing]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every payer submission needs a budget impact and cost-effectiveness model, and each is built from scratch in a workbook by an analyst.
**Tags:** #tabular-ml #workflow-orchestration #evaluation-metrics #data-integration #automation

## The Problem
A coverage dossier carries an economic argument: what the technology costs, what it displaces, what it saves, and over what horizon. That means a budget impact model for a payer's population and often a cost-effectiveness model with a defined comparator.

These are built in spreadsheets. Each engagement starts from a template or a prior client's model, is rebuilt around a new technology and comparator, populated with epidemiology and cost inputs gathered from literature and public data, and shipped as a workbook the payer's analysts will interrogate.

The structures repeat enormously across engagements in the same therapeutic area. The inputs — disease prevalence, procedure costs, complication rates, resource use — are gathered repeatedly by different analysts from the same public sources, with different vintages and different choices, and nobody can reconstruct why a particular number was used two years later.

## What Already Exists
Health economic modelling software exists and is used in pharmaceutical HTA. Decision analytic and Markov modelling tools are mature. Scientific computing platforms handle the mathematics trivially.

## The Customization Gap
The available tooling models the mathematics. The problem is the inputs and the reuse.

**A maintained input library with provenance.** Epidemiology, cost, and utility inputs sourced once, versioned, cited, and reused — so a model's every number traces to a source and a vintage. Today each analyst re-gathers, and models built six months apart in the same therapeutic area disagree for reasons nobody can reconstruct.

**Model structures as reusable components.** A budget impact model for a device displacing a surgical procedure has a recurring shape. Composing models from validated components rather than copying workbooks removes both the labour and the class of arithmetic errors that survive review.

**Payer-population parameterization.** The same model must be rerun for many plans with different populations, benefit designs, and cost structures. That is a parameter sweep, and it is currently a workbook duplicated per payer.

**Scrutiny-ready transparency.** Payer analysts interrogate these models and challenge assumptions. Every input needs a citation, every assumption a rationale, and the whole thing has to be reproducible under challenge — which spreadsheets famously are not.

**Sensitivity analysis as a default output.** The credible presentation is a range with the drivers identified, not a point estimate, and generating it should be automatic rather than a further manual exercise.

## Target Customer
Head of health economics or practice leader at a market access consultancy, where model construction is the largest labour item and model defensibility is the deliverable's whole value.

## Impact If Solved
Economic models are built by hand for every engagement, disagree with each other for undocumented reasons, and are challenged by exactly the audience most equipped to find errors. A versioned input library with composable structures makes them faster to build, consistent across a practice, and defensible line by line under the scrutiny they were built for.
