# Campus Health Scoring Dashboard

**Niche:** [[niches/faith-organizations/megachurch-multisite/profile|Megachurch Multi-Site]]
**Industry:** [[industries/faith-organizations|Faith Organizations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool today aggregates attendance trends, giving patterns, volunteer engagement, and small group participation across multiple campuses into a single health score that helps executive pastors identify struggling locations before decline becomes visible.
**Tags:** #gradient-boosting #anomaly-detection #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
Multi-site churches with 3-15 campuses need to detect when a campus is struggling — attendance plateauing, giving declining, volunteer participation dropping, small group launches stalling. Executive pastors currently rely on monthly reports from each campus pastor, but these reports are subjective and each pastor presents their campus in the best light. By the time decline is obvious in the numbers, it's 6-12 months into the trend and much harder to reverse. Experienced executive pastors develop a "feel" for campus health from scattered data points, but this intuition doesn't scale to 10+ locations.

## Why Nobody Has Built This
Church management platforms track individual metrics (attendance, giving, groups) but don't composite them into a health score because "health" is theologically and operationally subjective — what constitutes a healthy church is a values judgment. Multi-site churches use different combinations of tools at each campus, making cross-campus data aggregation a significant integration challenge. Additionally, church leaders are uncomfortable with "scoring" campuses because it feels corporate and raises sensitivity about campus closures.

## What to Build
A multi-campus analytics dashboard that pulls attendance, giving, volunteer hours, small group participation, new visitor return rate, and digital engagement data from Planning Center/Rock RMS across all campuses. The system calculates campus health scores using configurable weightings (the executive team decides what matters most), surfaces trend lines and anomalies (campus 3's giving dropped 15% while attendance held — indicating a giving fatigue pattern), and generates quarterly campus comparison reports. Alerts trigger when a campus's composite score drops below historical norms.

## Target Customer
Executive pastors and operations directors at multi-site churches with 3+ campuses and 5,000+ aggregate weekly attendance. There are approximately 1,500 multi-site churches in the US.

## Impact If Built
Enables early intervention when a campus begins declining — catching trends 6 months earlier than current reporting, potentially preventing campus closures that cost $500K-$2M each and displace 200-500 attending members.
