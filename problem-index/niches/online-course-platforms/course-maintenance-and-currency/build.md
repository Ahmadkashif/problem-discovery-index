# Detecting Decay Before the Complaint

**Niche:** [[niches/online-course-platforms/course-maintenance-and-currency/profile|Course Maintenance & Currency]]
**Industry:** [[industries/online-course-platforms|Online Course Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The course teaches a version that no longer exists and keeps selling because the ratings are from three years ago.
**Tags:** #change-point-detection #transformers #evaluation-metrics #confidence-intervals #automation #large-language-models #descriptive-statistics #bert
**Contested on:** Every serious competitor in this niche is fighting to know which courses have gone materially wrong as the tools they teach changed — and whoever detects decay before a learner complains stops selling instruction that no longer matches reality.

## The Problem
Software, frameworks, interfaces and platforms change. A course recorded against one version becomes confusing, then misleading, then wrong. The learner follows the steps, the screen does not match, and they conclude they have made a mistake. The platform's signals — rating, enrolment, review count — are accumulated over years and move slowly, so a decayed course continues to rank above a current one. The only detection mechanism is a learner writing a complaint.

## Why Nobody Has Built This
Ranking signals are cumulative by design because that is what makes them stable, so they are structurally incapable of reflecting a recent change — a metric built for stability cannot detect decay. Maintenance costs the instructor real work and earns nothing extra. The platform has no view of the external world the course describes. And nobody measures how much of the catalogue is out of date.

## What to Build
Detect decay from inside and outside. Monitor external version and release signals for the tools a course teaches, which is the core and is the earliest possible indicator — a framework's major release is public and a course teaching the prior version is now suspect. Detect decay from internal signals too: rising confusion in the Q&A, increased abandonment at specific points, falling recent ratings against historical ones. Weight recent ratings separately from cumulative ones, since a course that was excellent and is now wrong looks identical in a lifetime average. Identify which sections are affected rather than flagging the whole course, so the instructor's update is targeted and achievable. Prompt and support instructors with specific findings, because most would update if told exactly what broke. Reflect currency in ranking, as that is what makes maintenance rational for the instructor. Warn learners when a course teaches a superseded version, which is honest and is the minimum. Report catalogue currency as a quality metric, which nobody produces and which would be uncomfortable and useful. Support partial re-recording rather than a full rebuild, since the cost is why updates do not happen. And detect the course that has been abandoned by its instructor entirely, as those are the worst case and are identifiable.

## Target Customer
Catalogue and quality leadership, learners following instructions that no longer work, instructors who would update if prompted, and course authoring vendors.

## Impact If Built
A metric built for stability cannot detect decay, so cumulative ratings keep obsolete courses ranking. External release signals plus recent-versus-historical rating divergence detect it before the complaint.
