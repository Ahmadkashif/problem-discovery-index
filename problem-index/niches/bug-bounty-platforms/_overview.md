# Niche Analysis — Bug Bounty Platforms

**Parent Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]

## Niche Selection

A bounty platform holds the complete record of both sides of its market — every submission, its quality, its outcome, its severity, its payment, and every researcher's history across every programme — and uses it to run a workflow. The eight niches below start from what that record could answer and does not: whether the spend bought security, and whether the rules the researcher worked under were knowable before they started.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Triage Operations | 🔵 High Market Share | ~$375M | Moderate — workflow, manual judgement | Platform triage leadership, programme managers |
| 2 | Programme Effectiveness Measurement | 🔵 High Market Share | ~$330M | Very low — activity reported as outcome | Programme owners, security leadership |
| 3 | Severity & Scope Adjudication | 🟠 Low Digitized | ~$270M | Very low — prose and judgement | Programme managers, researcher community |
| 4 | Disclosure Coordination | 🟠 Low Digitized | ~$135M | Low — email and goodwill | Disclosure and legal staff, vendors |
| 5 | The Researcher | 🟣 Underserved Audience | ~$180M | Low — a reputation score | Independent researchers |
| 6 | The Triage Analyst | 🟣 Underserved Audience | ~$105M | Low — a queue and a clock | Platform triage operations |
| 7 | Submission Deduplication & Filtering | ⚡ Highly Automatable | ~$75M | Moderate — partial automation | Platform engineering |
| 8 | Payments & Programme Operations | ⚡ Highly Automatable | ~$30M | Moderate — solved mechanics | Platform operations |

## Why These Niches

Triage is the operational reality and the largest cost: most submissions to a public programme are duplicates, out of scope, scanner output or non-issues, and every one must be read by someone qualified to tell the difference. Effectiveness measurement is the thing the category sells and does not report. Severity and scope adjudication is where both sides' grievances concentrate, because the rules are decided after the work. Disclosure coordination is the part that touches parties outside the marketplace entirely. The two underserved populations are the researcher, paid on a lottery, and the analyst reading invalid submissions all day where the cost of missing the real one is a breach. The last two are mechanical: filtering the queue, and moving money across jurisdictions.

## Niches

- [[niches/bug-bounty-platforms/triage-operations/profile|🔵 Triage Operations]]
- [[niches/bug-bounty-platforms/programme-effectiveness/profile|🔵 Programme Effectiveness Measurement]]
- [[niches/bug-bounty-platforms/severity-and-scope/profile|🟠 Severity & Scope Adjudication]]
  - [[niches/bug-bounty-platforms/scope-specification/profile|🎯 Scope Specification]]
  - [[niches/bug-bounty-platforms/severity-calibration/profile|🎯 Severity Calibration]]
- [[niches/bug-bounty-platforms/disclosure-coordination/profile|🟠 Disclosure Coordination]]
- [[niches/bug-bounty-platforms/the-researcher/profile|🟣 The Researcher]]
- [[niches/bug-bounty-platforms/the-triage-analyst/profile|🟣 The Triage Analyst]]
- [[niches/bug-bounty-platforms/submission-deduplication/profile|⚡ Submission Deduplication & Filtering]]
- [[niches/bug-bounty-platforms/payments-and-operations/profile|⚡ Payments & Programme Operations]]

## Filter Notes

Seven of the eight are terminal — each names one contest every serious competitor is fighting over, and decomposing further would produce features rather than markets.

**Severity and scope adjudication** is not. It covers the two decisions a researcher works under and cannot see in advance, and they are different problems with different owners and different data. Scope specification is decidable *before* the work: what is in bounds is a statement about assets, domains, techniques and conditions, it could be machine-checkable at submission time, it is resolvable inside a single programme with no reference to any other, and a platform could ship it for one customer next quarter. Severity calibration is decidable only *after*: what a finding is worth depends on comparison with how similar findings were rated across many programmes, which requires the cross-programme corpus, cannot be done by any single programme alone, and is meaningless until enough history exists. One is a specification problem answerable in advance and locally; the other is a valuation problem answerable in retrospect and only collectively. A platform can ship scope tooling and never build severity calibration, and most would, because scope tooling reduces triage cost this quarter while calibration mainly reduces disputes the platform is not paying for.

Two adjacent candidates were rejected as belonging elsewhere: **contracted, time-boxed expert testing** is the subject of [[industries/penetration-testing-firms|Penetration Testing Firms]], and **vulnerability and exploit intelligence as a product** belongs to [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]].
