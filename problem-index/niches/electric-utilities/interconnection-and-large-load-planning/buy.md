# Planning Software With a Screening Layer on Top

**Niche:** [[niches/electric-utilities/interconnection-and-large-load-planning/profile|Interconnection & Large-Load Planning]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Load-flow tools can answer any capacity question exactly, one carefully built case at a time, which is too slow for today's request volume.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #data-integration #automation #workflow-orchestration
**Contested on:** *Not terminal as stated.* The honest partial sentence is: every serious competitor in this niche is fighting to tell an applicant quickly what capacity exists and what connecting will cost. But for small distributed generation, storage and chargers the contest is clearing thousands of applications against a hosting number the study later confirms. For data centres and factories it is answering a few huge, often speculative requests with a megawatt figure, date and cost that hold until energisation. Different volumes, buyers and winners, so it is decomposed into contested sub-niches below.

## The Problem
Planners already own powerful simulation tools and many utilities publish hosting-capacity maps. But a full study is a manual case build, and a hosting map is a static snapshot computed months ago under assumptions applicants can't see. Between the two there is nothing that answers quickly and stays honest about uncertainty.

## What Already Exists
Eaton CYME, DNV Synergi Electric and Siemens PSS SINCAL with their hosting-capacity modules; EPRI's DRIVE method and OpenDSS; interconnection portals such as PowerClerk and GridUnity; analytics vendors such as Gridsight, Kevala and envelio.

## The Customization Gap
The missing layer: automatic case generation for each new request from the current model plus AMI loading; batch screening across seasons in minutes; calibration of screen results against the studies that followed; request-stage tracking that separates committed loads from placeholders; and outputs mapped to the utility's own tariff screens (the fast-track and supplemental-review criteria in its interconnection rules) so results can be used in the regulated process, not just as advice.

## Target Customer
Planning and interconnection managers at utilities already licensing a load-flow platform who need throughput, not another engine.

## Impact If Solved
Batch screening could let the same planning team clear ~2–3× as many requests a year (estimate), so existing software clears the queue rather than queuing behind a few senior modellers.
