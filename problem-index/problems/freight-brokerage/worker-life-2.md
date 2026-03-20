# Check-Call Automation and Shipment Status Monitoring

**Industry:** [[freight-brokerage|Freight Brokerage]]
**Type:** Worker Life Changing
**One-liner:** Freight brokers who call drivers once or twice during transit to confirm location and ETA — a task that takes 1-2 minutes per load per check-call, adding up to 45-90 minutes daily for a broker managing 20-30 active loads — get automated check-calls via carrier app or ELD integration with exceptions surfaced when a shipment is behind schedule.
**Tags:** #logistic-regression #time-series-forecasting #feature-engineering #evaluation-metrics #change-point-detection #automation #worker-facing

## The Problem

Shippers expect proactive communication about their freight while it's in transit. Brokers who don't have automatic tracking must manually call drivers at regular intervals to confirm location and ETA — the "check-call" — and then relay that information to the shipper. For a broker managing 25 active loads across different transit days, check-calls consume 45-90 minutes daily of low-value status relay work.

Modern ELD (Electronic Logging Device) mandates mean most carriers have GPS tracking on their trucks. The data exists — the problem is the broker's TMS doesn't always have automated access to it, and for carriers not using a track-and-trace integration, the manual call remains necessary.

## Why It Matters to the Worker

Check-calls are the most mechanical task in freight brokerage — the broker is a human API relay between the driver and the shipper. It adds no judgment, no relationship value, and no margin. It is purely coordination overhead that consumes the broker's most limited resource: continuous attention throughout the business day.

## What a Solution Looks Like

A TMS integration that: (1) connects to ELD/GPS data for carriers with tracking integration (Samsara, KeepTruckin, Motive); (2) for carriers without tracking, sends automated SMS check-calls ("Reply with your current location and ETA to [destination]") at configured intervals; (3) computes expected arrival time from current location and remaining drive hours; (4) sends proactive shipper updates when shipment is on time; (5) alerts the broker only when a shipment is behind schedule or a driver goes dark. Broker manages exceptions, not routine status.

## Impact If Solved

Returns 45-90 minutes per day. Improves shipper satisfaction (proactive updates without requiring broker intervention). Enables earlier detection of service failures (shipment going dark = fraud signal) before the delivery appointment is missed.
