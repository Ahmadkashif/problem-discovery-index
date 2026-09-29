# A Scan With No Memory

**Niche:** [[niches/software-supply-chain-security/scanning-and-analysis/profile|Scanning & Analysis]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Fix (Pain Point)
**One-liner:** A security engineer establishes that a finding does not apply, the scan runs again that night, and the finding returns exactly as it was.
**Tags:** #descriptive-statistics #k-means-clustering #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #quick-win #automation
**Contested on:** Every serious competitor here is fighting to say something about an artefact that the commoditised scan cannot — and that contest is a program analysis problem in one market and an attestation problem in the other, which is why this niche is not terminal and is decomposed below.

## The Problem
An engineer spends forty minutes establishing that a reported vulnerability is not reachable in this application, records the assessment, and moves on. The nightly scan regenerates the finding. Some tools support suppression, which requires the engineer to add an entry with an expiry, in a file, per finding — and which is frequently scoped so narrowly that a patch version bump invalidates it and the finding returns anyway. Across an estate this is a large recurring cost for work that has already been done correctly once.

## Why It's Still Broken
Scanners are stateless by design: they inspect an artefact and report what they find, which is the correct architecture for a scanner and the wrong one for a workflow. Suppression was added as a file-based mechanism because it fits that architecture, and its scoping is version-specific because that is the safe default — which makes it break on every upgrade. Assessments are also not portable between tools or between services, so the same determination is made repeatedly across an organisation. And the regenerated queue looks like diligence.

## What a Fix Looks Like
Make the assessment durable and portable. Store assessments as first-class records keyed on the finding's substance — this vulnerability, in this component, in this application, is not reachable because of this evidence — rather than on a version string, so a patch bump does not invalidate a determination that is still true. Re-evaluate assessments when the evidence changes rather than when the version does, which means detecting that the previously-unreachable code is now reached and surfacing it, and is the behaviour that makes durable suppression safe. Propagate assessments across services where the same component is used the same way, since the determination is frequently identical and is currently repeated per service. Expire assessments deliberately with a review rather than allowing them to persist indefinitely, since a permanent suppression is how a real finding gets buried. Record the reasoning and the assessor, which makes the assessment reviewable and is what an auditor will ask for. Adopt the emerging exploitability exchange formats, which exist precisely to express these determinations portably and are thinly supported. And report the assessment reuse rate, which is the measure of how much work the memory saved.

## Who Feels the Pain
Security engineers reassessing the same findings; organisations paying repeatedly for determinations already made; and teams whose suppression files have become an unreviewable accumulation.

## Impact If Fixed
Keying assessments on substance rather than on version stops determinations expiring on every patch bump, which is the mechanism that regenerates most of the queue. Re-evaluating on evidence change rather than on version change is what makes durable assessment safe rather than dangerous.
