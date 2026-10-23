# The Service Call That Might Be a Setup

**Industry:** [[armored-car-services|Armored Car Services]]
**Type:** Worker Life Changing
**One-liner:** An ATM first-line technician drives alone to every jam the monitoring system raises, and cannot tell a worn card reader from a fault staged by robbers waiting in the car park; a dispatch that read the fault first would give back the safety of knowing which calls are real.
**Tags:** #lstms-and-grus #hidden-markov-models #gradient-boosting #evaluation-metrics #worker-facing #workflow-orchestration #compliance

## The Problem
A first-line ATM technician works a queue of fault tickets: a jammed card reader, a dispenser error, a full reject bin, a receipt printer out of paper, a deposit module that will not accept notes. Most calls are routine and take minutes. The technician usually travels alone, often in an ordinary van, and opens the machine's top section in front of whoever is standing nearby. On cash-handling calls the vault may be opened too.

Since at least July 2022, according to court documents, robbers have jammed ATMs on purpose and waited for the technician sent to fix them, a scheme the FBI was still tracking in 2026, and at least one technician has been injured in these robberies. To the dispatch system a staged jam looks like any other ticket. It is routed to the nearest technician to meet the contract's response time, at whatever hour the fault occurred.

## Why It Matters to the Worker
The technician carries a risk the job description does not mention. Every isolated drive-up machine after dark becomes a calculation: is this one real? Technicians who refuse a call or ask for backup lose time against a schedule that measures them on response and fix rates, and many are contractors paid by the call (estimate), so caution costs them money directly.

The fear does not stop at the incidents. A technician who has heard of a colleague being ambushed approaches every call differently: circling the site, waiting in the van, cutting short the checks that would find the real fault. Some quit. The ones who stay are left with no tools to tell the calls apart.

## What a Solution Looks Like
Dispatch that reads the fault before it sends a person. The machine's event log in the minutes before the fault, its fault history, the site's type and isolation, the hour and recent attacks elsewhere in the fleet produce a risk flag on each ticket. Flagged calls go out with two people, wait for daylight, get a guard or police escort, or get a remote check first. The technician sees why a call was flagged and can escalate any call without penalty. Every finding of foreign objects or tampering is recorded with one tap, so the flag improves.

## Impact If Solved
If a fleet's riskiest ~5% of calls, by site and hour, took most staged faults out of solo dispatch (estimate), technicians would face a fraction of today's ambush exposure. The other ~95% of calls would keep their response times, and a technician would get back the confidence to work an ordinary call as an ordinary call.
