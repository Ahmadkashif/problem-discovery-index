# Seasonal Service Demand Positioned Before the Season

**Niche:** [[niches/field-service-software/equipment-dealer-service/profile|Equipment Dealer Service Departments]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Equipment service demand arrives in predictable seasonal waves against an installed base the dealer knows machine by machine, and dealers still discover the wave by being overwhelmed by it.
**Tags:** #time-series-forecasting #survival-analysis #gradient-boosting #confidence-intervals #evaluation-metrics #optimization-fundamentals #revenue-impact #automation
**Contested on:** Every serious competitor in dealer service software is fighting to get a machine back into the field inside the window the customer's season allows — and whoever cuts downtime during the narrow weeks that matter takes the dealership.

## The Problem
Harvest begins and the phone starts ringing. The shop fills, the parts the failures require are not on the shelf because they were not ordered, technicians work sixteen-hour days, and machines wait. Six weeks later the shop is quiet. Every element of this was foreseeable: the dealer knows every machine it sold and services, their hours, their ages, their service histories, and the date harvest starts in its territory within a week or two. The failures that arrive are the failures that always arrive. The positioning — parts on the shelf, technician capacity scheduled, pre-season inspections performed on the machines most likely to fail — is done by whatever the service manager remembers from last year.

## Why Nobody Has Built This
Dealer software is dominated by the manufacturers' own systems and by dealer management vendors whose centre of gravity is sales and finance rather than service operations, so service has had the least product investment of any part of the dealership. The forecast also requires joining the dealer's installed base records, service history, parts consumption and the manufacturer's telematics, which sit in three or four systems the dealer does not control. And service managers are experienced people who do position for the season by instinct and would say, correctly, that they already do this — the difference between instinct and a model is at the margin, and the margin is where the machines that waited three days live.

## What to Build
A seasonal demand forecast at the level of parts and technician hours, built from the dealer's installed base. Failure likelihood per machine over the coming season is modelled from model, age, accumulated hours, service history and, where available, telematics; aggregated, that yields expected demand by part and by repair type for the weeks ahead. From it follow three actions: parts stocking ahead of the season rather than after it, technician capacity and shift planning against a forecast curve, and — the highest-value one — a ranked list of customers whose machines are most likely to fail, for pre-season inspection. That last output converts a reactive emergency into scheduled work in the quiet weeks, which is better for the dealership's capacity, better for the technician's hours, and much better for the customer.

## Target Customer
Agricultural, construction and commercial truck equipment dealers, dealer groups, and the dealer management system and manufacturer software teams serving them.

## Impact If Built
Downtime during a season window is the dealership's entire service reputation, and moving even a modest share of in-season failures into pre-season scheduled work reduces it directly while smoothing a demand curve that currently forces overtime and then idleness. Parts positioned ahead of the season rather than expedited during it is a straightforward cost reduction that the dealer currently pays for in freight and in waiting.
