# Re-Exported and Unrecognisable

**Niche:** [[niches/digital-goods-marketplaces/asset-fingerprinting-at-scale/profile|Asset Fingerprinting at Web Scale]]
**Industry:** [[industries/digital-goods-marketplaces|Digital Goods Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** The platform checks uploads against a hash of the original, so a copy that was opened and saved once passes straight through onto its own storefront.
**Tags:** #contrastive-learning #evaluation-metrics #confidence-intervals #automation #quick-win #dimensionality-reduction #compliance #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to recognise a modified copy of a template, font or plugin anywhere on the web — and whoever can do that for asset types nobody has fingerprinted makes enforcement possible at all.

## The Problem
Someone buys an asset, opens it, changes the accent colour, saves it under a new name, and lists it on the same marketplace it came from. The upload check compares file hashes and possibly a preview image. The hash differs, the preview differs slightly, and the listing goes live. The original creator discovers it when a buyer mentions it. The marketplace has both files in its own storage — the original and the derivative — and its own duplicate detection did not connect them, which is the most embarrassing possible version of the detection gap because no crawling or web-scale infrastructure was needed at all.

## Why It's Still Broken
Upload duplicate checking was built to catch accidental re-uploads, not deliberate derivation, and hashing is adequate for that narrow purpose. Preview-image comparison looks like a reasonable upgrade and fails on exactly the modifications people make. Structural comparison of design formats is unbuilt. And the case only surfaces when a creator notices, so the frequency is unknown and assumed to be low.

## What a Fix Looks Like
Check derivation at upload, inside the platform, where both files are already held. Compare structure rather than bytes or previews — layer names, component trees, style definitions, glyph metrics, parameter values — which catches the recoloured re-export immediately and is the fix; the platform is the one party that has both files in full. Flag near-duplicates for review rather than blocking, since legitimate derivative work exists and blocking would be wrong. Check against the uploader's own purchase history first, because the copy was usually bought by the person listing it and this narrow check is cheap, fast and catches a large share of cases. Cross-check against licence terms, since a buyer with a redistribution grant is entitled and one without is not, and only the platform can tell them apart. Scan the existing catalogue retrospectively, as this has been happening for years and the accumulated cases are recoverable. Notify the original creator when a derivative is listed, which is what turns detection into enforcement. Score uploaders by derivation history, since the behaviour repeats and is a strong account-level signal. Publish that structural checking happens, because deterrence is most of the value and the current absence is widely known among the people doing it. Keep the false positive path cheap and fast, so a legitimate creator flagged in error is inconvenienced for an hour rather than a fortnight. And report the derivative detection rate, which is the number that tells creators whether the marketplace they sell on is defending them at all.

## Who Feels the Pain
Creators whose work is resold beside their own listing; buyers purchasing a degraded copy believing it original; and marketplaces hosting the infringement they are best placed to prevent.

## Impact If Fixed
The platform holds both files in full and its own duplicate check did not connect them, so no crawling was ever needed. Structural comparison plus a check against the uploader's own purchase history catches the recoloured re-export at the moment it is listed.
