# The Draft Report That Disagrees With Its Own Tables

**Niche:** [[niches/biotech-research-firms/glp-safety-assessment/profile|IND-Enabling GLP Safety Assessment]]
**Industry:** [[industries/biotech-research-firms|Biotech Research Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A GLP report's narrative, summary tables, individual data and SEND datasets are produced by different people and drift apart, and sponsors and QA find the mismatches one comment at a time.
**Tags:** #large-language-models #transformers #evaluation-metrics #compliance #quick-win #automation
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every preclinical CRO is fighting to deliver an audit-clean IND-enabling package on the date the sponsor's IND depends on, but small-molecule and biologics programmes are won on different things — compressing the calendar across disciplines, versus securing or replacing non-human primates — so it is decomposed into contested sub-niches below.

## The Problem
A body-weight change quoted as 12% in the text is 11.6% in the table; a finding upgraded at pathology peer review is updated in the pathology report but not the study director's summary; the SEND dataset carries an earlier version. Each mismatch costs a QA finding, a sponsor comment and a revision cycle, and the final report slips.

## Why It's Still Broken
Report sections are written by different contributing scientists from exported tables, and consistency is checked by reading. The validated data system and the word processor are separate worlds, and nothing links a sentence to the number it quotes.

## What a Fix Looks Like
A consistency checker that parses the draft, extracts every quoted value and finding, matches each to the validated tables and the SEND domains, and lists mismatches with locations before QA review. It flags, and a person corrects.

## Who Feels the Pain
Study directors assembling reports; QA auditors re-checking numbers; sponsors whose IND waits on the final version.

## Impact If Fixed
Fewer review cycles per report and fewer late findings, which bears directly on whether the package lands on the sponsor's date.
