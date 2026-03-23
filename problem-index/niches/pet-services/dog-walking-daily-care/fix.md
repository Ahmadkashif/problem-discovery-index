# Unpaid Travel Time Between Walks

**Niche:** [[niches/pet-services/dog-walking-daily-care/profile|Dog Walking & Daily Pet Care]]
**Industry:** [[industries/pet-services|Pet Services]]
**Type:** Fix (Pain Point)
**One-liner:** Dog walkers spend 25-35% of their work day traveling between client homes with no compensation — effectively earning $12-15/hour when travel time is included in their hourly rate calculation.
**Tags:** #regression #tabular-ml #automation #worker-facing

## The Problem
A walker charges $20 for a 30-minute walk but spends 15-20 minutes traveling to the next client. Their effective hourly rate drops from $40/hour (walk time only) to $24-27/hour (including travel). Over a 6-hour work day with 8 walks, 2-3 hours are unpaid travel. Walkers don't track this because they view each walk as a discrete transaction, not a day of work with productive and unproductive time. The result: walker income is systematically lower than it appears, and the business is less viable than the per-walk pricing suggests.

## Why It's Still Broken
The per-walk pricing model (industry standard across Rover, Wag, and independent walkers) doesn't account for geography. A walk at a client 5 minutes away is the same price as a walk at a client 25 minutes away. Walkers resist geographic pricing surcharges because clients compare on per-walk price. There's no tool that helps walkers understand their true effective rate by client, identify money-losing routes, or make data-driven decisions about which clients to keep, which to price higher, and which geographic zones to focus growth efforts on.

## What a Fix Looks Like
A profitability tracker that logs walk start/end times and GPS location, calculates travel time between each walk, and shows the walker their effective hourly rate per client, per day, and per week. The system identifies unprofitable clients (those requiring 20+ minutes of travel for a $20 walk) and suggests actions: raise the price for distant clients, cluster new client acquisition near existing clients, or restructure the daily schedule to minimize travel. Simple color-coded geography shows "profitable zones" vs. "money-losing zones."

## Who Feels the Pain
Solo walkers doing 6-10 walks per day who feel busy but can't understand why their take-home pay doesn't match their walk count — the hidden cost of travel is invisible without tracking.

## Impact If Fixed
Increases effective hourly rate by 15-25% through geographic optimization and informed pricing, worth $300-600/month for a full-time walker, and gives walkers the data to make smart growth decisions about where to add clients.
