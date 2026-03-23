# Age-Appropriate Vehicle Configuration Management

**Niche:** [[niches/non-emergency-medical-transport/pediatric-medical-transport/profile|Pediatric Medical Transport]]
**Industry:** [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Fleet management tools track vehicles but not the child restraint equipment installed in each vehicle, leading to mismatches between child age/weight and available car seats.
**Tags:** #automation #data-integration #compliance

## The Problem
NEMT fleets serving pediatric patients must maintain an inventory of child restraint systems across vehicle types: rear-facing infant seats (for children under 2/30 lbs), convertible car seats (2-4 years/30-65 lbs), high-back boosters (4-8 years/40-100 lbs), and specialized restraints for children with medical equipment. Different vehicles may have different base anchors, LATCH system configurations, and space constraints that affect which car seats can be installed. Dispatchers must match the child's age/weight to a vehicle with the correct seat — a verification they do from memory, often incorrectly. When a driver arrives with the wrong car seat, the trip fails, and the driver must return to the depot, swap seats (a 15-minute process), and re-attempt the pickup.

## What Already Exists
Fleet management platforms (Samsara, Fleetio, Verizon Connect) track vehicle maintenance, location, and mileage. NEMT dispatch platforms track vehicle type (sedan, wheelchair van, stretcher). Car seat inventory management tools exist for retail (Graco, Britax dealer portals) and for car seat inspection stations, but not for fleet-level operational deployment. No NEMT tool links car seat assignments to vehicle IDs and patient profiles.

## The Customization Gap
NEMT providers need a car seat management module within their dispatch system that: maintains an inventory of car seats by type and assigned vehicle, maps each seat to the vehicle anchor type (LATCH vs. seat belt, position availability), automatically validates child-to-seat compatibility when a pediatric trip is scheduled, tracks car seat expiration dates (car seats expire after 6-10 years per manufacturer), and logs installation verification (car seats must be properly installed, which should be confirmed before each trip).

## Target Customer
NEMT providers with 10+ vehicles serving pediatric patients who manage car seat assignments informally and experience 5-10 failed pickups per month due to car seat mismatches.

## Impact If Solved
Eliminates car-seat-related failed pickups (saving $50-100 per failed trip in wasted driver time and rescheduling), ensures regulatory compliance with state child restraint laws during transport, and reduces the risk of injury from improperly matched or expired car seats — a significant liability exposure.
