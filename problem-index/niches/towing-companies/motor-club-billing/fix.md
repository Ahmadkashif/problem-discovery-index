# Chronic Under-Billing from Documentation Gaps

**Niche:** [[niches/towing-companies/motor-club-billing/profile|Motor Club Billing & Claims Reconciliation]]
**Industry:** [[industries/towing-companies|Towing Companies]]
**Type:** Fix (Pain Point)
**One-liner:** Drivers forget to photograph the odometer, dispatchers don't record mileage, and the billing team can't submit $50-$200 in accessorial charges because the supporting documentation doesn't exist.
**Tags:** #automation #compliance #worker-facing #revenue-impact

## The Problem
Motor club billing requires specific documentation at the point of service: odometer reading (for mileage-based charges), scene photos (for special equipment charges), VIN verification (for vehicle identification), and service-specific evidence (tire change photos, fuel delivery receipts). Tow truck drivers are focused on the service — changing a tire on a highway shoulder at night, hooking up a car in a flooded parking lot — not on documentation. They forget the odometer photo 30% of the time, skip the scene photo 40% of the time, and rarely record the VIN unless the motor club dispatch provided it. Without this documentation, the billing team can't bill for legitimate charges: a $75 winch-out surcharge denied for lack of scene photo, a $50 mileage adjustment denied because the odometer reading wasn't captured.

## Why It's Still Broken
The documentation burden falls on the person least equipped to handle it: the driver, at the least convenient moment (on a roadside, at night, in weather). Training drivers to "always take photos" works for a week and then compliance drops. Paper checklists get soaked, lost, or ignored. The driver sees documentation as administrative overhead that doesn't affect their pay — and they're right, because most towing companies don't tie driver compensation to billing completeness.

## What a Fix Looks Like
A mandatory mobile workflow that the driver must complete to close a job in the dispatch system: step-by-step prompts for each required documentation item (photo of vehicle on hook, odometer reading photo, VIN photo/scan, scene condition photo if applicable), with the dispatch system refusing to mark the job complete until all required items are captured. Which items are required varies by motor club program — the system applies the right checklist automatically based on the call source. Completed documentation auto-attaches to the billing claim, eliminating the billing team's manual assembly.

## Who Feels the Pain
The billing manager who reviews 300 completed jobs per month and finds that 90 are missing documentation needed to bill accessorial charges — representing $4,500-$18,000/month in unbillable revenue that was legitimately earned but can't be proven.

## Impact If Fixed
Captures $3,000-$15,000/month in previously unbillable accessorial charges by ensuring drivers document at the point of service. Reduces claim denial rate from 8-15% to 2-4% by attaching required documentation automatically.
