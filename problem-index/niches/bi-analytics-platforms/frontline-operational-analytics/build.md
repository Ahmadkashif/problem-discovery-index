# A Dashboard for Someone With Both Hands Full

**Niche:** [[niches/bi-analytics-platforms/frontline-operational-analytics/profile|Frontline Operational Analytics]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The people making the most frequent operational decisions have the least analytical support, and giving them a smaller version of an analyst's dashboard has failed everywhere it has been tried.
**Tags:** #gradient-boosting #time-series-forecasting #decision-trees #causal-inference #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor here is fighting to put a decision-shaped answer in front of someone standing on a shop floor in the moment they can act on it — and whoever does that takes the operations account, because a dashboard nobody on shift opens is worth nothing.

## The Problem
A shift supervisor has forty seconds between a machine stopping and deciding what to do about it. The company has invested heavily in analytics: there is a production dashboard, a mobile app, and a screen on the wall showing throughput against target. None of them tells the supervisor whether to reallocate the two operators to the other line or wait for maintenance, which is the decision in front of them. They decide from experience, which is usually right and is entirely undocumented, and the analytics investment plays no part in the highest-frequency decision-making in the building.

## Why Nobody Has Built This
The category's design assumptions — a large screen, exploration, an analytically trained user with time — are wrong in every respect for this user, and the industry's response has been responsive layout rather than a different product. The decisions are also vertical-specific, so building for them means understanding a shop floor or a ward rather than building a generic tool, which is uncomfortable for horizontal software companies. And the buyer is operations rather than the data team, which is a different sale through a different door, with a different and much shorter tolerance for anything that does not immediately work.

## What to Build
Decision support rather than data presentation. Enumerate the recurring decisions for a role — the eight or ten things a shift supervisor actually decides in a day — which is a bounded and knowable list and is the piece nobody has written down. For each, deliver a recommendation with the two or three facts that drive it and an honest confidence, at the moment it is needed, pushed rather than pulled, on a phone or a handheld in an interface readable at arm's length in three seconds. Capture the decision made and the outcome, which is what makes the system improve and which is also the first record any of these organisations will have of how their frontline decisions are actually taken. Learn from the operators who are consistently right, since the experienced supervisor's judgement is the benchmark rather than the thing being replaced — the system should encode what they do and give it to everyone else, which is also the framing that determines whether the frontline accepts it. And measure the outcome in operational terms, because a supervisor will not adopt a tool on the basis of a data team's dashboard-usage metric.

## Target Customer
Operations leadership in retail, manufacturing, logistics, healthcare and hospitality; and the vertical operational software vendors already present on these floors, for whom this is the analytical layer they lack.

## Impact If Built
The highest-frequency, most consequential decisions in the operational economy are made with no analytical support by people the category never designed for. The decision list is bounded and the outcome capture is the part that compounds, since no organisation currently has any record of frontline decision quality.
