# A Look-Drift Check Across Episodes and Versions

**Niche:** [[niches/postproduction-studios/long-form-picture-finishing/profile|Long-Form Picture Finishing]]
**Industry:** [[industries/postproduction-studios|Postproduction Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A series' look is set by one colorist in episode one and carried by others through episode ten, and drift is found by the cinematographer in a supervised session that costs hundreds of dollars an hour.
**Tags:** #tacit-knowledge-ml #cnns #contrastive-learning #feature-engineering #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to carry a series' look consistently across every episode, colorist, HDR grade and SDR trim inside the streamer's delivery window, and whoever does it with the fewest supervised sessions and redeliveries takes the show.

## The Problem
The look of a series (skin tone, contrast, how night exteriors sit, how the two timelines differ) is a set of decisions a lead colorist and DP make early and then hold. Later episodes are graded by other colorists, sometimes at other facilities, under deadline. The SDR trim has to keep the same intent. Drift is subtle: a location that is warmer in episode six, a character's skin a touch magenta, a flashback palette creeping toward the present. The DP spots it in a supervised session, and the fix eats time booked for creative work.

## Why Nobody Has Built This
Grading tools measure signals (waveforms, vectorscopes, Dolby Vision analysis), not look consistency against a reference. "Same look" is a colorist's tacit judgement, and nobody has captured the reference shots and accepted grades as a dataset.

## What to Build
A look reference built from the approved shots of early episodes, embedded per scene type, location and character. Each new episode's grade is compared against it shot by shot, and the tool flags the shots that sit outside the accepted range, with the deviation shown (warmer, lifted blacks, skin hue shift) and the closest approved reference beside it. HDR and SDR trims are checked against each other the same way.

## Target Customer
Heads of finishing and lead colorists at facilities grading multiple scripted series a year.

## Impact If Built
If drift is caught before the supervised session, one session per episode could go back to creative work (estimate), and later-episode colorists get an objective reference instead of a memory of the lead's look.
