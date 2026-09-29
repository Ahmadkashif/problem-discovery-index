# The Edge Case Discovered for the Fifth Time

**Niche:** [[niches/ai-agent-platforms/the-forward-deployed-engineer/profile|The Forward-Deployed Engineer]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The exception that breaks an agent at a fifth customer is one four colleagues have already found and fixed at four other customers, and none of them wrote it down anywhere the fifth could find.
**Tags:** #tacit-knowledge-ml #worker-facing #evaluation-metrics #k-means-clustering #descriptive-statistics #automation #quick-win #data-integration
**Contested on:** Every serious competitor in this niche is fighting to make a deployment work without a person living inside it — and whoever does that takes the account, because the delivery model is currently a headcount line that grows with revenue.

## The Problem
A support agent deployment breaks on a customer whose order was split across two shipments, one of which was returned. It is a genuinely awkward case and the engineer spends three days on it. Four other engineers have hit the same shape of case at four other retailers. Each solved it slightly differently, each fix lives in a customer-specific configuration, and none of them is discoverable by the fifth. The company has solved this problem five times, holds five slightly different answers, and has none of them in a form that would let the sixth customer avoid the problem entirely.

## Why It's Still Broken
Edge cases are found under deployment pressure and fixed in place, and documenting them is unbilled work at the worst possible moment. There is no system designed to hold them, so they land in customer configurations and in chat threads. Engineers are deployed rather than co-located, so the informal transfer that would normally happen does not. And the cost is entirely in repeated discovery, which nobody measures.

## What a Fix Looks Like
Capture the case, not just the fix. Record every edge case in a structured form — the situation, why the agent failed, the fix, the domain — at the moment it is solved, which is a few minutes when the context is fresh and impossible six months later. Index by domain and task shape so the fifth engineer finds it by describing their situation rather than by knowing it exists. Surface likely edge cases at deployment start based on the customer's vertical and systems, so a known case is designed for rather than discovered. Promote cases seen at three or more customers into the vertical template, which is the mechanism by which the library turns into product. Feed the cases into the evaluation set, since each is a test that should never regress. Report edge case reuse, which demonstrates the value and is what keeps the capture habit alive. Share resolution patterns rather than configurations, because the five slightly different answers usually share a structure worth naming. And review the library periodically to find the cases that should be handled by the platform rather than by five configurations, since a case appearing everywhere is a product gap wearing a deployment costume.

## Who Feels the Pain
Engineers rediscovering colleagues' work under deadline; customers whose deployment took three weeks longer for a known reason; and the company, paying five times for one piece of knowledge.

## Impact If Fixed
Five solutions exist and none is findable by the sixth engineer. Structured capture at the moment of resolution costs minutes and is impossible later, and promotion at three occurrences is the mechanism that turns a library into product.
