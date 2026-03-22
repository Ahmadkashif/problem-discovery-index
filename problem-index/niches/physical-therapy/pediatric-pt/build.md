# Pediatric Developmental Milestone Tracker

**Niche:** [[niches/physical-therapy/pediatric-pt/profile|Pediatric PT Providers]]
**Industry:** [[industries/physical-therapy|Physical Therapy]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Pediatric PTs track a child's gross and fine motor development against age-normed curves — showing parents and IEP teams exactly where the child stands, how far they've progressed, and what milestones to target next.
**Tags:** #gradient-boosting #time-series-forecasting #feature-engineering #evaluation-metrics #data-integration #worker-facing

## The Problem
Pediatric PT progress is measured against developmental milestones — rolling, sitting, crawling, standing, walking, running, jumping, fine motor manipulation — not against a pre-injury baseline like adult PT. A 14-month-old child who isn't walking is developmentally delayed, but by how much? How does their trajectory compare to age norms? Are they closing the gap or falling further behind? No PT tool provides a visual developmental trajectory showing where the child plots on gross/fine motor development curves across visits. Therapists administer standardized assessments (PDMS-2, GMFM) periodically, document scores in narrative notes, and present results verbally to parents and IEP teams. No system connects these assessments into a longitudinal developmental trajectory that stakeholders can see and understand.

## Why Nobody Has Built This
Pediatric PT is a niche within a niche — perhaps 5-6% of the PT market. EMR vendors build for the orthopedic mainstream. The clinical data model is fundamentally different: adult PT tracks improvement relative to a patient's own baseline (pre-surgery ROM vs. current ROM), while pediatric PT tracks development relative to population norms (where is this child compared to typical development for their age). Building this requires: age-normed developmental reference data, the ability to plot individual children against these norms, longitudinal tracking across months or years (not the 6-8 week episodes typical in adult PT), and output formats compatible with IEP/IFSP documentation requirements (which are education system formats, not healthcare formats). The cross-domain nature (healthcare data presented in education system formats) means neither healthcare nor education technology vendors have built it.

## What to Build
A developmental trajectory platform for pediatric PT: (1) Clinician input: record standardized assessment scores (PDMS-2 gross motor, fine motor, GMFM dimensions A-E, Alberta Infant Motor Scale) at each assessment interval, plus milestone achievement dates (date of first independent sitting, date of first steps, etc.). (2) Trajectory visualization: plot the child's motor development on age-normed curves showing percentile position and trajectory direction (closing the gap, maintaining, or falling behind). Compare across motor domains (gross motor may be ahead of fine motor). (3) Parent dashboard: simplified visual showing "Your child's progress" with milestone achievements highlighted, next milestone targets, and home activity recommendations. (4) IEP/IFSP reporting: auto-generate progress reports in the format required by school districts, showing objective data supporting continued services or goal modification. (5) Predictive modeling: based on the child's trajectory and diagnosis, estimate the timeline for upcoming milestone achievement to set realistic goals.

## Target Customer
Pediatric PT practice owners and early intervention agency directors who need to track, visualize, and report developmental progress across a caseload of children with varying diagnoses, ages, and developmental trajectories.

## Impact If Built
Replaces manual milestone tracking in spreadsheets and narrative notes with a visual, automated system — saving therapists 20-30 minutes per progress report. Gives parents a clear picture of their child's development that reduces anxiety and increases engagement in home carryover activities. Strengthens IEP/IFSP documentation with objective longitudinal data, supporting continued authorization for therapy services.
