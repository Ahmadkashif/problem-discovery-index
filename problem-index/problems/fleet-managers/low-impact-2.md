# Fuel Management and Theft Detection

**Industry:** [[fleet-managers|Fleet Managers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Fuel card systems track purchases, but they can't detect the subtle patterns that distinguish legitimate fuel use from theft — fuel card sharing, odometer manipulation, and strategic fueling at non-contracted stations.
**Tags:** #isolation-forest #anomaly-detection #tabular-ml

## The Problem
Fuel is typically the second-largest fleet expense after depreciation. Fuel card fraud — drivers filling personal vehicles, selling fuel access, or manipulating odometer readings — costs fleets 3-7% of fuel spend. Beyond outright theft, suboptimal fueling behavior (ignoring contracted stations, fueling partially rather than fully, fueling at peak price times) adds 5-10% to costs. Fleet managers review fuel card reports monthly, but the volume of transactions (hundreds per day) makes manual detection of anomalies impossible.

## What Already Exists
WEX, Comdata, and Fleetcor provide fuel cards with transaction reporting, purchase controls (gallon limits, time-of-day restrictions, vehicle matching), and basic exception flagging. Telematics providers correlate fuel purchases with GPS location. These tools catch obvious violations but miss sophisticated patterns.

## The Customisation Gap
An intelligent fuel management system needs to: (1) model expected fuel consumption for each vehicle-route-driver combination, (2) detect anomalies that deviate from expected patterns (consumption too high, purchase location doesn't match route, transaction timing anomalies), (3) distinguish between theft patterns and legitimate explanations (detour due to road closure, extra load weight), (4) optimize fueling strategy across contracted station networks, and (5) predict fuel cost trends to optimize purchasing timing.

## Impact If Solved
Recovers 3-5% of fuel spend from theft and behavioral waste. For a 200-vehicle fleet spending $1.5M annually on fuel, that's $45K-$75K recovered. Reduces fleet manager time spent on fuel report review from 8-10 hours/month to 1-2 hours of exception review.
