# Commitments Made by Phone and Forgotten by Friday

**Niche:** [[niches/movie-theaters/film-programming-and-booking/profile|Film Programming & Booking]]
**Industry:** [[industries/movie-theaters|Movie Theaters]]
**Type:** Fix (Pain Point)
**One-liner:** A buyer promises a distributor the large auditorium for a second week in exchange for a better scale, and the theatre schedules over it because the promise was never written where the scheduler looks.
**Tags:** #large-language-models #transformers #workflow-orchestration #compliance #quick-win #automation
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to turn each week's screen time into the most theatre margin, but that produces two contests with different winners: the weekly allocation of screens and showtimes, won by whoever forecasts each theatre's demand best, and the terms and settlement negotiated with each distributor, won by whoever keeps the best record of what was agreed and how each sales office settles. Decomposed into contested sub-niches below.

## The Problem
Holdover calls produce commitments: minimum showtimes, auditorium size, run length, no move to matinees before week three. They are agreed verbally and noted, if at all, in the buyer's own file. The theatre manager or scheduler building the grid doesn't see them, and the distributor's sales office notices the breach in the next week's grosses.

## Why It's Still Broken
Commitments don't fit any field in the ticketing system, buyers are on the phone all Monday, and there is no shared place between the head office and the theatres for anything but the schedule itself.

## What a Fix Looks Like
Capture each call's outcome as a short structured record (film, theatre, commitment, dates) drafted from the buyer's notes or a recorded summary, and enforce it as a constraint the scheduling screen warns on. Close each record when the run ends and attach it to the settlement.

## Who Feels the Pain
Film buyers whose word with distributors is their main asset; theatre managers blamed for breaches they couldn't see; distributors' sales offices.

## Impact If Fixed
Fewer broken commitments means fewer settlement disputes and better terms on the next booking, at the cost of a minute per call.
