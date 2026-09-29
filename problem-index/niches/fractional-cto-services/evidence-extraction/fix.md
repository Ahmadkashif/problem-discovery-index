# Fix: History That Lies

**Niche:** Evidence Extraction
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Fix (Pain Point)
**One-liner:** Every analysis built on repository history is quietly wrong wherever that history was disrupted, and nothing detects the disruption or says so.
**Tags:** #change-point-detection #gradient-boosting #hypothesis-testing #confidence-intervals #evaluation-metrics #automation
**Contested on:** Whether a stranger can derive a truthful picture of a system from the artefacts the organisation already produces, fast enough to matter inside an eight-week engagement.

## The Problem

Change frequency is the load-bearing signal in behavioural code analysis. Files that change often are where effort goes, where defects cluster, and where a rebuild will hurt. The entire technique rests on the assumption that the commit record is a faithful account of how the code evolved.

For most real private codebases it is not. A repository that has been consolidated from several others has a path rewrite in it, after which every file appears to have been created on the same day. A linter or formatter rollout produces a single commit touching tens of thousands of lines, which ranks every file it touched as hot. A vendored dependency directory, a generated client, a checked-in build artefact — each contributes thousands of machine-authored changes indistinguishable from human effort. A squash-merge policy collapses a hundred real commits into one and destroys the granularity the analysis depends on. A quarter where the team abandoned the tracker leaves a hole that averages into a misleadingly good cycle time.

None of this is exotic. Almost every codebase over four years old has at least one of these events. And the analysis produces a confident ranking regardless, with no indication that the period it covers is unanalysable.

On a team's own estate someone eventually notices — an engineer sees their stable module ranked as the top hotspot and knows why. On an estate a stranger is assessing in two weeks, nobody notices, and the wrong finding goes into a report that informs an acquisition.

## Why It's Still Broken

**The products were validated on clean corpora.** The research that established these techniques used curated open-source repositories selected for analysability, and the products inherited that assumption without inheriting the curation. The gap between the validation set and the private estate has never been closed because closing it produces no new technique.

**Nobody sees the failure.** A wrong hotspot ranking looks exactly like a right one. There is no error message, no crash, no obviously implausible output — just a list of files in the wrong order. The failure is invisible by construction, so it generates no support tickets and no roadmap pressure.

**Detection is per-pathology.** There is no single fix. Reformat commits, path rewrites, vendored directories, squash policies and tracker gaps each need their own detector with its own signature and its own correction, and each one is fiddly work that a product manager will rank below a feature that demos.

**Admitting the limit is commercially unattractive.** A product that says "the last eighteen months of this repository cannot support hotspot analysis" has just told a prospect its core feature does not work on their estate. Saying nothing and producing a ranking is, in the short term, the better commercial outcome — which is precisely the dynamic that keeps the problem in place.

**The correction is judgement-laden.** Once a reformat commit is detected, what should happen? Exclude it entirely, weight it down, or treat it as a boundary and analyse the periods separately? Each is defensible, the right answer varies, and there is no ground truth to settle it — so the safe choice is to do nothing.

## What a Fix Looks Like

A preprocessing layer that runs before any history-derived analysis and does three things: detect, correct where correction is defensible, and refuse where it is not.

**Detect.** Reformat and mass-mechanical commits by their shape — line counts orders of magnitude above the distribution, low semantic diff density, authored near a tooling-config change. Path rewrites and consolidations by rename topology, spotting the moment when a large fraction of the tree changes path simultaneously. Vendored, generated and build-output directories by content signature and by authorship concentration in tooling accounts. Squash-merge policies by commit cadence and message structure. Tracker abandonment by transition-density collapse against the repository's own activity in the same window.

**Correct.** Reconstruct file identity across renames and moves so change history follows the code rather than the path — this alone repairs most consolidation damage. Exclude machine-authored changes from effort signals while keeping them visible as a separate category. Where squashing has destroyed granularity, fall back to coarser units and say so.

**Refuse.** Every derived figure carries the effective window it was computed over and the disruptions inside it. Where the data cannot support a finding, the output is "unanalysable for this period, because of this event" rather than a number. That refusal is the feature — an instrument feeding an eight-figure recommendation is worth more for knowing its limits than for having an opinion about everything.

Publishing the detectors, or open-sourcing them, would be the fastest route to their becoming a standard step, and the credibility gain for whoever does it is larger than the feature advantage of keeping them.

## Who Feels the Pain

The advisor, who is professionally exposed. They present a finding derived from data they cannot independently verify, to a room that will act on it, and the mechanism that could have made the finding wrong is one they have never been told about.

The engineering team being assessed, who are told their stable, well-maintained module is the riskiest part of the codebase because a formatter touched it once, and have to argue against a number.

The investor or board acting on the report, who are the ones paying for a decision informed by an artefact of a `git filter-branch` run three years ago.

And every existing customer of every behavioural-analysis and engineering-analytics product whose estate contains a migration — which is a large fraction of them, none of whom have been told.

## Impact If Fixed

Repository-derived evidence becomes citable. The difference between a finding an advisor will put in front of an investment committee and one they will not is whether they can say where it came from and what would have to be true for it to be wrong.

It removes the largest source of silent error from an entire analysis category, improving every product built on change history at once — and the detectors are reusable, small, and mostly independent of the analysis they protect.

Most importantly, it makes the instrument honest about its own coverage, which is the only basis on which a profession that sells judgement will ever let one into the room.
