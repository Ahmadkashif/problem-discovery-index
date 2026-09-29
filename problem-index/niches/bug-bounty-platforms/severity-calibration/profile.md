# Severity Calibration

**Parent Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Whether a finding's severity can be referenced against how comparable findings were rated across the whole market, or remains one programme's private judgement.

## Profile

**Market Size:** ~$120M
**Share of Parent Industry:** ~8%
**Digital Adoption:** Very low — a scale cited, not applied
**Target Buyer:** Platform policy teams, researcher community, programme managers
**Automation Potential:** High — the corpus exists and is unqueried

## What Makes This a Distinct Niche

This is the half of adjudication that cannot be solved by any single programme. What a finding is worth is only meaningful relative to how comparable findings have been valued elsewhere, and no programme can calibrate itself against its own ratings.

That dependency makes it structurally different from its sibling. [[niches/bug-bounty-platforms/scope-specification/profile|🎯 Scope Specification]] is a local statement a programme can publish tomorrow and a machine can check immediately. Calibration requires the cross-programme corpus, returns nothing until enough history is assembled, and belongs to the platform rather than to any customer of it. One is answerable in advance and locally; the other only in retrospect and only collectively.

The platform holds everything required. Every severity ever assigned, every finding class, every payout, across every programme, with the context that would let like be compared with like. It is used to run a workflow and to compute reputation scores.

The contest is over whether a reference can be built that respects legitimate context. The same flaw genuinely is more severe on a payment system than on a marketing site, and a naive comparison that ignores that would be wrong in ways programmes would rightly reject. Producing a reference that distinguishes justified variation from arbitrary variation is the whole problem, and whoever does it credibly defines how this market prices its product.

## Current Tools & Gaps

CVSS is cited by most programmes and applied loosely — the band is usually decided and the score reverse-engineered. EPSS and SSVC offer exploitability and decision-oriented alternatives with little adoption here. Payout tables map severity bands to amounts. Platform mediation handles disputes case by case with no published outcome.

The gaps are large and unusually tractable. No cross-programme severity distribution exists for any finding class, despite the data. Nothing shows a triager whether their assessment is an outlier relative to comparable ratings. Nothing lets a researcher see what a class typically earns before they choose where to spend a week. Context factors that justify divergence are not recorded, so justified and arbitrary variation are indistinguishable. And no programme publishes its own rating distribution, so systematic under-rating carries no reputational cost.

## Problems

- [[niches/bug-bounty-platforms/severity-calibration/build|🔨 Build: The Severity Reference]]
- [[niches/bug-bounty-platforms/severity-calibration/buy|🛒 Buy: Rater Calibration From Assessment Science]]
- [[niches/bug-bounty-platforms/severity-calibration/fix|🔧 Fix: CVSS Is Cited, Not Applied]]
