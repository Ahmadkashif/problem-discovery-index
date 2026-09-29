# Waste Recorded as a Number Nobody Wrote Down

**Niche:** [[niches/restaurant-tech-platforms/kitchen-staff-tools/profile|Kitchen Staff & Back-of-House Tools]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Food waste is the largest unmeasured cost in a restaurant kitchen, every waste log is a clipboard that gets filled in retrospectively or not at all, and the resulting number is used in costing as though it were real.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #cnns #automation #worker-facing #quick-win
**Contested on:** Every serious competitor building for the back of house is fighting to get the prep list, the par levels and the station setup to the line in a form usable with wet hands during service — and whoever the cooks actually use takes the kitchen.

## The Problem
A kitchen throws away prepped items that aged out, trim from butchery, over-produced batches, and plates that came back. A waste log exists on a clipboard by the bin. It is filled in sometimes, by whoever remembers, in categories nobody agreed on, and is transcribed weekly by a manager who knows it is incomplete. Food cost variance is then explained as waste using a number everyone knows is wrong, which means the largest controllable cost in the kitchen is managed against fiction.

## Why It's Still Broken
Recording waste is work performed at the exact moment somebody is discarding something, by a person whose hands are full, with no benefit to them and a mild implication of blame. Every solution offered has been a better form on a tablet, which changes nothing about the incentive or the moment. Kitchens also genuinely disagree about what counts — is trim waste or yield — so even diligent logs are not comparable across shifts or units. And because the number is known to be bad, nobody invests in improving it, which keeps it bad.

## What a Fix Looks Like
Make the recording physical and near-zero effort, and separate the categories that behave differently. A scale at the bin with a small screen — weigh, tap a category, done — takes three seconds and captures weight rather than an estimate, which is the difference between a log and a measurement. Camera-based bin capture is a further step and is available now at reasonable cost, identifying category automatically from the image and asking only for confirmation. Separate pre-service waste from trim and from plate returns, because they have different causes and different fixes and averaging them tells nobody anything. Report by item and by shift back to the kitchen rather than only to the office, since the cooks are the people who can act on it and are currently the only people never shown it. Start by measuring for two weeks deliberately, even manually, to establish the true scale — most kitchens will find it is well above what their costing assumes.

## Who Feels the Pain
Cooks asked to fill in a clipboard nobody reads; chefs defending a food cost variance they cannot explain; and owners costing plates against a waste assumption that is a guess.

## Impact If Fixed
Weighing waste at the bin converts the largest unmeasured line in the kitchen into a measured one, and the first honest measurement almost always resets the operator's understanding of where the money goes. Separating pre-service waste from trim is what makes the number actionable, because it points at prep quantities — which is exactly what the build note computes.
