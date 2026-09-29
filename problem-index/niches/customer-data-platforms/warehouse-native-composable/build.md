# Activating Data You Never Hold

**Niche:** [[niches/customer-data-platforms/warehouse-native-composable/profile|Warehouse-Native Composable]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The composable model activates from the customer's own warehouse and does not hold their data, which solves governance and cost and leaves identity, latency and the modelling burden unaddressed.
**Tags:** #data-integration #workflow-orchestration #automation #graph-theory #evaluation-metrics #compliance #confidence-intervals #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to activate from a warehouse the vendor never touches, at the reliability and latency a customer-facing use case needs — and whoever does that takes the organisations that already own their data.

## The Problem
An organisation with a warehouse adopts the composable model. It works well for audience syncs on a daily cadence. Then someone asks for a suppression that must apply within minutes of a purchase, and the warehouse's own latency makes it impossible. Then someone asks who this person is across their three logins and there is no identity resolution because the model assumed the warehouse had one, which it does not. Then the data team, who now own the modelling the packaged platform used to do, become the bottleneck for every marketing request. The architecture's advantages are real and its gaps are structural.

## Why Nobody Has Built This
The composable model grew from the reverse activation category, which solved sync and treated everything else as the customer's problem — that scoping was correct for the beachhead and is now the constraint. Identity resolution is hard and the incumbents own the expertise. Real-time from a warehouse is a genuine technical limitation nobody has resolved cleanly. And the modelling burden is invisible in a sales process and decisive in operation.

## What to Build
Close the gaps without taking the data. Provide identity resolution that runs inside the customer's warehouse, which is the largest gap, is what the incumbents repositioned onto, and is the capability that would make the composable model complete. Solve the latency case with a streaming path alongside the batch one, since suppression and triggered messaging are customer-facing and daily is not acceptable for them. Supply the customer data model rather than requiring the customer to build it, because the modelling burden is where composable implementations actually stall and a good default model is most of what a packaged platform provided. Make audience definition usable by marketers rather than requiring the data team, which removes the bottleneck that is the model's main operational complaint. Monitor sync correctness at the destination, connecting to the packaged niche's fix, since the failure mode is shared. Integrate governance with the warehouse's own controls rather than reimplementing them, which is the model's structural advantage and should be exploited harder. Handle schema evolution in the customer's warehouse gracefully, which is the fix note's subject. Keep the vendor out of the data path as a stated guarantee, since that is the differentiator and should be auditable. Support organisations with a small data team, because the model currently assumes more capability than most buyers have. And measure the total operational burden it places on the customer, which is the honest comparison against the packaged alternative.

## Target Customer
Organisations with a warehouse and a data team, composable vendors competing on an incomplete stack, and the packaged incumbents deciding whether to meet the model.

## Impact If Built
The category solved sync and scoped everything else to the customer, which was right for the beachhead and is now the constraint. Identity resolution inside the customer's warehouse is the largest gap and is the capability that would make the model complete.
