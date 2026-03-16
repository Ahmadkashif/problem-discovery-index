# Driver DOT/HOS Compliance on Long-Distance Moves

**Industry:** [[moving-companies|Moving Companies]]
**Type:** Worker Life Changing
**One-liner:** Long-distance moving drivers get proactive scheduling that prevents HOS violations before they happen, eliminating the stress of choosing between illegal driving and missed delivery windows.
**Tags:** #gradient-boosting #regression #tabular-ml #worker-facing #compliance

## The Problem
Drivers on interstate moves operate under FMCSA Hours of Service regulations: 11 hours driving within a 14-hour on-duty window, mandatory 30-minute breaks, and 10-hour off-duty periods. But moving is not trucking — drivers don't just drive. They load at origin (2-6 hours of physical labor), drive to destination (sometimes 2-3 days), unload (another 2-6 hours), and handle customer walkthroughs, paperwork, and payment collection at both ends. Loading and unloading time counts toward the 14-hour on-duty window but not the 11-hour driving limit, creating a planning puzzle that dispatchers and drivers routinely miscalculate. Drivers face a constant tension: the customer expects delivery on the promised date, but HOS math may make that impossible without a violation.

## Why It Matters to the Worker
A driver who violates HOS faces personal fines of $1,000-$16,000 per offense, CSA points that threaten their CDL, and the stress of knowing they're driving fatigued on public roads. But the pressure to deliver on time is enormous — customers have taken time off work, their lease starts tomorrow, the storage unit is only reserved through Friday. Drivers describe this as the most stressful part of long-distance moving: the feeling of being squeezed between regulatory compliance and customer commitments, with dispatch often unreachable or unsympathetic. Many drivers quietly violate HOS rules rather than call dispatch at 10 PM to explain they need an extra rest day.

## What a Solution Looks Like
A planning tool that takes the move's load time estimate, drive distance and route, expected unload time, and delivery window, then back-calculates a compliant schedule before the truck leaves — including rest stops, fuel stops, and buffer time for loading overruns. During the move, a mobile app tracks actual on-duty and driving hours against the plan, alerts the driver when they need to stop (with nearby safe parking options), and automatically notifies dispatch and the customer if the delivery window needs to shift. A regression model trained on historical move data predicts actual load/unload times more accurately than dispatcher guesses, accounting for home size, floor level, access conditions, and crew experience.

## Impact If Solved
Eliminates the 15-20% of long-distance moves where drivers currently face HOS pressure or violations. Reduces driver turnover attributable to compliance stress — a factor that drivers consistently rank in their top 3 reasons for leaving the industry. Protects the company from DOT audit exposure that can result in out-of-service orders.
