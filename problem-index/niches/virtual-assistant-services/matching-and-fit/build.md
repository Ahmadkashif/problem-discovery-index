# Build: Outcome-Trained Matching and Early Failure Detection

**Niche:** [[niches/virtual-assistant-services/matching-and-fit/profile|Matching & Placement Fit]]
**Industry:** [[industries/virtual-assistant-services|Virtual Assistant Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Train matching on the agency's own placement outcomes rather than on a recruiter's reading, and detect a failing placement in week three rather than month four.
**Tags:** #gradient-boosting #survival-analysis #matrix-decompositions #confidence-intervals #evaluation-metrics #change-point-detection #revenue-impact #tacit-knowledge-ml
**Contested on:** Whether placement success can be predicted from characteristics knowable before the placement starts.

## The Problem

An agency makes thousands of placements and learns nothing from them. Each match is a fresh judgement by a recruiter from a profile and a brief, and whether the last five hundred placements with similar characteristics worked out is not information anyone has.

Meanwhile the failure mode is expensive and slow. A mismatched placement does not announce itself; it degrades. The executive finds themselves checking everything, the assistant senses it and becomes cautious, clarification exchanges multiply, and three or four months later the client asks for a replacement. By then the executive has spent a quarter supervising and the context is lost.

The signals of a failing placement appear far earlier — in week two or three — in the volume of clarification, the rework rate, the response patterns, the tone. Nobody watches them.

## Why Nobody Has Built This

Agencies are service businesses with recruiting teams, not data teams, and matching has always been the recruiter's craft. There is a genuine belief, not entirely wrong, that fit is a human judgement.

The outcome data also sits in fragments. Placement records in an ATS, durations in a billing system, complaints in an account manager's inbox, and the reason a placement ended recorded as a free-text note if at all. Assembling a placement outcome table is the unglamorous prerequisite nobody has done.

And early failure detection requires visibility into the working relationship — the message volume, the clarification rate — which sits in the client's systems and raises the same access conversation as everything else here.

## What to Build

An outcome dataset, a matching model over it, and an early warning signal.

**Assemble the placement history.** Every placement: client characteristics, assistant characteristics, task scope, duration, whether it ended and why, satisfaction, and hours billed over time. For an agency with a few years of operation this is hundreds to thousands of rows, and it is the first real asset the business has never built.

**Model placement survival.** Time-to-termination with the covariates, which gives both a predicted match quality and, more usefully, the features that actually matter — which will contain surprises, since recruiter intuition in this industry weights task-skill overlap heavily and the failures are mostly about working style.

**Capture the dimensions that predict fit.** Communication style and volume. How much autonomy the executive grants. How much structure they provide in a brief. How they respond to an error. Preference for proactivity versus waiting to be asked. Timezone overlap expectations. These are askable at intake in ten minutes and are largely absent from current intake forms, which ask about tasks.

**Model it as an interaction.** Fit is a property of the pair, not a ranking of assistants. Latent-factor structure over the placement history with side information for new assistants is the right shape, and the agency's own history is exactly the data it needs.

**Detect failure early.** Clarification message volume rising, rework rate, response latency changes, task completion time drifting, tone shifts in the correspondence. A change-point signal in week three is worth more than any matching improvement, because it converts a replacement into a conversation — most early mismatches are fixable with a briefing adjustment or a scope change, and they are only unfixable once three months of frustration have accumulated.

**Intervene rather than replace.** The account manager's response to an early signal should be a structured conversation with both parties about how the work is being briefed, which is cheap and frequently works. Replacement is what happens when nothing was detected.

## Target Customer

Agency leadership, where the case is replacement rate — the single largest cost in the business, absorbing recruiting, onboarding, lost context and client churn — and where a measurable improvement is directly visible in margin.

## Impact If Built

Matching starts learning from the agency's own two thousand attempts rather than repeating an afternoon's judgement. The dimensions that actually predict fit get asked about at intake. And failing placements get caught in week three, when a conversation fixes them, rather than month four, when only a replacement will.
