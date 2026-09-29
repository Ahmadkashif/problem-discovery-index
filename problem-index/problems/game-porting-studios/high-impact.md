# Bidding a Fixed Price on a Codebase You Have Not Read

**Industry:** [[game-porting-studios|Game Porting Studios]]
**Type:** High Impact
**One-liner:** The quote is a fixed price against a fixed date for work whose difficulty depends entirely on properties of a codebase the studio cannot see until after the contract is signed.
**Tags:** #gradient-boosting #graph-neural-networks #bert #confidence-intervals #bayesian-inference #survival-analysis #evaluation-metrics #revenue-impact

## The Problem
A publisher asks several studios to bid on porting a title. The information supplied is typically the engine and version, the platforms, a build to play, some technical documentation of variable quality, and a deadline. The bid is a fixed price.

What determines the actual cost is mostly invisible at that point. How much platform-specific code has leaked into gameplay systems. Whether the renderer uses features that have no equivalent on the target. How the memory budget is spent and how much headroom exists. Whether the engine version is supported on the target platform or requires an upgrade that cascades. How much custom code sits under an engine that appears standard. Whether the original team's assumptions about threading, file access or input hold on the target.

Each of these can change the effort by a large multiple, and none is reliably assessable from a build and a conversation. The estimate is therefore made by an experienced technical director applying pattern recognition from previous projects, plus a contingency margin chosen by feel.

The error lands on margin. A port that takes twice the estimate is absorbed by the studio, because the contract is fixed price and the client's position is that the studio quoted it. Services businesses in this sector operate on thin margins and a small number of badly-estimated projects is the difference between a profitable year and a loss.

The estimate also drives the bid, so studios face the classic adverse selection problem: the studio that underestimates most wins the work. That dynamic pushes prices toward the most optimistic assessment in the market rather than the most accurate.

## Why It's Unsolved
Access before contract is the structural obstacle. Publishers are reluctant to hand a full codebase to several competing vendors during a bid, and the studios therefore estimate from the outside. Where deeper access is granted, it usually comes with a compressed evaluation window that does not allow real analysis.

Nobody has assembled the data. A studio with forty completed ports has forty observations linking codebase characteristics to realised effort, and those observations are scattered across project files, time-tracking systems and people's memories. Turning them into an estimation model requires treating completed projects as data, which no studio in this sector does.

The measurement is also awkward because effort was not recorded against the right categories. Time tracking captures hours per person per project, not hours per cause, so a studio that overran cannot say precisely what consumed the budget beyond a general account.

And the sales incentive undermines the analysis. A technical director who produces a well-calibrated estimate that is higher than a competitor's loses the work, so the organisation's revenue depends on the estimate being optimistic, which is not an environment in which estimation accuracy improves.

## What a Solution Looks Like
Build the estimation model from completed projects. Codebase characteristics measurable through automated analysis — engine and version, size and structure, platform-specific code concentration, renderer feature usage, threading model, dependency graph, custom module footprint — related to realised effort by category, across a studio's own project history. That relationship is learnable from a few dozen projects if the outcome data is assembled properly.

Estimate as a distribution. The bid needs a number and the business needs the range, and knowing that a project's effort is 8,000 hours with a plausible range up to 15,000 changes the contingency, the contract structure and the decision whether to bid at all. Studios currently carry that uncertainty implicitly and price it as a flat margin.

Make pre-bid analysis fast and cheap. An automated codebase assessment that runs in hours rather than weeks — inside the publisher's environment if necessary, reporting only aggregate risk indicators — addresses the access problem directly, since publishers object to handing over code rather than to being told what the code implies.

Record effort by cause. Categorising hours against what consumed them — renderer, memory, certification, client-side churn, platform-specific gameplay code — turns each completed project into a usable observation and is a process change rather than a technology one.

And restructure the risk where it cannot be estimated. Where analysis says the uncertainty is genuinely wide, a contract with a shared-risk structure is a better answer than a fixed price with a large margin, and the analysis is what makes that conversation possible.

## Impact If Solved
Estimation error is the primary commercial risk in this business and is currently managed by experienced intuition plus a contingency percentage. A model built from a studio's own completed projects, producing distributions rather than points, would improve both pricing and the decision of which work to bid on — and the fast pre-bid assessment addresses the access problem that makes accurate estimation structurally impossible today.
