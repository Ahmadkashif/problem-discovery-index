# The Call Record That Writes Itself in the Car Park

**Niche:** [[niches/crm-platforms/field-sales-distributor-crm/profile|Field Sales & Distributor CRM]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A field representative makes fifteen calls a day and writes them up at home in the evening from memory, because every capture interface in the category was designed for someone sitting at a desk.
**Tags:** #transformers #seq2seq #large-language-models #cnns #evaluation-metrics #confidence-intervals #automation #worker-facing
**Contested on:** Every serious competitor in field sales software is fighting to capture what happened on a call from a vehicle in under a minute without typing — and whoever the representatives actually use takes the account.

## The Problem
The representative leaves the fifteenth account at half past four. In the day they have taken four orders, noticed a competitor's new facing in two stores, been told about a delivery that arrived short, agreed a promotion with one buyer and been asked to follow up on three things. At home that evening they open a laptop and enter what they can remember into a CRM designed for enterprise opportunity management. Most of it does not fit the data model, some of it is forgotten, and the competitive observations — the most valuable thing they saw all day — become a free-text note nobody reads.

## Why Nobody Has Built This
The buyer is sales leadership, whose requirement is visibility, and the resulting products are reporting systems with a data entry front end. The representative is not consulted and cannot refuse. The technical enablers for a genuinely different interaction — reliable offline speech recognition, structured extraction from natural language, photo understanding — have only recently become cheap enough to assume, so previous attempts at mobile field CRM reasonably produced forms on a smaller screen. And the segment is served by customisation of a horizontal product rather than by a vertical one, which means nobody owns the interaction design.

## What to Build
A call record produced from thirty seconds of speech in the car park. The representative says what happened — who they saw, what was ordered, what the issue was, what they promised — and on-device transcription and extraction produce a structured record: account, contacts, order lines, issues raised, commitments made, competitive observations. Photographs taken in the store are attached and classified, since a shelf photograph carries the competitive and compliance information that a text field never captures well. Orders flow into the order system rather than being re-entered. Commitments become follow-up tasks with dates. Everything works offline, because the back of a store has no signal. The representative confirms with one tap and drives to the next call. The measured objective is time from leaving the account to the vehicle moving, reported to the vendor and the customer, because it is the only number that predicts whether the product is used.

## Target Customer
Distributors, manufacturer representative organisations and consumer goods field teams, and the specialist field sales vendors competing against customised horizontal CRM.

## Impact If Built
An evening of unpaid administration per representative per day is the segment's defining complaint, and removing it is the difference between a system that is used and one that is worked around. The competitive and shelf observations that currently evaporate are the second prize and are arguably worth more to the organisation than the call record itself.
