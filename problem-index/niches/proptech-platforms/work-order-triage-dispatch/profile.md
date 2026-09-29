# Work Order Triage & Vendor Dispatch

**Parent Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in maintenance triage is fighting to turn a resident's free-text complaint into the right trade, the right urgency and the right vendor without a site manager reading it — and whoever triages most accurately takes the account.

## Profile
**Market Size:** ~$1.3B US spend across maintenance triage, dispatch and vendor coordination
**Share of Parent Industry:** ~12% of proptech revenue
**Digital Adoption:** Medium-High — intake is digital, the decision after intake is a person
**Target Buyer:** VPs of Maintenance and regional operations directors; vendor marketplace operators
**Automation Potential:** Very High — this is text classification and matching against a corpus of millions of prior work orders with known outcomes

## What Makes This a Distinct Niche
A work order starts as a sentence a resident typed on a phone: "the sink is doing something weird," "there's a noise from the wall," "it's cold." Everything that follows — the trade dispatched, the urgency assigned, the parts the technician brings, whether a maintenance technician or an outside vendor goes, whether anyone needs to enter today because a leak is active — is inferred from that sentence by a property manager who has forty other things to do. The inference is genuinely hard for a person and unusually tractable for a model, because the operator holds millions of prior work orders where the same sentences were followed by a known diagnosis, a known trade, known parts and a known outcome. It is one of the best-posed supervised problems in the vault and it is performed by the busiest person in the building.

## Current Tools & Gaps
Work order intake through resident portals is universal, and some platforms offer a guided category picker, which residents use inconsistently because they do not know whether a wall noise is plumbing or HVAC. Vendor marketplaces have introduced dispatch automation based on availability and coverage rather than on suitability. Emergency detection is typically a keyword list. The gaps are consistent: nothing classifies the request against the operator's own corpus to infer the likely problem, nothing predicts whether the request can be resolved in-house or needs a specialist, nothing predicts required parts, and urgency is determined by the resident's choice of words rather than by what the described condition usually turns out to be. A resident who writes calmly about an active leak is triaged as routine.

## Problems
- [[niches/proptech-platforms/work-order-triage-dispatch/build|🔨 Build: Diagnosis, Urgency and Trade Inferred From the Resident's Own Words]]
- [[niches/proptech-platforms/work-order-triage-dispatch/buy|🛒 Buy: Conversational Intake Instead of a Category Picker]]
- [[niches/proptech-platforms/work-order-triage-dispatch/fix|🔧 Fix: Emergency Detection by Keyword List]]
