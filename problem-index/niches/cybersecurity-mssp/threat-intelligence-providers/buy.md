# Collection Triage Adapted to Analyst Attention as the Constraint

**Niche:** [[niches/cybersecurity-mssp/threat-intelligence-providers/profile|Threat Intelligence Providers]]
**Industry:** [[industries/cybersecurity-mssp|Cybersecurity MSSPs]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data platforms scale collection effortlessly and analyst hours do not, so the binding constraint is which fraction of an enormous intake a human ever reads — and no product optimizes for that.
**Tags:** #bert #transformers #large-language-models #contrastive-learning #word-embeddings #evaluation-metrics #k-means-clustering #transfer-learning #automation #data-integration #workflow-orchestration

## The Problem
Collection is cheap and growing; analysis is expensive and fixed. Forums, marketplaces, paste sites, malware repositories, and scanning data produce a volume no team can read, so triage decides what the product actually contains. Triage today runs on keyword rules, source priority, and analyst habit, which systematically surfaces what looks like previous findings and buries what does not — precisely inverting the value, since novelty is what intelligence is for. Coverage of non-English sources is thinnest for the same reason, and that is where a substantial share of the relevant activity is.

## What Already Exists
The tooling market is well supplied. Elastic and the search platforms handle indexing at scale; the LLM and embedding services make semantic clustering and summarization cheap; commercial dark web collection and monitoring products handle acquisition and basic alerting; translation is a commodity. Every individual component is available.

## The Customization Gap
Everything available optimizes retrieval — surfacing content matching a query or resembling a known pattern. The operative problem is the inverse: identifying what an analyst has not seen before and would want to, which is a novelty and consequence problem rather than a similarity one. The adaptation is triage that scores intake on expected analytic value — novelty against the firm's own existing knowledge base, connection to actors, infrastructure, or targets the firm already tracks, and consequence for clients given their known exposure — rather than on keyword match. Novelty must be measured against what the firm knows rather than against a general model, which requires the knowledge base itself to be a first-class input. Multilingual handling has to be native to the scoring rather than a translation step, since the meaning that signals novelty is frequently the part translation flattens. And the triage model should learn from analyst behaviour — what got picked up, what led to a published assessment — which is a feedback signal the firm generates constantly and does not use.

## Target Customer
Heads of collection and intelligence operations at threat intelligence providers, and the analysts whose reading capacity is the actual bottleneck on the product's value.

## Impact If Solved
Raises the yield on the constrained resource, which is the only way to increase output without proportionally increasing headcount. It also directly addresses the failure mode that most limits the product — finding what resembles what is already known while missing what is new — and extends usable coverage into the language and source communities where collection is currently thinnest.
