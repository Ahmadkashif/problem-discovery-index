# Media & Large Object Delivery

**Parent Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor here is fighting to deliver a byte more cheaply while holding playback quality — and whoever does that takes the media account, because egress is a dominant cost line and quality of experience is the product.

## Profile
**Market Size:** ~$2.2B US media and large object delivery
**Share of Parent Industry:** ~24% of category revenue
**Digital Adoption:** Very High
**Target Buyer:** Media operations and streaming engineering
**Automation Potential:** High — bitrate selection, prefetch and peak management are all optimisable

## What Makes This a Distinct Niche
Media delivery is a volume business with a quality constraint. The unit economics are unforgiving: egress is frequently the largest cost line in a streaming operation, and the difference between providers on price per delivered byte translates directly into margin. The technical contest is correspondingly specific: origin offload determines how much of the library has to be served from origin, prefetch and warming determine whether a newly released title is cached before the audience arrives, peak capacity determines what happens during a live event, and the interaction between the player's bitrate adaptation and the network's behaviour determines whether the viewer sees buffering. None of this resembles the dynamic application contest, and the buyers — media operations teams with a cost per stream target — are a different population from application platform engineering.

## Current Tools & Gaps
Delivery networks with tiered caching, multi-CDN steering products, adaptive bitrate packaging, and quality of experience monitoring from specialist vendors. The gaps: quality of experience is measured by one set of vendors and delivery is configured by another, so the join that would show which delivery decisions affect viewers is absent; prefetching and cache warming for a known release are manual; peak capacity for a live event is arranged by a conversation with the provider rather than modelled; bitrate ladder decisions are made by encoding teams with no delivery cost input, although they determine the egress bill; and per-title and per-region cost is rarely computed, so nobody knows which content is expensive to serve.

## Problems
- [[niches/edge-cdn-providers/media-large-object-delivery/build|🔨 Build: The Bitrate Ladder Nobody Prices]]
- [[niches/edge-cdn-providers/media-large-object-delivery/buy|🛒 Buy: Prefetching and Demand Forecasting]]
- [[niches/edge-cdn-providers/media-large-object-delivery/fix|🔧 Fix: Quality Measured by One Vendor, Delivery Configured by Another]]
