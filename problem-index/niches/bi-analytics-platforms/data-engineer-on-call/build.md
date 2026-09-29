# The Same Failure, the Same Remedy, the Eleventh Time

**Niche:** [[niches/bi-analytics-platforms/data-engineer-on-call/profile|Data Engineer On-Call]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Data observability tells an engineer that a pipeline broke and leaves them to rediscover, at two in the morning, that it broke the same way as the last eleven times and takes the same fix.
**Tags:** #k-means-clustering #dbscan #bert #word-embeddings #graph-theory #evaluation-metrics #confidence-intervals #worker-facing
**Contested on:** Every serious competitor here is fighting to turn a pipeline alert into a diagnosis and a remedy rather than a page — and whoever does that takes the data platform account, because detection is a solved and crowded market and remediation is nobody's product.

## The Problem
At 02:14 a page fires: the customer dimension table did not refresh. The engineer opens a laptop, traces through the orchestration graph, finds that an upstream export from a source system landed late again, waits for it, reruns three jobs in order, and confirms the downstream tables. Fifty minutes. It is the eleventh time this quarter and the sequence has been identical every time. The remedy is recorded in a chat channel eleven times over, in eleven slightly different phrasings, and nowhere else.

## Why Nobody Has Built This
Observability vendors compete on detection breadth and on how early they catch things, which is where the demonstrations happen, and remediation is a support burden they have been happy to leave to the customer. Recognising a failure as a repeat requires clustering incidents by signature, which nobody does because incidents are stored as individual alerts rather than as a corpus. The remedy knowledge lives in chat and in memory rather than in a runbook, since writing runbooks at two in the morning is not what happens. And automated remediation makes people nervous, which is a reasonable instinct that argues for a proposed-and-confirmed design rather than for leaving the engineer to do it manually forever.

## What to Build
Turn the alert into a diagnosis with a proposed remedy. Cluster incidents by signature — the failing asset, the error, the upstream state, the timing — which identifies repeats immediately and is a straightforward clustering problem over data every orchestrator holds. Attach the diagnosis from the dependency graph: what failed first, what is downstream of it, and what changed recently, which is where the engineer's first twenty minutes go. Mine the chat history for what was done last time, since the remedy is there in every organisation, unstructured but recoverable, and presenting it at page time is most of the value without automating anything. Then offer execution for the deterministic remedies — rerun in this order, clear this lock, backfill this partition — proposed and confirmed by the engineer rather than applied silently, which is the design that gets adopted. And report repeat failures as a ranked list with their cumulative on-call cost, which is the argument for fixing the upstream cause and is currently made on the basis of how tired somebody is.

## Target Customer
Data platform engineering leadership, data observability vendors for whom this is the obvious next layer, and orchestration vendors who hold the dependency graph and the execution capability already.

## Impact If Built
Detection is crowded and remediation is empty, which is an unusual asymmetry in a well-funded category. Repeat identification and the chat-mined remedy require no automation at all and remove most of the diagnostic work, and the repeat-cost ranking is what finally gets the underlying causes fixed.
