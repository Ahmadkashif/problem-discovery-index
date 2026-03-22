# Plaintiff Qualification Screening

**Niche:** [[niches/personal-injury-law/mass-tort-mdl/profile|Mass Tort / MDL]]
**Industry:** [[industries/personal-injury-law|Personal Injury Law]]
**Type:** Fix (Pain Point)
**One-liner:** Mass tort firms stop wasting months of resources on unqualified plaintiffs — automated screening against litigation-specific criteria at intake identifies the 30-50% of sign-ups who don't meet case requirements before a single record is requested.
**Tags:** #gradient-boosting #logistic-regression #decision-trees #feature-engineering #evaluation-metrics #cross-validation #automation #revenue-impact

## The Problem
Mass tort plaintiff acquisition runs on volume: TV ads, social media campaigns, and lead generators produce thousands of sign-ups. But qualification rates are brutal — only 40-70% of sign-ups actually meet the case criteria. A Roundup plaintiff must have used the product for a sustained period AND been diagnosed with Non-Hodgkin Lymphoma. A 3M earplug plaintiff must have served in the military between specific dates AND have documented hearing loss. The problem is that firms don't discover a plaintiff is unqualified until weeks or months into the relationship, after intake staff have called them multiple times, requested medical records, and opened a case file. The unqualified plaintiff consumed resources identical to a qualified one during that period.

## Why It's Still Broken
Qualification criteria are litigation-specific and change as MDL courts issue new orders. Current intake workflows rely on self-reported information (the plaintiff fills out a web form saying they used Roundup for 10 years, but their actual usage was sporadic lawn application that may not meet the exposure threshold). Self-reported data is unreliable — plaintiffs overstate exposure because they want to qualify. Proper screening requires cross-referencing intake data against objective criteria (diagnosis codes, service records, product usage documentation), but this verification happens downstream, not at intake. No existing tool provides real-time qualification scoring at the point of lead intake.

## What a Fix Looks Like
A qualification scoring engine configured per litigation. Input: structured intake form data (self-reported exposure, diagnosis, dates) plus any available documentary evidence (pharmacy records, military DD-214, diagnostic reports). Processing: rules engine checks hard criteria (correct diagnosis, correct exposure period) and a gradient-boosted classifier estimates qualification probability based on historical qualification patterns for leads with similar intake profiles. Output: a tri-color score — green (high confidence qualified, proceed with records collection), yellow (needs additional verification on specific criteria before investing resources), red (does not meet threshold, route to rejection review). The model learns from the firm's own historical qualification outcomes, improving as more leads are processed.

## Who Feels the Pain
Intake coordinators and case managers who spend hours calling, emailing, and chasing records for leads that ultimately don't qualify. Firm partners who see their cost-per-qualified-plaintiff balloon because 30-50% of intake resources are spent on dead-end leads.

## Impact If Fixed
Identifies 30-50% of unqualified leads at intake instead of 2-3 months downstream. For a firm processing 5,000 leads per litigation, that saves 1,500-2,500 unnecessary record requests, intake calls, and case file setups — estimated savings of $150K-$400K per litigation in wasted intake labor. Reduces average cost-per-qualified-plaintiff by 25-40%.
