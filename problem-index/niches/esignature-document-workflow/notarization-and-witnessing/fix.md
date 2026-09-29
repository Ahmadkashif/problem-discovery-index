# Finding a Commissioned Notary at Eight in the Evening

**Niche:** [[niches/esignature-document-workflow/notarization-and-witnessing/profile|Notarization & Witnessing]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Fix (Pain Point)
**One-liner:** Notary availability is a scheduling problem with hard constraints — commission state, act type, language, urgency — and it is solved by telephoning a list.
**Tags:** #convex-optimization #dynamic-programming #markov-chains #time-series-forecasting #evaluation-metrics #confidence-intervals #automation #quick-win
**Contested on:** Every serious competitor in remote notarization is fighting to produce an act that will be accepted — by the recipient county, registry, court or counterparty — in every jurisdiction the customer transacts in, and whoever has the widest accepted footprint takes the volume.

## The Problem
A signer needs an act completed this evening. The notary must be commissioned in the right state, available now, competent for this act type, and able to communicate with the signer — who may prefer Spanish. A coordinator works down a list, calling. It takes forty minutes to find someone or the act happens tomorrow, which for a closing or an estate document sometimes matters a great deal. On the other side, notaries sit idle at times when demand exists somewhere they cannot see.

## Why It's Still Broken
Notary marketplaces exist and mostly operate as directories with a booking layer rather than as matching systems: they list who is available and leave selection to the requester. The constraints are genuinely awkward — commission geography, act eligibility, language, and a demand profile that is bursty and concentrated at month and quarter end. Supply is independent contractors with their own schedules, which makes capacity planning a forecasting problem nobody runs. And the pain is distributed across many small coordinators rather than concentrated in one buyer, so it has never been anyone's priority.

## What a Fix Looks Like
Treat it as constrained matching, which is what it is. Eligibility as hard constraints — commission state and validity, act type, signer location where the state requires it, language — filtered before anything else, since an ineligible match is worse than no match. Assignment optimised over the eligible set on time-to-start, cost and the notary's completion history. Demand forecasting at daily and hourly resolution, which is very predictable given month-end, quarter-end and business-hour concentration, feeding into availability incentives so capacity exists when demand arrives rather than being discovered absent. Honest wait-time estimates to the requester, since the practical need is usually to know whether this can happen tonight rather than to have it happen instantly. And measurement of the fill rate by state, language and hour, which would immediately show where the supply gaps are — most obviously in non-English-language acts, where a coordinator's forty minutes is often a failure rather than a delay.

## Who Feels the Pain
Closing and legal coordinators calling down lists at inconvenient hours; signers whose act slips a day for scheduling reasons; notaries whose idle capacity is invisible to the people looking for them; and non-English-speaking signers, for whom the search frequently fails outright.

## Impact If Fixed
Constrained matching with forecast supply is standard operations research applied to a market currently running on directories and telephones. The language fill-rate measurement is the finding most likely to matter, because it is a documented access problem that nobody has quantified.
