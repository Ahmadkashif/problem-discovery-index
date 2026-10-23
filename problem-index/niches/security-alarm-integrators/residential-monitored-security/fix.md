# The Panel That Stopped Arming and Nobody Noticed

**Niche:** [[niches/security-alarm-integrators/residential-monitored-security/profile|Residential Monitored Security & Smart Home]]
**Industry:** [[industries/security-alarm-integrators|Security Alarm Integrators]]
**Type:** Fix (Pain Point)
**One-liner:** A household that stops arming its system is already halfway out the door, and the arming log that shows it is never read.
**Tags:** #change-point-detection #descriptive-statistics #feature-engineering #quick-win #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to keep a monitored home paying through its contract term, its owner's move and the next communicator sunset, and whoever holds gross attrition lowest for each dollar spent acquiring the account takes the account.

## The Problem
Households stop arming for ordinary reasons. A sensor causes false alarms, a new dog trips the motion detector, the keypad code was forgotten, or the system feels like a bill rather than protection. The central station sees every open and close, or their absence. Nobody acts on it, because a disarmed system generates no signal and no work.

## Why It's Still Broken
Stations are paid to respond to signals, not to the absence of them. Dealers rarely receive arming data from wholesale stations as a routine feed, and when they do, no one owns reviewing it. Arming behaviour also varies by household, so a fixed rule produces noise.

## What a Fix Looks Like
A weekly change-point check on each account's arming frequency against its own baseline. When arming drops sharply, the system finds the likely cause in the same log (repeat false alarms on one zone, a recent trouble, a fine) and triggers a matched action: a service visit, a pet-immune sensor swap, a code reset or a check-in call.

## Who Feels the Pain
Retention teams who meet the customer only at cancellation; dealers whose purchased accounts go quiet inside the chargeback window; and households paying for protection they've stopped using.

## Impact If Fixed
Catching disengagement months before cancellation turns a lost account into a service visit, at the cost of a scheduled query on data the station already holds.
