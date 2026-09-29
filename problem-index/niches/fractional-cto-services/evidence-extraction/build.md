# Build: Cold-Start System Evidence

**Niche:** Evidence Extraction
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A derivation engine that produces a confidence-scored picture of an unfamiliar codebase, team and delivery process from an afternoon's worth of exports, with no configuration and no baseline.
**Tags:** #graph-neural-networks #gradient-boosting #time-series-forecasting #change-point-detection #confidence-intervals #evaluation-metrics #automation
**Contested on:** Whether a stranger can derive a truthful picture of a system from the artefacts the organisation already produces, fast enough to matter inside an eight-week engagement.

## The Problem

The advisor's question is always some version of "can this system absorb the change the business needs, and at what cost." Everything that bears on the answer is recorded somewhere. Where change concentrates and whether it concentrates in the places the roadmap will touch. Which components move together regardless of what the architecture claims. Where defects cluster. How much of the system only one person has ever modified. How long work actually takes from start to delivery and where it stops moving. Whether the team's throughput has been stable or declining.

The practitioner derives approximately none of this, because deriving it requires knowing what to compute, writing the extraction, cleaning data they have never seen, and interpreting the output against no baseline — three days of work in an engagement that has ten. So they read code and ask questions, which gives them structure and opinion but not dynamics.

The cold start is the whole difficulty. A team's own analytics platform accumulates a baseline over quarters and learns the estate's idiosyncrasies. An advisory instrument gets one shot at an estate it has never seen, whose history contains events nobody will think to mention — the monorepo consolidation eighteen months ago that rewrote every path, the linter rollout that touched forty thousand lines in one commit, the two quarters where the tracker was abandoned for a spreadsheet. Run naive change-frequency analysis across any of those and the hotspot ranking is noise wearing the costume of a finding, which in this setting is worse than no finding at all.

## Why Nobody Has Built This

Repository mining is an old research field with strong results and almost no commercial productisation, and the reason is that the results were established on curated corpora — clean open-source histories selected for analysability. The techniques that work beautifully on a well-behaved repository degrade badly on a real private estate, and closing that gap is unglamorous engineering rather than a publishable contribution, so it has not been done.

The buyer is small, fragmented, and — as with the parent niche — professionally ambivalent about a tool whose premise is that a large part of expert reading is derivable.

There is a harder technical reason. The valuable outputs require joining sources that are joined badly or not at all in most organisations: commits to tickets, tickets to business capability, deployments to changes. Every organisation does this differently or not at all, and inferring the joins from the data itself — rather than requiring configuration the advisor cannot supply — is the actual product. It is substantial work that looks like plumbing.

And confidence is genuinely hard. An instrument that says "this module is the hotspot" when the history is too disrupted to support the claim will be caught once and discarded forever. Knowing when the data cannot answer is a first-class requirement and is much harder than computing the answer.

## What to Build

A derivation engine that takes a repository clone, a tracker export and any available CI or deployment log, and returns a confidence-scored evidence base with no configuration step.

**History repair first.** Before any analysis, detect the events that break it: mass reformats and linter rollouts by commit shape, path rewrites and monorepo migrations by rename topology, vendored and generated directories by content signature, abandoned tracker periods by density collapse. Reconstruct file identity across renames and moves so change history follows the code rather than the path. Every downstream figure carries the effective window it was computed over, and where repair fails the engine says the period is unanalysable instead of averaging through it. This is the foundation and most of the engineering.

**Structure from behaviour.** Module and dependency graph from the code; temporal coupling from co-change, which is the finding that most often contradicts the client's own architecture diagram and most often determines whether a rebuild is bounded. Knowledge concentration from authorship, surfaced as a risk register of components with a single living author.

**Concentration.** Change frequency weighted by complexity and by defect-fix commits, producing a ranking of where effort actually goes, with the effort mapped onto business capability wherever ticket labels, commit references or directory semantics allow the inference — and explicitly marked as unmapped where they do not.

**Flow.** State durations inferred from tracker transitions, with the semantic problem handled by inferring what each team's states mean from transition topology rather than requiring a mapping the advisor cannot provide. Where work stalls, how much is in flight per person, how often items are reopened.

**Confidence on everything.** Each finding carries the data that supports it, the window, the known disruptions in that window, and a stated confidence. The practitioner must be able to see why a number is what it is, because they will be asked in a room where being wrong is expensive.

**Portable and disposable.** Runs local or in an isolated tenant, needs no agent, no production access and no org-level integration — a clone and an export, both obtainable by one friendly engineering lead under the existing NDA, and deletable at engagement end.

## Target Customer

Fractional CTOs and technical due diligence practitioners, where the derivation is needed on every engagement and the deadline is fixed. Due diligence is the sharper wedge: a two-week diligence with restricted code access has a harder constraint and a buyer — the investor — who is entirely comfortable paying five figures per engagement for better evidence.

Secondary: engineering leaders inheriting a system through acquisition or reorganisation, who have the same cold-start problem on an estate they now own.

## Impact If Built

The advisor's first days shift from constructing a picture to testing one. Temporal coupling, effort concentration and flow bottlenecks are available before the interviews, which turns the interviews into a check on specific hypotheses and frees the scarce resource — senior judgement — for the part that is actually judgement.

The failure mode the profession fears most is missing the thing that mattered because it was in a part of the system nobody read. Systematic derivation over the whole estate is the only defence against that, and it currently does not exist.

History repair alone has value beyond this market. Every engineering analytics product silently produces wrong hotspot rankings on estates with disrupted history, and none of them tell the user.
