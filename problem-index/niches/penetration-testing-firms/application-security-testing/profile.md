# Application Security Testing

**Parent Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Category:** High Market Share
**Contested on:** Whether assessment can keep pace with a codebase that ships daily, or whether a point-in-time test is obsolete before the report is written.

## Profile

**Market Size:** ~$1.32B
**Share of Parent Industry:** ~22%
**Digital Adoption:** Moderate — good tooling for the shallow half, manual for the deep half
**Target Buyer:** Application security leadership, engineering leadership
**Automation Potential:** High for known classes, low for business logic

## What Makes This a Distinct Niche

Application testing is the largest single service line in offensive security and the one where the engagement model has aged worst. A two-week assessment against an application that deploys forty times a week produces a report describing a version of the software that no longer exists by the time it is read.

The tension is specific. The classes of weakness that automated tooling finds well — injection, misconfiguration, known-vulnerable dependencies, many categories of missing control — are increasingly handled in the pipeline, continuously, at no marginal cost. What remains for a human is the part tooling cannot touch: authorisation logic, business logic abuse, workflow state manipulation, chained weaknesses that are individually harmless, and the reasoning about what this specific application is for and how someone would misuse it.

Every serious competitor is fighting over that boundary. A firm whose testers are rediscovering what the client's own pipeline already reports is selling a commodity that is getting cheaper every year. A firm that reliably finds the logic flaws nobody's scanner will ever catch is selling something that cannot be automated — and the industry has no way to demonstrate which kind of firm it is buying.

## Current Tools & Gaps

Static and dynamic analysis, software composition analysis, interactive testing agents and now assistant-driven code review are all deployed in mature engineering organisations, running continuously in the pipeline. Manual testing sits on top as a periodic engagement. Some firms offer continuous or retainer-based testing; some clients run bug bounty programmes alongside. Fuzzing has become practical for a wider range of targets.

The gaps concentrate where the human work is. Business logic and authorisation flaws — consistently the highest-impact findings and the ones tooling cannot detect — have no systematic methodology, so coverage depends entirely on the individual tester's imagination and the time they had. Nothing tells a tester which parts of the application changed since the last assessment, so repeat engagements re-walk stable code. Findings are not fed back into the pipeline as regression tests, so the same class returns. And no firm can show a client what its manual testing found that the client's own tooling had already reported — which is the single most useful thing a buyer could know about the engagement they just paid for.

## Problems

- [[niches/penetration-testing-firms/application-security-testing/build|🔨 Build: Testing What the Pipeline Cannot See]]
- [[niches/penetration-testing-firms/application-security-testing/buy|🛒 Buy: Continuous Testing From the Pipeline Vendors]]
- [[niches/penetration-testing-firms/application-security-testing/fix|🔧 Fix: The Report Describes Code That No Longer Exists]]
