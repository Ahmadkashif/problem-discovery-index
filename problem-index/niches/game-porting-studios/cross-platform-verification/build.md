# Verification That Scales With Platforms

**Niche:** [[niches/game-porting-studios/cross-platform-verification/profile|Cross-Platform Verification]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Verification cost multiplies with every platform and every client patch, and the method is people playing.
**Tags:** #automation #workflow-orchestration #evaluation-metrics #object-detection #change-point-detection #data-integration #confidence-intervals #cnns
**Contested on:** Every serious competitor in this niche is fighting to verify every change on every platform when verification means people playing the game and the client keeps shipping updates — and whoever automates that takes the account.

## The Problem
A port to four platforms means every change must be verified four times, by people, playing. The client ships a patch and the completed verification is invalidated. The cost scales with platforms multiplied by builds, and the method does not scale at all. It is the largest recurring cost in most projects and the one that most often consumes the schedule, and the studios respond by hiring more testers because there is no alternative on offer.

## Why Nobody Has Built This
Game test automation is genuinely hard — the output is a rendered frame and the input is a controller. Each project is bespoke, so automation investment does not amortise. Console devkits complicate infrastructure. And the cost is billable, which weakens the incentive to remove it.

## What to Build
Automate the repetitive passes and let people test what only people can. Build automated playthroughs that traverse the game deterministically and capture output, which is the core and turns the repeated regression pass from a week into a night. Compare rendered output across platforms automatically with tolerance for legitimate differences, since visual divergence is the commonest port defect and is mechanically detectable. Detect performance regressions automatically per build and per platform, as frame time is the thing that most needs continuous measurement and is currently sampled by hand. Scope the test selection to what the change actually touched rather than re-running everything, which is where most of the waste is. Run the full pass overnight on devkit farms so mornings start with results. Capture crash and hang state automatically with enough context to diagnose. Reuse the traversal across builds and platforms, which is what makes the investment amortise. Report per-platform divergence rather than per-platform pass or fail, since the useful output is where they differ. Keep human testing for the things that genuinely need judgement, which is a smaller set than it currently covers. And build it as reusable infrastructure across projects, which is the only way the economics work in a bespoke services business.

## Target Customer
Porting and co-development studios, publisher QA organisations, platform holders, and game test automation vendors.

## Impact If Built
Verification cost scales with platforms multiplied by builds, and the method does not scale at all. Automated deterministic playthroughs with cross-platform output comparison turn the recurring pass into an overnight job.
