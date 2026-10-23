# The Expediter's Hot List

**Industry:** [[aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Worker Life Changing
**One-liner:** The expediter spends the day on the phone finding out where parts are at outside heat treaters, platers and NDT houses, then repeating it to a prime's buyer who wants a recovery date, when an honest predicted date per lot would give back their days and their credibility.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #feature-engineering #worker-facing #workflow-orchestration #data-integration #automation

## The Problem
Most aerospace detail parts leave the shop at least once. A machined fitting goes out for heat treatment, comes back for finish machining, goes out for penetrant inspection and anodise or cadmium plating, and comes back for final inspection and FAI. Each outside processor must hold Nadcap accreditation and appear on the customer's approved list, so the choice is narrow, and the processors are themselves full. Nadcap's most-audited categories (chemical processing, heat treating, NDT) are exactly these.

The person in the middle is the expediter or production controller. Every morning they work the hot list: the prime's delinquent and at-risk lines from its supplier portal, sorted by aircraft need date. For each lot at an outside processor they call or email for status, because the processor's system does not talk to theirs and a "ship date" on a processor's quote is a hope. Then they phone the prime's buyer, who has a daily call of their own with the line, to give a recovery date. Each rate increase lengthens the list. Boeing's move from 42 to 47 737s a month in 2026, with further increases planned (Boeing 10-Q), flowed straight onto these lists.

## Why It Matters to the Worker
The job is all exposure and no control. The expediter answers for dates set by processors they don't manage, under supplier scorecards that affect whether the shop keeps the work. They spend ~1–3 hours a day (estimate) asking and relaying the same status questions, often to people who can't answer. A promise date that slips damages their credibility with the buyer and with their own plant manager, and recovery means weekend overtime that they have to ask the floor to work. Good expediters know which processor tells the truth and which lot will be late before it is. That knowledge is never written down, and it leaves when they do.

## What a Solution Looks Like
A view of every open lot with a predicted completion date and a confidence range, learned from the shop's own history of each processor's actual turn times by process, part family, season and load, and updated when a processor confirms receipt or shipment. Status requests go out automatically, and replies are read and posted to the lot. The tool proposes which lots to pull forward and where alternative approved processors exist. It drafts the daily response to each prime's delinquency list from the same data.

## Impact If Solved
Removing status-chasing returns ~5–15 hours a week per expediter (estimate). Dates that hold within a few days, instead of slipping a week or more, cut the weekend recoveries and the buyer calls that make the job miserable, and lift on-time delivery a few points where scorecards decide the next contract.
