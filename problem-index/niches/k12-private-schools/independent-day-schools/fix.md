# Advancement-Enrollment Data Disconnect

**Niche:** [[niches/k12-private-schools/independent-day-schools/profile|Independent Day Schools (Non-Sectarian)]]
**Industry:** [[industries/k12-private-schools|K-12 Private Schools]]
**Type:** Fix (Pain Point)
**One-liner:** The advancement office cultivates donors without knowing which families are at attrition risk, and the enrollment team manages retention without knowing which families are major donors — two critical functions operating blind to each other.
**Tags:** #data-integration #revenue-impact #workflow-orchestration #worker-facing

## The Problem
The advancement director is cultivating a family for a $100K gift. The division head is about to have a difficult conversation with the same family about their child's academic performance. Neither knows about the other's interaction. When a major donor family withdraws, the school loses both the tuition and the giving — a $75K-$175K annual impact. When a family at attrition risk receives a solicitation call instead of a retention outreach, it accelerates their departure. These collisions happen because advancement and enrollment data live in separate systems managed by separate teams.

## Why It's Still Broken
Advancement platforms (Raiser's Edge, Blackbaud's fundraising suite, Virtuous) track donor relationships and giving history. The SIS tracks enrollment, academic performance, and parent engagement. These systems serve different departments with different workflows and privacy considerations — advancement staff should not necessarily see a student's grades, and teachers should not see a family's giving history. But the leadership team (head of school, division heads) needs a synthesized view for strategic decisions about retention and cultivation.

## What a Fix Looks Like
A leadership dashboard that joins enrollment health data (attrition risk score, engagement metrics, academic trajectory) with advancement data (giving history, solicitation status, donor tier) at the family level. The dashboard is accessible only to school leadership and flags conflicts: "Family X is a major donor prospect AND at attrition risk — coordinate outreach." It does not give advancement staff access to academic data or teachers access to giving data — it gives leadership the synthesis they need to avoid costly collisions.

## Who Feels the Pain
Heads of school who discover after a withdrawal that the family was both a major donor prospect and had unaddressed concerns that could have been resolved with a coordinated outreach.

## Impact If Fixed
Prevents 3-5 major donor family withdrawals per year worth $225K-$875K in combined tuition and giving revenue. Enables coordinated retention-cultivation strategies that deepen donor relationships among at-risk families.
