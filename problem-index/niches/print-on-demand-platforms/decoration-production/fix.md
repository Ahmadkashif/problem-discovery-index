# Quality Judged at the Last Station

**Niche:** [[niches/print-on-demand-platforms/decoration-production/profile|Decoration Production]]
**Industry:** [[industries/print-on-demand-platforms|Print on Demand Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Quality is inspected after the item is decorated, which is after the garment and the labour are spent, and everything the inspector rejects was already paid for.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #revenue-impact #descriptive-statistics #automation #quick-win #change-point-detection
**Contested on:** Not terminal — the contest differs by decoration method, and the decomposition is recorded in the profile.

## The Problem
The inspector is the last station. By the time an item reaches them the blank garment has been consumed, the ink or thread has been used, and the machine time has been spent. Everything they reject is a total loss plus the cost of producing the replacement. The defects they find are frequently systematic — a machine drifting, a substrate lot behaving differently, an artwork that was never going to work — which means the same defect was produced dozens of times before anybody saw one, because the inspection is at the end of a batch rather than at the start of it.

## Why It's Still Broken
End-of-line inspection is the conventional arrangement and is simple to staff. Detecting a problem earlier requires either measuring the process or inspecting the first article, neither of which fits a batch of one in the current workflow. The scrap cost is absorbed into a blended reject rate. And the inspector's findings go to a reject bin rather than to the process that caused them.

## What a Fix Looks Like
Detect earlier and feed back faster. Inspect and record automatically at the press with a camera, comparing the decorated result to the intended artwork, which catches defects on the item that produced them rather than at the end of a run and is now inexpensive — this is the fix and the imaging is the same imaging the outcome corpus wants. Run a first-article check when a machine, ink lot or substrate lot changes, since that is when systematic defects begin and it costs one item to find them. Alert on a rising defect rate per machine within a shift rather than reporting it the next day, since the cost of a drifting machine accumulates hourly. Attribute every reject to the machine, lot, settings and artwork, which requires the traceability the buy note describes and is what turns a reject bin into a finding. Report defect Pareto by cause per facility, so the recurring causes are addressed rather than the individual items replaced. Feed rejects into the outcome prediction, since they are the clearest negative labels available. Distinguish artwork-caused from process-caused defects in the reporting, because they have completely different owners and are currently pooled in a reject rate. And measure the cost of scrap at the point where it is generated rather than in a monthly blended figure.

## Who Feels the Pain
Inspectors rejecting items nobody could have used; operators producing a defect repeatedly before anybody notices; and platforms whose reject rate is a blended number over several unrelated causes.

## Impact If Fixed
Everything the inspector rejects was already fully paid for, and the systematic defects were repeated dozens of times before one was seen. Automatic comparison at the press catches the defect on the item that produced it, using the same imaging the outcome corpus already wants.
