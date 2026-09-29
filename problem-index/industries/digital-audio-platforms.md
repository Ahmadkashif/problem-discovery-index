# Digital Audio Platforms

## Profile
**Category:** Digital Media & Creator Economy
**Market Size:** ~$18B US recorded music streaming revenue plus podcast and audiobook consumption on the same surfaces; Spotify, Apple Music, Amazon Music, YouTube Music, Pandora, SoundCloud, Tidal and Deezer hold the subscriber base
**Tech Maturity:** World-class recommendation, contested accounting. These platforms run some of the largest deployed recommender systems in existence and handle catalogues receiving well over a hundred thousand new tracks a day. The part that determines whether anyone gets paid — how a subscription fee is divided, which recording a stream belongs to, and whether the stream was a person — is the least examined and most disputed part of the business.
**Workforce:** Recommendation and personalisation engineers, editorial curators and music programmers, rights and royalty operations analysts, catalogue and metadata engineers, trust and integrity teams, artist and label relations

## Key Pain Themes
Royalties are allocated pro-rata: a rights holder receives a share of the total pool proportional to their share of total streams. That means a subscriber's fee does not follow their listening — it is pooled and redistributed toward whatever was most streamed overall. The alternative, allocating each subscriber's fee according to what they actually played, has been debated for a decade and adopted only partially. Policy changes at the major platforms since 2024 — minimum annual stream thresholds before a track earns, minimum play durations for functional audio — have reallocated real money and intensified the argument rather than settling it.

Fraud sits directly on top of that structure. Because the pool is fixed, artificially inflated streams do not create money, they take it from everyone else. Detection is adversarial and improving on both sides, and the platforms publish little about their own rates.

The third theme is matching. A recording arrives with metadata supplied by distributors and labels, and when it does not match a rights record cleanly the resulting royalty sits unattributed. The accumulated unmatched pool is a persistent and real sum, and the people whose work it belongs to generally do not know it exists.

## Current Tech Landscape
Spotify, Apple, Amazon and YouTube dominate subscription; Pandora and SiriusXM hold radio-style listening; SoundCloud and Audiomack serve the upload-first tier where most new music first appears. Distribution into them runs through DistroKid, TuneCore, CD Baby and the label supply chain. Rights administration involves publishers, collecting societies, and the Mechanical Licensing Collective in the United States, whose creation was itself a response to the unmatched-royalty problem. Audio understanding — embeddings, similarity, automatic tagging — is mature inside the platforms and is used almost entirely for recommendation rather than for rights or integrity.

## Problems
- [[problems/digital-audio-platforms/high-impact|🔴 High Impact: The Pool Pays by Share of Total Streams, Not by Who Anybody Listened To]]
- [[problems/digital-audio-platforms/low-impact-1|🟡 Low Impact: Discovery for a Catalogue Nobody Can Listen Through]]
- [[problems/digital-audio-platforms/low-impact-2|🟡 Low Impact: Metadata Matching and Unattributed Royalties]]
- [[problems/digital-audio-platforms/worker-life-1|🟢 Worker Life: The Curator Under Pitch Volume]]
- [[problems/digital-audio-platforms/worker-life-2|🟢 Worker Life: The Royalty Analyst Reconciling a Statement Nobody Believes]]
- [[problems/digital-audio-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/digital-audio-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These platforms know exactly what every subscriber listened to, for how long, and in what context — and then divide the money by a formula that deliberately discards most of that information. The pro-rata pool was a licensing convenience that became an entrenched settlement, and its consequences are now measurable: fraud is profitable because it redistributes from a fixed pot, niche and dedicated audiences subsidise mass listening, and the artists most affected have no way to audit any of it. Every quantity needed to compute the alternative allocations sits in the platform's own logs. The industry's central economic argument is therefore not a data problem at all; it is a question nobody has been willing to compute and publish.
