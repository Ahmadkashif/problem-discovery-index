# The Edge Case Nobody Designed

**Niche:** [[niches/product-design-studios/deliverable-production/profile|Deliverable Production & Handoff]]
**Industry:** [[industries/product-design-studios|Product Design Studios]]
**Type:** Fix (Pain Point)
**One-liner:** The developer needs the empty state, it was never designed, and they are building something at four in the afternoon.
**Tags:** #quick-win #automation #workflow-orchestration #evaluation-metrics #compliance #descriptive-statistics #worker-facing #data-integration
**Contested on:** Every serious competitor in this niche is fighting to get a design from a file into something a development team can build without a designer spending days producing specifications — and whoever automates that handoff takes the account.

## The Problem
Development reaches a state the design does not cover — no results, a long name, an error, a slow connection — and the designer is unavailable or gone. The developer makes a reasonable decision under deadline. Dozens of these accumulate across a build, and the shipped product diverges from the design in ways nobody intended and everyone later attributes to poor implementation.

## Why It's Still Broken
Nothing lists what is missing — a design has no definition of completeness, so an omission is indistinguishable from a deliberate choice until a developer hits it. Designers draw the happy path. Review looks at what is there. And the gap appears after the studio has left.

## What a Fix Looks Like
Use a checklist, because the omissions are the same every time. Apply a standard state checklist to every screen and component before handoff, which is the fix and catches most of it in an hour. Cover the recurring set — empty, loading, error, long content, truncation, permission, offline — since those account for the large majority. Test the design against extreme content lengths, which is the single commonest break. Mark states deliberately left to the developer, so an omission is a decision. Provide a default pattern for the states not individually designed rather than nothing. Review the checklist with the development team before handoff, as they know what they will need. Keep a channel open for the questions that will arise, which they will. Record each question and its answer so the next handoff includes it. Add the recurring gaps to the studio's own checklist, which is how it improves. And treat handoff completeness as a deliverable quality rather than as a courtesy.

## Who Feels the Pain
Developers inventing design under deadline; designers whose work ships altered; clients whose product diverges from what they approved; and the studio, blamed for an implementation it did not see.

## Impact If Fixed
A design has no definition of completeness, so an omission is indistinguishable from a deliberate choice until a developer hits it. A standard state checklist catches most of it in an hour.
