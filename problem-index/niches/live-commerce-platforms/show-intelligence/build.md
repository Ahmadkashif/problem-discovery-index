# The Richest Commerce Data Nobody Models

**Niche:** [[niches/live-commerce-platforms/show-intelligence/profile|Show Intelligence]]
**Industry:** [[industries/live-commerce-platforms|Live Commerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Platforms hold second-by-second records of what was shown, said and bought — stimulus and response on one timeline — and use it to rank streams by engagement.
**Tags:** #transformers #large-language-models #causal-inference #gradient-boosting #time-series-forecasting #evaluation-metrics #revenue-impact #object-detection
**Contested on:** Every serious competitor in this niche is fighting to turn the second-by-second record of what was shown, said and bought into what a host should do next — and whoever does that owns the only proprietary asset the category has.

## The Problem
At 9:47:12 the host held up a jacket. At 9:47:19 they said it runs small. At 9:47:24 viewer count rose. At 9:47:31 forty people tapped. At 9:47:38 it sold. The platform has all of it — the video, the transcript, the room, the transaction — aligned to the second, across millions of shows. Every other commerce business would pay enormously for a dataset where the sales pitch and the purchase are recorded together. The platforms compute gross merchandise value per show and a viewer curve, and the host is told they had a good night.

## Why Nobody Has Built This
Analytics is built for the viewer-side ranking problem, and the seller-facing surface is a reporting afterthought. Using the video and audio requires understanding both at scale, which was expensive until recently. Attribution inside a stream is genuinely hard because everything is confounded with everything and naive correlation produces advice that is worse than none. And sellers are not the buyer, so nobody funds it.

## What to Build
Model the show as stimulus and response. Align video, transcript, room state and transactions on one timeline as the base representation, which is the foundation and is mostly a plumbing exercise the platforms have not done. Attribute purchases to what was shown and said with the confounding handled properly — order, time, price, audience composition and the host's own tendencies all move together, and this is where a careless version produces confident nonsense. Learn which descriptions actually sell, since the host's words are the treatment and this is the only commerce setting where the pitch is recorded; the finding that a specific disclosure raises conversion is worth more than any dashboard. Analyse pacing and ordering to find where rooms empty and where they fill, which is the largest controllable variable a host has. Give pricing feedback from the room's response, since a host who sells everything in four seconds is pricing too low and has no way to know. Benchmark against comparable hosts rather than against the platform average, which is the only comparison that means anything to a seller. Recommend forward — what to show, in what order, at what time, at what price — because a diagnosis without a next action does not change behaviour. Feed the same signals into discovery, since what works in a show predicts who should see it. And let hosts run a genuine experiment across shows, which is possible here and rare anywhere.

## Target Customer
Live commerce platforms, live sellers and host agencies, and the brands running live selling as a channel.

## Impact If Built
The pitch and the purchase are recorded together, which is true in no other commerce format, and the output is a viewer count. Handling the confounding properly is what separates real attribution from confident nonsense, and forward recommendations are what change a host's behaviour.
