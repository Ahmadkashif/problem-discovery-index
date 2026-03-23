# Mobile Parts Inventory for Roadside Vans

**Niche:** [[niches/towing-companies/roadside-tire-battery/profile|Roadside-Only Tire & Battery Services]]
**Industry:** [[industries/towing-companies|Towing Companies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Auto parts inventory systems exist for shops with shelves and barcode scanners — not for a van where 30 batteries, 50 tire plugs, and 20 lug nut sets rattle around in the back.
**Tags:** #automation #data-integration #quick-win

## The Problem
A roadside technician carries $2,000-$5,000 of inventory in their van: 15-25 batteries (different group sizes), tire repair kits, lug nut sets, jumper cables, fuel cans, and lockout tools. When they arrive at a call for a dead battery, they need to know: do I have a Group 35 battery in the van? They physically check — opening bins, moving boxes, checking stock. If they don't have the right battery, they drive to AutoZone (20-30 minute detour, losing the customer who calls someone else) or tell the customer they can't help. No tool tracks what's in the van in real time, auto-replenishes when stock is low, or pre-warns the technician when they're about to accept a call for a vehicle that needs a battery they don't carry.

## What Already Exists
Auto shop inventory systems (Mitchell 1, ShopBoss, Tekmetric) track parts on shelves in a fixed location with barcode scanning. Vehicle inventory apps (Sortly, Asset Panda) track general mobile inventory but don't understand automotive part compatibility (Group 35 battery fits Toyota Camry 2015-2023). None connect to the call queue to pre-check: "You're about to take a battery call for a 2019 Honda Civic — you need a Group 51R and you have 2 in the van."

## The Customization Gap
The tool needs: (1) a mobile-optimized inventory tracker designed for van storage (simple count by part category, no barcode scanning required), (2) vehicle-to-part compatibility lookup (customer's make/model/year mapped to required battery group, tire size, etc.), (3) pre-call inventory check ("you have the right battery for this call — proceed" or "you don't carry this battery — decline or detour to parts store"), and (4) auto-generated replenishment orders when stock drops below par level. The compatibility database is the key differentiator — linking customer vehicle data to required parts.

## Target Customer
Solo roadside technicians carrying $2,000-$5,000 in van inventory who currently track stock by memory and visual inspection.

## Impact If Solved
Eliminates 2-3 failed service calls per week caused by arriving without the right part ($100-$240/week in lost revenue). Prevents 1-2 parts store detours per week ($50-$80 in wasted time and fuel each).
