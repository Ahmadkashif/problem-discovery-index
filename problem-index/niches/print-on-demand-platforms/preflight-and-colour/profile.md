# Preflight & Colour

**Parent Industry:** [[industries/print-on-demand-platforms|Print on Demand Platforms]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to make the file check catch the things customers actually complain about — and whoever does that stops the reprints, because the current check passes almost everything that later fails.

## Profile
**Market Size:** ~$540M US
**Share of Parent Industry:** ~9% of category revenue
**Digital Adoption:** Low — checks the wrong things
**Target Buyer:** Prepress and platform engineering
**Automation Potential:** Very High — every check is mechanical

## What Makes This a Distinct Niche
Preflight tooling is a mature discipline in commercial printing and the version shipped here checks resolution and dimensions, which are not what causes customers to complain. The defects that produce complaints are colours outside the achievable gamut, transparency and blending flattened unexpectedly, embedded colour profiles ignored, thin strokes below the process minimum, placement running across a seam, and artwork whose light areas disappear against a coloured substrate. Every one of those is mechanically checkable given a product model and a process profile, none requires judgement, and almost none is in the check that runs. The gap between what preflight verifies and what actually goes wrong is the clearest example in this industry of an installed capability pointed at the wrong target.

## Current Tools & Gaps
Resolution and dimension validation, file format handling, and a size warning. The gaps: no gamut check; transparency and colour space handling is inconsistent and unreported; minimum feature size is not checked against the process; placement is not validated against product geometry; substrate colour interaction is ignored; and the merchant receives a pass or a technical error rather than an explanation.

## Problems
- [[niches/print-on-demand-platforms/preflight-and-colour/build|🔨 Build: Checking Resolution, Not What Goes Wrong]]
- [[niches/print-on-demand-platforms/preflight-and-colour/buy|🛒 Buy: Commercial Prepress Verification]]
- [[niches/print-on-demand-platforms/preflight-and-colour/fix|🔧 Fix: Transparency Flattened by Surprise]]
