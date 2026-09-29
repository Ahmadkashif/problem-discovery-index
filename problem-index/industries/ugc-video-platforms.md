# UGC Video Platforms

## Profile
**Category:** Digital Media & Creator Economy
**Market Size:** ~$70B US advertising and subscription revenue across user-generated video; YouTube, TikTok, Instagram Reels, Snapchat, Twitch, Kick and Rumble hold essentially all of it
**Tech Maturity:** Among the most advanced systems operating anywhere, with a governance layer that has not kept pace. Recommendation, transcoding, live delivery and content matching at these platforms are extraordinary engineering. The decisions that determine whether a person can earn a living — whether a video is removed, demonetised, or suppressed in distribution — are made by classifiers that cannot explain themselves, at a volume no appeal process has ever been resourced to handle.
**Workforce:** Recommendation and infrastructure engineers, trust and safety policy specialists, content moderators largely employed through outsourcing vendors, creator support and partner managers, rights and copyright operations staff

## Key Pain Themes
Enforcement at this scale is automated by necessity and consequential in the individual case. A video is removed, a channel demonetised, or — most often and least visibly — a video's distribution is quietly reduced. The creator receives a policy category and no specifics, appeals into a queue, and frequently receives a decision with no more explanation than the first. For someone whose income depends on the platform, that is an economic determination made by a system they cannot see, contest meaningfully or learn from.

The copyright layer has a similar shape with an additional problem: the dispute mechanism can be used as a weapon. Automated matching generates claims, revenue is redirected while a dispute runs, and the incentive structure rewards claiming broadly. Creators describe claims on public domain material, on their own original audio, and on fragments too short to constitute anything — each individually small and collectively a meaningful transfer.

The third is the human cost of the review layer. The material that classifiers escalate is reviewed by people, most of them employed through outsourcing vendors, and the occupational harm of sustained exposure to the worst content on the internet is documented in litigation, in reporting and in the platforms' own policies. The work is concentrated in lower-cost labour markets, performed under throughput targets, with support provisions that reporting has repeatedly found inadequate.

## Current Tech Landscape
Recommendation systems at these platforms are the reference implementations for the field. Content matching — Content ID and its equivalents — operates at enormous scale against reference libraries supplied by rights holders. Moderation combines classifiers with human review through vendors including Accenture, Teleperformance, Majorel and others. Appeals are handled through ticketing systems with limited context. Creator-facing analytics are rich on audience and thin on enforcement. Regulatory pressure — the EU's Digital Services Act above all — has begun to require statements of reasons and appeal mechanisms that the systems were not built to produce.

## Problems
- [[problems/ugc-video-platforms/high-impact|🔴 High Impact: Livelihood Decisions Made by Systems That Cannot Explain Themselves]]
- [[problems/ugc-video-platforms/low-impact-1|🟡 Low Impact: Copyright Matching and Weaponised Claims]]
- [[problems/ugc-video-platforms/low-impact-2|🟡 Low Impact: Recommendation Objectives Beyond Watch Time]]
- [[problems/ugc-video-platforms/worker-life-1|🟢 Worker Life: The Content Moderator]]
- [[problems/ugc-video-platforms/worker-life-2|🟢 Worker Life: The Partner Manager Explaining a Decision They Cannot See]]
- [[problems/ugc-video-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/ugc-video-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These platforms have built the most capable content understanding systems in existence and applied almost none of that capability to the governance side of their own operation. A classifier that can identify a subject, a context and a tone well enough to rank a billion videos could also state which passage of a video triggered an enforcement decision and how confident it was — and the absence of that is a product decision rather than a technical limit. The same is true of the review layer: the volume of distressing material a human sees is a function of how much pre-classification is deployed to spare them, and the platforms' own models are the most capable tool available for reducing it. The gap between what these systems can do and what they are pointed at is the largest single opportunity in this industry, and regulatory requirements for reasoned decisions are closing it from the outside rather than the inside.
