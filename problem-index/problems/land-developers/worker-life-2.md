# The Superintendent Waiting on Dry Utilities

**Industry:** [[land-developers|Land Developers]]
**Type:** Worker Life Changing
**One-liner:** The horizontal development superintendent coordinates grading, utility and paving subs, city inspectors and the electric, gas and fibre companies to deliver lots by a builder's takedown date, and gets back control over a schedule set mostly by other people's crews.
**Tags:** #survival-analysis #time-series-forecasting #large-language-models #cnns #worker-facing #workflow-orchestration #data-integration

## The Problem
Once a phase is approved and the subcontracts are let, a development superintendent runs it in the field: mass grading, storm and sanitary sewer, water lines, paving, curbs, street lights. The sequence is a relay. The grading sub must finish the pads before the utility sub can trench. The city must inspect and test each line before paving. The plat cannot record, and lots cannot close, until the city accepts the public improvements or the developer posts a bond for the remainder. Lots are not deliverable to the builder until the dry utilities are in: the electric co-op or utility sets transformers and pulls service, the gas company runs mains, the fibre provider lays conduit. Each of those has its own design queue, work order and crew schedule, which the developer cannot control and often cannot see.

The superintendent spends the day on the phone and in the truck. He chases a utility designer for the electric layout, reschedules a city inspector who cancelled, settles a dispute between the grading and utility subs over who owns a damaged line, and walks punch lists with the city engineer. Meanwhile the builder's purchasing and sales teams call to ask whether lots will be ready for the takedown date in the contract. Progress lives in a spreadsheet, a whiteboard and photos on his phone.

## Why It Matters to the Worker
The superintendent is accountable for a date he does not control. A transformer backlog or a re-inspection can push lot delivery by weeks or months, and the builder and his own management hear only that the lots are late. The work is long days in the field and evenings answering messages, with no single view of where each lot stands. Experienced superintendents carry a mental model of how long each utility and each city really takes. New ones learn it by being late.

## What a Solution Looks Like
A lot-delivery board fed by the sources that already exist: drone scans and grade checks for earthwork, subcontractor daily reports, city inspection results from the permit portal, utility work-order status where providers share it, and the takedown schedule from the contracts. For each lot or block it would show what is complete, what is waiting on whom, and a predicted delivery date with its uncertainty, learned from how long each city, inspector type and utility provider has actually taken on past phases. It would draft the weekly update to builders and management, flag the critical waits early (a utility design not yet started eight weeks before the takedown), and keep the punch list with photos.

## Impact If Solved
The superintendent gets a schedule he can defend and early warning on the waits that matter, saving ~5–8 hours a week of status calls and reports (estimate). Builders get a delivery date they can plan starts against, which is what protects the developer's takedown.
