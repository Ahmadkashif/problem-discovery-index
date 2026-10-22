# The Room Number That Changed After the Signs Were Ordered

**Niche:** [[niches/graphic-design-studios/wayfinding-and-environmental-graphics/profile|Wayfinding & Environmental Graphics]]
**Industry:** [[industries/graphic-design-studios|Graphic Design Studios]]
**Type:** Fix (Pain Point)
**One-liner:** The architect renumbers a wing in the last drawing revision, the message schedule doesn't follow, and a hundred tactile signs are fabricated with the wrong numbers.
**Tags:** #object-detection #data-integration #workflow-orchestration #quick-win #compliance
**Contested on:** Every serious competitor in this niche is fighting to deliver a sign message schedule and fabrication drawings that pass ADA review and go out to fabricator bid without RFIs, and whoever produces a schedule fabricators can price without questions takes the project.

## The Problem
Room names and numbers change throughout design and construction — a department moves, an addition renumbers a corridor, the owner renames a suite after a donor. Each change must reach the message schedule. When one doesn't, tactile signs with braille are fabricated wrong and must be remade, because they can't be relabelled.

## Why It's Still Broken
The room data lives in the architect's model; the message schedule is a separate spreadsheet copied from it once and then edited by hand. Neither party owns keeping them in step, and drawing revisions arrive as full PDF sets with changes clouded somewhere among hundreds of sheets.

## What a Fix Looks Like
Read each new drawing revision, extract room tags, and diff them against the message schedule automatically, listing every sign whose room name or number no longer matches, with the sheet and cloud reference. Hold fabrication release on any unresolved difference.

## Who Feels the Pain
Wayfinding designers reconciling schedules; fabricators remaking tactile signs; owners delaying occupancy for missing room signs.

## Impact If Fixed
Remakes of tactile signs, often costly per sign because they cannot be corrected after fabrication, disappear, and late renumbering becomes a routine update rather than a crisis.
