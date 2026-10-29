# The Dispatcher Taking 911 Calls and Hospital Transfer Requests on One Console

**Industry:** [[ambulance-services|Ambulance Services]]
**Type:** Worker Life Changing
**One-liner:** The ambulance dispatcher gets back the attention a cardiac arrest call deserves when the hospital discharge coordinator asking for a stretcher at 3 p.m. no longer has to be taken by phone on the same console.
**Tags:** #large-language-models #transformers #time-series-forecasting #worker-facing #automation #workflow-orchestration

## The Problem
At a private operator that holds a county 911 contract and hospital transfer contracts, one communications centre does both jobs. On an afternoon shift a dispatcher may handle a 911 cardiac arrest, a fall at a nursing home, and twenty calls from hospital case managers and transfer centres. One wants a BLS stretcher for a discharge home, one an ALS transfer to a cardiac centre, one a critical care truck with a nurse for a ventilated patient, and one a dialysis patient whose ride has not appeared. Each phone request means asking the same questions: pickup and destination, level of care, oxygen, weight, isolation, insurance, whether there is a PCS. Then the dispatcher has to find a unit without dropping the county below its coverage plan.

The transfer calls are long and repetitive, and they arrive in clusters when hospitals discharge after rounds. The 911 calls arrive at random. When both peak together the dispatcher is typing a facility address while a unit waits for an assignment. She is also moving ambulances between posts every few minutes to keep the county map covered, and the crews she moves resent it.

## Why It Matters to the Worker
Dispatch is shift work with mandatory overtime, and centres short of staff hold dispatchers over into double shifts. The stress is not the volume alone. It is the constant switching between a life-threatening call and a clerical one, knowing that a wrong address, a missed oxygen requirement or a delayed assignment lands on a patient and on a crew who will blame dispatch. Each late 911 response is reviewed. Each angry hospital call about a late discharge is escalated. Neither is in her control when both queues share one person.

## What a Solution Looks Like
Take the scheduled and interfacility requests off the phone. Hospital case managers and transfer centres submit through a structured web form or a voice agent that asks the same questions the dispatcher would. The intake records level of care, equipment, isolation, weight, payer and PCS status. It flags what is missing, books a time window against forecast 911 demand and the units the plan reserves for it, and drops the request into the CAD queue as a ready-to-assign job. The dispatcher sees a clean queue, ranked by when each job must leave. She speaks to a hospital only when something is unusual. A short-horizon call forecast shows when the next 911 peak is likely, so transfers can be held or moved before the board runs dry.

## Impact If Solved
If even half of an operator's 300 daily transfer requests (an estimate for a mid-size urban operator) moved to structured intake, at four to six minutes per phone booking, each centre would get back 10 to 15 dispatcher-hours a day. That time goes back to the 911 console and to fewer held-over shifts.
