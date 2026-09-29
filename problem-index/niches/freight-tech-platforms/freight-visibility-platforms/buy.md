# Exception Management From Operations Research Practice

**Niche:** [[niches/freight-tech-platforms/freight-visibility-platforms/profile|Freight Visibility Platforms]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Alert prioritisation under limited attention is a solved problem in operations and in every monitoring discipline, and freight visibility ships an exception list sorted by time.
**Tags:** #gradient-boosting #optimization-fundamentals #evaluation-metrics #confidence-intervals #hypothesis-testing #workflow-orchestration #automation #revenue-impact
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A logistics coordinator opens the visibility platform and sees 180 shipments flagged as exceptions. Some are three minutes late to a delivery with no appointment. One is a refrigerated load whose temperature has drifted and whose contents are at risk. One is a production input that will stop a line tomorrow morning. They all look the same. The coordinator works down the list until they run out of morning, and the ordering of that list is effectively arbitrary with respect to consequence.

## What Already Exists
Alert prioritisation, triage under resource constraints and consequence-weighted queueing are thoroughly developed in operations research, in clinical triage practice and in every mature monitoring discipline. Alert fatigue and its remedies are extensively documented. Routing and workflow tooling is commodity. The concepts and the implementations are all available; the freight category has simply not applied them.

## The Customization Gap
The adaptation is to freight's specific consequence structure. It requires: (1) consequence estimation per shipment — what actually happens if this is late, which depends on what the freight is, what it feeds, whether the receiving facility has an appointment and what the penalty structure is, none of which the visibility platform currently knows because the shipper never told it; (2) actionability filtering, since an exception nobody can do anything about is noise regardless of its consequence, and the list should surface the ones where intervention still changes the outcome; (3) intervention recommendations attached to the alert — reschedule the appointment, expedite, notify the customer — rather than a flag, because the coordinator's time is in deciding what to do rather than in noticing; (4) suppression of the predictable, since a lane that is late 40% of the time generates alerts that carry no information and should change the plan rather than the alert; and (5) outcome tracking, so the platform learns which exception types were actually worth attention at this shipper — which is the only way the prioritisation gets better.

## Target Customer
Visibility platforms, shippers with large exception volumes, and the brokerage operations teams reselling visibility to their own customers.

## Impact If Solved
Consequence-weighted prioritisation is the difference between a coordinator handling the five shipments that matter and the first twenty that appeared. The methods are borrowed; the adaptation is in eliciting consequence from the shipper, which no visibility platform currently asks for and which is the missing input rather than a missing technique.
