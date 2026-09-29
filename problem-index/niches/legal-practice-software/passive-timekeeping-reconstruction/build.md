# A Timesheet Draft the Lawyer Edits Rather Than Writes

**Niche:** [[niches/legal-practice-software/passive-timekeeping-reconstruction/profile|Passive Timekeeping & Billable Reconstruction]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every vendor sells captured time and ships an activity log, because segmenting a day into billable work sessions, attributing them to matters and narrating them is four hard problems and the log is one easy one.
**Tags:** #hidden-markov-models #change-point-detection #large-language-models #gradient-boosting #evaluation-metrics #confidence-intervals #worker-facing #revenue-impact
**Contested on:** Every serious competitor in legal timekeeping is fighting to produce a reconstructed timesheet a lawyer accepts with minimal editing — and whoever gets the accepted-unedited share highest takes the account.

## The Problem
A lawyer's Tuesday contains forty document opens, ninety emails, six phone calls, two hours in a deposition and an unrecorded conversation in a hallway that resolved a matter. Friday afternoon, the timesheet is constructed from memory, and the memory is worse for Tuesday than for Thursday. The firm's product offers a reconstruction: a chronological list of files and messages. Interpreting it into billable entries takes longer than remembering, so it is ignored. Meanwhile the lawyer's guessed entries are systematically short, because reconstructed-from-memory time is biased downward and everyone in the profession knows it.

## Why Nobody Has Built This
Each of the intermediate steps is genuinely hard and none of them is demonstrable in a sales meeting, whereas an activity log is both easy and demoable. Segmentation requires inferring session boundaries from noisy, interleaved activity where a lawyer switches matters six times an hour. Attribution requires mapping a document or a message to a matter when the filename says "draft 3 final v2" and the email is from a client with four open matters. Narration requires language that satisfies a reviewing client, and in defense work a carrier's bill review engine. Duration requires excluding idle and personal time in a way that is both accurate and non-invasive, which is a design problem as much as a modelling one. Vendors have shipped the easy end and marketed it as the whole.

## What to Build
A reconstruction pipeline that outputs entries, not activity. Sessions are segmented with sequence models over the activity stream, where the transitions are the target rather than the events. Attribution combines document location, client and matter identifiers, recipients, calendar context and the lawyer's own correction history, which is the signal that makes it personal rather than generic. Narration is generated per entry in the firm's own voice, learned from that timekeeper's accepted entries, and for defense work it is checked against the carrier's reduction patterns before it is offered. Duration is estimated with explicit idle handling that the lawyer can see and adjust. The whole thing is judged on one number — the share of entries accepted unedited — which is measured continuously and shown to the customer, because every edit is a label and the system should visibly get better at that lawyer's practice over weeks.

## Target Customer
Every practice management vendor in the category, and directly the small firms whose partners believe, correctly, that they are giving away a fifth of their hours.

## Impact If Built
Recovering even a third of the unbilled fraction is, for a small firm, the largest single financial improvement available from software, and it is the thing the category has promised for fifteen years. The measurable form — accepted-unedited share — also gives the market its first honest basis for comparing products, which is why no incumbent is eager to publish it.
