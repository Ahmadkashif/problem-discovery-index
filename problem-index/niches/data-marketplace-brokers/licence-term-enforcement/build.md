# Permitted Use Written in Prose

**Niche:** [[niches/data-marketplace-brokers/licence-term-enforcement/profile|Licence Term Enforcement]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every dataset arrives with permitted-use terms written in contract prose, and nothing in the delivery path knows what they say — so compliance depends on whoever read the agreement remembering it two years later.
**Tags:** #large-language-models #compliance #data-integration #graph-theory #workflow-orchestration #automation #evaluation-metrics #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to make permitted-use terms something the delivery path can read and enforce rather than prose somebody has to remember — and whoever does that takes the account, because compliance currently depends on institutional memory.

## The Problem
A dataset was licensed three years ago for internal analytics by the marketing function, with derivatives permitted but external publication forbidden and model training not contemplated. Today it is a table in the warehouse. A data scientist in a different business unit joins it into a training set for a model whose outputs go to customers. Every step of that was reasonable from where they stood, nothing in the platform said otherwise, the person who negotiated the terms left last year, and the company is now in breach of a contract nobody has read since signing. This is not an edge case; it is the default trajectory of every dataset a company buys.

## Why Nobody Has Built This
Contract prose is genuinely varied, so extraction is a real problem rather than a parsing exercise — though a tractable one now. Enforcement requires a point in the data path that evaluates policy, which means integrating with the warehouse, the pipeline and the training stack. Legal owns the terms and platform owns the data path, and neither owns the gap. And the exposure is invisible until it is not, so the work is never urgent.

## What to Build
Turn the terms into structure and put them in the path. Extract permitted use into a machine-readable policy — permitted purposes, permitted parties, derivative rights, combination restrictions, output restrictions, training permission, term and territory — which language models now make tractable at scale with human review, and which is the step everything else depends on. Attach the policy to the dataset in the catalogue and propagate it to every derived asset through lineage, since derived tables are where the use actually happens and where terms are currently lost entirely. Evaluate the policy at the point of use — query, export, model training — so a forbidden use is blocked or flagged rather than discovered at audit. Compose policies when datasets are combined, taking the intersection of what each permits, which is the correct semantics and is exactly what nobody does manually. Track expiry and termination, since data used past its licence is a common and entirely avoidable breach. Maintain an audit trail of what each dataset was used for, which is what turns an assertion of compliance into evidence. Surface the terms to the person at the moment of use in plain language, because most breaches are ignorance rather than intent. And feed the extracted structure back to the marketplace, so terms can be filtered on before purchase.

## Target Customer
Data governance and legal functions, platform teams, and the marketplaces and providers whose terms are currently unenforceable by construction.

## Impact If Built
The default trajectory of every purchased dataset ends in unknowing breach. Propagating policy through lineage to derived assets is where the use actually happens, and policy intersection on combination is the correct semantics that manual processes never apply.
