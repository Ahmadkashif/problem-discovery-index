# Twenty Prompts in a Spreadsheet

**Niche:** [[niches/ai-model-evaluation-firms/application-regression-harnesses/profile|Application Regression Harnesses]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The alternative these products compete against is a spreadsheet of twenty prompts and an engineer reading the outputs, and for most teams it remains the honest choice because the products cost more and resolve less.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #automation #worker-facing #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in this sub-niche is fighting to tell a product team whether their change made their own application better, per commit, at a cost that fits a tooling budget — and whoever does that takes the account, because that is the only question an application team is asking.

## The Problem
A team evaluates a prompt change by running twenty cases and reading the outputs. It is slow, subjective, and unrepeatable, and it has one property the platform alternative lacks: the engineer actually looks at what came out. The platform runs two hundred cases through an unvalidated judge and returns 84 percent, and the team has no idea whether that judge agrees with them about what good looks like, whether the two-point movement is real, or which outputs changed. The spreadsheet is worse in every respect except the one that determines whether anybody trusts it, which is why adoption stalls after the trial.

## Why It's Still Broken
Products are sold on scale — more cases, more metrics, a dashboard — which is not what the spreadsheet is providing and not why the team is holding onto it. Validating the judge against the team's own judgement is work that happens before any value appears, so it is skipped in onboarding. Showing which outputs changed is a diff problem nobody has solved well for generated text. And the trial always demonstrates the dashboard rather than the trust-building.

## What a Fix Looks Like
Earn the trust the spreadsheet already has. Start onboarding by calibrating the judge against the team's own labels on thirty of their cases and report the agreement, which takes an hour, tells the team exactly how much to trust every subsequent number, and is the single change most likely to convert a stalled trial. Always show the outputs that changed, side by side, ranked by how much they changed, because the engineer reading outputs is the behaviour the spreadsheet supports and the product suppresses — preserving it is what makes the automated number believable. Report agreement between the judge and the team continuously as cases are reviewed, so the calibration stays current rather than being a one-time onboarding step. Report uncertainty on every comparison, so a team stops chasing noise. Keep per-run cost visible, since suite size is being chosen on budget and the team should see the trade-off explicitly. Support fast subset runs during iteration and the full suite on merge, which matches how people actually work. And measure the product against the spreadsheet honestly in the trial — same change, both methods, compare conclusions — because that is the comparison the team is making silently anyway.

## Who Feels the Pain
Engineering teams paying for a platform and still reading outputs in a spreadsheet; the vendors whose trials stall at the trust question; and the users of applications shipped on a number nobody believed.

## Impact If Fixed
Calibrating the judge against the team's own labels in the first hour of onboarding tells them how much to trust every number that follows, and it is the change most likely to convert a stalled trial. Showing the changed outputs preserves the one behaviour the spreadsheet supports and the platform suppresses.
