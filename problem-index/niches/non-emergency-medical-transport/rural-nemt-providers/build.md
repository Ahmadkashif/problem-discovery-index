# Rural NEMT Dispatch and Billing Platform

**Niche:** [[niches/non-emergency-medical-transport/rural-nemt-providers/profile|Rural NEMT Providers]]
**Industry:** [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No affordable dispatch-to-billing platform exists for rural NEMT providers operating 2-8 vehicles across sprawling service areas with spotty connectivity.
**Tags:** #workflow-orchestration #automation #data-integration #compliance

## The Problem
A rural NEMT provider with 4 vehicles covers a 2,500 square mile service area, completing 15-30 trips per day. The owner-operator manages scheduling via paper calendar, dispatches via cell phone calls to drivers, records trip data on paper logs, and manually keys completed trips into the state Medicaid portal for billing — often 2-3 weeks after the trip occurred. This delay between service delivery and billing submission means cash flow is perpetually 30-60 days behind expenses. Errors in manual data entry (wrong odometer readings, incorrect pickup times, missing authorization numbers) trigger claim denials that take hours to rework. The entire operation depends on the owner's personal knowledge and relationships — there is no system to transfer.

## Why Nobody Has Built This
Rural NEMT providers are small accounts — $10K-$30K/year in potential software spend — that NEMT software vendors cannot profitably serve with enterprise-grade platforms. The rural use case also requires offline capability (trips occur in areas without cellular coverage), simplified workflows (a 2-person shop cannot adopt a 50-screen dispatch platform), and Medicaid billing integration that handles the lower-volume, higher-complexity claims typical of rural transport (long-distance specialist trips with different reimbursement codes).

## What to Build
A mobile-first dispatch and billing platform designed for 2-8 vehicle fleets: the driver's smartphone captures GPS-verified pickup/dropoff timestamps and odometer readings (with offline sync when connectivity is unavailable), the dispatcher/owner sees a simple daily schedule view with drag-and-drop trip assignment, and completed trips auto-populate Medicaid billing fields ready for one-click submission. Pricing at $50-$150/month makes it accessible to the smallest rural providers. The platform includes basic compliance documentation (driver files, vehicle inspections, trip logs) in a single system.

## Target Customer
Rural NEMT providers with 2-8 vehicles who currently operate entirely on paper and phone, billing Medicaid manually through state portals.

## Impact If Built
Reduces billing cycle from 30-60 days to same-week submission, decreasing claim denials by 40-50% through automated data capture. Saves the owner-operator 10-15 hours/week of administrative work, allowing them to add trip capacity without adding staff.
