# Niche Analysis — Digital Audio Platforms

**Parent Industry:** [[industries/digital-audio-platforms|Digital Audio Platforms]]

## Niche Selection

These platforms run some of the largest deployed recommender systems in existence over catalogues receiving well over a hundred thousand new tracks a day, and the part that determines whether anyone gets paid — how a subscription fee is divided, which recording a stream belongs to, and whether the stream was a person — is the least examined and most disputed part of the business. Royalties are pooled and divided by overall stream share, so a subscriber's fee does not follow their listening, fraud is profitable because it redistributes from a fixed pot, and niche audiences subsidise mass listening. Every quantity needed to compute the alternatives sits in the platform's own logs. The eight niches below split the category by what competitors actually fight over.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Royalty Allocation | 🔵 High Market Share | ~$5B | Very Low | Executive and rights leadership |
| 2 | Recommendation & Discovery | 🔵 High Market Share | ~$4.5B | Very High | Product and data leadership |
| 3 | Catalogue Matching & Metadata | 🟠 Low Digitized | ~$2.5B | Low | Rights operations leadership |
| 4 | Editorial Curation & Programming | 🟠 Low Digitized | ~$2B | Low | Editorial leadership |
| 5 | The Rights Operations Analyst | 🟣 Underserved Audience | ~$1.5B | Low | Operations leadership |
| 6 | The Independent Artist | 🟣 Underserved Audience | ~$1.3B | Low | Artist relations leadership |
| 7 | Catalogue Intake at Scale | ⚡ Highly Automatable | ~$800M | Medium | Catalogue engineering leadership |
| 8 | Listener Data & Artist Reporting | ⚡ Highly Automatable | ~$400M | Medium | Artist services leadership |

## Why These Niches

Royalty allocation takes the largest share because it decides where eighteen billion dollars goes and rests on a licensing convenience nobody has been willing to compute the alternatives to. Recommendation is level with it because it determines what is listened to and therefore what is earned, and is the category's strongest technical capability aimed at engagement. The two low-digitized niches are the ones performed against volume with thin tooling: matching recordings to rights records, and a small editorial team deciding what tens of millions of people hear. The two underserved audiences are the analyst explaining a payment they cannot derive and the independent artist with no way to audit anything. The two automatable niches are a hundred thousand daily arrivals and the reporting artists receive.

## Niches

- [[niches/digital-audio-platforms/royalty-allocation/profile|🔵 Royalty Allocation]]
  - [[niches/digital-audio-platforms/allocation-model-design/profile|🎯 Allocation Model Design]]
  - [[niches/digital-audio-platforms/stream-integrity/profile|🎯 Stream Integrity]]
- [[niches/digital-audio-platforms/recommendation-and-discovery/profile|🔵 Recommendation & Discovery]]
- [[niches/digital-audio-platforms/catalogue-matching-and-metadata/profile|🟠 Catalogue Matching & Metadata]]
- [[niches/digital-audio-platforms/editorial-curation-and-programming/profile|🟠 Editorial Curation & Programming]]
- [[niches/digital-audio-platforms/the-rights-operations-analyst/profile|🟣 The Rights Operations Analyst]]
- [[niches/digital-audio-platforms/the-independent-artist/profile|🟣 The Independent Artist]]
- [[niches/digital-audio-platforms/catalogue-intake-at-scale/profile|⚡ Catalogue Intake at Scale]]
- [[niches/digital-audio-platforms/listener-data-and-artist-reporting/profile|⚡ Listener Data & Artist Reporting]]

## Filter Notes

Seven of the eight level-1 niches are terminal. Royalty Allocation is not: the label names a function rather than a contest, and writing the contested statement produces two sentences whose winners are different companies. Allocation model design asks how the money should be divided — an economics and policy computation over data the platform already holds, where the winner is whoever computes and publishes what each allocation would actually pay. Stream integrity asks whether a stream was a person — an adversarial detection problem against an opponent improving in step, where the winner is whoever detects manipulation most accurately without penalising legitimate artists. One is an argument about a formula and the other is a contest against an adversary; the first is settled by economists and licensors and the second by detection engineers. It therefore decomposes into **Allocation Model Design** and **Stream Integrity**.

Two candidates were considered and rejected. **Getting recordings onto the platforms** is upstream of everything here but the contest over it belongs to [[industries/music-distribution-platforms|Music Distribution Platforms]]. **Video subscription streaming** shares the recommendation and content economics shape and is the contest of [[industries/streaming-video-platforms|Streaming Video Platforms]].
