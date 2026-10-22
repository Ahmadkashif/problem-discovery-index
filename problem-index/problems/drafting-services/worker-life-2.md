# The Detailer Re-Detailing a Moving Design

**Industry:** [[drafting-services|Drafting Services]]
**Type:** Worker Life Changing
**One-liner:** A detailer who has modelled and drawn half a building receives a reissued design set with revision clouds that miss half the changes, and spends nights and weekends finding what moved, redrawing approved sheets and absorbing the blame for errors that began upstream.
**Tags:** #cnns #semantic-segmentation #graph-neural-networks #k-nearest-neighbors #worker-facing #automation #data-integration

## The Problem
Design keeps changing after detailing starts. The engineer issues a revised structural set, an architect's supplemental instruction moves an opening, an RFI answer changes a connection, a bulletin shifts a floor elevation by two inches. Each change is supposed to be clouded and listed in a revision narrative. In practice clouds are missed, a change on one sheet implies changes on others that are not marked, and a revised set can arrive as two hundred PDFs in which a dozen things matter.

The detailer has to find every change, trace it to the pieces and sheets it affects, revise the model, reissue the shop drawings and often re-check sheets that were already approved, all while the fabricator's schedule holds. If a change is missed, the piece is fabricated to the old design, and the field fix lands on the detailer's record even though the change was never clouded.

## Why It Matters to the Worker
This is the part of the job detailers describe with the most frustration: unpaid hours spent overlaying PDFs and hunting for differences, on work that was already finished, under a deadline someone else moved. It is invisible when done well and personal when missed; the back-charge names the detailer, not the engineer who failed to cloud the change. On fixed-price or per-ton jobs, the hours often go unbilled, and the detailer's evenings and weekends absorb the gap between the quoted revision rounds and the design's actual churn.

## What a Solution Looks Like
A revision comparator that reads the old and new design sets — PDFs or models — and lists every change, clouded or not, with its location, and then maps each change to the model objects, piece marks and shop drawings it affects. The detailer sees "these fourteen pieces on these six sheets are affected; three changes were not clouded", reviews the list and makes the edits. The same record documents which changes arrived when, so that unclouded and late changes are visible as the client's, not the detailer's.

## Impact If Solved
Finding changes in minutes instead of hours on each reissue would give detailers back most of the evenings now spent overlaying sheets, cut the fabrication errors that come from missed changes, and give them evidence when a back-charge traces to an unclouded design change rather than their own work.
