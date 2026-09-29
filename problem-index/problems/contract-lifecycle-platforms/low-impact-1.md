# Clause Library and Playbook Curation

**Industry:** [[contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Clause libraries and negotiation playbooks are standard CLM features and they encode what a senior lawyer believes is acceptable, which drifts from what the company has actually been agreeing to.
**Tags:** #bert #word-embeddings #large-language-models #dbscan #hypothesis-testing #evaluation-metrics #compliance

## The Problem
A playbook states the company's negotiating position: preferred clause language, acceptable fallbacks, the walk-away point, and when to escalate. A clause library holds the approved wording. Together they are how a legal team scales itself, letting less senior lawyers and sometimes salespeople handle standard negotiations.

Both are authored by senior counsel from experience and judgement, and both drift immediately. The company signs agreements with terms outside the playbook because a deal mattered. Fallback positions that the playbook calls acceptable are refused by every counterparty in a particular industry. A clause the playbook treats as non-negotiable is conceded routinely. Market practice moves on limitation of liability, and the playbook does not.

Nobody checks the playbook against the executed contracts. So a company can be operating on a stated position it has abandoned in practice for two years, and the first person to discover it is usually a lawyer who joined recently and asks why the guidance does not match the files.

## What Already Exists
Clause libraries with approved and fallback language are standard in every CLM product. Playbook features encode positions and escalation rules. Version control and approval workflows are built in. Some platforms track clause usage. Legal publishers offer market-standard clause benchmarks based on published agreements.

## The Customisation Gap
The comparison between stated position and executed reality is absent everywhere, and it is straightforward: extract the operative terms from executed agreements, compare against the playbook position, and report where practice has diverged and how often. That single report would be new to almost every legal department.

Achievability is the more valuable version. A playbook says a position is acceptable; the data says what proportion of counterparties actually accepted it, by industry, deal size and counterparty type. That converts negotiation guidance from assertion into evidence, and it is exactly what a junior lawyer needs when deciding whether to hold a position.

Cross-customer benchmarking is the platform's unique asset. What terms are actually market — as observed across thousands of executed agreements — is a question every legal team asks and answers from anecdote, and published-agreement benchmarks are a poor substitute because they cover only filed public contracts.

Staleness detection is the third gap: clauses in the library that have not been used in two years, or that are routinely edited when used, are telling you the library is wrong.

## Impact If Solved
Playbooks are how legal departments delegate, and they drift from practice without anyone noticing. Comparing stated position against executed reality, and attaching achievability rates to each position, turns a document of assertions into a maintained instrument grounded in what the company actually signs.
