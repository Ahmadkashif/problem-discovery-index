# Matchmaker Objective Design

**Parent Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this niche is fighting to turn measured experience costs into a matchmaking policy that runs in milliseconds against a live queue — and whoever builds that policy engine takes the account.

## Profile
**Market Size:** ~$350M US
**Share of Parent Industry:** ~12% of category revenue
**Digital Adoption:** High but hand-tuned
**Target Buyer:** Platform engineering leadership
**Automation Potential:** High — policy optimisation under real-time constraints

## What Makes This a Distinct Niche
This half consumes the measurement and turns it into behaviour. Given what a bad match, a long queue and excess latency cost, the matchmaker must decide in milliseconds whether to start now or wait, and where to place the session — across a queue whose composition changes continuously, at peak and at four in the morning, in dense and thin regions. It is an optimisation and systems problem sold to the platform team, entirely separable from who produced the cost estimates.

## Current Tools & Gaps
A weighted scoring function, expanding search bands over time, and a latency cap. The gaps: greedy per-match decisions rather than queue-level optimisation; no adaptation to population density; no per-mode policy; no continuous validation; and no principled handling of thin populations.

## Problems
- [[niches/game-hosting-providers/matchmaker-objective-design/build|🔨 Build: Policy Instead of Weights]]
- [[niches/game-hosting-providers/matchmaker-objective-design/buy|🛒 Buy: Real-Time Dispatch From Ride-Hailing]]
- [[niches/game-hosting-providers/matchmaker-objective-design/fix|🔧 Fix: Four in the Morning in a Small Region]]
