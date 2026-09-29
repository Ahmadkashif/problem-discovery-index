# Policy Engines and Rights Expression

**Niche:** [[niches/data-marketplace-brokers/licence-term-enforcement/profile|Licence Term Enforcement]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Policy-as-code engines and rights expression languages exist and are mature, and data licences are enforced by remembering.
**Tags:** #compliance #graph-theory #data-integration #automation #workflow-orchestration #evaluation-metrics #quick-win #large-language-models
**Contested on:** Every serious competitor in this niche is fighting to make permitted-use terms something the delivery path can read and enforce rather than prose somebody has to remember — and whoever does that takes the account, because compliance currently depends on institutional memory.

## The Problem
Expressing rules about who may do what with which resource, evaluating them at a decision point, and auditing the result is what policy engines do, and they are deployed widely for access control and infrastructure governance. Rights expression languages were built specifically to encode what a licence permits. Both are mature, open and well documented. Data licences in this market remain in signed documents and human memory.

## What Already Exists
Policy-as-code engines with declarative rules, decision APIs and audit logging; attribute-based access control frameworks; digital rights expression languages designed to encode licence permissions; data governance platforms with classification and policy attachment; and contract lifecycle management with clause extraction.

## The Customization Gap
The adaptation is to permissions over use and derivation rather than over access. It requires: (1) policy attached to data and inherited through transformation, since the governed thing is a dataset that becomes other datasets and access control models assume a stable resource — inheritance through lineage is the central adaptation; (2) purpose as a first-class input to the decision, because the question is not who is asking but what for, and purpose is rarely captured at query time and would need to be; (3) composition semantics for combined datasets, which rights languages handle poorly and which arises constantly here; (4) model training as an expressible use, which predates none of these languages and is now the most commercially significant term; and (5) extraction from prose into the policy language, since the terms exist as contracts and the translation is the practical barrier — which is where the recent progress in language models changes what is feasible.

## Target Customer
Data governance platforms, legal operations, marketplaces, and the policy engine and rights management communities.

## Impact If Solved
Policy engines and rights languages are mature and were never pointed at data licences. Inheritance through lineage and purpose as a decision input are the two adaptations, and prose extraction is the barrier that has recently become tractable.
