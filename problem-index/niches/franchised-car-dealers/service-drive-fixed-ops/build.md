# One Service Funnel From First Call to Closed Repair Order

**Niche:** [[niches/franchised-car-dealers/service-drive-fixed-ops/profile|Service Drive & Fixed Ops Revenue]]
**Industry:** [[industries/franchised-car-dealers|Franchised Car Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The store measures calls in one system, appointments in another and repair-order gross in the DMS, so nobody can say which service contacts turned into money.
**Tags:** #gradient-boosting #survival-analysis #feature-engineering #data-integration #evaluation-metrics #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor is fighting to raise customer-pay gross per service customer", but it splits into two contests with different winners: capturing inbound demand into booked appointments, won on the share of inbound service calls and messages that become kept appointments, and converting the vehicle once it is in the drive, won on approved labour hours per repair order from inspection findings. Decomposed into contested sub-niches below.

## The Problem
A fixed ops director sees a call-tracking report (calls answered, missed), a scheduler report (appointments, no-shows) and a DMS report (repair orders, hours, gross), each from a different vendor. None is joined at the customer and vehicle level, so the director cannot tell whether the agent that booked more appointments booked the ones that showed up and spent money, or whether a declined brake job came back three months later.

## Why Nobody Has Built This
Each vendor sells one stage and reports its own metric. The joins need DMS repair-order data, call recordings and scheduler data under different contracts, and DMS access has been contested.

## What to Build
A customer-and-VIN level funnel: inbound contact, intent, booking, arrival, repair order, inspection findings, approvals, declined work and return visit, with survival models of time-to-return for declined items and attribution of gross to the channel and agent that started it. It reports kept appointments and gross per inbound contact, not calls answered.

## Target Customer
Fixed ops directors at dealer groups running several brands and several phone, scheduling and inspection vendors.

## Impact If Built
The director can compare vendors and staff on the dollars that matter and spot the stage where the drive loses customers. A ten-store group handling ~300,000 service contacts a year (estimate) that lifts kept appointments per contact by one percentage point gains ~3,000 repair orders, ~$1M a year at ~$350 each (estimate).
