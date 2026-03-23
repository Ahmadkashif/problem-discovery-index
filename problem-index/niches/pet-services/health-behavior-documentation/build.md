# Longitudinal Pet Health Observation Tracker

**Niche:** [[niches/pet-services/health-behavior-documentation/profile|Pet Health & Behavior Documentation]]
**Industry:** [[industries/pet-services|Pet Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool captures pet service providers' daily observations and detects gradual health/behavior trends over weeks and months — turning daily walkers and sitters into an early warning system for pet health decline.
**Tags:** #gradient-boosting #change-point-detection #tabular-ml #tacit-knowledge-ml

## The Problem
A dog walker sees Bella 5 times per week and notices she's slightly less energetic than usual. Is it the heat? Is she aging? Is something wrong? The walker doesn't know because they have no baseline data — just memory. Two months later, Bella is diagnosed with hypothyroidism, and the owner says "she's been slowing down for months." The walker noticed — but without data, the gradual decline was invisible. The same applies to behavioral changes (increasing anxiety, decreasing appetite, new reactivity), weight changes, and physical observations (limping, coat quality, eye clarity).

## Why Nobody Has Built This
Building a health trend detector requires: (1) structured daily observations from providers (who don't want to fill out forms), (2) enough historical data per pet to establish baselines, (3) change-point detection that distinguishes normal variation (tired on hot days) from meaningful trends (gradually declining energy over weeks), and (4) a way to communicate findings to owners and vets without being alarmist or practicing veterinary medicine. The data collection burden on providers is the primary barrier — logging must take under 30 seconds per visit to achieve adoption.

## What to Build
A 15-second post-visit observation logger: the provider rates 3-5 dimensions (energy level, appetite/water intake, mobility, mood, bathroom) on a simple scale (1-5 or emoji), with an optional note field. Over weeks and months, the system builds a baseline for each pet and flags deviations: "Bella's energy rating has decreased by 30% over the past 3 weeks — this is unusual for her." Flagged trends are shared with the owner as a "heads up" (not a diagnosis), with the recommendation to mention it at the next vet visit. A vet-facing summary shows the observation timeline if the owner chooses to share it.

## Target Customer
Dog walkers and pet sitters seeing the same pets 3-5 times per week who want to provide value beyond the service itself — becoming trusted health monitors that deepen client loyalty and justify premium pricing.

## Impact If Built
Detects pet health issues 2-8 weeks earlier than typical owner recognition, potentially saving pets' lives through early intervention, while differentiating providers as premium health-aware caregivers — justifying $2-5/visit price premiums.
