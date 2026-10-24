# Protocol-Aware Slot Lengths and Priced Overbooking

**Niche:** [[niches/diagnostic-imaging-centers/advanced-imaging-scheduling-utilisation/profile|Advanced Imaging Scheduling & Scanner Utilisation]]
**Industry:** [[industries/diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** MRI schedules use one slot length per body part and no model of who will show, when both table time and attendance can be predicted per booking.
**Tags:** #gradient-boosting #survival-analysis #monte-carlo-methods #optimization-fundamentals #time-series-forecasting #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn each MRI and CT referral into a completed, paid exam in the next open scanner slot, and whoever completes the most paid exams per scanner hour takes the account.

## The Problem
A scheduler books a 3T magnet into 30-minute brain slots and 45-minute prostate slots. The 9:00 patient is claustrophobic and takes 50 minutes, the 9:30 contrast study starts late, and by 2:00 the technologist is 40 minutes behind. Meanwhile the 3:30 slot, booked six weeks ago by a patient who has rescheduled twice, goes empty. Nobody priced the overbooking that would have filled it, because nobody knew the risk.

## Why Nobody Has Built This
RIS vendors sell record-keeping and templates, not optimisation, and centres have treated scheduling as clerical work. The data to predict table time sits in scanner logs and DICOM headers that the scheduling module never reads. Capacity vendors have chosen hospitals' operating rooms and infusion centres, where buyers are larger.

## What to Build
A scheduling layer over the RIS. It predicts each booking's attendance (gradient boosting on lead time, reschedules, prior no-shows, referral source, distance) and table time (quantile models on protocol, contrast, implant and sedation flags, coil, technologist). It simulates the day under those predictions and recommends slot lengths, which slots to double-book and which waitlist patients to move up, within each patient's authorization window. The schedule is scored on completed paid exams per scanner hour and technologist overtime, not on bookings.

## Target Customer
COOs of multi-site operators with ten or more magnets, and health-system imaging joint ventures run as freestanding sites.

## Impact If Built
Two extra completed exams per scanner per day is roughly 500 a year per magnet (estimate). At several hundred dollars of technical fee each, that adds $150,000–$250,000 a year per scanner, with overtime reduced rather than added.
