# A Power-Ratio Explainer the Station Group Will Believe

**Niche:** [[niches/media-rep-firms/national-spot-tv-representation/profile|National Spot TV Representation]]
**Industry:** [[industries/media-rep-firms|Media Representative Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every rep reports power ratio to its station groups; none can say how much of a change came from ratings, how much from pricing and how much from buyers moving money, which is the question the renewal turns on.
**Tags:** #bayesian-inference #causal-inference #confidence-intervals #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to lift each represented station's power ratio, its share of the national dollars in its market against its share of the audience, and whoever proves that lift, market by market, keeps the station group when the rep contract comes up.

## The Problem
A station group reviewing its rep looks at power ratio by station and quarter. When it falls, the rep explains: the news ratings dropped, a competitor priced aggressively, an agency moved a client's money to streaming. Each explanation may be true. None is quantified, because nobody has decomposed the change. The group cannot tell a rep that is losing share through weak pricing from one that is holding share in a falling market, and the rep cannot prove which it is.

## Why Nobody Has Built This
The inputs belong to different parties: orders to the station, share to a pooled revenue report under subscription terms, ratings to the measurement vendor, proposals and counters partly in the agency's system. Rep firms' research teams produce decks, not models, and a decomposition that showed pricing losses would be uncomfortable to share.

## What to Build
A model per station and quarter that splits power-ratio change into an audience component (ratings and share of viewing), a price component (the station's CPP against market clearing levels) and an allocation component (agency and advertiser mix shifts). It is built from the rep's orders and proposals, pooled revenue share by agency and category, ratings, and occurrence data, with credible intervals rather than point claims. It produces a renewal pack: where the rep added share, where it lost share, and why.

## Target Customer
EVPs of sales at the two national TV rep firms, and station group EVPs of national sales choosing between a rep and an in-house desk.

## Impact If Built
A rep that can evidence its share contribution defends contracts that run up to ten years. A station group gets a fair basis to judge its rep or its own desk.
