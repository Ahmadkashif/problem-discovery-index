# The Board Somebody Booked on a Spreadsheet

**Niche:** [[niches/ci-cd-platforms/embedded-and-hardware-pipelines/profile|Embedded & Hardware Pipelines]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The scarcest resource in a firmware organisation is the test hardware, and it is allocated by a shared document, a chat message and whoever is physically in the lab.
**Tags:** #descriptive-statistics #optimization-fundamentals #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #automation #worker-facing
**Contested on:** Every serious competitor here is fighting to give firmware and device teams the pipeline discipline that web software has had for fifteen years, on real hardware — and whoever does that takes those organisations, because the current tooling assumes a container and they do not have one.

## The Problem
There are six boards of the relevant revision. Three teams need them. Allocation happens through a spreadsheet that is out of date, a chat channel, and the fact that one engineer sits next to the rack. Two boards are reserved by someone who finished on Tuesday. One is wedged and nobody has noticed. An engineer waits a day and a half for hardware, and the organisation's view of its own utilisation is that the boards are always booked — which is true and tells them nothing about whether they are used.

## Why It's Still Broken
Lab hardware sits between facilities and engineering and is owned by neither, so nobody has been asked to manage it. The allocation mechanism started as an informal convention and works well enough to avoid becoming a project. Utilisation is unmeasured, so the organisation cannot distinguish genuine scarcity from poor allocation and responds to complaints by buying more hardware, which is expensive and does not fix the allocation. And a wedged device is invisible until someone tries to use it.

## What a Fix Looks Like
Manage the pool as a resource. A real reservation system with automatic expiry, so a booking ends when the work does rather than when somebody remembers — which alone typically recovers a significant fraction of apparent scarcity. Health monitoring per device, so a wedged or failed board is detected and removed from the pool rather than discovered by the next person. Actual utilisation measurement — time reserved against time executing — which distinguishes a genuine hardware shortage from a booking problem and is the number that should precede any purchase. Queue transparency, so an engineer can see the wait rather than asking. Remote access where the hardware supports it, since a large share of lab visits are to do something that could be done over a serial connection. Prioritisation rules agreed in advance, because the current mechanism resolves contention by proximity and seniority. And report the wait time, since it is a real and entirely unmeasured tax on firmware engineering productivity.

## Who Feels the Pain
Firmware engineers waiting days for hardware that is reserved and idle; teams whose test coverage is limited by device availability; and organisations buying more hardware to solve an allocation problem.

## Impact If Fixed
Expiring reservations and health monitoring are elementary and typically recover a large share of apparent scarcity without buying anything. Measuring reserved-against-executing is the number that should precede every hardware purchase and almost never exists.
