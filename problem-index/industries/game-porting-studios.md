# Game Porting Studios

## Profile
**Category:** Gaming & Interactive
**Market Size:** ~$2B US in porting and co-development services; Virtuos, Sumo, QLOC, Iron Galaxy, Panic Button, Feral, Aspyr, Nixxes and a long tail of specialist shops do the work that gets games onto platforms their original teams did not target
**Tech Maturity:** Deep platform expertise, no estimation science. These studios hold genuinely scarce knowledge — console architectures, constrained memory budgets, graphics API differences, certification regimes — and bid fixed prices on codebases they have not seen, using the judgement of whoever has done the most ports.
**Workforce:** Porting and graphics engineers, technical directors, QA and certification specialists, producers managing client relationships, build and tools engineers

## Key Pain Themes
The business is priced on estimation and the estimation is a guess. A port is quoted before the studio has meaningful access to the codebase, as a fixed price against a fixed date, and the actual effort depends on things that are invisible at bid time: how the renderer is structured, how much platform-specific code is buried in gameplay systems, how the memory budget was used, whether the engine version is supported on the target, and how much undocumented custom work sits under an engine that looks standard. Estimation error is absorbed directly out of margin.

The second theme is that the hardest target defines the project. Porting to a constrained platform means finding and fixing performance problems in a codebase written by someone else, for different hardware, with different assumptions — and the performance work is both the most skilled and the least estimable part.

The third is that the client keeps working. A port frequently runs concurrently with the original team shipping patches and content, so the porting studio is chasing a moving codebase, merging continuously, and re-testing work that was finished.

## Current Tech Landscape
Unity and Unreal handle much of the abstraction and shift the difficulty to engine-specific and custom code. Platform toolchains and profilers are provided under NDA by each holder and are genuinely good. Certification requirements are documented per platform and tested through submission portals. Automated testing for games exists and is adopted unevenly. Cloud build infrastructure and remote development tooling have improved substantially. Static analysis is used lightly, and there is essentially no tooling anywhere aimed at estimating porting effort.

## Problems
- [[problems/game-porting-studios/high-impact|🔴 High Impact: Bidding a Fixed Price on a Codebase You Have Not Read]]
- [[problems/game-porting-studios/low-impact-1|🟡 Low Impact: Performance Attribution on a Constrained Target]]
- [[problems/game-porting-studios/low-impact-2|🟡 Low Impact: Cross-Platform Regression Testing]]
- [[problems/game-porting-studios/worker-life-1|🟢 Worker Life: The Engineer Reading Somebody Else's Undocumented Code]]
- [[problems/game-porting-studios/worker-life-2|🟢 Worker Life: The Producer and the Codebase That Will Not Stop Moving]]
- [[problems/game-porting-studios/ml-opportunity|🧠 ML Opportunities]]
- [[problems/game-porting-studios/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
A porting studio that has completed dozens of projects holds the only dataset that exists about what makes a port expensive: the codebases, the estimates, the actual hours, the specific things that went wrong and what they cost. That corpus supports estimation directly — the relationship between measurable codebase characteristics and realised effort is learnable — and nobody has built it, because each project is treated as a bespoke engagement rather than as an observation. The consequence is that the sector's core commercial risk is priced by intuition, and the studios that are good at it are good because of a small number of experienced people whose judgement is neither transferable nor checkable.
