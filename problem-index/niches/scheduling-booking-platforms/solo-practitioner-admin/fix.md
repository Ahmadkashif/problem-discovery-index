# Chasing a Deposit by Hand, Every Week

**Niche:** [[niches/scheduling-booking-platforms/solo-practitioner-admin/profile|Solo Practitioner Admin]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A practitioner takes a booking with a deposit due, the deposit does not arrive, and the only mechanism for noticing and chasing it is the practitioner remembering.
**Tags:** #descriptive-statistics #logistic-regression #hypothesis-testing #confidence-intervals #evaluation-metrics #worker-facing #quick-win #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to remove the unpaid administrative hour from a day whose income is measured in booked time — and whoever does that takes the independent practitioner, who is the category's largest and least-served population.

## The Problem
A booking is taken on Tuesday with a deposit due within forty-eight hours. Nothing happens. There is no unpaid-deposit list, no reminder, and no automatic release of the slot. The practitioner notices on Sunday while looking at next week, sends an awkward message, receives an apology and the deposit, and repeats this three or four times a week. Occasionally they forget entirely, the client arrives having never paid, and asking at that point is more uncomfortable than absorbing it.

## Why It's Still Broken
Deposits were implemented as a payment collected at booking, so the case where payment does not complete was treated as an abandoned booking rather than as a booking with an outstanding balance — a modelling gap rather than a missing feature. There is no outstanding-balance concept in most of these products, so there is nothing to build a chase on. And the practitioner absorbs the cost personally, which means it never becomes a support ticket the vendor would see.

## What a Fix Looks Like
Model the outstanding balance and act on it. An explicit unpaid-deposit state with a due time, visible as a list, which is the minimum and does not exist in most products. Automatic reminders on a short escalating sequence, in the practitioner's voice, with a payment link, which resolves the large majority without any human involvement. A stated release rule — the slot returns to availability if the deposit is not paid by a given time — communicated to the client at booking, which is fairer than the current implicit arrangement and removes the awkward conversation entirely. Payment on arrival as a fallback path, prompted at check-in rather than left to the practitioner to remember. And a weekly summary of what is outstanding and what was recovered, so the practitioner can see the money the mechanism is returning, which is what makes them keep it switched on.

## Who Feels the Pain
Practitioners doing collections work between clients; clients receiving an awkward personal message about a payment they simply forgot; and businesses absorbing unpaid deposits because chasing them is more uncomfortable than the amount.

## Impact If Fixed
An outstanding-balance state and a short reminder sequence are ordinary functionality that resolves most of these cases without the practitioner's involvement. The stated release rule removes the awkwardness rather than automating it, which is the better outcome for both parties.
