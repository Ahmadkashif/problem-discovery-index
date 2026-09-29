# The Fragility Knowledge That Leaves With the Person

**Niche:** [[niches/qa-test-automation-vendors/test-automation-engineer/profile|The Test Automation Engineer]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A test engineer knows which parts of the system are fragile, which changes always break something, and where the defects hide — and none of it is written down anywhere.
**Tags:** #tacit-knowledge-ml #bert #k-means-clustering #descriptive-statistics #evaluation-metrics #confidence-intervals #worker-facing #quick-win
**Contested on:** Every serious competitor that takes this seriously is fighting to return a test engineer's week from repair to design — and whoever does that takes the quality function, because repair is currently the job and design is what the role was created for.

## The Problem
An engineer who has tested a system for four years knows that a particular module breaks whenever anything near it changes, that a specific integration fails in a way that looks like something else, that two features interact badly under a condition nobody documented, and that a certain kind of change always needs a manual check. None of this is in the test suite, the documentation or anywhere else. They leave. Their successor rediscovers each of these over eighteen months, one production incident at a time, and the organisation experiences it as a quality dip with no identified cause.

## Why It's Still Broken
The knowledge is tacit and its holder does not experience it as knowledge — it is simply what they know, applied automatically, which is the classic reason tacit expertise is never documented. There is no place to put it: a test suite encodes what is verified rather than what is risky, and documentation is about how the system works rather than about where it breaks. Nobody asks for it, including at departure, where the handover covers process and access. And much of it is derivable from evidence nobody has assembled.

## What a Fix Looks Like
Derive what can be derived and capture the rest while the person is present. Compute the fragility map from history: which modules have the highest defect density, which changes have most often caused failures elsewhere, which components consistently break together, and which defects escaped and where — all of which are in the version control and incident record and reproduce a substantial share of what the engineer knows. Present it to the engineer for confirmation and extension, which is far easier than asking them to recall it unprompted and is the technique that works for tacit knowledge throughout this vault. Capture observations in the moment, since an engineer repairing a test notices fragility constantly and needs somewhere to record it in one line. Attach the knowledge to the code rather than to a document, so a person changing that module sees the warning rather than having to look for it. Include it in departure explicitly, as a structured conversation about where the system is risky rather than a process handover. And maintain it, since fragility moves and a stale map is a different kind of hazard.

## Who Feels the Pain
Successors rediscovering the same fragilities through production incidents; engineers whose most valuable knowledge has nowhere to go; and organisations whose quality degrades after a departure for reasons they never connect.

## Impact If Fixed
A substantial share of the fragility map is derivable from version control and incident history and is never computed. Presenting it for confirmation rather than asking for recall is what makes the remaining tacit portion obtainable, and attaching it to the code is what makes it reach the person who needs it.
