# Orientation in Somebody Else's Code

**Niche:** [[niches/game-porting-studios/the-engineer-in-a-strangers-codebase/profile|The Engineer in a Stranger's Codebase]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every question that would take a colleague thirty seconds to answer takes an afternoon of reading.
**Tags:** #worker-facing #large-language-models #graph-theory #data-integration #evaluation-metrics #automation #workflow-orchestration #transformers
**Contested on:** Every serious competitor in this niche is fighting to make a large unfamiliar codebase comprehensible to an engineer with no access to its authors and no documentation of why anything is the way it is — and whoever does that takes the account.

## The Problem
A porting engineer joins a codebase of a million lines written over five years by people they will never speak to. They must understand enough to change it safely, on hardware it was not written for, under a schedule set by an estimate. Why is this system structured this way? Is this a deliberate optimisation or a workaround? What breaks if this changes? Every one of these would be a quick conversation on the original team and is instead an afternoon.

## Why Nobody Has Built This
Code comprehension tooling targets teams working in their own code, where the authors are available. Porting engineers are a small population. The difficulty is regarded as the nature of the job. And the studio's answer is to hire people who are good at it.

## What to Build
Recover intent from what the codebase contains and capture what engineers learn. Generate an orientation map of the codebase — its systems, their relationships, the entry points and the platform layer — which is the core and replaces the first two weeks of every project. Recover intent where the history allows, using commit messages, issue references and comments to explain why something is as it is. Identify the platform-specific and performance-sensitive code explicitly, since those are where changes are dangerous and the engineer cannot tell by looking. Show what depends on a given piece of code before it is changed, which is the question asked most often and answered least reliably. Answer natural-language questions about the codebase from its own contents, which is what an engineer would ask a colleague. Capture what each engineer learns as they learn it, so the second engineer on the project does not repeat the first's discovery. Highlight the unusual and non-idiomatic, as those are where the surprises live. Build a question queue to the client that batches and tracks rather than losing questions in email. Carry the accumulated knowledge across the project's phases rather than losing it at handover. And keep it advisory, since an engineer working in dangerous code will not trust an assertive tool.

## Target Customer
Porting and co-development studios, engineering leadership, outsourced development providers, and developer tooling vendors.

## Impact If Built
Every question that would take a colleague thirty seconds has to be answered by reading, and there is no colleague. An orientation map with intent recovery replaces the first two weeks of every project.
