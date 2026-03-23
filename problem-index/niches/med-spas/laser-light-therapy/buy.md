# Scheduling System with Device-Aware Capacity Optimization

**Niche:** [[niches/med-spas/laser-light-therapy/profile|Laser & Light Therapy Clinics]]
**Industry:** [[industries/med-spas|Med Spas]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Scheduling tools book appointments by provider availability but don't optimize for device utilization — leaving expensive lasers idle while technicians are double-booked on simpler treatments.
**Tags:** #reinforcement-learning #recommendation #tabular-ml #automation #revenue-impact

## The Problem
A laser clinic's scheduling constraint is two-dimensional: provider availability AND device availability. A technician might be free at 2pm, but the IPL machine they need is booked until 3pm, while the fractional CO2 (which could serve the same patient for a different protocol) sits idle. Current scheduling systems model provider availability but not device allocation, leading to suboptimal device utilization. Clinics with 5-8 devices routinely have 2-3 idle while staff is fully booked on other equipment.

## What Already Exists
Vagaro, Booker, and AestheticsPro handle appointment scheduling for med spas. Some support "resource" scheduling (rooms, devices) as secondary calendar layers. However, none optimize scheduling to maximize device utilization — they simply prevent double-booking. The optimization question ("schedule this IPL session at 2pm or 4pm to maximize total device utilization for the day?") is not addressed.

## The Customization Gap
The scheduling engine needs device-aware optimization: modeling each appointment as requiring both a provider AND a device for a specific duration, then suggesting time slots that maximize total device utilization across the day. This includes: device-specific room assignments, prep and cooldown time between treatments, technician-device skill matching (not every tech is trained on every device), and priority booking for high-revenue devices during peak hours.

## Target Customer
Laser-intensive med spas with 4+ devices and 3+ technicians where device idle time exceeds 30%.

## Impact If Solved
Increases device utilization from 50-60% to 70-80%, generating $3,000-8,000/month in additional revenue per device from recovered idle time.
