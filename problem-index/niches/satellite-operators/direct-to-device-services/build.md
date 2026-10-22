# A Coverage Promise the Carrier Can Market

**Niche:** [[niches/satellite-operators/direct-to-device-services/profile|Direct-to-Device: Users Beyond the Last Tower]]
**Industry:** [[industries/satellite-operators|Satellite Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A carrier selling satellite texting can't tell a customer the chance a message gets through from a given valley at a given hour, because nobody models direct-to-device coverage as a probability.
**Tags:** #gradient-boosting #gaussian-processes #time-series-forecasting #monte-carlo-methods #revenue-impact #feature-engineering
**Contested on:** Every serious competitor in this niche is fighting to deliver texts, then voice and data, to ordinary phones outside terrestrial coverage within the FCC's emission limits and its carrier partner's spectrum, and whoever lights up coverage the carrier can promise to its customers first, without degrading the terrestrial network next door, takes the carrier partnership.

## The Problem
Direct-to-device service depends on how many satellites are overhead, beam capacity shared among everyone under it, the phone's position and surroundings (tree cover, canyon walls, inside a car), and emission limits that cap power near terrestrial networks. A carrier marketing the service has coverage maps, but a map says nothing about delay or the odds of success.

## Why Nobody Has Built This
The service is new, measured outcomes are sparse, and each satellite operator holds its own constellation and beam data while the carrier holds the subscriber data. Neither has an incentive to publish a number that may disappoint.

## What to Build
A model trained on delivery logs (attempt, location, time, device, satellites visible, beam load, latency, success) that predicts success probability and expected delay for any place and hour, updated as the constellation grows. It drives marketing claims, in-app guidance ("move into the open; expected delay four minutes"), and capacity planning for disaster surges.

## Target Customer
Satellite partnership leads at carriers and product teams at direct-to-device operators.

## Impact If Built
Claims the carrier can defend, fewer disappointed customers, and a measured case for each step from texting to voice and data.
