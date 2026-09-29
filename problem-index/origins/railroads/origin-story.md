# Origin Story: TOPS, and What It Did Not Solve

**Origin:** [[origins/railroads/profile|Railroads]]
**Wave:** [[series/eras/wave-02-departmental-item-level|2 — Departmental & Item-Level]]

## What Was True Before

A freight car is an asset that belongs to no one journey. It is loaded, moved, unloaded, and then must be found a new load — and a railroad might own tens of thousands of them, moving across thousands of miles of shared track at any given moment.

Before computerisation, knowing where a specific car was, what it carried and what condition it was in meant paper waybills, yard clerks with clipboards, and telegraph traffic between yard offices. Coordinating a car's next move meant someone physically checking a written record and communicating the result down the line — slow, and locally accurate at best.

## What They Built

**Southern Pacific began a feasibility study with IBM in June 1960.** What emerged became **TOPS — Total Operations Processing System** — developed through the 1960s. Southern Pacific bought the commercial version outright for **$21.5 million in 1966**, a striking figure for a single railroad's IT spend in that decade.

**British Railways adopted TOPS from August 1973** (approved 1971), running it on IBM System/370 mainframes, replacing manual, paper-based wagon tracking and telegraph-coordinated yard operations — the same shift Southern Pacific had made, exported to a different railway system.

## What TOPS Actually Was — and the distinction worth making carefully

**TOPS computerised asset tracking: the location, status and maintenance record of every car in the system.** A dispatcher could query a central system and get a current answer to "where is this car, and what state is it in" without a telegram and a wait.

**It did not solve network-wide scheduling optimisation.** TOPS told you what you had and where it was. It did not decide, in any mathematically optimising sense, the best way to route, block and sequence tens of thousands of cars through a congested shared network to minimise transit time or idle time. That is a different, harder problem, and conflating "we can now see our fleet" with "we now run our fleet optimally" repeats a mistake this series has already flagged in [[origins/airlines/legacy|airlines]]: infrastructure that makes a capability possible is not the same thing as the capability being exploited.

Visibility arrived in the 1960s and 70s. **What to do with that visibility — a genuine change to how the network was scheduled — arrived as a management decision, not an algorithm, nearly two decades later.**

**Sources:** IBM corporate history, Southern Pacific TOPS; historical records of British Railways' TOPS adoption (approved 1971, live from August 1973), IBM System/370-based deployment; general rail-industry accounts of pre-computerisation waybill and telegraph-based car tracking.
