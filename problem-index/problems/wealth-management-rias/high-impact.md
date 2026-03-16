# Client Behavioral Risk Detection

**Industry:** [[wealth-management-rias|Wealth Management RIAs]]
**Type:** High Impact
**One-liner:** Advisors can sense when a client is about to panic-sell before the client says it explicitly — this tacit skill can be captured and scaled across every client relationship in the firm.
**Tags:** #gradient-boosting #bert #anomaly-detection #nlp #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
Experienced RIA advisors develop a sixth sense for client anxiety. They notice subtle shifts — emails that get shorter and more frequent, calls at unusual hours, specific phrases like "I just want to be safe" or "my neighbor moved to cash," tone changes in voicemails, or sudden requests for account balance checks after years of ignoring them. This pattern recognition prevents billions in AUM loss industry-wide, but it is entirely non-transferable: it lives in individual advisor heads, cannot be taught to junior advisors, and vanishes when an advisor retires or leaves the firm.

## Why It's Unsolved
The data collection challenge is severe: you need to capture the advisor's real-time assessment of client emotional state alongside the communication artifacts (emails, call logs, meeting notes) that triggered that assessment. Advisors disagree with each other and with themselves across time about what constitutes "pre-panic" behavior. Labeling is retrospective and biased — advisors remember the clients who did panic-sell but forget the false positives where they intervened or the client self-corrected. Deployment requires sub-24-hour latency to be useful, and the model must surface actionable alerts without generating so many false positives that advisors ignore the system entirely.

## What a Solution Looks Like
A model ingests all client communication metadata (email frequency, length, time-of-day, call duration, CRM note sentiment) alongside market context (portfolio drawdown magnitude, sector-specific losses, media fear indices). It outputs a daily risk score per client with an explanation of which behavioral signals changed. The advisor sees a prioritized list each morning: "These 5 clients show communication patterns consistent with emotional decision-making — here's what changed and a suggested outreach script."

## Impact If Solved
A mid-size RIA managing $500M in AUM could prevent 2-5% annual AUM loss from panic-driven withdrawals during market corrections, translating to $10-25M in retained assets and $100-250K in preserved annual revenue per downturn. Across the industry, this represents tens of billions in preventable AUM attrition.
