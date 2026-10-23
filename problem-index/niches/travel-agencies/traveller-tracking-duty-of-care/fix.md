# The Check-In Nobody Answers

**Niche:** [[niches/travel-agencies/traveller-tracking-duty-of-care/profile|Traveller Tracking & Duty of Care]]
**Industry:** [[industries/travel-agencies|Travel Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** After an incident the tracking tool sends "are you safe?" messages, a large share go unanswered, and the security team cannot tell a traveller in danger from one who ignored a text.
**Tags:** #logistic-regression #bayesian-inference #evaluation-metrics #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to tell a company within minutes of an incident which of its people are in the affected area, including those who booked outside the programme, and whoever accounts for every traveller fastest takes the account.

## The Problem
Check-in requests go to everyone flagged near an incident, including people who left yesterday or were never there. Responses trickle in; non-responses pile up; the team escalates by phone in arbitrary order.

## Why It's Still Broken
The flag list is built from stale itineraries, so many recipients rightly ignore it, which trains everyone to ignore it. Nothing scores who among the non-responders is most likely to be affected.

## What a Fix Looks Like
Send check-ins only to people whose current location is likely inside the area, using the latest flight status and hotel evidence; rank non-responders by probability of being affected and by vulnerability; escalate in that order; and record each resolution so the next incident's targeting improves.

## Who Feels the Pain
Security operations staff in the first hours of an incident; travellers spammed with irrelevant alerts; executives waiting for a number.

## Impact If Fixed
Fewer false alerts, higher response rates, and phone escalation spent on the people who might actually need help.
