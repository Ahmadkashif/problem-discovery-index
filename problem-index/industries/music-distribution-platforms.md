# Music Distribution Platforms

## Profile
**Category:** Digital Media & Creator Economy
**Market Size:** ~$1.5B US revenue across independent distribution services, on top of several billion in royalties flowing through them to artists
**Tech Maturity:** Delivery is solved, accounting is not — DistroKid, TuneCore, CD Baby, UnitedMasters, Symphonic, Believe and Amuse push a release to every major streaming service in days, then reconcile royalty statements arriving in dozens of formats against a metadata layer that determines who gets paid and is wrong often enough to matter.
**Workforce:** Artist support and claims staff, metadata and content operations, royalty accounting and reconciliation, rights and publishing administration, integration engineers for DSP delivery, trust and safety for fraud and infringement

## Key Pain Themes
The business is a matching problem dressed as a distribution service. A stream occurs; the money for it must reach a recording owner and, separately, the writers and publishers of the underlying composition. Those two rights are administered by different systems with different identifiers, and the join between them depends on metadata supplied by whoever uploaded the track. When the metadata is wrong or incomplete, money accumulates unmatched — the mechanical licensing collective's unmatched pool being the most visible instance — and the eventual distribution of that pool is a contested question about whose money it actually is.

Around it sits the second structural problem: streaming manipulation. Artificial streams generated to inflate payouts draw from a fixed pool, so fraud is a transfer from every legitimate artist. The platforms respond with detection and penalties, and the enforcement falls on distributors and artists who are frequently unable to tell what triggered it or to contest it effectively.

And the people at the centre — the artist support agents handling claims, takedowns and payout questions — are explaining accounting systems they cannot see into, to people whose income depends on the answer.

## Current Tech Landscape
Delivery runs through the DDEX standard to each service's ingestion pipeline, with per-service specification quirks that are the actual work. Identifiers are ISRC for recordings and ISWC for compositions, with the persistent problem that the link between them is not authoritative anywhere. The Mechanical Licensing Collective administers US mechanical royalties for digital services and holds the unmatched pool. Royalty statements arrive monthly per service in proprietary formats and are normalised, matched and split by the distributor. Content identification systems handle infringement claims. Streaming services introduced minimum-stream thresholds and artificial streaming penalties from 2024, which pushed enforcement economics onto distributors.

## Problems
- [[problems/music-distribution-platforms/high-impact|🔴 High Impact: The Unmatched Pool]]
- [[problems/music-distribution-platforms/low-impact-1|🟡 Low Impact: Release Delivery and DSP Specification Compliance]]
- [[problems/music-distribution-platforms/low-impact-2|🟡 Low Impact: Streaming Manipulation Detection and Penalties]]
- [[problems/music-distribution-platforms/worker-life-1|🟢 Worker Life: The Artist Support Agent Explaining the Statement]]
- [[problems/music-distribution-platforms/worker-life-2|🟢 Worker Life: The Metadata Operations Reviewer]]
- [[problems/music-distribution-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/music-distribution-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
A distributor sits at the point where a piece of music becomes an identified, licensable asset, and the quality of what it records there determines whether the money finds its owner for as long as the recording exists. That is an unusually consequential data-entry problem, currently solved by asking an uploading artist to fill in a form. Distributors hold the largest corpora in existence of recordings matched to compositions, writers and splits — the exact training data for the matching problem the industry loses hundreds of millions of dollars to — and they use it to validate their own uploads. The industry-level matching failure is solvable with data the distributors already hold, and the obstacle is that no participant is paid for the money that reaches someone else.
