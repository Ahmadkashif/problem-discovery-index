# Establishing Whose Fault It Was

**Niche:** [[niches/api-infrastructure-providers/integration-support-triage/profile|Integration Support Triage]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Integration support engineers spend every ticket establishing whose fault it is, and the request and response are both on record with the provider the whole time.
**Tags:** #descriptive-statistics #k-means-clustering #bert #logistic-regression #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to answer whose fault a failed integration call was, in seconds rather than in an exchange of messages — and whoever does that takes the support organisation, because fault attribution is where every integration ticket begins and most of them end.

## The Problem
A ticket says calls are failing with a 400. The support engineer asks for a correlation identifier; the consumer does not have one because the error response did not include it. They ask for the timestamp and the account, search the logs, find several thousand requests and narrow by error code. Eventually they locate a request missing a field that became required in a release six weeks ago. Two days have passed, four messages have been exchanged, and the answer was available in the first minute to anyone with the request in front of them.

## Why Nobody Has Built This
Support tooling in this category is the generic ticketing stack, which knows nothing about requests, and the request logs are in the platform, which knows nothing about tickets. Nobody joined them. Exposing a consumer's own requests back to them raises access-control questions that are entirely solvable and have functioned as a reason not to do it. And the failure that matters most — the provider's behaviour changed and the documentation did not — is uncomfortable to surface, so the tooling that would surface it has not been built.

## What to Build
Make the request the unit of support. Put a correlation identifier in every response, especially error responses, and tell the consumer to quote it — which is a one-line change that removes the first day of most tickets. Give consumers direct, authenticated access to their own request and response history, with the request exactly as received, since the most common resolution is the consumer seeing what they actually sent. Classify the failure automatically into provider fault, consumer fault, or contract ambiguity, which is determinable from the request, the specification and the implementation's behaviour, and is the question the ticket exists to answer. Detect repeated identical failures from one consumer and reach out before they file, because a consumer failing the same way four hundred times an hour is a broken integration the provider can see and they cannot. Cluster failures across consumers, since a pattern affecting many is a provider problem regardless of what each ticket says. And feed the aggregate back into the documentation and the error messages, since the consumer error distribution is a precise specification of where the API misleads people.

## Target Customer
API provider support organisations, developer relations teams, and the API management vendors whose products hold the logs and stop at the dashboard.

## Impact If Built
Fault attribution consumes most of the elapsed time on integration tickets and is determinable immediately from data the provider already has. Self-service request history and a correlation identifier in error responses together remove a large share of the ticket volume outright.
