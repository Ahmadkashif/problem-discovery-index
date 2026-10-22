# Delta Merge/Purge for Late Changes

**Niche:** [[niches/direct-mail-agencies/mail-file-data-processing/profile|Mail File Data Processing]]
**Industry:** [[industries/direct-mail-agencies|Direct Mail Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A one-line change from the client — add a suppression file, cut a list by 20,000 names — forces a full merge/purge rerun overnight, because the tools have no way to apply a change to a finished file.
**Tags:** #k-nearest-neighbors #word-embeddings #evaluation-metrics #data-integration #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to build a deduplicated, suppressed, Move-Update-compliant mail file from a dozen sources by the list due date, with every surviving name traced to its source for net-name billing — and whoever does it fastest with counts the list owners never dispute takes the account.

## The Problem
Merge/purge is run as a batch: all inputs, all rules, one output. Late changes are routine — a strategist trims a list, the client sends a fresh buyer file, a list arrives after the due date — and each forces the processor to rerun the job, re-key the output, regenerate net-name reports and re-presort, often overnight before the lettershop's slot.

## Why Nobody Has Built This
Merge/purge software descends from mainframe-era batch design, priced per job; incremental processing changes the commercial model as well as the architecture. Match decisions are not stored as reusable objects, only as an output file.

## What to Build
A match store that keeps every record's cluster membership, source priority and suppression status as state, so a change is applied as a delta: new records are blocked and matched against existing clusters, removed lists release their names to the next priority, suppressions flip flags, and net-name, multi-buyer and keycode counts update instantly. Borderline matches are queued for review with confidence scores, and the decision is remembered for the next job.

## Target Customer
Data services directors at agencies and mail houses running hundreds of merge/purge jobs a year.

## Impact If Built
Late changes stop costing a night, list due dates can move later without risking the drop, and processors spend their time on match decisions rather than reruns.
