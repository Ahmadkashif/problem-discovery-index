# Performance Attribution on a Constrained Target

**Industry:** [[game-porting-studios|Game Porting Studios]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The game runs at half the required frame rate on the hard platform and the work is finding out why, in a codebase written by strangers for different hardware.
**Tags:** #gradient-boosting #change-point-detection #graph-neural-networks #time-series-forecasting #confidence-intervals #evaluation-metrics #feature-engineering #transfer-learning

## The Problem
Porting to a constrained platform is fundamentally a performance problem. The title runs, and it runs too slowly, and the project is the work of finding and fixing the reasons. That work is skilled, slow and hard to schedule, because the causes are distributed: draw call volume, shader complexity, memory bandwidth, texture streaming, CPU-side gameplay code, garbage collection behaviour, asset budgets authored for a different target, and engine features that behave differently on the platform.

Profilers show where time goes and not what to do about it. A profile identifies that a subsystem is expensive; converting that into a change requires understanding why it is expensive in this codebase, which requires reading unfamiliar code. Platform-specific profiling tools are good and each is different.

The estimation problem from the bid returns here in operational form: nobody can say in advance how many optimisation passes will be needed, so the performance phase absorbs whatever schedule remains and frequently more.

And the fixes interact. Reducing memory pressure changes streaming behaviour; simplifying shaders shifts load to the CPU; lowering resolution changes the bandwidth profile. Optimisation is a sequence of decisions in a coupled system, and its path is chosen by experience.

## What Already Exists
Every platform holder provides genuinely capable profiling and debugging tools under NDA. Engine-level profilers in Unity and Unreal give subsystem breakdowns. GPU vendors provide frame analysis tooling. Automated performance testing harnesses exist and are used by larger teams. Optimisation knowledge circulates through conference talks, platform documentation and studio experience. Dynamic resolution scaling and similar runtime techniques handle part of the problem generically.

## The Customisation Gap
The generic tools measure and the studio needs attribution and prioritisation. A profile that says a subsystem costs six milliseconds does not say which of the twenty candidate causes is responsible, how much each would return if fixed, or what fixing it would cost — which is the ranking the technical director actually needs to plan a phase.

The transferable knowledge is the missing asset. A porting studio that has optimised forty titles for the same platform has seen the same causes repeatedly, and the mapping from profile signature to likely cause and typical fix is precisely the expertise that makes the studio valuable. It lives in a handful of engineers and is transferred by apprenticeship.

Estimating the return before doing the work is the second gap. What a given optimisation will recover is predictable from the profile and the codebase structure, and having that estimate turns the optimisation phase from an open-ended search into a planned sequence with a projected end state — which is what makes the schedule defensible.

And the cross-title comparison is available only to a studio with a portfolio. What is normal for this genre on this platform, and how far this title is from a comparable one, is the frame of reference that tells a team whether they are near the achievable limit or missing something large.

## Impact If Solved
The performance phase is where port schedules are lost and where the scarcest expertise is spent. Profile-to-cause attribution learned from a studio's own portfolio, return estimates that let the phase be planned, and cross-title baselines that say what is achievable would make the least predictable part of these projects predictable — and would spread expertise currently held by a small number of engineers whose availability determines what work the studio can take.
