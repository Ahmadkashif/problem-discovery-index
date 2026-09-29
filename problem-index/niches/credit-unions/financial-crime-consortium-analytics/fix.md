# Typology Knowledge Lives With Investigators and Retires With Them

**Niche:** [[niches/credit-unions/financial-crime-consortium-analytics/profile|Financial Crime Consortium Analytics]]
**Industry:** [[industries/credit-unions|Credit Unions]]
**Type:** Fix (Pain Point)
**One-liner:** The firm's senior investigators can recognize a scheme from three details in an alert, and the only artifact of that expertise is the rules they occasionally ask an engineer to write.
**Tags:** #large-language-models #bert #transformers #word-embeddings #graph-neural-networks #evaluation-metrics #k-means-clustering #tacit-knowledge-ml #compliance #worker-facing

## The Problem
Financial crime detection is a pattern recognition discipline built on experience. A senior investigator who has worked hundreds of cases sees an alert and knows which scheme it resembles, what to check next, and which explanations are usually innocent. That knowledge shapes the product through an indirect and lossy channel — occasionally a rule gets written, occasionally a typology document gets updated — and otherwise stays in the investigator's head. Meanwhile schemes evolve continuously, so the knowledge that matters is the most recent and least documented. When a senior investigator leaves, the firm loses detection capability it cannot inventory, and a new investigator rebuilds it case by case over years.

## Why It's Still Broken
Investigation is delivered under time pressure where documentation is the first thing to go, and case notes are written for the file and the regulator rather than for retrieval. Typology documents exist and go stale, because maintaining them is nobody's primary job. The confidentiality regime around reporting also makes investigators cautious about writing down reasoning in shareable form, even where the underlying pattern is not itself protected. And the organization measures investigators on case throughput, which is exactly the metric that discourages capturing anything.

## What a Fix Looks Like
Structured capture of investigative reasoning as a by-product of casework. When an investigator escalates or clears, they record the typology recognized, the indicators relied on, and the checks performed, selected from a controlled vocabulary that grows from what investigators actually write rather than being imposed. Case narratives already produced for regulatory purposes are parsed into the same structure, which recovers reasoning that is being written anyway. Across the organization the accumulated records make several things possible: emerging typologies become visible as clusters of cases that do not match existing patterns, which is the earliest possible warning of a new scheme; detection rules can be proposed from investigator-recognized patterns rather than waiting for someone to request one; and a new investigator learns from a searchable body of worked reasoning instead of from apprenticeship. Confidentiality is handled by separating the pattern from the particulars, which is what makes the corpus shareable at all.

## Who Feels the Pain
Investigators repeatedly re-deriving what colleagues already know; detection engineering waiting for typology guidance that arrives as anecdote; member institutions facing schemes the vendor's senior people have already seen elsewhere; and the firm, whose detection capability is concentrated in a small number of people it cannot replace quickly.

## Impact If Fixed
Converts an ageing and irreplaceable workforce's expertise into an institutional asset, and shortens the path from an investigator noticing something to the detection layer acting on it — which is the loop that determines whether a consortium stays ahead of schemes that evolve faster than annual model refreshes.
