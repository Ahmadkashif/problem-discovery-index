# Streaming Video Platforms

## Profile
**Category:** Digital Media & Creator Economy
**Market Size:** ~$60B US subscription and advertising revenue across direct-to-consumer streaming services and free ad-supported television
**Tech Maturity:** Exceptional delivery and recommendation, medieval commissioning — Netflix, Max, Disney+, Peacock, Paramount+, Tubi and Roku Channel deliver adaptive bitrate video globally at scale and personalise catalogues with sophisticated systems, then spend billions a year on content decided by executives using comparables, relationships and instinct because nobody can attribute a subscriber to a title.
**Workforce:** Content acquisition and commissioning executives, data science and personalisation teams, content operations and quality control, metadata and localisation staff, ad operations for the ad-supported tiers, streaming reliability engineers

## Key Pain Themes
The central unanswered question is what a title is worth. A platform observes every second of viewing across its entire subscriber base and cannot say which titles caused a signup, which prevented a cancellation, or which would have been watched by people who would have stayed anyway. The industry's substitute is completion rate and hours viewed, which measure consumption rather than causation, and which systematically overvalue titles watched by loyal subscribers who were never going to leave and undervalue the narrow title that holds a segment nobody else serves.

That single gap propagates. Commissioning is made on comparables. Renewal decisions are made on viewing thresholds whose relationship to retention is assumed. Licensing negotiations are conducted without a defensible valuation. Marketing spend is allocated to titles by anticipated audience rather than by measured incremental effect.

Around it sit the operational layers: a content operations function checking thousands of assets against platform and accessibility specifications, an advertising business on the ad-supported tiers whose measurement is weaker than the subscription side, and a reliability function whose failures are public and simultaneous.

## Current Tech Landscape
Delivery runs on adaptive bitrate streaming across multiple CDNs with per-title and per-scene encoding optimisation. Recommendation and artwork personalisation are mature and heavily invested in. Content operations handle ingest, transcoding, quality control, captioning, audio description and localisation at enormous volume. Measurement is internal and proprietary, with Nielsen providing a contested third-party view and the platforms publishing selective figures. The ad-supported tiers use standard CTV ad serving with frequency capping that works poorly across a fragmented supply chain. Rights and windowing are managed in systems that predate streaming and are frequently spreadsheets.

## Problems
- [[problems/streaming-video-platforms/high-impact|🔴 High Impact: No Title Has a Price]]
- [[problems/streaming-video-platforms/low-impact-1|🟡 Low Impact: Metadata, Artwork and Localisation]]
- [[problems/streaming-video-platforms/low-impact-2|🟡 Low Impact: Ad Tier Inventory and Frequency]]
- [[problems/streaming-video-platforms/worker-life-1|🟢 Worker Life: The Content Operations Specialist at Ingest]]
- [[problems/streaming-video-platforms/worker-life-2|🟢 Worker Life: The Reliability Engineer on Premiere Night]]
- [[problems/streaming-video-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/streaming-video-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
Streaming platforms hold the most complete record of media consumption ever assembled — every play, pause, abandonment and rewatch, by individual, over years, alongside the subscription decision. They have used it to build recommendation systems of real sophistication and have not used it to answer the question their entire cost base depends on, which is what any given title is worth in subscribers. That gap is not primarily technical: it is a causal inference problem with unusually good data and unusually poor experimental design, in an industry where the people who commission content have strong reasons to prefer that the number remain unknown. The platform that measures it credibly changes what it spends billions of dollars on.
