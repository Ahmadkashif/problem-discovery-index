# A Single Unit Across Every Surface

**Niche:** [[niches/esports-organizations/cross-surface-attention/profile|Cross-Surface Attention Aggregation]]
**Industry:** [[industries/esports-organizations|Esports Organizations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Six platforms report six incompatible metrics about the same audience and the organisation adds them together.
**Tags:** #data-integration #descriptive-statistics #evaluation-metrics #confidence-intervals #k-nearest-neighbors #automation #workflow-orchestration #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to turn a broadcast, a dozen streams, several short-form platforms and a set of social accounts into one comparable unit of attention — and whoever defines that unit takes the account.

## The Problem
A broadcast reports peak and average concurrents. A stream reports concurrents and hours watched. A short-form platform reports views counted after three seconds. A social account reports impressions. These are not the same thing and they overlap heavily: the fan watching the final is the same person who watched the player's stream and saw the clip. The organisation needs one figure it can defend, and the arithmetic to produce it has never been done.

## Why Nobody Has Built This
Each platform's data is behind a different interface with different granularity. Deduplication requires identity signals nobody has. The conversion between units involves judgement that could be challenged. And an honest number is smaller than the one currently used, which nobody wants to be first to publish.

## What to Build
Convert everything to time, then remove the double counting. Normalise every surface to attention time using platform-specific conversion factors with published assumptions, which is the core — the conversion is defensible only if the assumptions are visible, and that is what makes an honest smaller number sellable. Collect automatically from every available interface on a schedule, since manual collection is why this never happens. Estimate overlap between surfaces using the signals that exist — geography, timing, engagement patterns — because deduplicated reach is the figure sponsors ask for and nobody supplies. Report reach and frequency separately from total attention, as they answer different questions. Separate owned surfaces from borrowed ones, which sponsors will discount for anyway. Keep a historical series from day one so trends become available. Handle short-form's three-second view honestly rather than treating it as equivalent to a broadcast hour. Provide confidence ranges where the platform data is thin. Export in a format a media agency recognises, which is what determines whether it is used. And publish the methodology alongside the number, since credibility is the actual product here.

## Target Customer
Esports organisations, leagues and tournament operators, sponsorship agencies, and social analytics vendors.

## Impact If Built
The conversion between units is defensible only if the assumptions are visible, which is what makes an honest smaller number sellable. Normalising to attention time with estimated overlap produces the deduplicated reach sponsors have been asking for.
