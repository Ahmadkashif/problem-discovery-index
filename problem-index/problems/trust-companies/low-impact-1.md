# The Annual Account Review Done Two Thousand Times

**Industry:** [[trust-companies|Trust Companies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every discretionary account's assets must be reviewed at least once a calendar year under 12 CFR 9.6, and generic portfolio review tools check drift against a model portfolio rather than against the trust instrument, the retention clause and the beneficiaries' competing interests.
**Tags:** #gradient-boosting #large-language-models #feature-engineering #evaluation-metrics #compliance #automation #workflow-orchestration

## The Problem
A national bank acting as trustee with investment discretion must review all the assets of each such account at least once during every calendar year to decide whether they remain appropriate, individually and together (12 CFR 9.6(c)); state-chartered trust companies follow the same practice under their own rules and examiners. A trust company with 2,000 discretionary accounts therefore runs 2,000 reviews a year, and the reviews bunch up before year-end and before examinations. Each review asks whether the investments still fit the instrument and the beneficiaries: an income beneficiary who needs yield against remainder beneficiaries who need growth, a concentrated low-basis position the grantor told the trustee to retain, a farm the family will not sell, cash drag in a trust nobody has called in three years. Most accounts are clean. A few carry real exposure, and they get the same checklist as the rest.

## What Already Exists
Portfolio management and rebalancing tools (Envestnet's Tamarac, Orion, and the portfolio modules inside trust accounting platforms from FIS, SEI and SS&C Innovest) measure drift against a model, flag concentration above a threshold and produce a review report. Trust accounting systems keep a tickler that tells the officer a review is due. Investment policy statement templates record the objective chosen when the account opened.

## The Customisation Gap
The generic tools do not know what the trust says. A fiduciary review has to encode the instrument's investment provisions (retention clauses for family stock or real estate, prohibited investments, directed-trust carve-outs where an outside adviser holds investment authority), the duty of impartiality between income and remainder beneficiaries, power-to-adjust or unitrust elections under the state's principal and income act, the tax cost of diversifying low-basis positions, and special assets valued on a different cycle. It also has to produce the evidence an examiner looks for — what was checked, what was found, what was decided — rather than a drift chart. The customisation is an exception-ranked review: score every account on the probability that a review would find something requiring action, review the top of the list in depth, clear the clean accounts with a documented short-form review, and record the reason for every retained exception.

## Impact If Solved
Reducing a clean-account review from ~1–2 hours to ~20 minutes (estimate) frees roughly 1,500–3,000 officer hours a year at a trust company with 2,000 discretionary accounts, and concentrating attention on the ~10–20% of accounts with real issues (estimate) is what reduces examiner findings and surcharge exposure.
