# Schedule Slip Prediction from Field Signals

**Industry:** [[construction-tech-platforms|Construction Tech Platforms]]
**Type:** High Impact
**One-liner:** The platform predicts which activities will slip weeks before the schedule shows it, using RFI latency, submittal turnaround, crew counts and change order flow that it already captures and currently only displays.
**Tags:** #gradient-boosting #survival-analysis #time-series-forecasting #feature-engineering #cross-validation #evaluation-metrics #causal-inference #confidence-intervals #revenue-impact

## The Problem
Construction projects finish late. This is so routine that the industry treats it as weather rather than as a failure to predict, and schedule performance has not measurably improved in decades despite enormous investment in software.

The schedule itself is not the problem. A baseline schedule is built in Primavera or Microsoft Project, with activities, durations, logic and float. It is updated monthly, sometimes weekly, by someone reconciling what the field says against what the plan said. That update is retrospective: it records slip that has already happened.

Everything that would have predicted the slip was captured, in the same platform, weeks earlier. An RFI on a critical path activity that has been open for eighteen days when the project average is six. A submittal for long-lead equipment that has been rejected twice. Daily reports showing a trade at half its planned crew count for a week. A change order in the area of an upcoming activity. Weather. A subcontractor who is late on every project the general contractor has run with them.

Each of these is visible to somebody. None is joined to the schedule, and no system anywhere puts them together and says: this activity will not start on the fourteenth.

## Why It's Unsolved
The schedule lives outside the platform. Primavera and Microsoft Project are the systems of record for the critical path, they are updated by a scheduler rather than by the field, and the integration between them and the construction management platform is typically a periodic import. Joining the field signal to the activity it affects requires knowing which RFI, submittal and daily report line relates to which schedule activity, and that mapping is almost never maintained.

The label is also slippery. What counts as slip depends on which baseline you measure against, and baselines are re-baselined — frequently for commercial reasons, which erases the record of the original failure. Constructing a clean training target means reconstructing the original plan before it was quietly revised.

There is a commercial disincentive nobody says out loud. Schedule slip is contested territory between owner, general contractor and subcontractors, with delay claims and liquidated damages attached. A system that documents predictable slip creates evidence, and the parties best placed to deploy it are the parties most exposed by it. This is the real reason the analysis has not been built, and it points at the owner as the natural buyer rather than the contractor.

Finally, every project is genuinely somewhat unique, which the industry uses as a reason not to model. The uniqueness is at the project level; the failure mechanisms repeat.

## What a Solution Looks Like
A model that produces, for every activity in the current schedule, a probability distribution over its actual start and finish, updated daily from field signal. It draws on the open RFI and submittal state mapped to that activity, crew presence from daily reports, change order activity in the same area, the subcontractor's own historical performance across the vendor's whole customer base, weather, and the project's own trajectory so far.

The output is a ranked list of activities at risk with the specific driver named — this activity is exposed because a critical submittal has been in review for nineteen days — not a score. Named drivers are what make it actionable at the weekly coordination meeting, which is where schedule decisions actually get made.

## Impact If Solved
Two weeks of warning on a critical path activity is the difference between resequencing and paying acceleration costs. On a project where liquidated damages run into thousands per day, a single avoided slip pays for the platform many times over — and the prediction rests on a cross-project corpus that no individual contractor can assemble.
