# The Emulator That Is Not the Device

**Niche:** [[niches/qa-test-automation-vendors/browser-device-grids/profile|Browser & Device Grids]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Tests pass on the emulated environment and the defect appears on the real device, and no provider publishes where the two diverge.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #k-means-clustering #quick-win #automation #cross-validation
**Contested on:** Every serious competitor here is fighting to offer the combinations that actually matter, on environments that behave like real ones, at a price per parallel session that beats running a lab — and whoever does that takes the grid account, because the alternative is self-hosting.

## The Problem
A suite runs against emulated environments because they are cheaper and faster. It passes. Users on the real device encounter a defect involving touch behaviour, memory pressure, a hardware-backed feature or a rendering difference that the emulator does not reproduce. The team's response is to add real-device runs for everything, which multiplies the cost, or to keep using emulators and be surprised again. What they need is the list of where emulation diverges, which the provider knows better than anyone and publishes nowhere.

## Why It's Still Broken
Emulation fidelity is a commercial sensitivity: a provider selling both emulated and real sessions has an awkward incentive around publishing where the cheaper option is inadequate. The divergences are also numerous, version-specific and tedious to catalogue. And customers experience the failure as a defect in their own application rather than as a testing gap, so the feedback rarely reaches the provider as a fidelity complaint.

## What a Fix Looks Like
Characterise and publish the divergence. Run a standard behavioural comparison between each emulated environment and its real counterpart on a regular basis, covering the areas known to differ — rendering, touch and gesture handling, hardware-backed capabilities, memory and performance behaviour, and platform-specific interfaces — which is a harness the provider can run and nobody else can. Publish the divergence list per environment, so a customer knows which test categories are safe to emulate and which are not, which is the actionable output and turns a binary choice into an informed one. Recommend a split rather than a choice: emulate what emulates faithfully, use real devices for the categories that diverge, which is cheaper than either extreme and is what a knowledgeable customer does anyway. Detect divergence from customer results, since a test that passes emulated and fails real is a fidelity data point the provider can collect across their whole customer base and nobody is collecting. Report fidelity as a measured property rather than an implied one, which is a competitive claim for whoever is genuinely better. And warn when a customer's test is in a category known to diverge on the environment they selected, which is a check at configuration time.

## Who Feels the Pain
Teams whose tests pass and whose users find the defect; customers paying for real devices for everything because they cannot tell what is safe to emulate; and providers whose fidelity advantage, where they have one, is invisible.

## Impact If Fixed
A behavioural comparison harness is something only the provider can run and would turn an unqualified choice into an informed split. Collecting divergence from customer results across the fleet builds the catalogue from real evidence rather than from a test plan.
