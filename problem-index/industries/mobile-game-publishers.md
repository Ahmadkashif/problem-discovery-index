# Mobile Game Publishers

## Profile
**Category:** Gaming & Interactive
**Market Size:** ~$25B US mobile game consumer spending plus in-game advertising revenue; Zynga, Playtika, Scopely, SciPlay, Moon Active, Voodoo, Homa and Tripledot hold much of the Western publishing tier
**Tech Maturity:** Industrial testing machinery pointed at a very short signal. These publishers run prototype funnels at scale — dozens of concepts a month, small paid tests, kill decisions on retention thresholds — alongside sophisticated live monetisation and user acquisition. The thresholds that decide which games live are largely inherited folklore, and the model that predicts a 180-day outcome sees three days.
**Workforce:** Prototype and game teams, user acquisition managers, monetisation and live product managers, data scientists and analysts, publishing and partner managers working with external studios

## Key Pain Themes
The publishing model is a funnel: build many cheap prototypes, run small install campaigns, measure early retention and cost per install, kill the overwhelming majority within weeks, and scale the survivors. That funnel was built for hypercasual games with shallow depth and cheap acquisition, and it survived the collapse of that model — when tracking restrictions raised acquisition costs, the industry moved to hybridcasual and hybrid monetisation while keeping the same three-day kill metrics designed for a different economic structure.

The second theme is that the kill decision is made on a signal with enormous uncertainty. Day-one retention on a few thousand installs, compared against a threshold, decides whether a team's three weeks of work continues. The relationship between that number and eventual performance is weak and heavily genre-dependent, and the threshold is rarely derived from the publisher's own outcome history.

The third is revenue concentration. A small fraction of players produce most in-app purchase revenue, and monetisation design is consequently optimised around that fraction. The design patterns that follow — limited-time offers, escalating bundles, randomised rewards — have drawn regulatory attention in several European jurisdictions and consumer protection scrutiny elsewhere, and publishers largely measure their effect on revenue rather than on the players generating it.

## Current Tech Landscape
Unity and custom engines underpin production; LiveOps, remote configuration and A/B testing platforms run the live side. User acquisition runs through Meta, Google, AppLovin, Moloco, Unity and ironSource under SKAdNetwork and its successors. Analytics runs on internal stacks plus GameAnalytics, Amplitude and similar. Mediation and ad monetisation run through AppLovin MAX, LevelPlay and Google's stack. Soft launch in selected geographies remains the standard pre-scale validation. Prototype testing is increasingly automated into a repeatable internal pipeline at the larger publishers.

## Problems
- [[problems/mobile-game-publishers/high-impact|🔴 High Impact: Killing Most Prototypes on Three Days of Data]]
- [[problems/mobile-game-publishers/low-impact-1|🟡 Low Impact: Soft Launch Geography and Readout]]
- [[problems/mobile-game-publishers/low-impact-2|🟡 Low Impact: Hybrid Monetisation Configuration]]
- [[problems/mobile-game-publishers/worker-life-1|🟢 Worker Life: The Developer Whose Game Is Killed Every Three Weeks]]
- [[problems/mobile-game-publishers/worker-life-2|🟢 Worker Life: The Product Manager Who Knows Where the Revenue Comes From]]
- [[problems/mobile-game-publishers/ml-opportunity|🧠 ML Opportunities]]
- [[problems/mobile-game-publishers/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
A mobile publisher runs the largest continuous experiment in consumer product design that exists anywhere — hundreds of games tested against real audiences, with complete behavioural telemetry and known outcomes — and uses it almost entirely to make binary kill decisions against inherited thresholds. The accumulated record of which prototypes were killed, which survived, and what happened to them is the material for a genuinely better selection model, and it is also contaminated by the funnel itself: nobody knows what the killed games would have done, so the evidence base for every threshold is the population that passed it. Fixing that requires deliberately letting some failures through, which costs money visibly and saves it invisibly — the same shape as the measurement problems running through this whole segment.
