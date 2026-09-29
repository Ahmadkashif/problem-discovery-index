# Line Items Carry a Number and Not the Evidence Behind It

**Niche:** [[niches/cleaning-companies/facility-cost-data-publishers/profile|Facility & Construction Cost Data Publishers]]
**Industry:** [[industries/cleaning-companies|Cleaning Companies]]
**Type:** Fix (Pain Point)
**One-liner:** A cost engineer sets a productivity figure after weighing quotes, studies, and judgment, and the database stores the figure — so when it is challenged three years later, the defence is a person's recollection.
**Tags:** #tacit-knowledge-ml #large-language-models #bert #transformers #descriptive-statistics #evaluation-metrics #confidence-intervals #data-integration #worker-facing #workflow-orchestration

## The Problem
The database is used to justify bids, to support claims, and occasionally to argue about payment in front of an arbitrator, and its authority rests on the rigour of how each figure was derived. That derivation is not stored. A cost engineer researching a task gathers supplier quotes, consults time studies, weighs an unusual crew configuration, decides how much a regional labour practice matters, and writes a number. The reasoning exists in working files and in the engineer's head. When a subscriber challenges a figure, the response is reconstructed. When the engineer retires, the basis for several thousand line items becomes unavailable, and the next person maintaining them starts from a number they cannot interrogate — which in practice means they leave it alone, because revising a figure you cannot reconstruct is expensive and risky.

## Why It's Still Broken
The production system was built to publish a database, and a database stores values. The volume argues against documentation: an engineer maintaining thousands of line items under a release deadline treats every additional keystroke as real cost, and there has never been a structure that made the recording cheap. Institutionally, cost research has been treated as craft — the value of a senior engineer is precisely that they know what a figure should be — and the corollary that this knowledge is uninspectable and non-transferable has been accepted rather than examined.

## What a Fix Looks Like
A derivation record attached to every line item, captured as the work is done. It holds the sources consulted with their dates, the studies referenced, the judgments applied and their stated basis, the confidence the engineer holds in the figure, and — the highest-value field — what would cause the figure to change. That last item converts a static number into a standing trigger: when a wage determination moves or a material index breaks its historical relationship, the line items whose derivations depend on it surface themselves for review instead of waiting for the escalation cycle. Across the database the accumulated records support things that are impossible today: identifying figures resting on a single stale source, measuring consistency between engineers on comparable tasks, and answering a subscriber's challenge with an account rather than an assertion. It also makes maintenance transferable, which is the succession problem every cost publisher has and none has solved.

## Who Feels the Pain
Cost engineers inheriting thousands of figures they cannot interrogate and therefore do not revise; the research director with no instrument to measure consistency across a database whose entire value is consistency; subscribers whose challenged bids rest on figures the publisher can only defend from memory; and the business, whose most senior expertise is unrecorded and retiring.

## Impact If Fixed
Turns a collection of numbers into a body of evidence, which is the more defensible product and the more valuable one in the disputes where these figures are actually tested. It also unblocks the rest — outcome validation and targeted collection both need to know why a figure is what it is before they can say anything useful about whether it is right.
