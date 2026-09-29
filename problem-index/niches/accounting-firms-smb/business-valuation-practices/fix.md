# Discount Selection Rationale Dies With the Engagement
**Niche:** [[niches/accounting-firms-smb/business-valuation-practices/profile|Business Valuation Practices]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The report states the discount applied; the reasoning that produced it lives in the appraiser's workpapers and memory, and when the opinion is challenged three years later that reasoning has to be reconstructed.
**Tags:** #large-language-models #transformers #workflow-orchestration #data-integration #worker-facing #tacit-knowledge-ml #compliance

## The Problem
Marketability and minority discounts are the most challenged inputs in a valuation, and they are the least documented. The report typically states the discount and cites supporting studies. What it does not capture is the specific reasoning — which subject facts pushed the number up or down, which alternatives were considered and rejected, how much weight each study actually carried. Under challenge the firm must reconstruct that reasoning, sometimes with a different appraiser, and the reconstruction is not always consistent with what the original appraiser actually did.

## Why It's Still Broken
The report is written for the reader, not for the firm's own future retrieval. Workpapers hold fragments but are organised by engagement, are not searchable across the practice, and are not linked to the specific input they support. Capturing the reasoning properly means writing it down at a moment when the appraiser is under deadline and the report is already saying what the conclusion is — so it does not get written.

## What a Fix Looks Like
Capture at the point of decision, at a cost of seconds. When the appraiser sets a discount, the system records the value alongside the subject facts relied on, the studies weighted, and alternatives considered — drafted from the workpaper context so the appraiser corrects rather than composes. Those records accumulate into a practice-wide base that answers, on challenge, exactly what was done and why, and that shows the firm where its own discount selections have drifted apart on similar facts.

## Who Feels the Pain
Appraisers defending opinions they wrote years earlier; practice leaders carrying liability on positions whose basis is undocumented; and litigation counsel who need the reasoning fast and get a PDF.

## Impact If Fixed
Turns challenge defence from reconstruction into retrieval. Surfaces inconsistency across appraisers while it is still correctable, rather than when opposing counsel finds it.
