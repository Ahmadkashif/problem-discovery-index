# The Service Advisor Buried in Status Calls

**Industry:** [[franchised-car-dealers|Franchised Car Dealers]]
**Type:** Worker Life Changing
**One-liner:** A service advisor spends the day answering "is my car ready?" and chasing approvals by phone while new customers' calls ring out, and gets back the hours to do the part of the job that requires judgement.
**Tags:** #large-language-models #transformers #seq2seq #worker-facing #automation #workflow-orchestration #revenue-impact

## The Problem
A service advisor at a franchised store writes up ~15–25 repair orders a day (estimate). Each one means greeting the customer in the drive, interviewing them about the concern, walking around the car, writing the concern line the technician will work from, then selling the inspection findings, calling for approval, ordering parts, updating the customer, and cashing them out. In between, the phone rings. Customers call for status, to approve work, to ask about a recall letter, to book next week. Car Wars tracked roughly 53 million inbound service calls across its dealer network in 2025 and counted about 19 million of them as missed opportunities: 53% of the missed calls went to voicemail and 29% of callers hung up on hold, and only about 4 million appointments were booked (Car Wars CEO, CBT News, March 2026).

The advisor is the person those missed calls land on later, as an angry customer at the counter or a voicemail queue at 5 p.m. The independent-shop version of this overload is mapped at [[problems/auto-repair-shops/worker-life-2|Service Advisor Communication Overload]]. What the franchise adds is three layers that shop doesn't have. Many franchised stores route calls through a BDC, but status and approval calls still end up at the advisor, because the BDC agent cannot see the technician's progress or price the job. A share of the work needs the OEM's say-so: recall bookings depend on parts and campaign status, and warranty repairs above a threshold need prior authorisation before the advisor can tell the customer anything. And the advisor's handling of all of it shows up in the OEM's service satisfaction survey.

## Why It Matters to the Worker
Advisor pay commonly mixes a base with commission on customer-pay sales, and at many franchised stores a bonus tied to the OEM satisfaction score (estimate; pay plans vary by store). So every interrupted write-up and every unanswered approval call costs them money as well as the store, and so does every customer who leaves unhappy about a callback that never came. The work is constant context switching: a status call breaks off an inspection presentation, which breaks off a parts order. Long days and high turnover in the role are widely reported (estimate; no turnover survey was checked).

It also wastes the part of the job that needs a person: listening to a customer describe a noise and asking the questions that pin it down, explaining why a repair matters, and deciding what to recommend.

## What a Solution Looks Like
An agent that answers the store's service line and texts in the advisor's name: it books and reschedules appointments directly into the DMS scheduler against real technician capacity, gives status from the repair order and the technician's clock, sends inspection photos and estimates for approval by text and records the approval on the repair order, and looks up open recalls by VIN. It hands the advisor only the calls that need them, with a summary. At write-up, it drafts the concern line from the customer's own words and the advisor's walk-around notes, for the advisor to edit.

## Impact If Solved
If an advisor fields ~30–60 calls a day at a few minutes each (estimate), taking status and approval traffic off them returns one to two hours a day, cuts the voicemail backlog that turns into counter complaints, and lets them spend the time on write-ups and recommendations, where their commission and the customer's trust are earned.
