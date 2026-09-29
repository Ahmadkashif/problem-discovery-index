# Embedded & Hardware Pipelines

**Parent Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Category:** Low Digitized
**Contested on:** Every serious competitor here is fighting to give firmware and device teams the pipeline discipline that web software has had for fifteen years, on real hardware — and whoever does that takes those organisations, because the current tooling assumes a container and they do not have one.

## Profile
**Market Size:** ~$530M US attributable to embedded, device and hardware-in-the-loop delivery
**Share of Parent Industry:** ~13% of category revenue
**Digital Adoption:** Very Low — much of this work still runs on a bench and a spreadsheet
**Target Buyer:** Firmware, device, automotive and industrial engineering functions
**Automation Potential:** High — the bottleneck is device orchestration rather than analysis

## What Makes This a Distinct Niche
Software that runs on physical devices is built and tested under conditions the category's tooling does not contemplate. The test target is a board rather than a container, of which the organisation has a limited number that must be shared, reset between runs and physically maintained. Test cycles take hours rather than minutes because the device must boot, flash and exercise real peripherals. Builds are cross-compiled for architectures the hosted runners do not offer. Regulated domains — automotive, medical, aerospace, industrial — require traceability from requirement to test to release that general-purpose pipelines do not produce. And the consequence of a bad release is a recall or a field visit rather than a rollback. These organisations frequently run a benchtop process with manual steps and a spreadsheet, which is where web software was in the early 2000s.

## Current Tools & Gaps
Hardware-in-the-loop rigs, usually bespoke; device farms for mobile; cross-compilation toolchains; test automation frameworks from the embedded world; and general-purpose CI orchestrating parts of it awkwardly. The gaps: device pools are managed by a booking spreadsheet or by whoever is in the lab, so the scarcest resource is allocated worst; flashing, resetting and recovering a wedged device is manual, which is why the pipeline stops at the bench; test results from physical runs are not joined to the change that caused them in a queryable way; traceability evidence is assembled by hand for audits; and over-the-air release to a fleet has none of the progressive delivery discipline that web deployment takes for granted.

## Problems
- [[niches/ci-cd-platforms/embedded-and-hardware-pipelines/build|🔨 Build: The Pipeline Stops at the Bench]]
- [[niches/ci-cd-platforms/embedded-and-hardware-pipelines/buy|🛒 Buy: Device Farms and Resource Scheduling Already Exist]]
- [[niches/ci-cd-platforms/embedded-and-hardware-pipelines/fix|🔧 Fix: The Board Somebody Booked on a Spreadsheet]]
