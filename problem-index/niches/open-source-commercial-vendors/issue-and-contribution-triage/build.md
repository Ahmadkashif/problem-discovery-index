# Tooling That Organises and Does Not Reduce

**Niche:** [[niches/open-source-commercial-vendors/issue-and-contribution-triage/profile|Issue & Contribution Triage]]
**Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Issue templates, labels, stale bots and contribution guides are standard practice in every project, and a small maintainer team still faces a queue from a community orders of magnitude larger than itself.
**Tags:** #bert #word-embeddings #k-means-clustering #large-language-models #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor here is fighting to reduce the queue rather than to organise it — and whoever does that takes the maintainer teams, because templates, labels and bots have been standard for a decade and the arithmetic is unchanged.

## The Problem
A project receives forty new issues a week. Perhaps eight are genuine defect reports with enough information to act on. Of the rest, a large portion are usage questions, a portion are duplicates of open issues, a portion are reports missing a version, a configuration or a reproduction, and a portion are feature requests outside any direction the project intends to take. The maintainer processes all forty to find the eight. The template collected the fields and did not ensure they were useful; the labels describe the issues after somebody has read them; the stale bot will close some of them in sixty days regardless of whether they mattered.

## Why Nobody Has Built This
The standard tooling was designed when the constraint was thought to be organisation, and it solved that: a labelled queue is better than an unlabelled one. Reducing the queue requires deflecting questions, detecting duplicates semantically and collecting sufficient information interactively, which needed capabilities that were not practical when the conventions were established and are now routine. Nobody has revisited the conventions since. And the maintainers who would benefit have no budget, which is why the tooling is contributed rather than built.

## What to Build
Change the composition rather than the labels. Answer the usage questions before they become issues, using the documentation, the prior issue corpus and the discussions — which is support deflection applied to a population with no support organisation and addresses the largest single share of the queue. Detect duplicates semantically at submission time and show the reporter the existing issue, since duplicate detection by lexical search fails on differently-worded reports and a maintainer recognising a duplicate is the expensive alternative. Collect sufficient information interactively rather than through a form: ask for what is missing, validate that a reproduction actually reproduces, and hold the report until it is actionable — which turns the first maintainer response from a request for information into a decision. Classify by what the maintainer must do rather than by subject, since the useful queue is grouped by decision type. Route to the right maintainer and to the community, since much of the queue does not need the core team at all and no mechanism directs it elsewhere. Retire by relevance rather than by age, because a stale bot closing a valid unaddressed defect is worse than leaving it open. And measure the queue's composition, since the tooling should be built against what is actually arriving and nobody has looked.

## Target Customer
Maintainer teams, the vendors employing them, foundations supporting large projects, and the code hosting platforms whose triage conventions are a decade old.

## Impact If Built
The queue's composition is dominated by questions, duplicates and incomplete reports, and the standard tooling addresses none of them. Deflection and semantic duplicate detection change the arithmetic rather than the presentation, which is the difference between organising a queue and reducing one.
