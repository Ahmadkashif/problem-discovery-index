# The Line Mechanic Who Writes Everything Twice

**Industry:** [[aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Worker Life Changing
**One-liner:** A line mechanic on a night shift fixes the fault in forty minutes and then spends another twenty writing it up on the work order, the logbook and the tracking system in wording that will survive an FAA inspector. The job they trained for shrinks while the paperwork grows.
**Tags:** #large-language-models #transformers #seq2seq #evaluation-metrics #worker-facing #automation #compliance

## The Problem
Picture an A&P on the night shift at an FBO maintenance shop or an airline line station. A business jet arrives with a pilot write-up: "Left pack trips off in climb." The mechanic troubleshoots with the fault isolation manual, finds a sensor connector with a bent pin, repairs it, runs the pack and clears the write-up. Under 14 CFR 43.9 the entry must describe the work, reference the approved data, carry the date and their signature and certificate number. In practice they write it three times. Once on the shop work order, so the hours can be billed. Once in the aircraft logbook or the operator's tech log. Once more when someone keys it into the customer's tracking system. If a part was changed, there are also the removed and installed serial numbers, the 8130-3 tag and the core return form.

The wording matters more than it should. A quality inspector or the customer's records team rejects entries that don't cite the manual revision, use the wrong ATA chapter, or say "checked OK" instead of describing what was done. Corrections come back days later, after the mechanic has moved on to three other aircraft. On a busy night a third or more of the shift goes to records (estimate), and the entries are written at 4 a.m. from memory.

## Why It Matters to the Worker
Mechanics take pride in the fix and resent the write-up, and the write-up is what carries their certificate on the line. A vague entry can turn into an FAA letter of investigation if the fault recurs or an incident follows. The shortage makes it worse. With ~9,100 certificated mechanics short in North America in 2026 (ATEC/Oliver Wyman), the same people cover more aircraft, and the paperwork doesn't shrink with them.

For newer mechanics the write-up is also where they lose time and confidence. They know what they did but not how a senior inspector would phrase it, or which manual reference to cite. Each rejected entry is a small public correction.

## What a Solution Looks Like
The mechanic talks while working, or straight after: "Left pack, found pin 4 bent on connector P12 of the temperature sensor, straightened per the wiring practices manual, ops check good." The system turns that into a compliant draft entry with the right manual reference, ATA code and part data taken from the tag photo. It posts the same entry to the work order, the tech log and the tracking system in each one's format. It flags anything a reviewer would reject before the mechanic signs: a missing reference, an unclear corrective action, a part with no tag. The mechanic reads it, edits a word, and signs.

Zymbly (YC W26) and Fleetcraft both pitch voice notes turned into compliant records. The test is whether the draft passes QA without a callback.

## Impact If Solved
Saving ~15 minutes per write-up on ~8 write-ups a shift returns ~2 hours a shift to actual maintenance (estimate), ~400 hours a year per full-time line mechanic. Rejected entries and callbacks fall, and new mechanics learn the house style from drafts instead of corrections.
