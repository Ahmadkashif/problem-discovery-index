# Electric Utilities

**Layer:** Origin — a parent industry, not a prospect
**Primary Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**Secondary Wave:** [[series/eras/wave-08-mobile-gps|8 — Mobile & GPS]]
**Founding event:** Economic dispatch computed on analog computers by the 1950s; digital control-room systems replacing them from the late 1960s; AMI/smart-meter rollout accelerated by ARRA, 2009–2012
**Children in this vault:** solar installers, energy auditors, utility contractors, agtech platforms

## Profile

**What it is:** Generation, transmission and distribution of electricity, under close regulatory oversight, selling a product that must be produced the instant it is consumed and cannot be economically stored at grid scale.

**Who pays:** Ratepayers, at tariffs set overwhelmingly by state public utility commissions rather than by the seller. The utility is usually a regulated monopoly earning a set return on capital, not a firm competing on price.

**The economics:** Supply must equal demand continuously across a shared network with hard physical limits — line thermal ratings, voltage bands, system frequency. Get the balance wrong for even seconds and equipment trips or the grid fails. The operating problem is not "what to charge" but **"how to keep output matched to load, this instant, without breaking anything."**

## Why This Is an Origin

Electric utilities were solving a large-scale constrained optimisation problem — allocating generator output to minimise cost without violating a physical limit — on dedicated computing machinery **before most industries had computers of any kind.**

It is also the cleanest teaching case in this series for a different lesson: that a **software defect, not a shortage of electricity**, can take down a system serving 50 million people. Airlines taught that infrastructure can sit unexploited for decades. Electric utilities teach that infrastructure can fail silently, and that a failed alarm is worse than a failed line.

## The Contested Decision

> **Given generators already running, how do you allocate their output, second by second, to minimise cost without exceeding a limit anywhere on the network — and, over a longer horizon, which generators do you start or stop, knowing that starting one costs money, takes time, and cannot be cheaply undone?**

The first question is **economic dispatch**. The second is **unit commitment**. Every utility control room answers both, continuously, and has for seventy years.

## The Files

- [[origins/electric-utilities/origin-story|Origin Story]] — from the switchboard to the algorithm
- [[origins/electric-utilities/the-fight|The Fight]] — the alarm that went silent
- [[origins/electric-utilities/the-mechanism|The Mechanism]] — economic dispatch and unit commitment
- [[origins/electric-utilities/legacy|Legacy]] — smart meters, demand response, and what they actually bought

**Sources:** electricenergyonline.com, *A Brief History of Electric Utility Automation Systems*; IEEE Annals of the History of Computing, *Transitions from Analog to Digital Computing in Electric Power Systems* (2015); U.S.–Canada Power System Outage Task Force, *Final Report on the August 14, 2003 Blackout* (2004); EIA, smart meter and AMI data series; DOE, *Smart Grid Investment Grant Program* progress reports.
