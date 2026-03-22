# Technician Upsell Consistency

**Niche:** [[niches/electrical-contractors/residential-service-repair/profile|Residential Service & Repair]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** Experienced residential electricians recommend panel upgrades, whole-house rewires, and surge protection when warranted — junior technicians miss the same signs on the same calls, creating a 2-3x revenue gap per technician that takes years of ride-alongs to close.
**Tags:** #tacit-knowledge-ml #cnns #object-detection #gradient-boosting #feature-engineering #worker-facing #revenue-impact #evaluation-metrics

## The Problem
In residential electrical service, the difference between a $150 outlet repair call and a $4,000 panel upgrade sale is whether the technician recognizes the signs that warrant the recommendation. An experienced electrician walks into a home, glances at the panel, and immediately sees: Federal Pacific Stab-Lok breakers (fire risk, recommend full replacement), double-tapped breakers (code violation), aluminum branch wiring (fire risk in pre-1975 homes), undersized main breaker for current load, or corrosion from water intrusion. They also notice ambient signals — knob-and-tube wiring visible in the basement, ungrounded outlets throughout the home, lack of GFCI protection in kitchens and bathrooms. A junior technician on the same call fixes the outlet and leaves, generating $150 instead of $4,000. There is no standardized assessment checklist that captures what experienced technicians see, and ride-along training takes 6-12 months before a junior begins recognizing these patterns reliably.

## Why It's Still Broken
The upsell identification problem is fundamentally a tacit knowledge challenge. Experienced electricians don't follow a mental checklist — they pattern-match across dozens of visual and contextual signals simultaneously. "The panel just looks wrong" is a real diagnostic statement from master electricians. Training programs teach NEC code but not the visual gestalt that experienced field electricians develop over thousands of panel inspections. ServiceTitan and competitors track upsell revenue per technician but offer no tools to help underperforming technicians identify opportunities — they can see the revenue gap but can't close it. The data collection problem is severe: to train a model, you'd need paired data of panel photos with expert annotations identifying every issue, and experts disagree on severity ratings 20-30% of the time.

## What a Fix Looks Like
A mobile-first diagnostic assistant that guides technicians through a structured whole-home electrical assessment at every service call. The technician takes 3-5 photos of the panel (cover off), and a CNN-based object detection model identifies manufacturer (flagging recalled brands like Federal Pacific, Zinsco), double-tapped breakers, visible heat damage, wire gauge mismatches, and corrosion. The system also prompts a 2-minute walkthrough checklist: "Check kitchen GFCI? Check bathroom GFCI? Visible knob-and-tube? Aluminum wiring at outlets?" Based on findings, it generates a prioritized recommendation sheet with NEC code references that the technician presents to the homeowner — transforming subjective judgment into a documented, defensible assessment that junior technicians can deliver as effectively as 20-year veterans.

## Who Feels the Pain
Junior technicians who know they're missing revenue opportunities but don't know what to look for, shop owners watching their best technician generate 3x the revenue of their newest hire, and homeowners living with hazardous electrical systems because the technician who showed up didn't recognize the danger signs.

## Impact If Fixed
Closes the 2-3x revenue gap between junior and senior technicians within 3-6 months instead of 3-5 years, adding $150K-400K in annual revenue per junior technician brought up to experienced-level upsell identification rates. Improves homeowner safety by catching hazardous conditions that junior technicians currently miss on 40-60% of service calls.
