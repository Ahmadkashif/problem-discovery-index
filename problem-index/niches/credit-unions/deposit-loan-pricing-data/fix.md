# Peer Group Construction Is the Product and Is Undocumented

**Niche:** [[niches/credit-unions/deposit-loan-pricing-data/profile|Deposit & Loan Pricing Benchmark Data]]
**Industry:** [[industries/credit-unions|Credit Unions]]
**Type:** Fix (Pain Point)
**One-liner:** A benchmark is a peer set plus a statistic, the peer set is assembled by an analyst applying judgment about which institutions are genuinely comparable, and only the statistic is recorded.
**Tags:** #k-means-clustering #dimensionality-reduction #feature-engineering #evaluation-metrics #confidence-intervals #descriptive-statistics #tacit-knowledge-ml #data-integration #worker-facing #workflow-orchestration

## The Problem
The whole analytical act is deciding who counts as a peer. An institution's benchmark depends on market geography, asset size, field of membership, branch density, digital maturity, and competitive set, and an analyst weighs those to construct the comparison. That construction determines the number, and the deliverable records the number. When a client asks why their benchmark moved, or why it differs from a figure a competitor quoted, the answer requires reconstructing a peer set from memory. Two analysts building a benchmark for the same institution would produce different peer sets, and nobody measures how different, because the sets are not retained in a comparable form.

## Why It's Still Broken
Peer group construction has been treated as expertise rather than as method, which has been broadly true and therefore unexamined. The delivery system stores outputs because that is what clients receive, and adding a structured record of the construction reads as overhead against a delivery deadline. And clients have not pressed, because a benchmark that arrives with authority is easier to use than one that invites questions about its basis — until the moment it is challenged, which is exactly when the absence hurts most.

## What a Fix Looks Like
Peer sets as stored, versioned objects attached to every benchmark: which institutions were included, which were considered and excluded with the reason, and the criteria applied. Captured as the analysis is built rather than documented afterward. With that in place, several things follow that are impossible today. Consistency becomes measurable, since the same brief can be independently constructed and the sets compared. Recurring construction patterns become visible and promotable into house method, so judgment applied consistently by senior analysts becomes institutional rather than personal. Sensitivity becomes reportable — how much the benchmark moves under reasonable alternative peer definitions is the single most useful thing a client can be told about a figure they are about to act on. And a challenged benchmark can be explained in terms of its actual basis rather than defended by describing methodology in general terms.

## Who Feels the Pain
Analysts reconstructing peer logic colleagues have already worked out; the research director accountable for consistency across a book of benchmarks with no instrument to check it; clients setting rates on comparisons whose composition they cannot see; and the vendor, whose authority rests entirely on the credibility of a construction it does not record.

## Impact If Fixed
Turns the vendor's core skill from personal to institutional, which lifts both the consistency ceiling and the capacity ceiling. Sensitivity reporting is also a straightforward product improvement with an obvious buyer — a treasurer deciding a rate wants to know how robust the benchmark is, and today nobody can tell them.
