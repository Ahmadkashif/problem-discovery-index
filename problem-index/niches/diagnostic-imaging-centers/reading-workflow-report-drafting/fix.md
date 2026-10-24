# The Prior Exam the Radiologist Spent Four Minutes Finding

**Niche:** [[niches/diagnostic-imaging-centers/reading-workflow-report-drafting/profile|Reading Workflow & Report Drafting Software]]
**Industry:** [[industries/diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Type:** Fix (Pain Point)
**One-liner:** The relevant prior was done at the operator's other site under a slightly different patient record, and the radiologist finds it, or doesn't, by searching by hand.
**Tags:** #word-embeddings #k-nearest-neighbors #large-language-models #data-integration #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to cut the radiologist's time from opening a study to signing the report, and whoever raises studies finalised per radiologist hour with no rise in addenda takes the account.

## The Problem
Comparison with priors is central to a good read. Multi-site operators and centres that changed PACS keep priors under different identifiers and descriptions ("MRI LS SPINE WO" against "Lumbar MRI non-con").

## Why It's Still Broken
Patient matching and exam-description normalisation are integration chores nobody owns, and PACS shows priors only when identifiers match exactly.

## What a Fix Looks Like
Probabilistic patient matching across sites, embedding-based matching of exam descriptions to body region and modality, and automatic hanging of the two most relevant priors with their reports summarised.

## Who Feels the Pain
Radiologists reading from home; referrers receiving reports that say "no prior available" when one exists.

## Impact If Fixed
Saving even two minutes on the fraction of studies with hard-to-find priors adds dozens of reads a week per radiologist (estimate). It also removes a common cause of missed interval change.
