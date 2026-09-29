# The Waiting Developer

**Parent Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Category:** Underserved Audience
**Contested on:** Every serious competitor that takes this seriously is fighting to shorten the interval between a developer pushing a change and knowing whether it worked — and whoever does that takes the engineering organisation, because that interval is paid by every developer every day and appears in no budget.

## Profile
**Market Size:** ~$410M US attributable to feedback loop tooling and pipeline experience
**Share of Parent Industry:** ~10% of category revenue
**Digital Adoption:** None — the waiting is measured by nobody
**Target Buyer:** Nominally platform engineering; the beneficiary is every developer
**Automation Potential:** Very High — ordering, early failure and local feedback are all straightforward

## What Makes This a Distinct Niche
The developer's experience of the pipeline is an interval of dead time several times a day, and a set of small indignities within it. They push and wait. They discover at minute forty that the failure was in the first test that ran, because the pipeline ran everything and reported at the end. They cannot tell whether their job is queued or running. They cannot reproduce the failure locally because the environment differs. They re-run and wait again. None of this is anybody's metric: pipeline duration is reported as a platform statistic and the developer's cumulative waiting is reported nowhere. The aggregate across an engineering organisation is enormous, entirely invisible, and mostly addressable with ordering and reporting changes rather than with faster compute.

## Current Tools & Gaps
Pipeline status pages, notifications on completion, and duration metrics. The gaps: pipelines run to completion rather than failing fast, so a failure in step one is reported after step twenty; ordering is as written rather than by probability of failure, so the most likely failure runs last as often as first; status does not distinguish queued from running, so the developer cannot tell whether waiting is theirs or the platform's; local reproduction of a pipeline failure is difficult enough that most developers push again instead, which is the most expensive possible debugging loop; and notification is binary and final rather than progressive.

## Problems
- [[niches/ci-cd-platforms/the-waiting-developer/build|🔨 Build: Minute Forty, and It Was the First Test]]
- [[niches/ci-cd-platforms/the-waiting-developer/buy|🛒 Buy: Test Prioritisation Research, Unapplied]]
- [[niches/ci-cd-platforms/the-waiting-developer/fix|🔧 Fix: Push Again to Debug]]
