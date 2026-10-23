# The Study Report Nobody Can Find by Feeder

**Niche:** [[niches/electric-utilities/interconnection-and-large-load-planning/profile|Interconnection & Large-Load Planning]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Fix (Pain Point)
**One-liner:** A planner who wants to know what the last three studies on a feeder found has to ask a colleague, because the reports are filed by project number.
**Tags:** #large-language-models #transformers #feature-engineering #quick-win #data-integration #workflow-orchestration
**Contested on:** *Not terminal as stated.* The honest partial sentence is: every serious competitor in this niche is fighting to tell an applicant quickly what capacity exists and what connecting will cost. But for small distributed generation, storage and chargers the contest is clearing thousands of applications against a hosting number the study later confirms. For data centres and factories it is answering a few huge, often speculative requests with a megawatt figure, date and cost that hold until energisation. Different volumes, buyers and winners, so it is decomposed into contested sub-niches below.

## The Problem
Study reports, supplemental reviews and facility studies land in a document system keyed to the applicant's project number. When a new request arrives on the same feeder, nobody can easily pull up what was found before: which regulator or bank was binding, which upgrades were promised and never built because the earlier project withdrew. Studies get repeated, and inconsistent answers reach applicants on the same circuit.

## Why It's Still Broken
Document systems were set up for record retention, not engineering reuse. Feeder and substation identifiers appear only inside the PDF text and tables, and they change when circuits are renamed or reconfigured.

## What a Fix Looks Like
Extract feeder, substation, constraint, upgrade and cost fields from every existing study with a language model, verified by a planner on a sample. Index them by circuit with the renaming history, and show a feeder's study history whenever a new request is opened. Pending upgrades from withdrawn projects become visible.

## Who Feels the Pain
Junior planners without the institutional memory; applicants who get conflicting answers; managers explaining inconsistencies to commissions.

## Impact If Fixed
~2–4 weeks of extraction work (estimate) turns the archive into the first thing a planner checks, saves repeat studies on the same circuit, and becomes the training data for any screening model later.
