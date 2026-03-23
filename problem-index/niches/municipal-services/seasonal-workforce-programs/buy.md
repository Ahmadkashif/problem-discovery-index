# Scheduling Tool with Certification and Clearance Tracking

**Niche:** [[niches/municipal-services/seasonal-workforce-programs/profile|Seasonal Workforce Programs]]
**Industry:** [[industries/municipal-services|Municipal Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Deputy and WhenToWork handle shift scheduling but don't enforce that every pool shift has 2 lifeguard-certified staff or that no unchecked employee works with minors.
**Tags:** #automation #compliance #workflow-orchestration #worker-facing

## The Problem
A parks department schedules 80 summer staff across 12 sites (pools, camps, recreation centers) with varying certification requirements. Pool shifts require certified lifeguards. Camp counselor shifts require background-cleared adults. Sports program shifts require first-aid-certified staff. The scheduler — usually a recreation coordinator — builds weekly schedules in Excel, manually cross-referencing a separate certification spreadsheet to ensure compliance. Mistakes happen: an uncertified employee is scheduled at the pool, or a staff member whose background check is still pending is assigned to a children's camp. These errors create liability exposure that isn't discovered until an incident occurs.

## What Already Exists
Deputy, WhenToWork, Sling, and Homebase offer employee scheduling with shift swapping, availability tracking, and basic role assignment. These tools let you create a "lifeguard" role but don't enforce that the person assigned to a lifeguard shift actually holds a current lifeguard certification. They track hours but not certifications. They don't model the government-specific constraint that certain positions require cleared background checks before any shift assignment.

## The Customization Gap
A municipal-ready scheduling tool needs: (1) a certification registry per employee (certification type, expiration date, verification document) that blocks scheduling an employee for a role requiring a certification they don't have or that has expired, (2) a background-check status field that prevents assignment to youth-contact positions until clearance is confirmed, (3) minimum-staffing rules per site per shift (not just total headcount but qualified headcount — "2 of the 4 staff at Pool A must be lifeguard-certified"), (4) union/civil-service overtime rules that differ from private-sector FLSA calculations, and (5) integration with NEOGOV or the municipality's applicant tracking system to pull certification data automatically.

## Target Customer
Recreation coordinators and HR generalists responsible for scheduling 50–300 seasonal staff across municipal sites with certification-gated positions.

## Impact If Solved
Eliminates compliance gaps that expose cities to $100K–$500K in liability per incident. Reduces scheduling time from 8 hours per week to 2 hours. Prevents the 5–10 scheduling errors per month where uncertified staff are assigned to restricted positions.
