# Everyone Quit at the Same Place and Nobody Noticed

**Niche:** [[niches/indie-game-studios/playtest-and-demo-instrumentation/profile|Playtest & Demo Instrumentation]]
**Industry:** [[industries/indie-game-studios|Indie Game Studios]]
**Type:** Fix (Pain Point)
**One-liner:** Three hundred people played the demo, most stopped in the same five minutes, and the studio learned it from a review after launch.
**Tags:** #quick-win #automation #evaluation-metrics #descriptive-statistics #change-point-detection #survival-analysis #confidence-intervals #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn a playtest or a demo into a machine-readable account of where players stopped enjoying the game — and whoever does it best takes the account.

## The Problem
A common failure mode: a demo has a specific bad moment — an unclear objective, a difficulty spike, a control that nobody discovers — and a large share of players stop there. It is consistent, it is fixable in a day, and the studio cannot see it. They see downloads, a handful of Discord messages and, months later, reviews describing exactly the thing they could have fixed before launch.

## Why It's Still Broken
Nothing in the build records where the session ended — a failure that is uniform across hundreds of players is invisible without instrumentation, no matter how obvious it is in aggregate. Feedback channels surface the articulate minority. Small studios do not run structured playtests. And the cost of finding out is paid at launch, when it is too late.

## What a Fix Looks Like
Record the ending and surface the cluster. Log where every session ended and show the distribution, which is the fix and is a few hours of work that nobody does. Flag any location where an unusual share of sessions stop, since the whole insight is the concentration rather than the count. Show time-in-area against the studio's own expectation, as a spike is usually confusion rather than difficulty. Detect repeated failure and no progress, which is the stuck player the quit rate misses. Link Discord and form feedback to the point in the session it refers to, so scattered comments accumulate into a location. Compare the current build against the last one, which is how a studio learns whether the fix worked. Report the top three problem locations rather than a dashboard, because a small team will read three things. Cover the playtest as well as the demo, since the same instrumentation serves both. Sample rather than record everything, which keeps it cheap and private. And run it before the demo goes wide, as the value is entirely in the timing.

## Who Feels the Pain
Studios reading reviews describing a fixable problem; designers who suspected something and could not confirm it; players who stopped and never said why; and the launch that underperformed for a reason discovered afterwards.

## Impact If Fixed
A failure uniform across hundreds of players is invisible without instrumentation, no matter how obvious it is in aggregate. Logging where sessions end and flagging the concentration is hours of work that changes the launch.
