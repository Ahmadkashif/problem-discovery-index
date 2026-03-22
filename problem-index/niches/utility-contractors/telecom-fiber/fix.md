# Make-Ready Pole Attachment Delays

**Niche:** [[niches/utility-contractors/telecom-fiber/profile|Telecom & Fiber]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** Make-ready — the process of preparing utility poles for fiber attachment — takes 3-18 months per pole and is the #1 bottleneck in fiber deployment, adding $1,000-5,000 per pole in cost and delaying broadband access for millions of underserved communities.
**Tags:** #automation #workflow-orchestration #data-integration #compliance #revenue-impact

## The Problem
Before a fiber company can attach cable to a utility pole, the pole owner must: receive and review the attachment application, perform engineering analysis (can the pole support additional load?), design any required modifications (raise existing attachments, add a taller pole), permit the work, construct the modifications, and inspect the completed make-ready. FCC rules mandate that this process complete within 90 days for simple cases and 180 days for complex cases. In practice, it takes 6-18 months because pole owners (typically electric utilities) are understaffed for the volume of applications driven by the fiber deployment boom, engineering analysis queues are months long, and pole replacement (required for 15-25% of poles) has its own lengthy procurement and construction timeline. The delay impact: a fiber ISP that can build 50 miles of aerial fiber per month can only build 20 miles because make-ready on the remaining 30 miles isn't complete. Every month of delay is $200K-500K in deferred revenue for a mid-size deployment.

## Why It's Still Broken
The make-ready process involves multiple parties with misaligned incentives. The pole owner has no financial incentive to expedite — make-ready is a cost center funded by the fiber company's attachment fees, which don't cover the true cost of engineering and construction. The fiber company pays for make-ready but has no control over the pole owner's processing speed. FCC enforcement of the 90/180-day timelines is complaint-driven and slow. The manual, paper-based application process at many pole owners adds friction — applications arrive via email, engineering reviews are performed individually, and status updates require phone calls.

## What a Fix Looks Like
A make-ready management platform shared between fiber companies and pole owners that: (1) standardizes the application process — a digital application form with auto-populated pole data from GIS, eliminating the back-and-forth of incomplete applications; (2) automates engineering review queuing — applications are prioritized by complexity (simple attachment vs. pole replacement) and geographic clustering (process adjacent poles together for construction efficiency); (3) provides real-time status tracking visible to both parties — the fiber company sees exactly where each application is in the process without phone calls; (4) escalates timeline violations automatically — when an application exceeds the FCC-mandated timeline, the system generates an escalation notice with documentation; and (5) coordinates make-ready construction scheduling — grouping make-ready work geographically so that pole replacement crews work efficiently rather than scattered across the service territory.

## Who Feels the Pain
Fiber ISPs whose deployment timelines are driven by make-ready rather than construction capability — they have crews ready to build but no poles ready to receive fiber. Underserved communities waiting for broadband access while make-ready processing delays deployment by 6-18 months. Pole owners whose engineering departments are overwhelmed with applications and face FCC enforcement complaints.

## Impact If Fixed
Reduces average make-ready processing time from 6-18 months to 3-6 months through standardized applications, automated queuing, and geographic coordination. Accelerates fiber deployment by 30-50%, bringing broadband access to underserved communities months earlier. Reduces FCC complaints by providing timeline visibility and automated escalation. Saves fiber ISPs $1M-5M per deployment in reduced delay costs.
