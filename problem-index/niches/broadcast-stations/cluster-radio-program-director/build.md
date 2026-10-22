# Song Fatigue from the Station's Own Listening Data

**Niche:** [[niches/broadcast-stations/cluster-radio-program-director/profile|The Cluster Radio Program Director]]
**Industry:** [[industries/broadcast-stations|Broadcast TV & Radio Stations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A PD who can no longer afford callout research still has the station's stream logs and music log, and nothing turns them into a read on which songs are burning out.
**Tags:** #tacit-knowledge-ml #survival-analysis #gradient-boosting #change-point-detection #feature-engineering #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this niche (music research firms, music-scheduling vendors and listening-data analytics services) is fighting to tell a program director which songs to add, rotate and rest, and where listeners are tuning away, from signals measured between ratings releases and without a callout budget, and whoever gives the PD the music read they trust most takes the account.

## The Problem
Experienced PDs say they can hear when a song has peaked and when a currents category is wearing out the audience. Without tests, they rely on that ear, national charts and complaints. Burnt songs are rested late, and new songs are dropped before they have had a chance.

## Why Nobody Has Built This
Stream listening is a small, skewed sample of the broadcast audience. Joining it to the music log by the second takes data work no cluster can staff. Research vendors sell surveys, not models of the station's own data.

## What to Build
A model of tune-out and session survival around each song play on the station's stream and, in PPM markets, minute-level data where licensed. It controls for daypart, position in the hour and the preceding element, then tracks each song's effect over its life to flag fatigue and promising newcomers. The PD's past add and rest calls are recorded beside the signal, so the PD can see where their ear and the data agree.

## Target Customer
Cluster PDs and group heads of programming at radio groups that have cut research budgets.

## Impact If Built
A weekly music read at near-zero marginal cost, better-timed rests and adds, and the PD's ear captured where it is right.
