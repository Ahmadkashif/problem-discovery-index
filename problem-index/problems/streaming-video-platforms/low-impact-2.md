# Ad Tier Inventory and Frequency

**Industry:** [[streaming-video-platforms|Streaming Video Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The ad-supported tiers sell inventory that must be forecast, filled and frequency-capped across a supply chain that makes capping structurally difficult, and viewers notice.
**Tags:** #time-series-forecasting #gradient-boosting #convex-optimization #confidence-intervals #evaluation-metrics #feature-engineering #workflow-orchestration #revenue-impact

## The Problem
An ad-supported tier must forecast how many impressions it will have, by audience segment, weeks ahead, so that it can be sold. Viewing is variable and driven by content releases, so the forecast is coupled to a content calendar that changes.

Delivery is a constrained allocation problem. Guaranteed campaigns must deliver in full against their targeting and pacing; programmatic demand fills the remainder; competitive separation rules prevent conflicting advertisers in the same break; and frequency caps limit how often a viewer sees the same creative.

Frequency is where it visibly fails. Viewers on ad-supported streaming routinely report seeing the same advertisement repeatedly within a single session, which is an experience problem that damages both the viewer relationship and the advertiser's outcome. It happens because supply is fragmented across the platform's own sales, programmatic exchanges and third-party demand, each capping within its own view, with no shared identity across them.

Ad load is a tradeoff with a long tail. More advertising per hour increases immediate revenue and depresses viewing and retention, and the second effect is deferred and rarely measured with the rigour applied to the first.

Measurement on the ad side is weaker than on the subscription side. Reach, frequency and outcome attribution across connected television are contested, and the platform's own numbers are frequently disputed by advertisers and by third-party measurement.

## What Already Exists
Connected television ad serving is a developed category. Programmatic guaranteed and private marketplace deals are standard. Frequency capping exists per demand source. Identity resolution across household devices uses IP and account signals. Third-party measurement is provided by several contested vendors. Ad load policies are set per platform.

## The Customisation Gap
Inventory forecasting is coupled to a content calendar in a way most systems do not model. Viewing spikes with releases, and forecasting impressions by segment requires forecasting the content's audience, which is the same problem as the title valuation question one layer removed.

Cross-source frequency management is the most visible unsolved problem and requires a unified view across all demand sources at the platform level, which is architecturally possible and organisationally awkward.

Ad load optimisation against long-run retention is not attempted at the rigour it deserves. The correct ad load is the one maximising lifetime value, and that requires an experiment spanning months rather than a revenue comparison spanning a week.

Creative fatigue is unmodelled. The point at which repeated exposure stops working and starts harming is estimable from viewing and outcome data and is currently handled with a fixed cap.

And pod construction — which ads go together in a break, in what order — affects completion and viewer tolerance and is largely rule-driven.

## Impact If Solved
The ad-supported tiers are the growth story in streaming and their viewer experience is visibly worse than it needs to be for reasons that are architectural rather than inevitable. Unified frequency management, content-coupled inventory forecasting and ad load optimised against retention rather than immediate revenue address the experience problem and the revenue problem at the same point.
