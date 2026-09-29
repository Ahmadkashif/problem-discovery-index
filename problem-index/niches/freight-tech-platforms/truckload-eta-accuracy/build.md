# Arrival Prediction That Models Hours, Dwell and Carrier Behaviour

**Niche:** [[niches/freight-tech-platforms/truckload-eta-accuracy/profile|Truckload — Coverage and ETA Accuracy]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Truckload ETAs are computed from distance and average speed, while the three factors that actually determine arrival — remaining hours of service, dwell at the facility ahead, and how this carrier behaves — sit in the same platform unused.
**Tags:** #time-series-forecasting #gradient-boosting #survival-analysis #confidence-intervals #evaluation-metrics #feature-engineering #cross-validation #revenue-impact
**Contested on:** Every serious competitor in truckload visibility is fighting to get location from a fragmented carrier base and turn it into an arrival time a dock will plan against — and whoever holds tracked-shipment share and ETA accuracy highest takes the account.

## The Problem
A truck is 340 miles out. The platform divides by an average speed and reports an arrival time. The driver has three hours of drive time remaining before a mandatory break, the facility ahead of this delivery has averaged four hours of dwell on weekday afternoons for the last six months, and this carrier has arrived late on 40% of its loads into this receiver. All three of those facts are known to the platform and none of them is in the estimate. The reported ETA is a straight-line calculation dressed as a prediction.

## Why Nobody Has Built This
Hours of service data is available through the same telematics integrations that supply location, and using it requires handling a genuinely sensitive dataset with driver privacy and enforcement implications that vendors have been cautious about — reasonably, since hours data misused is a compliance and labour issue. Facility dwell modelling requires the platform to make and publish statements about specific shippers' and receivers' facilities, which are frequently its own customers, and a platform that tells one customer that another customer's facility is slow has a commercial problem. Carrier behaviour modelling has the same shape. Every input is available and each one is politically awkward, which is a more honest explanation of the gap than any technical one.

## What to Build
An arrival model that uses what the platform holds. Remaining drive and duty time bounds the achievable distance before a break, which is the single largest omitted factor and is deterministic rather than statistical. Facility dwell is modelled per facility per day-of-week and time-of-day from the platform's own observations across all carriers, which is an estimate no individual carrier or shipper could produce. Carrier punctuality is modelled as a per-carrier effect with appropriate shrinkage for small fleets. Traffic, weather and construction enter as ordinary features. The output is a distribution, as the parent niche describes. The commercial awkwardness is handled by giving each party its own view — a receiver sees its own facility's dwell distribution, which is information it wants and cannot otherwise get, rather than a comparison against its peers.

## Target Customer
Visibility platforms, brokerages whose customer service depends on arrival accuracy, and large receivers whose labour planning consumes ETAs directly.

## Impact If Built
Hours of service alone corrects the largest systematic error in current ETAs, and facility dwell modelling corrects the second. Together they move truckload arrival prediction from a calculation to a forecast, which is the difference between a tracking product and an operational input — and the facility dwell dataset produced along the way is the most commercially valuable by-product available in this mode.
