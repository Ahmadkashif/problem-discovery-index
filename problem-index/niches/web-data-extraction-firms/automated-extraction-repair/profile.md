# Automated Extraction Repair

**Parent Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to repair a broken extractor without a person, verified, at fleet scale — and whoever does that takes the account, because repair is now mechanically feasible and is still being done by hand.

## Profile
**Market Size:** ~$280M US
**Share of Parent Industry:** ~14% of category revenue
**Digital Adoption:** Low — repair is manual at fleet scale
**Target Buyer:** The firms operating scraper fleets
**Automation Potential:** Very High — the repair loop is fully closable

## What Makes This a Distinct Niche
Repairing a broken extractor means looking at the page, finding where the field moved, and updating the rule. Until recently that required a person. A model that can read a rendered page and identify the requested field can now do it, verify the result against the previous value distribution, and deploy the fix — which closes a loop that has consumed this industry's engineering capacity since it existed. The contest is doing this reliably enough to trust unattended: repairing correctly, verifying before deploying, recognising the cases that genuinely need a person, and not silently replacing a broken extraction with a plausibly wrong one, which is the failure mode this whole capability must avoid.

## Current Tools & Gaps
Manual selector updates, model-based extraction as a fallback, and alerting on failures. The gaps: no closed repair loop, so a model that could fix it is used to extract rather than to repair; no verification gate, so an automatic fix would be trusted blindly; no learning from human repairs, which are a labelled dataset of exactly this task; and no confidence-based routing between automatic and human repair.

## Problems
- [[niches/web-data-extraction-firms/automated-extraction-repair/build|🔨 Build: The Repair a Model Can Now Do]]
- [[niches/web-data-extraction-firms/automated-extraction-repair/buy|🛒 Buy: Self-Healing Automation and Program Repair]]
- [[niches/web-data-extraction-firms/automated-extraction-repair/fix|🔧 Fix: A Fix Deployed Without Verification]]
