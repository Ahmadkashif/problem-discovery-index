# Double-Booked Fields from Parallel Request Systems

**Niche:** [[niches/youth-sports-orgs/field-facility-schedulers/profile|Field & Facility Schedulers]]
**Industry:** [[industries/youth-sports-orgs|Youth Sports Organizations]]
**Type:** Fix (Pain Point)
**One-liner:** Field requests arrive through email, phone, paper forms, and the parks department website — with no single system showing real-time availability — causing 5-10% of field slots to be double-booked, discovered only when two teams arrive at the same field.
**Tags:** #data-integration #automation #compliance

## The Problem
A parks department receives field requests from multiple channels: league presidents email the coordinator, coaches call the front desk, rental requests come through the parks website, and tournament hosts submit paper permit applications. Each request is recorded separately — sometimes in a shared Google Sheet, sometimes in the coordinator's email, sometimes on a sticky note at the front desk. There is no single real-time view of field availability. The coordinator manually checks for conflicts, but with requests arriving through 4 channels, conflicts are inevitable. The most embarrassing failure: two teams arrive at the same field at the same time, and the coordinator must decide on the spot who stays and who leaves.

## Why It's Still Broken
Municipal parks departments have limited IT budgets and often use the same recreation management software (RecPro, ActiveNet) for program registration that they purchased years ago — software that handles facility booking at a macro level (reserve "the soccer complex" for "Saturday mornings") but not at the granular level needed (Field 3 from 9-10 AM, Field 4 from 9:30-11 AM). Adding a purpose-built field scheduling system requires budget approval, IT support, and workflow change for multiple staff members — organizational friction that exceeds the parks department's capacity for technology adoption.

## What a Fix Looks Like
A unified field booking system that: (1) serves as the single source of truth for all field availability, (2) accepts requests from any channel (web form, email parsing, phone log) into a single queue, (3) shows real-time availability by field, date, and time slot, (4) auto-detects conflicts before confirming any new booking, (5) sends confirmation to the requester with field assignment details, and (6) provides a public-facing availability calendar so leagues can self-serve requests against verified open slots. The system must be simple enough that any parks department staff member can use it without training.

## Who Feels the Pain
Parks coordinators who field angry calls from coaches who arrived at double-booked fields, and league administrators who can't trust the field assignment they received.

## Impact If Fixed
Eliminates the 5-10% of field slots lost to double-booking (worth $5K-20K in annual rental revenue at facilities that charge), prevents the 3-5 confrontations per season when teams arrive at the same field, and reduces the coordinator's field-management workload by 30-40%.
