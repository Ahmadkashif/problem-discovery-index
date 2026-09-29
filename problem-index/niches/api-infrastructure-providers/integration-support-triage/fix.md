# The Error Response That Names a Code

**Niche:** [[niches/api-infrastructure-providers/integration-support-triage/profile|Integration Support Triage]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Fix (Pain Point)
**One-liner:** A validation failure returns a status and a code, so the developer knows the request was rejected and not which field, which value, or why.
**Tags:** #bert #descriptive-statistics #k-means-clustering #evaluation-metrics #confidence-intervals #worker-facing #quick-win #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to answer whose fault a failed integration call was, in seconds rather than in an exchange of messages — and whoever does that takes the support organisation, because fault attribution is where every integration ticket begins and most of them end.

## The Problem
A request is rejected with a 422 and a body containing an error code and the message "validation failed". The payload has forty fields. The developer tries removing fields, changing formats and re-reading the documentation. Ninety minutes later they discover that a date was accepted in one format and not another, which the documentation does not mention because whoever wrote it did not know. The provider's validation layer knew exactly which field failed and why, and chose to return a code.

## Why It's Still Broken
Terse error responses became conventional partly from a defensible security instinct — do not leak internal detail — which has been applied indiscriminately to validation failures where there is nothing to leak. The validation framework produces detailed errors internally and the response layer discards them, usually because the response schema was designed before anyone thought about the debugging experience. And the cost lands entirely on the consumer's developer, who is not the provider's user in any way the provider measures.

## What a Fix Looks Like
Return what the validator already knows. Name the field, the value received, the constraint violated and the expected form, for every validation failure, which is a projection of information the validation layer already produced and is the single highest-return change available in this niche. Distinguish clearly between a malformed request, an unauthorised one, a request referencing something that does not exist, and a provider-side failure, since those four require entirely different responses from the developer and are frequently conflated behind one code. Include the correlation identifier, always. Link to the specific documentation section rather than to the documentation. Keep a small, stable, documented error taxonomy rather than an ad hoc set of codes that grows per release. Distinguish retryable from permanent failures explicitly, since consumers otherwise guess and their guesses cause either lost data or retry storms. And analyse the error distribution: the most common consumer errors are a ranked list of what the API or its documentation gets wrong, and no provider reads it.

## Who Feels the Pain
Consumer developers losing hours to a message that says validation failed; provider support engineers fielding the resulting tickets; and API programmes whose onboarding funnel loses developers at the first rejected request.

## Impact If Fixed
Detailed validation errors are a projection of information the provider already computed and discards, which makes this among the cheapest high-value fixes in the vault. The error distribution analysis turns consumer confusion into a ranked documentation backlog.
