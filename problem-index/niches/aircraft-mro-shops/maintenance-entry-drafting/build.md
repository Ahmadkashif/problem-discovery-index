# Voice-to-Record at the Aircraft

**Niche:** [[niches/aircraft-mro-shops/maintenance-entry-drafting/profile|Maintenance Entry & Non-Routine Card Drafting]]
**Industry:** [[industries/aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Mechanics describe their work perfectly well out loud; the record is written later, from memory, in a format QA rejects.
**Tags:** #large-language-models #seq2seq #transformers #evaluation-metrics #worker-facing #automation #compliance
**Contested on:** Every serious competitor in this niche is fighting to turn the mechanic's own words into a record that passes QA and the customer's records review first time, and whoever has the fewest rejected entries takes the account.

## The Problem
A mechanic finishes a job, then writes the corrective action on the work order, the logbook or tech log, and sometimes a tracking-system entry or a non-routine card. Each needs the approved-data reference, part numbers and serials, and a precise description. At the end of a shift, entries get vague ("checked OK"), references get skipped, and QA sends them back days later.

## Why Nobody Has Built This
Speech recognition was unreliable in hangars until recently, and generic dictation can't produce a compliant aviation entry with the right manual reference. Maintenance-system vendors built forms, not drafting. The record also has to land in several systems owned by different parties.

## What to Build
A mobile assistant used at the aircraft. The mechanic speaks while working or straight after and photographs part tags. The assistant drafts the 43.9 entry or non-routine card in the shop's and customer's format, fills the manual reference from the task and the fault isolation path, extracts part data from the tag, and posts the same content to each system. It pre-checks the draft against the shop's QA rejection history and flags likely problems before the mechanic signs.

## Target Customer
Directors of maintenance at airline line stations, heavy-check MROs and FBO shops. Zymbly (YC W26) is hiring a forward deployed engineer in San Francisco or London to build its version on site in hangars; Fleetcraft is hiring a founding engineer in London only.

## Impact If Built
Saving ~15 minutes per entry on ~8 entries a shift returns ~2 hours a shift per line mechanic (estimate), ~400 hours a year each. Cutting QA rejections by half removes the callbacks that pull mechanics off current work.
