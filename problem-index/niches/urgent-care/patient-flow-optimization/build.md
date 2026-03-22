# Real-Time Patient Flow Tracker with Bottleneck Detection

**Niche:** [[niches/urgent-care/patient-flow-optimization/profile|Patient Flow Optimization]]
**Industry:** [[industries/urgent-care|Urgent Care]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** UC site managers see a real-time visual map of every patient's position in the care workflow — with automatic bottleneck detection that alerts them when a workflow stage is backing up before the waiting room fills.
**Tags:** #gradient-boosting #time-series-forecasting #feature-engineering #evaluation-metrics #tacit-knowledge-ml #data-integration #revenue-impact

## The Problem
An experienced UC site manager walks through the clinic and intuitively senses flow problems — the waiting room is fuller than usual for 2pm, the triage nurse is overwhelmed, rooms are occupied but providers are charting on their last patient instead of picking up the next one. This tacit flow awareness, developed over years of managing UC operations, is what separates well-run clinics from chaotic ones. But it exists only in the manager's head, cannot be taught to new managers, and is unavailable to off-site operations directors managing multiple locations. When the manager is not physically present (evenings, weekends, manager vacation), flow deteriorates because no system replicates their pattern recognition. Bottlenecks compound: a 5-minute delay at triage cascades into a 20-minute wait for rooming, then a 30-minute LWBS event that costs $300 in lost revenue and generates a 1-star Google review.

## Why Nobody Has Built This
The data exists — Experity timestamps every workflow step for every patient. But converting timestamps into real-time flow visualization and bottleneck prediction requires: defining what "normal" flow looks like for each time of day and day of week (10am Monday has different expected throughput than 7pm Saturday); detecting deviations from normal in real time; attributing bottlenecks to specific workflow stages (is the delay at triage, at rooming, or at provider pickup?); and predicting wait time impact for patients still in the waiting room. This is a data product problem, not a feature addition to an EHR — it requires a purpose-built flow monitoring engine that consumes EHR timestamp data and produces operational intelligence. EHR vendors see it as outside their scope; analytics vendors see the UC market as too small.

## What to Build
A real-time patient flow monitoring platform that connects to Experity (or Athenahealth) via API and: displays a live flow map showing every patient's current stage and time-in-stage, color-coded by whether they are within normal range (green), approaching delay threshold (yellow), or in bottleneck (red); detects bottleneck formation by comparing current stage durations against time-of-day/day-of-week baselines; alerts the site manager or charge nurse when a bottleneck forms ("Triage is backing up — 4 patients waiting, average wait 12 minutes vs. 5-minute baseline"); predicts wait-to-provider time for patients in the lobby based on current flow state and historical patterns; and generates shift-end flow reports showing where time was lost and how throughput compared to capacity. The system learns each site's specific flow patterns, accounting for provider speed differences, staffing configurations, and patient mix variations.

## Target Customer
Site managers, charge nurses, and operations directors at high-volume UCs (30+ patients/day) who currently rely on physical walkthroughs and gut feel to manage patient flow, and chain operators who need flow visibility across multiple locations without being physically present.

## Impact If Built
Reduces average door-to-door time by 10-20 minutes through earlier bottleneck detection and intervention. Decreases LWBS rate by 25-40% by preventing bottleneck cascades that drive waiting room abandonment. Provides off-site operations directors with real-time flow visibility across all locations — the "experienced site manager in a box" that scales operational excellence beyond the individuals who currently provide it.
