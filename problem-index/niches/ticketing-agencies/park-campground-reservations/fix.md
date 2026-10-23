# Cancellations Taken by Scripts in Seconds

**Niche:** [[niches/ticketing-agencies/park-campground-reservations/profile|Public Park & Campground Reservations]]
**Industry:** [[industries/ticketing-agencies|Ticketing & Reservation Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** When someone cancels a peak-season campsite, it reappears instantly and is rebooked by an alert service or script before a person checking the site could see it.
**Tags:** #logistic-regression #change-point-detection #evaluation-metrics #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to allocate scarce campsites, permits and timed entries so that people rather than bots and cancellation scrapers get them, and whoever can show the agency the lowest share of bookings captured by automated tools takes the account.

## The Problem
Cancelled sites return to inventory immediately. Paid alert services poll the system constantly and notify subscribers, and some users run their own scripts. The occasional camper who checks the site by hand almost never sees a cancellation.

## Why It's Still Broken
Instant release looks fair and is simple to build. Polling traffic looks like ordinary browsing, and agencies have not defined a policy on alert services.

## What a Fix Looks Like
Batch cancelled sites into scheduled re-release windows or a short lottery among waitlisted users, and rate-limit high-frequency polling.

## Who Feels the Pain
Occasional campers, park staff answering complaints, and agencies under scrutiny over equitable access.

## Impact If Fixed
Cancelled sites go to a waitlist of people rather than to whoever runs the fastest poller.
