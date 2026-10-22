# The Ag Broker's Five A.M.

**Industry:** [[commodity-brokers|Commodity Brokers]]
**Type:** Worker Life Changing
**One-liner:** A farm-town futures broker starts before dawn rebuilding, from three or four disconnected screens, the position of every farmer they serve, and spends the hours that should go to advice on copying, calling and paperwork.
**Tags:** #large-language-models #transformers #time-series-forecasting #worker-facing #automation #workflow-orchestration

## The Problem
An agricultural associated person at an introducing broker or a hedging desk carries a book of roughly 150 to 400 farm, feedlot and elevator accounts (estimate). The day starts around 4:30 or 5:00 a.m. with the overnight session: where corn, beans and cattle traded, what moved them, what the weather models did. The broker then writes or records a morning comment for clients, and works out which accounts need a call. Some are in margin, some hold options near expiry, some have a hedge-to-arrive contract at the elevator that needs rolling, and some have just had a crop insurance price discovery date pass.

The information sits in different places. Futures positions come from the clearing FCM's statement or portal. Cash sales live in the elevator's contract confirmations, which the farmer may or may not have sent. Crop insurance coverage sits with the insurance agent, and the LRP endorsements on cattle with whoever wrote them. The broker's own notes are in a notebook or a CRM. Before advising a farmer whether to add to a hedge, the broker reconstructs the farmer's whole position from memory and phone calls. Every recommendation then has to be documented well enough to survive an NFA review of the recorded line.

## Why It Matters to the Worker
The job is supposed to be advice: helping a family farm lock in a margin over cost and stay hedged through a rally without panicking. Most of the broker's time goes instead to gathering numbers and making routine calls. On volatile days the margin calls crowd out the conversations that matter, and on report days such as USDA's crop estimates the phone does not stop. The broker carries the anxiety of every client's position personally, because farmers hold their broker, not the FCM, responsible.

Their livelihood is also fragile. Their book is their income, and a missed call or a confusing recommendation loses an account that took years to win.

## What a Solution Looks Like
A morning view that assembles each client's futures and options from the FCM, the cash contracts and insurance coverage the farmer has shared, and the broker's notes into one position per farm, measured in bushels and head as well as contracts. Accounts needing attention are ranked with the reason: margin, expiry, a roll, a hedge ratio drifting above what is planted. A draft morning comment uses the overnight move and the broker's own past commentary style, for the broker to edit. After each call, a short summary of the recommendation is drafted from the recorded conversation for the broker to confirm.

## Impact If Solved
Recovering one to two hours a day per broker (estimate) and moving them from assembly to advice raises how many farms one broker can serve well. It also gives the broker a defensible record of every recommendation, and makes it less likely that a family farm loses its hedge, or its broker, in a price spike.
