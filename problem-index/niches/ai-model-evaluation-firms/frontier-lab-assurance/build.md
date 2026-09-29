# A Negative Result That Means Nothing

**Niche:** [[niches/ai-model-evaluation-firms/frontier-lab-assurance/profile|Frontier Lab Assurance]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An evaluation reports that a model did not exhibit a capability, and nothing in the report distinguishes a model that lacks it from an evaluation that failed to elicit it.
**Tags:** #large-language-models #evaluation-metrics #hypothesis-testing #confidence-intervals #monte-carlo-methods #compliance #descriptive-statistics #transfer-learning
**Contested on:** Every serious competitor in this sub-niche is fighting to find capability or risk that the lab's own evaluation team did not — and whoever does that takes the contract, because a lab with a large internal team buys external evaluation for exactly one reason.

## The Problem
A report concludes that the model did not demonstrate a given capability across the evaluation suite. Three months later a member of the public elicits it in an afternoon with a prompting approach nobody in the engagement tried. The original finding was not wrong — the model did not demonstrate it under those conditions — and it was reported in a form that invited the reader to conclude the capability was absent. Nothing in the report said how hard anyone tried, what approaches were attempted, or what the plateau of elicitation effort looked like. The negative result was uninterpretable and was interpreted anyway.

## Why Nobody Has Built This
Elicitation effort has no accepted unit, so there is nothing to report even if a firm wanted to. Reporting effort invites the question of whether more would have found something, which is uncomfortable for both parties. The commercial logic rewards finding things rather than characterising the search, so effort spent on measuring the search is effort not spent finding. And the field's reporting norms were set by academic papers, which have the same problem and the same silence about it.

## What to Build
Make the search itself measurable. Report elicitation effort in stated units — techniques attempted, compute spent, expert hours, prompting strategies, fine-tuning and scaffolding applied — so a negative result carries information about how hard it was to obtain, which is the missing half of every such finding. Show the elicitation curve: capability demonstrated against effort applied, since a curve still rising at the end of the engagement means something entirely different from one that plateaued, and this single artefact would transform how negative results are read. Maintain a taxonomy of elicitation techniques and report coverage against it, which turns an ad hoc search into a stated one and lets a reader see what was not tried. Track findings across engagements so the firm builds on its own history rather than restarting, which is what makes the practice compound. Treat scaffolding, tool access and fine-tuning as elicitation dimensions rather than as out of scope, since capability under scaffolding is the relevant question for deployment and is frequently excluded on grounds of difficulty. Report what would have been tried with more resources, which is honest and is the thing the reader most needs to weigh. And state the conditions under which a negative result should stop being relied upon, because these reports are cited long after the elicitation landscape has moved.

## Target Customer
Frontier labs, the regulators and standards bodies citing these evaluations, and the assurance firms whose reports currently invite an over-reading.

## Impact If Built
A negative result with no measure of effort is uninterpretable and is interpreted anyway. The elicitation curve — capability against effort — is the artefact that would let a reader tell an absent capability from an unfound one.
