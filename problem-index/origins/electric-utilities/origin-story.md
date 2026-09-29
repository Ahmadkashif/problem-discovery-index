# Origin Story: From the Switchboard to the Algorithm

**Origin:** [[origins/electric-utilities/profile|Electric Utilities]]
**Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]

## What Was True Before

A power system has always had to solve a version of this problem: several generators, each with a different cost curve, must together meet a load that changes minute to minute. Solve it wrong and you either pay more than you need to, or push a line past its rated limit and something trips.

For decades this was arithmetic done by engineers with cost tables and slide rules, refined in real time by operators watching meters and talking by phone. It worked, roughly. It did not scale gracefully as networks grew larger and more interconnected — the number of ways power can flow through a mesh network grows far faster than the number of generators in it.

## What They Built, First in Analog

By the **1950s**, utilities were running **economic dispatch (ED)** on analog computers — machines that modelled the transmission network's losses and cost curves electrically, producing a generation schedule fast enough to be useful in a control room. These systems, and the automatic generation control built alongside them, were already being called **Energy Management Systems (EMS)**.

This is worth sitting with. A decade before SABRE, before ERMA, utilities had built purpose computing machinery to solve a constrained optimisation problem continuously, in production — one of the oldest continuously-running large optimisation problems in any industry, and one that rarely appears in histories of computing because the machines were analog and the industry does not narrate itself.

## The Digital Transition

**Digital computers began replacing the analog EMS from the late 1960s.** Through the 1970s and into the 1980s, digital SCADA (supervisory control and data acquisition) paired with digital EMS became standard control-room technology — telemetry feeding a model of the network's current state, dispatch and commitment routines recomputing schedules against it, alarms flagging anything approaching a limit.

> **Be precise about the shape of this transition.** It was not a single invention with a date, the way SABRE or ERMA had one — it was a decade-plus migration, vendor by vendor and utility by utility. Treat any single "digital EMS invented in year X" claim with suspicion; none was found in sourcing for this file.

## Why It Mattered

The shift let dispatch and commitment run against **live telemetry** rather than a schedule prepared in advance, and let the same system carry the **alarm and situational-awareness layer** — the software telling an operator when something is wrong before it becomes catastrophic.

That second capability is the one this origin's fight turns on. A dispatch algorithm that is mathematically correct is worthless to an operator who no longer knows the network's actual state. Electric utilities built the computation early. They did not build the alarm layer robustly enough — and forty years after digital EMS became standard, that gap surfaced in the largest blackout in North American history.

**Sources:** electricenergyonline.com, *A Brief History of Electric Utility Automation Systems*; IEEE Annals of the History of Computing, *Transitions from Analog to Digital Computing in Electric Power Systems* (2015); U.S.–Canada Power System Outage Task Force, *Final Report on the August 14, 2003 Blackout* (2004).
