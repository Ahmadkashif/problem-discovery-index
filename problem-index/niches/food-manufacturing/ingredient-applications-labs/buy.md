# The Formulation Is in a Notebook, the Panel Is in Another System, the Stability Is in a Spreadsheet

**Niche:** [[niches/food-manufacturing/ingredient-applications-labs/profile|Ingredient Applications Laboratories]]
**Industry:** [[industries/food-manufacturing|Food Manufacturing]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** A single brief generates formulations, sensory panels, stability pulls and cost models in four unconnected systems, and reassembling the record is somebody's afternoon.
**Tags:** #data-integration #workflow-orchestration #transformers #automation #evaluation-metrics

## The Problem
Working a brief produces a lot of separate evidence. Formulation versions in an electronic lab notebook. Descriptive and consumer panel results in a sensory system. Accelerated and real-time stability pulls tracked on their own schedule. Instrumental analysis in the analytical lab's platform. Cost and regulatory status in yet another. Customer feedback in an email thread.

Each system is reasonable. Together they mean that the fundamental object of the business — *this formulation, tested this way, performed like this, and cost this* — does not exist as a record anywhere. It is reassembled by a technologist when a report is due.

The costs compound quietly. Version confusion is endemic, because a formulation iterates a dozen times and the panel result attaches to one of them. Stability studies run on formulations that were superseded before the six-month pull. Nobody can answer straightforward analytical questions across briefs — how often does a retort application need a second iteration, how much does removing a given ingredient typically cost in sensory distance — because answering them means re-reading projects.

And the library problem above is downstream of this one. A corpus cannot be learned from if the formulation, its sensory result and its commercial fate were never in the same record.

## What Already Exists
Electronic lab notebooks and laboratory information management systems are mature and widely deployed. Product lifecycle management suites for food and beverage exist and handle specifications, regulatory and cost. Sensory data collection platforms are established and good at what they do. Experiment tracking tooling is commodity in other research settings.

What none of them models is the food applications workflow as a single object. PLM is built around a released specification, not around an exploratory brief that generates forty versions and abandons thirty-eight. Sensory platforms are designed around the panel session, not around the formulation lineage. ELNs record what was done without connecting it to what it was for.

## The Customization Gap
**The unit is the brief, and it branches.** A brief spawns a tree of formulation versions, most abandoned, some revived. Modelling that lineage properly — with every result attaching to a specific node — is the core requirement and no off-the-shelf system expresses it.

**Sensory results must bind to a version, not a project.** This single discipline fixes most of the confusion, and it requires the sensory system and the notebook to share an identifier they currently do not.

**Ingredient identity is a resolution problem.** The same material appears under supplier codes, internal codes, INS numbers and common names across systems. Without resolution, no cross-brief analysis is possible.

**Regulatory and cost status change under a live project.** A formulation that was compliant in one market when created may not be by the time it launches. The record has to be time-aware rather than current-state.

**Confidentiality is per customer and absolute.** Briefs are commercially sensitive, and any cross-brief learning has to work on a de-identified layer with governance that a customer would accept if they asked. This is a design constraint from the first line, not a later concern.

**The archive is the migration.** Decades of prior work sits in legacy notebooks and files. Reconstructing enough of it to be useful is a document extraction project in its own right, and it is where most of the asset actually is.

## Target Customer
VP of Applications or Head of R&D Digital at a flavour and ingredient house.

## Impact If Solved
The house's most valuable asset is a formulation history that currently cannot be queried, because the pieces were never joined. Making the brief the unit of record ends version confusion, makes iteration counts and reformulation costs measurable for the first time, and is the precondition for treating the library as anything other than an archive.
