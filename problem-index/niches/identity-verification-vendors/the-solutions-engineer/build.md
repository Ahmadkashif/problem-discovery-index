# Explaining One Person's Decision

**Niche:** [[niches/identity-verification-vendors/the-solutions-engineer/profile|The Solutions Engineer]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The customer asks why this person was rejected and the honest answer is a composite score the engineer cannot decompose.
**Tags:** #large-language-models #evaluation-metrics #worker-facing #confidence-intervals #compliance #workflow-orchestration #automation #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to let a solutions engineer explain why one specific person could not open an account — and whoever makes the decision articulable changes what the escalation conversation can be.

## The Problem
An escalation arrives: a named individual, a specific attempt, a customer who wants to know what happened. The engineer opens the logs and finds a sequence of check results and a composite score. Which check drove the outcome, how close it was to passing, whether a retry would help, and whether the same thing happens to similar applicants are all questions the tooling does not answer. So the engineer says the identity could not be verified, which is what the customer already knew.

## Why Nobody Has Built This
Explainability was scoped to model governance documentation rather than to individual case explanation, so what exists describes the model in general and not this decision — a document written for a model risk review cannot answer a question about one person. Exposing detail was seen as a security risk. Escalation volume is absorbed by engineers. And nobody counted the escalations or catalogued their causes.

## What to Build
Make a single decision reconstructable and explainable. Build a case reconstruction view showing every check, its result, its contribution and its distance from the threshold, which is the core and is the difference between an answer and a restatement. Express the outcome in human terms — the document read failed, the face match was below threshold, no matching record was found — rather than as a score. Show whether a retry or a different document would plausibly succeed, since that is the customer's actual question. Handle the evidence access properly, so an engineer can see what is needed without creating a data exposure. Catalogue recurring escalation causes, because the same handful account for most of the volume and none are recorded. Give the engineer a route to trigger a review or an alternative path, as an explanation with no remedy is still a dead end. Aggregate escalations into product signal, since each one is a report of a failure mode and they are currently resolved individually and forgotten. Show similar cases and their outcomes, which tells the engineer whether this is one person or a pattern. Make the explanation safe to pass to the customer and onward to the applicant. And measure escalation volume and resolution, which is the workload nobody has sized.

## Target Customer
Solutions and support leadership, solutions engineers, customers fielding applicant complaints, and applicants who want to know what happened.

## Impact If Built
A document written for a model risk review cannot answer a question about one person, so explainability exists and explains nothing useful here. Case reconstruction with threshold distances turns a restatement into an answer and a possible remedy.
