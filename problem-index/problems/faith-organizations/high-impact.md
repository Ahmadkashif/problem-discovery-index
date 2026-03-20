# Congregation Engagement & Retention Prediction

**Industry:** [[faith-organizations|Faith Organizations]]
**Type:** High Impact
**One-liner:** New attendees stop disappearing silently — staff get actionable alerts before a family drifts past the point of return.
**Tags:** #gradient-boosting #survival-analysis #decision-trees #feature-engineering #evaluation-metrics #maximum-likelihood-estimation #probability-distributions #expectation-variance-covariance #cross-validation #tacit-knowledge-ml #revenue-impact

## The Problem
Faith organizations lose 30-40% of new attendees within the first six months, and most never realize it until the family is already gone. Experienced pastors develop an intuitive sense for who is drifting — they notice a family switching from the 9 AM to the 11 AM service, then attending biweekly, then stopping small-group participation, then reducing their giving from weekly to monthly. These subtle, multi-signal patterns are invisible to anyone who hasn't spent years reading the room. When congregations grow past 150-200 members, even the most attentive pastor can't track every household, and the tacit pattern recognition that kept a small church tight-knit breaks down completely.

## Why It's Unsolved
The data exists in fragments — attendance check-ins, giving records, small-group rosters, event RSVPs — but no system synthesizes them into a longitudinal engagement trajectory. More fundamentally, the "label" is ambiguous: pastors disagree on when someone is disengaging versus simply busy for a season, making supervised learning difficult. The data collection challenge is that you need to capture the pastor's gut-level assessments of engagement over time and correlate them with behavioral signals to learn what the pastor is actually detecting. Privacy concerns in faith communities add another layer — members may resist the feeling of being "surveilled" by their church.

## What a Solution Looks Like
A survival-analysis model ingests weekly attendance, giving transactions, small-group check-ins, volunteer participation, and event registrations for each household. It outputs a time-to-disengagement hazard score and flags households crossing a configurable risk threshold. The pastor's dashboard shows a ranked list of at-risk families with the top contributing factors (e.g., "Attendance dropped 60% over 8 weeks; giving shifted from weekly to monthly; left men's group"), enabling targeted pastoral outreach — a personal phone call, a coffee invitation, a home visit — before the family is gone.

## Impact If Solved
Reducing new-attendee attrition by even 10 percentage points at a 500-member church with $2M annual giving translates to $150K-$300K in retained giving per year, plus the compounding community effects of families who stay, serve, and invite others. For the pastor, it replaces anxious mental scorekeeping with a reliable early-warning system.
