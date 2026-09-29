# Debugging a Run You Cannot Reproduce

**Niche:** [[niches/ai-agent-platforms/orchestration-frameworks/profile|Orchestration Frameworks]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An agent fails in a way an engineer needs to understand, and re-running the same input produces a different trajectory, so the investigation starts with trying to make the failure happen again.
**Tags:** #workflow-orchestration #automation #evaluation-metrics #graph-theory #large-language-models #descriptive-statistics #data-integration #compliance
**Contested on:** Every serious competitor in this sub-niche is fighting to let an engineer understand and control what their agent actually did — and whoever does that takes the adoption, because the buyer is building the agent themselves and debuggability is what they run out of.

## The Problem
A production trajectory went wrong: the agent called a tool with a malformed argument on step four, recovered oddly, and produced a plausible but incorrect final answer. The engineer re-runs the same input. The agent takes a different path and succeeds. They re-run it eleven more times and reproduce the failure twice, which tells them it is intermittent and nothing else. The information required to understand it — the exact model outputs, the exact tool responses, the exact state at each step — was produced once and is either not recorded or not replayable. The debugging loop that every other kind of software has is unavailable.

## Why Nobody Has Built This
Determinism looks impossible when the decision maker is a sampled model, so frameworks did not attempt it — even though the model output is an external event that can be recorded and replayed exactly, which makes the run reproducible in every respect that matters. Tracing was added as an observability integration rather than as a replay substrate, so the recorded data is shaped for dashboards and not for re-execution. And the pain lands on engineers who work around it rather than on anyone specifying the framework.

## What to Build
Make a past run re-executable. Record every non-deterministic input — model outputs, tool responses, timestamps, random choices — as events, and replay them exactly, so a failed trajectory can be stepped through repeatedly and deterministically, which is the build and it converts an intermittent mystery into ordinary debugging. Allow replay with a modification, so an engineer can change the prompt or the tool at step four and see what would have happened from there, which is the capability that turns debugging into fixing. Make state explicit and inspectable at every step rather than implicit in a conversation history. Support unit testing of individual nodes against recorded inputs, which is how a stochastic component becomes testable at all. Version the whole agent definition — graph, prompts, tools, model settings — as one artefact and bind every trajectory to it, so a regression is attributable to a change. Provide a diff between two trajectories, since comparing a successful and a failed run on the same input is the most informative view available and nobody offers it. Keep the raw model interaction accessible rather than wrapped, which the fix note develops. And export trajectories in a form the evaluation and corpus work can consume, since debugging and evaluation want the same record.

## Target Customer
Engineering teams building agents, the framework authors, and the observability vendors whose tracing stops short of replay.

## Impact If Built
Recording model outputs as external events makes a stochastic run exactly replayable, which the category has treated as impossible. Replay-with-modification is what turns debugging into fixing, and a trajectory diff between a passing and failing run is the most informative view nobody offers.
