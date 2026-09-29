# Compliance as a Rail the Landlord Cannot Fall Off

**Niche:** [[niches/proptech-platforms/small-landlord-tools/profile|Small Landlord Tools]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A small landlord's most expensive mistakes are procedural — the wrong notice period, a deposit held incorrectly, a screening question they may not ask — and every product in the segment ships a template and a disclaimer.
**Tags:** #large-language-models #bert #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #automation #worker-facing
**Contested on:** Every serious competitor selling to small landlords is fighting to get a person with four units from an empty unit to a compliant lease, a working ledger and a filed tax return without hiring anyone — and whoever makes that path unassisted takes the segment.

## The Problem
A landlord in a city with a source-of-income ordinance declines an applicant with a housing voucher, not knowing the ordinance exists. Another serves a notice with the wrong cure period and loses two months. A third holds a deposit in a personal account in a state that requires a separate one and owes statutory damages. None of these people intended to break a rule; they did not know the rule, and the software they were using presented a form and a disclaimer advising them to consult an attorney, which for a four-unit landlord is advice they will not take.

## Why Nobody Has Built This
Landlord-tenant law is genuinely local — state, county and municipal — and changes continuously, which makes maintaining it a content operation at a scale that free-to-landlord products have not been willing to fund. The liability question is the larger obstacle: a product that tells a landlord what to do is closer to giving legal advice than a product that supplies a form, and vendors have stayed on the safe side of that line for reasons their counsel can articulate clearly. The result is that the segment with the least legal capacity receives the least legal support, which is precisely backwards.

## What to Build
Encode the jurisdiction's requirements as rails in the workflow rather than as advice in a document. The product knows the property's address, so it knows the jurisdiction: the lease is assembled from clauses valid there, with required disclosures included automatically and prohibited terms structurally unavailable. Deposit handling enforces the state's rules on amount, account, interest and return timeline, with the itemisation deadline as a tracked obligation rather than something the landlord must remember. Screening criteria are constrained to what is permissible locally — which is the highest-stakes area, because the ordinances restricting criminal history and protecting source of income are exactly the ones a lay landlord has not heard of. Notices are generated with the correct period and service method. The content operation behind this is the product, and it is the same maintenance problem as court rules content — which means it is tractable with the same monitoring approach.

## Target Customer
Independent landlords with 1-20 units, the free-to-landlord platforms monetising through ancillary services, and housing agencies and landlord associations with an interest in compliance in this segment.

## Impact If Built
The errors this prevents are individually expensive for the landlord and individually harmful to the resident, and they happen because of ignorance rather than intent. Making the compliant path the default path is the only intervention that works at this scale, since neither training nor advice reaches a population doing this in the evenings. It also improves the position of residents in small-landlord housing, which is where enforcement is weakest.
