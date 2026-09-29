# Workflow Engines and Durable Execution

**Niche:** [[niches/ai-agent-platforms/agent-platforms-and-products/profile|Agent Platforms & Products]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Durable workflow engines solved long-running, failure-tolerant, resumable multi-step execution years ago, and agent frameworks reimplemented the easy half.
**Tags:** #workflow-orchestration #automation #graph-theory #data-integration #evaluation-metrics #compliance #dynamic-programming #descriptive-statistics
**Contested on:** Not terminal — the contest differs by whether the buyer is building the agent or buying its output, and the decomposition is recorded in the profile.

## The Problem
Executing a multi-step process that calls external systems, survives crashes, resumes where it stopped, retries safely, compensates for partial completion and can be inspected afterwards is exactly what durable workflow engines do. They have event-sourced state, deterministic replay, versioning and timers, and they are battle-tested in payments and logistics. Agent frameworks built graph-based control flow and largely stopped there, leaving durability, replay and compensation to the application.

## What Already Exists
Durable execution engines with event-sourced history and deterministic replay; workflow engines with compensation and saga patterns for partial failure; idempotency and exactly-once semantics for external calls; versioning of long-running workflow definitions; and human task steps as a first-class workflow construct.

## The Customization Gap
The adaptation is to a workflow whose next step is chosen by a model. It requires: (1) determinism under a non-deterministic decision maker, where the replay guarantee must cover recorded model outputs rather than recomputed ones — this is the key technical adaptation and it is entirely tractable once the decision is treated as an external event; (2) compensation for actions an agent chose rather than a developer, which means the compensating action must be derivable at run time rather than written in advance, and is the hardest part; (3) human approval as a durable workflow step with a timeout and an escalation path, which workflow engines model well and agent platforms implement as a blocking call; (4) versioning where the agent definition includes a prompt and a tool set, so a change in either is a version change with the same replay consequences; and (5) trajectory history as a queryable artefact rather than a log, since the history is the corpus everything else in this industry depends on.

## Target Customer
Agent framework authors, engineering teams building agents, and the durable execution community for whom agents are a natural and unclaimed workload.

## Impact If Solved
Durable execution solved resumability, replay and compensation, and agent frameworks left them to the application. Treating the model's decision as a recorded external event makes deterministic replay tractable, which is the foundation for debugging, audit and undo alike.
