# Reviewer Assignment and Editorial Queue Triage

**Niche:** [[niches/accounting-firms-smb/tax-research-content-publishers/profile|Tax Research Content Publishers]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Every editorial update needs the right credentialed reviewer, but assignment runs on the managing editor's memory of who knows what — so work piles behind two or three overloaded specialists while other analysts sit idle.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #cross-validation #workflow-orchestration #worker-facing #tacit-knowledge-ml

## The Problem
Tax editorial work cannot be assigned by round-robin. A partnership basis question goes to the two people who genuinely understand subchapter K; a multistate apportionment update goes to the SALT specialist; an international provision goes to a shrinking pool of analysts with the relevant background. Managing editors hold this expertise map in their heads and assign from it. The predictable result is severe load imbalance — a handful of specialists become the bottleneck for large portions of the corpus, their queues run weeks deep during peak periods, and analysts with adjacent competence are underused because the editor does not have a precise enough picture of what they can safely take. When a specialist leaves, the map leaves with them and assignment degrades to guesswork for months.

## Why It's Still Broken
Editorial and content management systems model assignment as a field on a work item, not as a matching problem. They record who was assigned but hold no representation of who *should* be assigned, and no publisher has an explicit competence model of its own staff — expertise is inferred from job title and from the editor's recollection of past work. Building the model requires evidence the systems technically hold but never connect: who has authored or reviewed in each subject area, whose reviews on which topics produced few downstream corrections, and how long each analyst actually takes on work of a given type. That data sits scattered across revision histories, review logs, and time records with no join between them.

## What a Fix Looks Like
A competence and capacity layer over the existing editorial system. It builds a per-analyst profile from revision history, review activity, and correction rates within the publisher's own subject taxonomy — a learned picture of demonstrated competence rather than an assumed one. For each incoming work item it produces a ranked set of qualified reviewers with current queue depth and predicted turnaround attached, so the editor assigns against real capacity instead of memory. Two secondary behaviors matter as much as the primary one: the system surfaces single points of failure by flagging subject areas where fewer than two analysts are qualified, and it identifies adjacency — analysts whose demonstrated work suggests they could take an area with modest supervision — turning assignment into a deliberate way to widen bench strength rather than a way to reinforce the existing bottleneck.

## Who Feels the Pain
The two or three overloaded specialists whose queues never clear and who become the reason releases slip; the managing editor who is accountable for turnaround but assigns from recollection; and the mid-level analysts whose development stalls because nothing outside their assigned lane ever reaches them.

## Impact If Fixed
Rebalances load away from chokepoint specialists and shortens the tail of the editorial queue, which is what actually determines whether content is current when subscribers need it. Makes key-person risk visible and reducible rather than discovered at resignation. Preserves the assignment logic as institutional property instead of one person's memory.
