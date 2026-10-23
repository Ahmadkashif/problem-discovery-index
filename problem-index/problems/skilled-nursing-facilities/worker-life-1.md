# The Med Cart, Thirty Residents and a One-Hour Window

**Industry:** [[skilled-nursing-facilities|Skilled Nursing Facilities]]
**Type:** Worker Life Changing
**One-liner:** An LPN pushing a medication cart spends most of her shift on passes that cannot fit inside the time window, interrupted every few minutes and personally exposed to every error; she could get back the time and the margin to think about the residents in front of her.
**Tags:** #optimization-fundamentals #large-language-models #gradient-boosting #worker-facing #automation #compliance #quick-win

## The Problem
Licensed practical nurses are the facility's medication workforce: 171,290 of them in nursing care facilities in May 2023, at a mean of $30.64 an hour (BLS OEWS). On a long-stay hall one LPN may hold the cart for ~20–30 residents (estimate). Many residents take ten or more scheduled medications. Some must be crushed and mixed with food, some need a blood pressure or blood sugar first, and residents with dementia may refuse and need to be approached again later. Each dose is meant to be given within the facility's time window around its scheduled time, commonly an hour either side (recalled). A morning pass can take ~2 hours or more (estimate). Meanwhile the same LPN is often the charge nurse. She takes calls from the pharmacy and physicians, receives an admission, answers families, and is pulled away by falls and call lights. Late doses, missed doses and "drug not available" entries pile up in the eMAR exception report.

## Why It Matters to the Worker
The pass is where the LPN's licence is most exposed. A wrong dose, a missed Parkinson's medication or an insulin given without a check can harm a resident and end up on a state board complaint, and the time pressure makes all of them more likely. Surveyors watch medication passes directly, and an error rate of 5% or more is a citable deficiency (recalled). The nurse who rushes to finish on time is cutting corners, and the nurse who does it properly finishes late and starts the next pass behind. Either way the clinical part of her job gets squeezed out: noticing that a resident has stopped swallowing well or is newly drowsy. That is why many LPNs move to clinics or home health, where the job is one patient at a time.

## What a Solution Looks Like
A med-pass assistant built on the eMAR the facility already uses. Before the pass, it orders the route by time-critical medications (insulin, Parkinson's drugs, antibiotics on fixed intervals) and by each resident's usual time of day. It flags in advance who is likely to refuse, who has a swallowing change noted by therapy, and which doses are not yet in the cart, so pharmacy can be called before the pass rather than during it. During the pass, a voice note ("Mrs. D. refused, will reattempt at 10") becomes the eMAR entry and a reminder. As-needed doses prompt their follow-up effectiveness note automatically. Interruptions that do not need the nurse are routed elsewhere.

## Impact If Solved
Shortening each pass by ~20–30 minutes (estimate) gives an LPN back an hour or more a shift across two passes. Fewer late and missed doses lower the error exposure surveyors test. Above all, the nurse regains enough time to use the clinical judgement she was licensed for rather than just keeping up with the cart.
