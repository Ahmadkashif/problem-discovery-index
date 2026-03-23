# Real-Time Urban Portfolio Operations Dashboard

**Niche:** [[niches/short-term-rentals/urban-multi-property-managers/profile|Urban Multi-Property Managers]]
**Industry:** [[industries/short-term-rentals|Short-Term Rentals]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No platform provides a real-time operational view of an urban STR portfolio — which units are turning over right now, which cleaners are en route, which guests haven't checked in yet, which maintenance issues are unresolved — in a single map-based dashboard optimized for managing 50+ dense urban units.
**Tags:** #automation #workflow-orchestration #data-integration #ai-platform

## The Problem
An urban STR manager with 80 apartments across a city has 15-25 turnovers on a busy Friday. At 2 PM, they need to know: which of the 15 turnovers are completed, which cleaners are still working, which guests arriving at 3 PM don't have access codes yet, and which units flagged maintenance issues during inspection. This information currently lives across 4-5 systems: Guesty (bookings), Breezeway (cleaning tasks), a WhatsApp group (cleaner status updates), email (maintenance reports), and a smart lock platform (access codes). The manager synthesizes this information mentally, losing 2-3 hours daily to context-switching between platforms.

## Why Nobody Has Built This
Each operational component (PMS, cleaning, locks, pricing) has its own platform with its own business model. Integration across these platforms requires API connections that are technically possible but commercially unaligned — Guesty doesn't want to be a cleaning dispatch tool, and Breezeway doesn't want to manage pricing. The unified dashboard is a middleware play that threatens none of the existing platforms but has thin margins unless it adds operational intelligence (not just aggregation).

## What to Build
A map-based operations dashboard that aggregates real-time data from the PMS (Guesty/Hostaway), cleaning platform (Breezeway/Properly), smart locks (August/Yale), and maintenance tracking into a single view. Each unit shows current status (occupied/turning/ready/issue), next guest arrival time, cleaner assignment status, and any open maintenance flags. Alerts for: turnovers running behind schedule, guests arriving to unready units, and maintenance issues that could generate negative reviews.

## Target Customer
Urban STR management companies operating 50+ units in a single metro — approximately 2,000-3,000 companies nationally. Average contract value: $200-$500/month.

## Impact If Built
Operations manager daily coordination time drops from 3-4 hours to 45 minutes. Guest-arrives-to-unready-unit incidents drop from 3-5% to under 1%. Maintenance issues are resolved before guest arrival instead of after complaint — preventing 1-star reviews that cost $2,000-$5,000 in lost booking revenue per incident.
