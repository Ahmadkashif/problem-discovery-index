# Weeks of Work on a Guess

**Niche:** [[niches/digital-goods-marketplaces/creator-opportunity-intelligence/profile|Creator Opportunity Intelligence]]
**Industry:** [[industries/digital-goods-marketplaces|Digital Goods Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The platform observes exactly what buyers wanted and could not find, and creators spend weeks making things on a guess and find out months later.
**Tags:** #time-series-forecasting #gradient-boosting #evaluation-metrics #descriptive-statistics #revenue-impact #confidence-intervals #word-embeddings #recurrent-forecasting
**Contested on:** Every serious competitor in this niche is fighting to tell a creator what to make next from the demand the platform already observes — and whoever does that controls the supply side of the marketplace.

## The Problem
A creator spends three weeks building a template set. They chose the subject because they saw something similar selling, which means they entered a category at the point of maximum saturation. It earns eleven dollars. Meanwhile, four hundred buyers a week search for a specific thing the catalogue does not contain, abandon their sessions, and leave. The platform has both facts — the unserved query volume and the saturated category — and the creator, whose livelihood depends on choosing correctly, is shown a bestsellers list, which is a list of what is already crowded.

## Why Nobody Has Built This
Platforms optimise for buyer conversion and treat supply as self-organising, so nobody owns telling creators what to make. Search logs live with the discovery team and have never been framed as a supply signal. Telling creators what to build invites blame when it does not sell. And the bestsellers list is easy, popular and actively harmful in a way that is not obvious.

## What to Build
Turn observed demand into a creator-facing product. Report unmet demand directly — queries with high volume and low satisfaction, sessions that ended without a purchase, results consistently viewed and rejected — which is the core and is a straightforward computation on logs the platform already keeps. Measure saturation alongside it, since demand without supply context is how creators end up entering crowded categories, and the platform is the only party that can measure both. Forecast the revenue for a candidate asset with an honest interval, because a creator deciding whether to spend three weeks needs a range and a confidence rather than an encouraging signal. Distinguish a durable gap from a passing one, as a fad that has already peaked is the most expensive thing a creator can chase. Personalise to the creator's demonstrated skills and style, since a gap they cannot credibly fill is not an opportunity for them. Tell them why an existing asset underperformed — not found, found and rejected, or found and too expensive — which are three different problems with three different fixes and are currently indistinguishable from a sales figure. Surface the specific missing variant, since most gaps are a format, a size, a language or a colourway of something that already exists, which is days of work rather than weeks. Ration and stagger recommendations, because telling every creator the same gap fills it overnight and reproduces the saturation problem. Feed compatibility and licence gaps in too, since an asset that exists but does not work for the buyer's environment is also unmet demand. And publish the accuracy of past recommendations, because a supply-side product that never reports its own record is indistinguishable from the bestseller list it replaces.

## Target Customer
Digital goods marketplaces, creators choosing what to make, and the creator communities currently guessing collectively.

## Impact If Built
The bestsellers list sends creators into the most crowded categories while four hundred unserved searches a week go unreported. Unmet demand and saturation are both computable from logs already kept, and the missing-variant case turns weeks of speculative work into days.
