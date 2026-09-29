# Percent Complete Reported by the Person Being Measured

**Niche:** [[niches/construction-tech-platforms/gc-project-management-platforms/profile|General Contractor Project Management]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every schedule update and every progress payment in commercial construction rests on percent-complete figures supplied by the party whose payment and reputation depend on the number, and no platform records how those figures have historically compared to reality.
**Tags:** #descriptive-statistics #hypothesis-testing #evaluation-metrics #confidence-intervals #change-point-detection #compliance #worker-facing #quick-win
**Contested on:** Every serious competitor in GC project management is fighting to tell a project team which activities will slip weeks before the schedule shows it — and whoever forecasts a slip earliest, with evidence a superintendent believes, takes the account.

## The Problem
A subcontractor reports 70% complete on an activity in the monthly pay application. The project manager knows the number is optimistic, applies a mental discount, and approves it because disputing it costs a relationship and a week. The schedule takes the 70% at face value. Two months later the activity is still not finished, the remaining 30% turns out to have been 55%, and the float everyone was relying on is gone. The pattern is universal, well understood by every practitioner, and recorded nowhere — so the discount that every project manager applies by instinct is never calibrated and never transfers between projects or people.

## Why It's Still Broken
Percent complete is a negotiation dressed as a measurement, and the platform is a neutral recorder of it. Nobody has wanted to build the tool that scores a subcontractor's historical reporting accuracy, because it names parties, it would be used in commercial arguments, and the vendor sells to both sides of the relationship on different projects. Technically it is trivial — compare each reported progress curve to the eventual actual — which makes the absence entirely a choice about what a platform is willing to say.

## What a Fix Looks Like
Record the curve and report the pattern to the party that carries the risk. For every activity, keep every reported progress figure with its date, and when the activity completes, compare the reported trajectory to the realised one. The output is a simple, unglamorous statistic: by trade, by subcontractor, by project type, how much does reported progress typically overstate actual, and at what stage does the overstatement appear — it is usually concentrated in the last quarter of an activity, which is exactly where float is consumed. Give the project manager a calibrated adjustment rather than an instinct, and give the subcontractor the same view of their own reporting, which is the version that changes behaviour rather than generating a fight. Where reality capture exists, use it as the reference; where it does not, actual completion date is enough to build the calibration.

## Who Feels the Pain
Project managers discounting numbers by feel and being wrong in both directions; schedulers updating a plan from figures they know are soft; and subcontractors who report honestly and are discounted at the same rate as those who do not.

## Impact If Fixed
A calibrated progress adjustment materially improves every downstream forecast and every float calculation, at no data cost — the history is already in the platform. The behavioural effect is the larger one: reporting accuracy becomes visible, and the honest subcontractor stops being penalised for the sector's habit.
