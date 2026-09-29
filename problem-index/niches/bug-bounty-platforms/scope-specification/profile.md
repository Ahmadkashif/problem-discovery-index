# Scope Specification

**Parent Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Whether what counts as in-bounds is machine-checkable before a researcher starts, or a paragraph of prose interpreted after they finish.

## Profile

**Market Size:** ~$150M
**Share of Parent Industry:** ~10%
**Digital Adoption:** Very low — a policy page
**Target Buyer:** Programme managers, platform engineering
**Automation Potential:** Very high — it is a specification problem

## What Makes This a Distinct Niche

This is the half of adjudication that is decidable in advance and decidable locally. Whether an asset, a technique or a condition is in bounds is a statement a programme can make about itself, before any work happens, without reference to any other programme.

That makes it separable from its sibling in every operational sense. [[niches/bug-bounty-platforms/severity-calibration/profile|🎯 Severity Calibration]] is a valuation question answerable only in retrospect and only by comparison across the whole corpus — a single programme cannot calibrate itself against anything. Scope is a specification a single programme can publish tomorrow, checkable by a machine at submission, and testable immediately: either the checker's verdict matches what the triager would have said, or it does not.

The commercial asymmetry between them is the reason to treat them separately. Scope tooling reduces triage cost, which is the programme's largest operational expense, so it pays for itself on the paying side of the market this quarter. Calibration mainly reduces researcher grievance, which the platform does not pay for. A platform will build the first and defer the second indefinitely.

The contest is over whether a scope can be specified without destroying the thing bounty programmes are for. An enumerated list excludes exactly the findings organisations most need — the asset nobody knew they owned — so the specification has to make the unknown case a first-class, stated outcome rather than an omission.

## Current Tools & Gaps

Programme policy pages with a scope table of in-scope domains and asset classes, an exclusions list, prohibited techniques and a set of known-accepted-risk items. The `security.txt` convention publishes where to report. Some platforms offer structured asset lists that feed a submission form. Attack surface management tooling on the programme's side enumerates assets and is not connected to the scope definition.

The gaps are specific. Scope is not queryable, so a researcher cannot ask about a target before investing a week. Nothing checks a submission against scope before a human reads it, which is why out-of-scope submissions are a large share of triage load. Scope drifts as infrastructure changes and the policy page does not, so a domain decommissioned in March is still listed in September. Chained findings crossing the scope boundary have no defined treatment anywhere. And the unknown-asset case — the most valuable finding type — has no stated policy in most programmes, which means it is resolved case by case in the researcher's disfavour.

## Problems

- [[niches/bug-bounty-platforms/scope-specification/build|🔨 Build: Scope as a Queryable Contract]]
- [[niches/bug-bounty-platforms/scope-specification/buy|🛒 Buy: Attack Surface Management Wired to the Policy]]
- [[niches/bug-bounty-platforms/scope-specification/fix|🔧 Fix: The Policy Page Is Out of Date]]
