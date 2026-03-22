# Route Optimization for Home Visit Scheduling

**Niche:** [[niches/physical-therapy/home-based-pt/profile|Home-Based PT Providers]]
**Industry:** [[industries/physical-therapy|Physical Therapy]]
**Type:** Fix (Pain Point)
**One-liner:** Home-based PTs stop spending 30-40% of their day driving unoptimized routes — geographic clustering and time-window-aware routing recovers 1-2 patient visits per day.
**Tags:** #gradient-boosting #bayesian-optimization #feature-engineering #optimization-fundamentals #worker-facing #revenue-impact

## The Problem
Home-based PTs spend 30-40% of their workday driving between patient homes. A typical day includes 4-6 visits spread across a metropolitan area, with each visit lasting 45-60 minutes. Without route optimization, a PT might drive from the north side to the south side for a 9am visit, back north for an 11am visit, then south again for 1pm — tripling their drive time. Scheduling is done by coordinators who see patient names and time preferences but have no geographic visibility. They schedule based on patient availability and therapist calendar openings, not on geographic clustering. The result: PTs who could see 6 patients in a well-routed day see 4-5, burning fuel, time, and morale on unnecessary driving.

## Why It's Still Broken
Home health scheduling systems (Axxess, WellSky) show patient addresses but don't optimize routes. They manage calendars, not geography. General route optimization tools (Google Maps multi-stop, Route4Me) handle geographic routing but don't understand clinical constraints: treatment frequency requirements (Patient A needs visits Mon/Wed/Fri, Patient B needs Tue/Thu), session duration variability (evaluations take 60 minutes, follow-ups take 45), patient availability windows (Mrs. Johnson is only available after her morning caregiver arrives at 10am), and therapist credential/specialty matching (not every PT can see every patient). The scheduling problem is a constrained optimization across geography, time windows, clinical requirements, and therapist qualifications — too complex for either calendar tools or simple route planners.

## What a Fix Looks Like
A scheduling and routing engine that ingests: patient addresses and availability windows, treatment frequency prescriptions, session duration by visit type, therapist home base location and working hours, and therapist-patient assignment rules. It generates daily route-optimized schedules that minimize total drive time while respecting all constraints. The coordinator sees a map view showing proposed routes with estimated drive times and can manually adjust. When a patient cancels, the system suggests either a nearby fill-in patient or recommends starting the next visit early. Weekly planning mode clusters patients geographically by day of week — Monday patients are all in the northwest quadrant, Tuesday in the southeast — establishing consistent route patterns.

## Who Feels the Pain
Home-based PTs who spend 2-3 hours daily driving, arriving at patients' homes stressed and fatigued. Scheduling coordinators who manually juggle geography, time preferences, and clinical requirements without tools. Agency directors who watch productivity metrics suffer because their therapists are driving instead of treating.

## Impact If Fixed
Recovering 60-90 minutes of drive time per therapist per day enables 1-2 additional patient visits — adding $150-$400 daily revenue per therapist. Across a 10-therapist home health PT team, optimized routing adds $300K-$800K in annual revenue. Reduces therapist burnout and fuel costs, improving retention in a high-turnover role.
