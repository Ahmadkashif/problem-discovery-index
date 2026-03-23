# AI-Powered Substitute Finder

**Niche:** [[niches/faith-organizations/volunteer-ministry-schedulers/profile|Volunteer Ministry Schedulers]]
**Industry:** [[industries/faith-organizations|Faith Organizations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool today can automatically find and confirm a qualified replacement when a volunteer cancels 24 hours before their shift — currently requiring the ministry leader to send 15-20 individual text messages on a Saturday night.
**Tags:** #recommendation #ranking #tabular-ml #ai-agent #automation

## The Problem
When a nursery volunteer cancels Saturday night for Sunday morning, the children's ministry director starts texting every qualified volunteer who isn't already scheduled. This process takes 45-90 minutes — sending individual texts, waiting for responses, getting "sorry, not available" replies, and repeating until someone says yes. If no one accepts, the director scrambles Sunday morning, potentially combining age groups (violating ratio policies) or pulling a volunteer from another ministry (creating a gap elsewhere). This happens 5-10 times per week across all ministries at a mid-size church.

## Why Nobody Has Built This
Planning Center Services allows volunteers to find their own substitutes from a list, but in practice, fewer than 20% of canceling volunteers actually find their own replacement — the burden falls back on the ministry leader. Building an automated substitute finder requires knowing each volunteer's qualifications (background check current, trained for specific age groups, approved for specific roles), availability patterns (not just what they reported 3 months ago, but how responsive they typically are to last-minute requests), and engagement health (asking someone who served 3 of the last 4 weeks is a burnout risk).

## What to Build
An AI substitute finder that activates when a volunteer cancels. The system identifies qualified replacements ranked by: training/certification match for the specific role, historical responsiveness to last-minute requests, current serving frequency (avoid overburdened volunteers), and recency of last serve (prioritize those who haven't served recently). It sends personalized requests via the volunteer's preferred channel (text, app notification, email) and auto-confirms the first acceptance, notifying the ministry leader that the gap is filled.

## Target Customer
Ministry directors and volunteer coordinators at churches with 100+ active volunteers who spend 3-5 hours per week finding substitutes for canceled volunteer shifts.

## Impact If Built
Reduces substitute-finding time from 60 minutes to 5 minutes per cancellation, fills 90% of volunteer gaps before Sunday morning, and prevents the burnout of ministry leaders who currently absorb the gap-filling burden.
