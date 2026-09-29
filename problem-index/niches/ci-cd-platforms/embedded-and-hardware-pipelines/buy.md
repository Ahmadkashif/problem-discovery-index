# Device Farms and Resource Scheduling Already Exist

**Niche:** [[niches/ci-cd-platforms/embedded-and-hardware-pipelines/profile|Embedded & Hardware Pipelines]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Mobile device farms solved remote device allocation, flashing and result capture at scale, and embedded teams three floors away book a board on a spreadsheet.
**Tags:** #optimization-fundamentals #convex-optimization #dynamic-programming #descriptive-statistics #evaluation-metrics #confidence-intervals #automation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to give firmware and device teams the pipeline discipline that web software has had for fifteen years, on real hardware — and whoever does that takes those organisations, because the current tooling assumes a container and they do not have one.

## The Problem
Mobile testing built an entire infrastructure for exactly this shape of problem: racks of physical devices, remotely allocated, automatically flashed and reset, with results and video captured and attached to the build. It works at commercial scale. Embedded and industrial teams have the same requirement with different hardware and almost none of the infrastructure, and solve it with a lab, a booking sheet and a person.

## What Already Exists
Mobile device farm platforms with allocation, flashing and capture; hardware-in-the-loop frameworks from the automotive world; laboratory instrument control standards; resource scheduling and reservation systems; power distribution units with programmatic control; and the open test automation frameworks used in embedded testing. The pieces exist across several disciplines.

## The Customization Gap
The adaptation is to heterogeneous, stateful, custom hardware. It requires: (1) a device abstraction that accommodates custom boards rather than a catalogue of known phones, which means capability description and driver plugins rather than a fixed device list — this is the difference between a mobile farm and something an embedded team can use; (2) robust recovery, since a development board can enter states a phone cannot and the recovery procedure is device-specific, and without reliable recovery the pool degrades to a rack of wedged hardware; (3) scheduling that accounts for setup cost, because reconfiguring a rig between test types can take longer than the test, which makes this a sequence-dependent scheduling problem rather than simple allocation; (4) instrumentation capture beyond the console — power draw, signals, sensor readings — since embedded test results frequently depend on measurements the software cannot self-report; and (5) physical maintenance as part of the model, because boards fail, cables come loose, and a pool with no health tracking becomes untrustworthy quickly.

## Target Customer
Device and firmware engineering organisations, hardware-in-the-loop rig vendors, mobile device farm providers with an adjacent market, and CI vendors.

## Impact If Solved
The infrastructure pattern is proven at commercial scale for phones and absent for everything else, which is a coverage gap rather than an unsolved problem. Custom device abstraction and reliable recovery are the two adaptations that determine whether an embedded team can actually use it.
