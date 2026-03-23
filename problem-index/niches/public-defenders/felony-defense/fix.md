# Discovery Overload Causing Systematic Case Under-Preparation

**Niche:** [[niches/public-defenders/felony-defense/profile|Felony Defense]]
**Industry:** [[industries/public-defenders|Public Defenders]]
**Type:** Fix (Pain Point)
**One-liner:** Defenders receive discovery dumps of thousands of pages with no indexing, no search, and no time to read them — cases go to plea because the attorney never found the exculpatory evidence buried on page 2,347.
**Tags:** #bert #text-classification #nlp #worker-facing #compliance

## The Problem
Prosecutors deliver discovery in bulk — boxes of paper, ZIP files of scanned PDFs, raw body camera footage — with no index, no organization, and often no Bates numbering. The public defender is expected to review everything, identify Brady material, and build a defense. With 100+ active felony cases, this is physically impossible. The result is that most felony cases resolve via plea bargain not because the evidence is overwhelming, but because the defender never had time to find the weaknesses.

## Why It's Still Broken
There's no financial incentive for prosecutors to organize discovery for the defense. Courts have been slow to mandate electronic discovery standards in criminal cases (unlike civil litigation). Public defender offices lack the budget for document management systems, and the problem is invisible — no one tracks "cases lost because discovery wasn't reviewed."

## What a Fix Looks Like
A standardized discovery intake workflow: every document is OCR'd, indexed, and searchable on arrival. An automated classifier flags police reports, lab results, witness statements, and video evidence into categories. A priority queue surfaces documents most likely to contain exculpatory or impeachment material. The defender opens a case and sees a dashboard, not a pile.

## Who Feels the Pain
Line public defenders who carry felony caseloads of 80-150 cases — they're the ones staying until midnight reading discovery, or worse, going to court unprepared because they couldn't.

## Impact If Fixed
Estimated 3-5 hours saved per felony case on discovery review. Across a 100-case caseload, that's 300-500 hours per year per defender — equivalent to hiring additional staff without increasing headcount.
