# Rejection Risk Scored Before Upload

**Niche:** [[niches/postproduction-studios/deliverables-qc-and-mastering/profile|Deliverables QC & Mastering]]
**Industry:** [[industries/postproduction-studios|Postproduction Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** QC operators watch every package with the same care, when the studio's own history could tell them which packages are likely to fail and on what.
**Tags:** #gradient-boosting #autoencoders #feature-engineering #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to pass each platform's inspection on the first submission, and whoever delivers the lowest redelivery rate per programme hour takes the studio's mastering work.

## The Problem
A mastering facility ships hundreds of packages a month. Automated QC flags thousands of warnings, most harmless, and human operators review in arrival order. Rejections still come back, and they cluster: a particular conform path, an HDR trim workflow, a subtitle vendor, an audio stem layout for one platform.

## Why Nobody Has Built This
QC vendors sell the checks and see only their own reports; platforms see only rejections. The facility holds both, plus the production metadata that explains the failures, but has never joined them.

## What to Build
A risk model per package that uses the automated QC results, essence-level measurements (loudness curves, metadata statistics), production metadata (which conform path, which colorist's export, which subtitle vendor) and the target platform and spec version. It predicts rejection probability and likely category. Human QC time goes to the top-risk packages, each with a list of what to look at.

## Target Customer
Heads of mastering and deliverables at facilities and studio delivery operations groups.

## Impact If Built
More rejections caught for the same operator hours. Cutting first-submission failures by a third (estimate) removes dozens of overnight redeliveries a month at a large facility.
