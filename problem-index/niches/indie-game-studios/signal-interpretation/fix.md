# The Demo Nobody Instrumented

**Niche:** [[niches/indie-game-studios/signal-interpretation/profile|Signal Interpretation]]
**Industry:** [[industries/indie-game-studios|Indie Game Studios]]
**Type:** Fix (Pain Point)
**One-liner:** Four thousand people played the demo and the studio knows only how many downloaded it.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #automation #survival-analysis #confidence-intervals #worker-facing #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to turn a studio's own wishlist shape, demo retention and playtest behaviour into a commercial forecast — and whoever reads those signals best tells a two-person team what three years of their life is worth while they can still change it.

## The Problem
A demo is the single best commercial signal an indie studio ever gets before launch: real players, real behaviour, real drop-off. Most studios ship one with no instrumentation at all, so they learn a download count and a wishlist bump. How far players got, where they stopped, how long they played, whether they finished — all of it happened and none of it was recorded, and the opportunity does not come back.

## Why It's Still Broken
Instrumentation is a task with no deadline attached, so it is cut when the demo ships late — a step that nobody is waiting for is the first thing dropped under pressure. Telemetry feels like something bigger studios do. Privacy and player sentiment concerns are raised and rarely examined. And nobody has shown a studio what the data would have told them.

## What a Fix Looks Like
Instrument the demo before it ships. Record the basic funnel — started, reached each section, session length, quit point, completed — which is the fix and is a few hours of work that determines what the studio learns from thousands of players. Report the quit point distribution, since a concentration at one moment is an actionable design finding and is the most common thing a demo reveals. Measure session length and return, as a player who came back is a different signal from one who finished once. Compare against the studio's own playtest expectations, which will frequently be wrong in an informative way. Ship the instrumentation as a default in an engine template, because the barrier is effort rather than objection. Handle privacy transparently with an opt-out and a plain explanation, as the concern is legitimate and manageable. Report it during the demo period rather than afterwards, so the studio can act while the demo is live. Connect the funnel to the wishlist conversion, which is the commercial link. Keep the data for the next project, since a studio's own history is the beginning of their benchmark. And tell studios in advance what a demo could tell them, because most do not know.

## Who Feels the Pain
Studios who learned nothing from their best signal; designers guessing where players stopped; publishers evaluating a project with no behavioural data; and developers who discover at launch what a demo would have told them a year earlier.

## Impact If Fixed
A step that nobody is waiting for is the first thing dropped under pressure, and instrumentation has no deadline. A few hours of work before a demo ships turns thousands of players into the studio's only pre-launch behavioural evidence.
