# The Pipeline Stops at the Bench

**Niche:** [[niches/ci-cd-platforms/embedded-and-hardware-pipelines/profile|Embedded & Hardware Pipelines]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Firmware teams automate the build and then flash the board by hand, because the tooling that would automate the rest assumes a container and they have a device on a desk.
**Tags:** #graph-theory #optimization-fundamentals #descriptive-statistics #change-point-detection #evaluation-metrics #confidence-intervals #automation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to give firmware and device teams the pipeline discipline that web software has had for fifteen years, on real hardware — and whoever does that takes those organisations, because the current tooling assumes a container and they do not have one.

## The Problem
A firmware team's pipeline compiles cleanly and produces an image. Everything after that is a person: take the image, find a free board, flash it, run the test procedure, watch the instrument, record the result in a shared document. The devices are in a lab that three teams share. A test run takes ninety minutes. Regressions are found days after the change that caused them, because nobody runs the full suite per change. The team knows what good practice looks like — they can see it on the web side of the company — and cannot apply it because nothing bridges to the hardware.

## Why Nobody Has Built This
The category's architecture assumes the target is ephemeral, identical and abundant, and a device is none of those: it is scarce, stateful, physically located and capable of getting stuck in a way no container can. Automating around that requires power control, flashing, serial capture, recovery from a wedged state and physical maintenance, which is systems engineering with a hardware component that software vendors have not wanted. The market is also fragmented across very different device types, so the general solution is harder to see. And the teams affected are engineering organisations rather than platform buyers, which is a different sales motion.

## What to Build
Treat devices as a managed, schedulable, recoverable resource pool. Pool the hardware with programmatic power control, flashing and serial capture, and expose it to pipelines as an allocatable resource with a type and a set of capabilities — which is the foundational change that lets everything else follow. Handle the failure modes that make manual operation necessary: detect a wedged device, power-cycle it, re-flash a known-good image, and take it out of the pool with an alert if it does not recover, since the fear of a stuck device is what keeps a human in the loop. Schedule against scarcity, because the devices are the constrained resource and the current allocation mechanism is a booking sheet — this is an ordinary scheduling problem with an unusually high payoff. Select tests by change impact, since a ninety-minute suite cannot run on every commit and running a targeted subset per change plus the full suite nightly is the practical compromise the software side reached long ago. Join physical test results to the change, the device and the conditions, so a failure that occurred on one board at one temperature is identifiable rather than mysterious. And carry traceability through, since the regulated domains need requirement-to-test-to-release evidence and the pipeline is where it naturally exists.

## Target Customer
Firmware, device, automotive, medical device and industrial engineering organisations; the device farm and test rig vendors serving them; and CI vendors seeking a market their architecture currently excludes.

## Impact If Built
These teams are running a process the software world left behind fifteen years ago, not from conservatism but because the tooling assumes conditions they do not have. Device pooling with automated recovery is the enabling change, and scheduling against the scarce resource is where the immediate return is.
