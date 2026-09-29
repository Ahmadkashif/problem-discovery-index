# Sequence Modelling and Process Mining

**Niche:** [[niches/ai-agent-platforms/trajectory-corpus-intelligence/profile|Trajectory Corpus Intelligence]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Process mining was built to discover, compare and conform real process executions from event logs, and a trajectory corpus is an event log of exactly the shape it expects.
**Tags:** #hidden-markov-models #graph-theory #markov-chains #evaluation-metrics #gradient-boosting #descriptive-statistics #confidence-intervals #k-means-clustering
**Contested on:** Every serious competitor in this niche is fighting to turn millions of complete task trajectories into empirical answers about where approval belongs, which failures are recoverable and what predicts a task going wrong — and whoever does that sets the standard the category is judged by.

## The Problem
Discovering the actual process from a log of executions, comparing it against the intended one, finding where executions deviate and predicting outcomes from a partial trace are exactly what process mining does, with a mature toolset, established algorithms and a substantial literature. An agent trajectory corpus is an event log with case identifiers, activities and timestamps — the precise input format the field assumes — and almost nobody in this category has noticed.

## What Already Exists
Process discovery algorithms producing models from event logs; conformance checking against an intended model; deviation and bottleneck analysis; predictive process monitoring that forecasts outcomes from partial traces; trace clustering for heterogeneous logs; and sequence models for behavioural prediction.

## The Customization Gap
The adaptation is to a process whose control flow is chosen at run time by a model. It requires: (1) conformance checked against an intended behaviour that is a prompt rather than a process model, which means the intended model has to be inferred from successful executions rather than declared — an inversion the field handles with discovery and which fits well; (2) trace clustering as the primary step, since agent trajectories are far more heterogeneous than the business processes the tools assume and clustering before discovery is what makes the output legible; (3) predictive monitoring on partial trajectories as the core deliverable, since predicting that a task will fail from its first four steps is the capability the category most needs and is precisely what predictive process monitoring does; (4) the model's own output as an activity attribute, which carries information no conventional event log has; and (5) outcome definitions beyond completion, since a trajectory can complete and still be wrong, which business process logs rarely have to express.

## Target Customer
Agent platforms, reliability teams, and the process mining community for whom agent trajectories are a large, well-formed and entirely unclaimed corpus.

## Impact If Solved
A trajectory corpus is an event log in exactly the format process mining assumes, and the field has not noticed. Predictive monitoring on partial traces is the capability this category most needs and is a solved problem one discipline over.
