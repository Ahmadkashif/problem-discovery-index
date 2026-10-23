# The Medical Assistant's Refill and Message Queue

**Industry:** [[physician-practices|Physician Practices]]
**Type:** Worker Life Changing
**One-liner:** Between rooming patients, a medical assistant clears dozens of refill requests, portal messages and result notifications under the physician's standing orders, and is blamed for both the delay and the mistake.
**Tags:** #large-language-models #bert #logistic-regression #evaluation-metrics #worker-facing #compliance #automation

## The Problem
A medical assistant's day has two jobs. The visible one is rooming: bringing the patient back, taking vitals, reconciling medications, running screening questionnaires and getting the room ready before the physician walks in, about every fifteen minutes. The other is the queue. Pharmacies send refill requests, patients send portal messages ("is this rash normal?", "can I get a letter for work?"), labs send results that need a call, and specialists send notes that need filing. Practices route much of this to MAs under standing protocols. An MA can approve a 90-day refill of a stable blood pressure drug if the patient was seen in the last year and the last potassium was normal. Anything outside the protocol goes to the physician.

BLS counts 430,490 medical assistants in physicians' offices, the largest occupation in the industry, at a mean $20.29 an hour (OEWS, May 2023). The queue grows while they room patients and is still there at 5 p.m.

## Why It Matters to the Worker
Each refill decision means opening the chart, finding the last visit date, the last relevant lab and any interacting drug, then checking the protocol, which often lives in a binder or the MA's memory. Doing it fast and doing it safely pull in opposite directions. A missed lab on a lithium or warfarin refill can harm a patient, and a refill held without reason triggers an angry call. The MA carries clinical risk without clinical authority and is paid accordingly. Portal messages are worse, because the MA must decide whether each one is routine, needs the nurse, or is an emergency written in casual language.

## What a Solution Looks Like
Each refill request arrives pre-checked against the practice's own protocol: last visit, last lab against the drug's monitoring rule, interactions, controlled-substance status. The MA sees "approve" or "route to physician" with the reason and the evidence. Portal messages arrive sorted by intent and urgency, with a drafted reply for the routine ones and the worrying ones flagged to the top. The MA confirms or corrects, and those corrections improve the triage.

## Impact If Solved
Pre-checked refills could cut handling time from ~3 minutes to under 1 per request (estimate). At ~40 requests a day per MA (estimate), that returns about an hour and a half a day. Fewer refills would be approved against a missing monitoring lab, and the MA could leave when clinic ends instead of an hour later.
