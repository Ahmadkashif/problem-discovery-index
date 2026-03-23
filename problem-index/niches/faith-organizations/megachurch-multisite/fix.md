# Cross-Campus Volunteer Burnout Detection

**Niche:** [[niches/faith-organizations/megachurch-multisite/profile|Megachurch Multi-Site]]
**Industry:** [[industries/faith-organizations|Faith Organizations]]
**Type:** Fix (Pain Point)
**One-liner:** Megachurch volunteer coordinators cannot see when a volunteer serves across multiple ministries at multiple campuses — a worship team member who also serves in children's ministry and parking may be serving 15+ hours/week without anyone noticing, until they disappear entirely.
**Tags:** #anomaly-detection #time-series-forecasting #tabular-ml #worker-facing #quick-win

## The Problem
Megachurches rely on 500-3,000 volunteers across 10-20 ministries. Each ministry manages its own volunteer roster in Planning Center Services, but no one has a cross-ministry view of total volunteer load. A dedicated volunteer might serve on the worship team Saturday evening, park cars Sunday morning, lead a small group Sunday evening, and join the tech team for Wednesday youth service — accumulating 12-18 hours/week. Ministry leaders see them as a reliable "once a week" volunteer without realizing they're serving 4 different ministries. The volunteer feels pressure to keep saying yes, burns out silently, and disappears — taking their skills, training, and relationships with them.

## Why It's Still Broken
Planning Center Services is organized by team, not by person. Each ministry leader schedules independently. There is no cross-ministry view that shows "this person is scheduled across 4 ministries this month." Volunteer coordinators at the organizational level exist at some megachurches but rely on manual spot-checks — pulling a name and checking across all ministry rosters. At 2,000 active volunteers, comprehensive cross-ministry monitoring is impossible without automation.

## What a Fix Looks Like
A volunteer health dashboard that aggregates scheduling data across all ministries and campuses, flags volunteers exceeding configurable thresholds (e.g., more than 8 hours/week, serving in 3+ ministries, no break in 8+ consecutive weeks), and trends serving hours per volunteer over time. When a volunteer's engagement pattern shifts (from consistent to sporadic — a burnout precursor), the system alerts the relevant ministry leaders and volunteer coordinator. The dashboard also identifies "single points of failure" — ministry roles where only one person is trained.

## Who Feels the Pain
Volunteer coordinators and executive pastors who watch their most dedicated volunteers cycle through enthusiasm, overcommitment, burnout, and departure on a 12-18 month cycle — losing 100+ trained volunteers per year to preventable burnout.

## Impact If Fixed
Reduces volunteer burnout-driven attrition by 30%, retaining 30-100 trained volunteers per year per megachurch. Each trained volunteer represents $2K-$5K in equivalent staff labor, making this a $60K-$500K annual retention impact.
