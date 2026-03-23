# Mobile Kitchen Load Planning and Equipment Manifest

**Niche:** [[niches/catering-companies/mobile-onsite-production/profile|Mobile & On-Site Production Caterers]]
**Industry:** [[industries/catering-companies|Catering Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product translates a catering menu and guest count into a truck loading manifest — what equipment, smallwares, provisions, and backup supplies to pack for an off-premises event.
**Tags:** #automation #workflow-orchestration #data-integration #tacit-knowledge-ml

## The Problem
Before every on-site event, the operations manager builds a loading manifest: which ovens, burners, sheet pans, chafing dishes, utensils, serving ware, and backup supplies go on the truck. This requires translating the menu into equipment needs (this menu requires 3 convection ovens, 2 burners, 14 sheet pans, 8 chafing dishes), checking what the venue provides, accounting for travel time and temperature maintenance, and adding backup items (extra Sterno, extension cords, a spare pan). An experienced operations manager does this from memory in 30 minutes; a new one spends 2 hours and still forgets the tongs.

## Why Nobody Has Built This
The menu-to-equipment mapping is tacit knowledge: the operations manager knows that a 200-person plated dinner needs different sheet pan counts than a 200-person station dinner, that outdoor events need twice the Sterno, and that this specific venue has only 3 working outlets. Encoding this knowledge into a systematic tool requires capturing hundreds of event configurations and their equipment outcomes — data that exists only in the operations manager's head.

## What to Build
An equipment planning system that takes the BEO (menu, guest count, service style, venue) and generates a loading manifest based on historical event data and rule-based equipment mapping. The system learns from the operations manager's adjustments ("I added 4 extra sheet pans because it was a complex dessert") to improve recommendations over time. Integrated checklist for truck loading and on-site setup verification.

## Target Customer
Operations managers at mobile catering companies who load trucks for 3-8 events per week and currently build manifests from memory and handwritten checklists.

## Impact If Built
Eliminating the "forgot the X" problem (which currently affects 15-20% of events, requiring emergency purchases or improvisation) saves $500-$2,000 per incident. Reducing manifest-building time from 2 hours to 15 minutes recovers 5-10 hours per week.
