# Severity & Scope Adjudication

**Parent Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Category:** Low Digitized
**Contested on:** Whether the rules a researcher works under — what counts and what it is worth — are knowable before the work, or decided afterwards by the party who pays.

## Profile

**Market Size:** ~$270M
**Share of Parent Industry:** ~18%
**Digital Adoption:** Very low — scope is prose, severity is judgement
**Target Buyer:** Programme managers, platform policy teams, researcher community
**Automation Potential:** High for scope checking, high for severity comparison

## What Makes This a Distinct Niche

A researcher spends a week finding something real. Two questions then determine whether they are paid and how much, and neither was answerable when they started.

Scope is prose. A programme policy names domains, excludes some asset classes, prohibits some techniques, and is written in paragraphs that do not anticipate the situation the researcher is actually in. Is a subdomain that resolves to a third-party service in scope? Is an issue on a staging host that was reachable a real finding? Is chaining two out-of-scope issues into an in-scope impact valid? The answer arrives after the submission, from the programme.

Severity is judgement. The same class of finding is rated high by one programme and medium by another, and the difference frequently reflects the programme's budget and the individual triager's disposition rather than anything about the vulnerability. The researcher has no basis to predict the rating and no reference against which to argue it.

Both decisions are made by the party who pays, after the work is complete, with no appealable standard. That asymmetry is the most consistent source of grievance in the researcher community and it is the largest suppressor of participation in a market where participation is the product.

### Contested sub-niches

- [[niches/bug-bounty-platforms/scope-specification/profile|🎯 Scope Specification]]
- [[niches/bug-bounty-platforms/severity-calibration/profile|🎯 Severity Calibration]]

## Current Tools & Gaps

Programme policy pages with scope tables and prose rules, a severity scale usually derived from CVSS, and a payout table mapping severity bands to amounts. Platforms provide mediation when a researcher disputes a decision, resolved case by case. Reputation systems record outcomes. The `security.txt` standard and the vulnerability disclosure policy conventions cover the announcement rather than the specification.

The gaps are structural. Scope is not machine-readable, so nothing checks a target before the researcher invests a week, and nothing checks a submission before a triager reads it. There is no mechanism for a researcher to ask whether an asset is in scope and get a binding answer in advance. Severity ratings are not comparable across programmes despite the platform holding every rating ever made. Disputes resolve privately with no precedent, so the same argument recurs indefinitely. And no programme publishes its own severity history, so a researcher choosing where to spend a week is choosing blind.

## Problems

- [[niches/bug-bounty-platforms/severity-and-scope/build|🔨 Build: Rules Knowable Before the Work]]
- [[niches/bug-bounty-platforms/severity-and-scope/buy|🛒 Buy: Adjudication Practice From Marketplaces That Solved It]]
- [[niches/bug-bounty-platforms/severity-and-scope/fix|🔧 Fix: The Referee Is Also the Payer]]
