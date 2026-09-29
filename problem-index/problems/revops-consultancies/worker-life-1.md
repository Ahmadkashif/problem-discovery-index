# The Consultant Rebuilding the Same Funnel Model

**Industry:** [[revops-consultancies|RevOps Consultancies]]
**Type:** Worker Life Changing
**One-liner:** A RevOps consultant builds the same funnel model, the same stage definitions and the same dashboard set for the twentieth time, each from scratch, because the last nineteen live in clients' systems.
**Tags:** #large-language-models #k-nearest-neighbors #gradient-boosting #bert #evaluation-metrics #worker-facing #automation #tacit-knowledge-ml

## The Problem
RevOps engagements follow a recognisable arc: audit the current state, redefine the funnel stages and their exit criteria, rebuild reporting, fix the data model, implement a forecasting process, document it, train the team. A consultant who has done this twenty times has built twenty versions of substantially the same thing.

Each one is rebuilt. The stage definitions from the last engagement are in a client's CRM under a confidentiality agreement; the dashboard specifications are in a client's environment; the documentation was written for a different audience. So the consultant rewrites stage exit criteria from memory, re-derives the same conversion metrics, and rebuilds a reporting pack that differs from the last one mainly in field names.

The audit phase is equally repetitive. The findings are broadly the same every time — stages are advanced without evidence, close dates slip repeatedly, the lead handoff has no definition, attribution is contested, the forecast has no history — and the consultant discovers them again through interviews and data exploration that take weeks.

Then the work lands in an organisation with its own politics, where the recommendation that matters most is usually the one that makes someone's number look worse, and the consultant has no evidence to support it beyond having seen it before.

## Why It Matters to the Worker
The repetition is demoralising for the same reason it is in every consulting discipline: the first few engagements teach a great deal and the twentieth teaches nothing, while the firm's economics require you to keep doing them.

The absence of evidence is the specific frustration here, because the people in this role are quantitative by disposition. A RevOps consultant knows that stage probabilities are miscalibrated and cannot prove it without a retained history the client does not have. They know the forecast judgement adjustment is probably making things worse and cannot demonstrate it. They end up asserting things they are confident about and cannot show, to audiences trained to ask for numbers.

And the recommendations that stick are the ones that survive after the consultant leaves, which they mostly do not — the process decays, the discipline lapses, and a successor firm is hired eighteen months later to rediscover the same findings.

## What a Solution Looks Like
Retrieve rather than rebuild. Stage definitions, metric definitions, dashboard specifications and documentation from the firm's prior engagements, abstracted from client specifics and retrievable at the point of need, turn authoring into adaptation. This requires the firm to extract and own those artefacts, which is a process decision it has not made.

Automate the audit. The standard findings are computable directly from a client's CRM: stage dwell distributions, close date change patterns, handoff definition gaps, forecast history availability, pipeline coverage ratios. A diagnostic that runs in a day and produces the findings with evidence replaces three weeks of interviews and arrives with the numbers that make the recommendation land.

Carry evidence between engagements. A firm that retains pipeline series across clients can say that this pattern of stage movement predicts this level of forecast error across thirty organisations, which is a completely different conversation from professional opinion.

And design for decay. Recommendations that depend on ongoing discipline will lapse; those instrumented with monitoring that flags the lapse survive. Building the monitoring into the deliverable is what makes the engagement's effect outlast the engagement.

## Impact If Solved
Audit repetition and artefact rebuilding are most of a RevOps engagement's hours and none of its value. Automating the diagnostic compresses weeks into a day and produces better evidence than interviews; cross-client patterns give the consultant the numbers their audience demands; and instrumented recommendations address the reason this discipline's work so often has to be done twice.
