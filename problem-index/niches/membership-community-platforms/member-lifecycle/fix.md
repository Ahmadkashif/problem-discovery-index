# Daily Active Users as a Health Metric

**Niche:** [[niches/membership-community-platforms/member-lifecycle/profile|Member Lifecycle]]
**Industry:** [[industries/membership-community-platforms|Membership & Community Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The community looks healthy because forty of the four hundred members are talking constantly.
**Tags:** #descriptive-statistics #quick-win #graph-theory #evaluation-metrics #confidence-intervals #worker-facing #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to keep a paying member who decides in a fortnight and cancels in a quarter — and the contest splits cleanly enough that it is not terminal.

## The Problem
The dashboard shows active users and posts per day, and both look fine. Underneath, a small minority produce nearly all the content, most members have never received a reply, and a large group have not opened the app in a month while continuing to pay. The aggregate is dominated by the most active members, so it reports the health of the core and says nothing about the majority — who are the ones about to cancel.

## Why It's Still Broken
Aggregate activity is what the analytics library provides, so it became the health metric — a number computed over the whole population is dominated by its most active members and reports their experience as everyone's. Member-level views require a different data model. Founders read what they are shown. And a rising number feels like progress.

## What a Fix Looks Like
Report the distribution and the individuals. Show the distribution of activity rather than the total, which is the fix and immediately reveals how concentrated participation is. Report how many members received a reply in the last month, since that single number is a better health signal than any activity count. List the members who have posted and never been answered, as that is a short, specific and highly actionable list. Report members who have not visited in thirty days but are still paying, because they are the cancellation queue and nobody is looking at it. Segment by tenure, since the newcomer's experience is the one that determines renewal and is invisible in an aggregate. Show reciprocity — how many members have a two-way relationship with anyone — which is the closest available proxy for belonging. Report the share of content produced by the top ten members, as the concentration is the structural risk. Track these weekly rather than watching a line go up. Give the founder a list of three people to reach out to, which is what they can actually do. And stop leading with activity, because the metric shown is the metric managed.

## Who Feels the Pain
Members who posted once and were never answered; founders reassured by a healthy-looking number; platforms whose churn is unexplained; and communities that feel busy and are hollow.

## Impact If Fixed
A number computed over the whole population is dominated by its most active members and reports their experience as everyone's. Replying-rate and members-with-no-reply are one query each and describe the community the aggregate conceals.
