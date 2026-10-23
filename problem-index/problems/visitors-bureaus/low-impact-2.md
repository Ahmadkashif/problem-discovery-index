# Convention Lead Distribution and Proposal Assembly

**Industry:** [[visitors-bureaus|Convention & Visitors Bureaus]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A bureau's sales team turns each planner's RFP into a lead for partner hotels and a bid proposal back to the planner, and the CRM that routes the lead knows little about which hotels actually fit the group or have the dates.
**Tags:** #large-language-models #word-embeddings #k-nearest-neighbors #logistic-regression #automation #workflow-orchestration #revenue-impact

## The Problem
A meeting planner looking for a city sends an RFP: dates and alternates, peak rooms and the room pattern by night, meeting space, rate range, history. It arrives through Cvent, the bureau's web form, email or a third-party sourcing firm, and often through more than one of those at once. The bureau's sales manager logs it as a lead (the reporting handbook's definition is any inquiry for at least ten peak rooms), decides which partner hotels to send it to, and collects their responses through the CRM's hotel extranet. They then assemble a proposal for the planner: hotel options and rates, the bureau's services, any incentive, venue photos and a destination pitch. A mid-sized bureau may handle several hundred leads a year (estimate).

The fit decision is done from memory. Does the group's space-to-rooms ratio work for this hotel, or will it eat the ballroom on a night the hotel can sell to a higher-rated group? Is the hotel already holding a tentative for those dates? Which general manager actually answers bureau leads? Hotels that get too many poor-fit leads stop responding, and planners who get slow or thin proposals drop the city from the shortlist.

## What Already Exists
Destination CRMs (Simpleview CRM, Tempest's iDSS) distribute leads to partner hotels, track responses through an extranet and log room nights for reporting. Cvent's sourcing platform carries the planner's RFP and lets hotels and bureaus respond. Groups360's GroupSync and hotel brands' own group tools target the same planners. Proposal tools such as DIGIDECK build polished bid documents.

## The Customisation Gap
The generic routing is a distribution list. The bureau-specific logic is: deduplicating the same RFP arriving by three routes; matching group profile to hotel fit using meeting-space ratios, room pattern, rate history and each hotel's displacement on the requested nights; knowing which hotels respond and win for which group types; tracking response deadlines per hotel so the proposal goes out inside the planner's window; and assembling the proposal from the hotels' actual responses rather than templates. The bureau also needs the lead record to feed its reporting definitions (lead, tentative, definite, lost with reason) without re-keying.

## Impact If Solved
Cutting lead handling from ~2-3 hours to ~30-45 minutes of a sales manager's time per lead (estimate), and sending each lead only to hotels that fit, gets proposals to planners faster and keeps hotel partners responding. For a bureau handling a few hundred leads a year, that returns several hundred hours of selling time.
