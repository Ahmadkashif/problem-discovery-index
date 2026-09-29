# Telemetry the Studio Did Not Have to Write

**Niche:** [[niches/indie-game-studios/playtest-and-demo-instrumentation/profile|Playtest & Demo Instrumentation]]
**Industry:** [[industries/indie-game-studios|Indie Game Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The demo is the strongest pre-launch signal a studio has and it returns a download count.
**Tags:** #automation #data-integration #evaluation-metrics #change-point-detection #survival-analysis #confidence-intervals #descriptive-statistics #k-means-clustering
**Contested on:** Every serious competitor in this niche is fighting to turn a playtest or a demo into a machine-readable account of where players stopped enjoying the game — and whoever does it best takes the account.

## The Problem
Playtests and demos are where a studio finds out whether the game is working, eighteen months before the number that matters. What comes back is impressions: someone seemed confused in the tutorial, a few people mentioned the second boss. What should come back is where sessions ended, how long the first fifteen minutes took across a hundred players, which mechanic nobody used, and whether the players who finished the demo wishlisted at a different rate from those who did not.

## Why Nobody Has Built This
Game analytics products are built for live-service titles with ongoing revenue, not for a pre-launch demo. Instrumenting a build is engineering time competing with making the game. Indie studios do not know what to measure. And nobody has connected demo behaviour to the wishlist outcome, which is the link that would make it obviously worth doing.

## What to Build
Instrument by default and report in design language. Ship a drop-in engine integration that emits a sensible default event set with no design work from the studio, which is the core — the reason this does not exist is that deciding what to instrument is itself the hard part, and a good default removes it. Produce a session funnel from launch to quit with the drop-off points named, since that single chart answers most of what a playtest is for. Cohort by build so the studio can see whether a change helped, which is the whole point of iterating and is currently unmeasurable. Link demo behaviour to wishlist conversion where the platform permits, as that is the connection to the commercial outcome. Detect the stuck player — long time in one area, repeated deaths, no progress — rather than only the quit. Aggregate qualitative feedback against the same session timeline so a comment lands where it happened. Report in the designer's vocabulary rather than in analytics terms, which is what determines whether it gets used. Compare against the studio's own earlier builds rather than against other games, which avoids the benchmark problem entirely. Keep the payload small and privacy-clean, since players are sensitive and platforms are stricter. And make it free for playtests, because the paid moment is later.

## Target Customer
Indie studios, publishers evaluating projects, playtest and user research services, and engine and middleware vendors.

## Impact If Built
Deciding what to instrument is itself the hard part, which is why studios ship uninstrumented demos. A drop-in default event set and a launch-to-quit funnel turn the strongest pre-launch signal into evidence.
