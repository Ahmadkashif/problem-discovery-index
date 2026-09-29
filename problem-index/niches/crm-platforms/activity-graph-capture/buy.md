# Entity Resolution and Identity Graph Tooling

**Niche:** [[niches/crm-platforms/activity-graph-capture/profile|Activity Graph Capture]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Identity resolution across messy signals is a mature discipline with commercial products and open tooling, and sales activity capture matches an email address to a contact with a domain lookup and a name comparison.
**Tags:** #bert #word-embeddings #k-nearest-neighbors #graph-theory #contrastive-learning #evaluation-metrics #confidence-intervals #data-integration
**Contested on:** Every serious competitor in activity capture is fighting to reconstruct a complete, correctly attributed engagement graph from email and calendar without asking a representative to do anything — and whoever holds coverage and attribution accuracy highest takes the account.

## The Problem
A buyer corresponds from a personal address while travelling, a consultant working for the account uses their own firm's domain, a champion changes jobs and reappears at a different company, and a subsidiary uses a domain that does not resemble the parent's. Each is a routine occurrence and each defeats a domain-and-name match. The identity resolution industry has spent two decades on exactly this class of problem for advertising and customer data, and the tooling has not been applied to a graph whose accuracy determines an enterprise forecast.

## What Already Exists
Entity and identity resolution is mature: probabilistic record linkage, embedding-based matching, graph-based clustering and active learning for match confirmation are all well developed with open implementations and commercial products. Customer data platforms do this for consumer identities at enormous scale. Corporate hierarchy and firmographic data is purchasable. Email signature parsing is a solved extraction task. Every component required is available.

## The Customization Gap
The adaptation is to a business-to-business graph with an organisational structure. It requires: (1) corporate hierarchy as a first-class structure rather than a flat account list, since subsidiaries, divisions and acquired entities are the normal case in enterprise selling and the account hierarchy niche exists because nobody models it; (2) role and seniority inference from signatures, titles and meeting participation, because a behavioural forecast needs to know whether the engaged contact is a champion or an intern and the graph currently treats them identically; (3) person-level identity that survives a job change, which is both a resolution improvement and a substantial commercial capability — a champion who moves to a new company is the highest-quality lead a seller can have and is currently discovered by accident; (4) active learning on the confirmation queue, so the representative confirmations described in the build note are chosen to maximise information rather than arriving in arrival order; and (5) a strict internal-external boundary, since the graph should contain interactions with customers and not a map of employees' internal correspondence.

## Target Customer
Activity capture vendors, CRM incumbents, and the enrichment providers whose firmographic data is the natural reference set for this resolution.

## Impact If Solved
Resolution quality is the binding constraint on graph coverage and the tooling to improve it is bought rather than built. Person-level identity across job changes is the capability with the clearest independent commercial value and is a by-product of doing the resolution properly.
