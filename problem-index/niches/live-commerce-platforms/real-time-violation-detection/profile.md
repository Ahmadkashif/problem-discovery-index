# Real-Time Violation Detection

**Parent Industry:** [[industries/live-commerce-platforms|Live Commerce Platforms]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to catch a violation while it is still airing rather than after it has been broadcast — and whoever closes that gap defines what the platform can safely allow to go live.

## Profile
**Market Size:** ~$1.3B US
**Share of Parent Industry:** ~10% of category revenue
**Digital Adoption:** Medium — classification exists, latency does not
**Target Buyer:** Trust and safety engineering
**Automation Potential:** Very High — the task is streaming classification

## What Makes This a Distinct Niche
Content classification for video, audio and text is mature and available as a service, and moderating a live stream is a different problem because the violation is broadcast before anyone can act. Every classifier in the field is built to answer a question about a finished artefact; here the artefact is being created, the evidence accrues over time, and the answer is worth much less a minute later. The contest is latency and context together — a fast classifier with no memory of the last five minutes misses almost everything that matters in live commerce, where violations are usually escalations and counterfeit claims rather than single frames.

## Current Tools & Gaps
Frame-sampled visual classification, audio transcription with keyword matching, chat text classifiers, and human review after the fact. The gaps: classification on isolated frames with no temporal context; no modelling of escalation across a stream; no detection of the category's own violations — counterfeits, prohibited goods, false claims — as opposed to generic content harms; no calibrated confidence; and no feedback loop from moderator decisions.

## Problems
- [[niches/live-commerce-platforms/real-time-violation-detection/build|🔨 Build: Detected After It Aired]]
- [[niches/live-commerce-platforms/real-time-violation-detection/buy|🛒 Buy: Content Classification Practice]]
- [[niches/live-commerce-platforms/real-time-violation-detection/fix|🔧 Fix: The Model That Cries Wolf at Scissors]]
