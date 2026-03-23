# Lapsed Giver Recovery

**Niche:** [[niches/faith-organizations/tithing-pledge-campaigns/profile|Tithing & Pledge Campaigns]]
**Industry:** [[industries/faith-organizations|Faith Organizations]]
**Type:** Fix (Pain Point)
**One-liner:** Churches lose 15-20% of regular givers each year to silent disengagement — giving stops without explanation — but no one notices for 2-3 months because giving data is reviewed as aggregates, not individual patterns.
**Tags:** #anomaly-detection #time-series-forecasting #tabular-ml #automation #worker-facing

## The Problem
A faithful member who gives $200/week suddenly stops giving. In a 500-member church receiving $30K/week, that $200 disappearance is invisible in the weekly total — especially if it coincides with a seasonal giving dip. By the time someone notices (usually at quarterly pledge reconciliation), the giver has been disengaged for 3 months. The reasons vary — job loss, health crisis, marriage difficulty, spiritual doubt, or simply switching to another church — but in all cases, earlier awareness enables pastoral care. The current system detects lapsed givers only when they're already gone.

## Why It's Still Broken
Churches resist individual giving monitoring because it feels intrusive — "Are we tracking how much people give so we treat big givers better?" This cultural norm means giving data is reviewed only in aggregate, and individual giving changes are noticed only by the volunteer counters who recognize handwriting on checks (and that system fails when giving moves online). The pastor may sense someone is pulling away based on attendance, but giving data — often a leading indicator — sits unreviewed in the giving platform.

## What a Fix Looks Like
A privacy-conscious alert system that flags significant giving pattern changes without exposing dollar amounts: "This household's giving pattern changed significantly in the last 30 days" — not "John Smith stopped giving $200/week." The alert goes to the care pastor, not the finance committee, framed as a pastoral care opportunity, not a financial concern. The system uses configurable thresholds (detect changes > 50% from baseline, after 3+ consecutive missed gifts) and can be set to alert only the senior pastor.

## Who Feels the Pain
Pastors who learn at year-end that a family they could have supported through job loss or crisis has been silently struggling for 6 months — and feels the church failed them by not noticing.

## Impact If Fixed
Enables pastoral outreach to struggling families 2-3 months earlier, retains 30-40% of would-be lapsed givers through timely care, and recovers $50K-$200K in annual giving per mid-size church that would otherwise silently leave.
