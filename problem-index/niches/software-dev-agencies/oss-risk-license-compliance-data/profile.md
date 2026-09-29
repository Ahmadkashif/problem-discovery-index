# Open Source Risk & License Compliance Data

**Parent Industry:** [[industries/software-dev-agencies|Software Development Agencies]]
**Category:** Insight Layer
**Value-Chain Position:** Data & benchmark vendors

## What They Do
Maintain the curated knowledge base that says, for every version of every open source package in every major ecosystem, which vulnerabilities affect it, which licence obligations it carries, and what depends on it — then scan customer codebases against that base and tell them what they are shipping. An agency delivering custom software delivers a dependency tree it did not write, and this layer is the only party that knows what is in it.

## Insight Function
**Size:** 200-1,000 security researchers, vulnerability analysts, licence and legal analysts, ecosystem engineers, and data scientists
**Output:** Curated vulnerability-to-version mappings, licence obligation and compatibility determinations, dependency and reachability analysis, software bills of materials, malicious package detection, remediation guidance
**Proprietary data:** Years of manual curation over public advisories that are systematically imprecise about affected versions, plus licence interpretation across hundreds of thousands of packages and a record of which findings customers acted on
**Clock:** Continuous vulnerability disclosure, with regulatory bill-of-materials and reporting requirements now attaching hard dates to it
**Buyer:** Chief Research Officer / VP of Security Research

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 4 |
| Q2 Labor mass + repeatable | ×2 | 5 |
| Q3 Proprietary data moat | ×3 | 5 |
| Q4 External clock | ×2 | 4 |
| Q5 Buyer + market | ×2 | 4 |
| **Weighted total** | | **53/60** |

**Kill switches:** none — the curation is the vendor's own work over public advisories and public package registries, and customer code is scanned rather than retained.
**Verdict:** Qualified — indexed
## Problems
- [[niches/software-dev-agencies/oss-risk-license-compliance-data/build|🔨 Build: Severity Scores Nobody Validates Against Exploitation]]
- [[niches/software-dev-agencies/oss-risk-license-compliance-data/buy|🛒 Buy: Advisories That Do Not Say Which Versions They Break]]
- [[niches/software-dev-agencies/oss-risk-license-compliance-data/fix|🔧 Fix: Every Finding Is Dispositioned and No Disposition Comes Back]]
