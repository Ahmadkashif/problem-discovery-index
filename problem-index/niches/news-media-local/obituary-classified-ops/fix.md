# Obituary Proofing Error Chain

**Niche:** [[niches/news-media-local/obituary-classified-ops/profile|Obituary & Classified Operations]]
**Industry:** [[industries/news-media-local|Local News Media]]
**Type:** Fix (Pain Point)
**One-liner:** Obituary name misspellings and factual errors trigger family complaints, reprint demands, and legal exposure — yet the proofing process is a manual human chain where the same tired eyes read the same text three times.
**Tags:** #nlp #named-entity-recognition #automation #compliance #worker-facing

## The Problem
Obituary errors are the most sensitive mistakes a community paper can make. A misspelled name, wrong date of birth, omitted survivor, or incorrect church name generates immediate, emotional complaints from grieving families — sometimes leading to reprint demands (free re-runs that cost the paper $200-500), reputation damage in a small community where word-of-mouth matters, and occasional legal threats. The proofing process is entirely manual: the classified clerk reads the funeral home submission, reformats it, and proofs it against the original. Then a second person (often the editor) proofs it again. Despite this double-check, error rates run 3-8% per obituary because the task is repetitive, the text looks similar (every obituary has the same structure), and staff are fatigued.

## Why It's Still Broken
Spell-check tools don't help because the names, churches, lodges, and geographic locations in obituaries are proper nouns that no dictionary contains. The only reliable proof is against the funeral home's source document, and that comparison is done by a human scanning back and forth between two documents. No tool cross-references the submitted text against the funeral home's structured records (which are increasingly digital but in proprietary funeral home software like FIMS or Passare). The volume is too low for any individual paper to justify automation, but the aggregate error cost across the industry is substantial.

## What a Fix Looks Like
An automated proofing layer that: (1) parses the submitted obituary into structured fields (name, dates, survivors, services, organizations), (2) cross-references against the funeral home's structured data via API integration with funeral home software, (3) flags discrepancies between the submission and the source record (name spelling differences, date mismatches, missing survivors), and (4) highlights potential errors for human review rather than requiring line-by-line manual proofing. The human still makes the final call, but the system catches the 80% of errors that are simple transcription mistakes.

## Who Feels the Pain
Classified desk clerks who carry the emotional burden of obituary errors — knowing that a mistake causes real pain to a grieving family — and who suffer proofing fatigue from repetitive comparison tasks.

## Impact If Fixed
Reduces obituary error rates from 3-8% to under 1%, eliminating $5K-15K annually per paper in reprint costs and reputation damage while significantly reducing the stress on classified desk staff who fear making mistakes during the most sensitive part of their job.
