# First-Pass Submittal Checking Against the Fixture Schedule

**Niche:** [[niches/electrical-distributors/lighting-desk-quoting-submittals/profile|The Lighting Desk: Package Quoting & Submittals]]
**Industry:** [[industries/electrical-distributors|Electrical Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Lighting submittals are rejected for details a machine could check — a CCT, a dimming protocol, a mounting option — and each rejection costs weeks.
**Tags:** #large-language-models #transformers #k-nearest-neighbors #evaluation-metrics #workflow-orchestration #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to turn a lighting fixture schedule into a priced package and a submittal the engineer approves on first review, and whoever gets the most fixture types approved without a resubmittal takes the account.

## The Problem
A lighting specialist assembles a submittal of 10 to 60 fixture types (estimate), each with a catalogue string that encodes dozens of options. The engineer's reviewer checks every type against the schedule and the spec's lighting-controls requirements and rejects mismatches. The specialist fixes them one at a time and resubmits, while fixture lead times run.

## Why Nobody Has Built This
Submittal tools assemble documents; they don't decode catalogue strings or read the spec's controls language. Each manufacturer encodes options differently, and nobody has collected rejection reasons.

## What to Build
A checker that decodes each manufacturer's catalogue string into attributes using spec sheets and configurator rules, compares them with the fixture schedule, the specification and energy-code controls requirements, and flags every mismatch before submission with the source. Engineer comments on past submittals are captured as labelled rejections to rank the checks that matter. A public demo works on manufacturer spec sheets and municipal bid sets.

## Target Customer
Lighting managers at distributors with commercial project books.

## Impact If Built
If first-pass approval rises from ~60–70% of fixture types to ~90% (estimate), each avoided resubmittal saves ~1–3 weeks on fixtures with long lead times (estimate), and lighting specialists spend their time on the package rather than the paperwork.
