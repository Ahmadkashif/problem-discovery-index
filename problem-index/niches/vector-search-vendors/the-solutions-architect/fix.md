# The Same Seven Checks, Every Time

**Niche:** [[niches/vector-search-vendors/the-solutions-architect/profile|The Solutions Architect]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Architects diagnose the same small set of causes across hundreds of tickets, and nothing accumulates — each case starts from scratch and the pattern across customers is never assembled.
**Tags:** #descriptive-statistics #evaluation-metrics #worker-facing #automation #k-means-clustering #data-integration #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to make the platform explain why a document was not returned — and whoever does that takes the support load, because that one question is most of the category's solutions engineering.

## The Problem
An architect has resolved four hundred of these tickets. They know that in a particular kind of deployment the cause is almost always chunk boundaries, that a certain embedding model handles a certain vocabulary badly, and that customers migrating from a keyword search engine consistently hit the same three problems in their first month. None of this is written down anywhere, none of it is in the documentation, and when they move to another company it leaves with them. A new architect starts from the seven checks with no priors at all.

## Why It's Still Broken
Ticket systems capture the resolution as free text, which is unqueryable in practice. Writing up a pattern is unbilled work with no owner. The patterns are partly about embedding models and chunking, which the vendor's official position is not to have opinions about — so documenting them contradicts the positioning. And the cost is entirely in repeated diagnosis time, which never appears as a line anybody owns.

## What a Fix Looks Like
Capture the diagnosis in a structured form and use it. Record every resolved case as a typed cause from a fixed taxonomy plus the deployment characteristics — corpus type, embedding model, chunking strategy, query shape — which is one dropdown at ticket close and is the entire precondition for everything else. Report cause frequency by deployment profile, which turns four hundred individual resolutions into a prior a new architect can use immediately and is the artefact that would most reduce time to competence. Feed the frequent causes into onboarding checks, so a new deployment is screened for the three problems its profile predicts before the customer finds them. Publish the patterns as guidance, accepting that this means taking positions on chunking and embedding, which the customers want and the positioning currently forbids. Detect recurring cases within a deployment, since a customer filing the same class of ticket repeatedly needs a configuration change rather than a fifth answer. Route by predicted cause, so the architect who knows that class gets the case. And report diagnosis time per cause class, which identifies where the automation in the build note pays best.

## Who Feels the Pain
Architects re-deriving what colleagues already know; new hires without access to the priors that make the job tractable; and customers receiving an answer in three days that a captured pattern would have given in three minutes.

## Impact If Fixed
Four hundred resolutions leave no trace and the pattern leaves with the person. One structured cause field at ticket close makes cause frequency by deployment profile computable, which is the prior a new architect currently spends a year acquiring.
