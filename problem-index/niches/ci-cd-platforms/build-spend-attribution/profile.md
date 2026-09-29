# Build Spend Attribution

**Parent Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor here is fighting to say where build spend actually goes in units somebody can act on — and whoever does that takes the cost conversation, because minutes by repository is not a unit anyone can act on.

## Profile
**Market Size:** ~$370M US attributable to build cost management and attribution
**Share of Parent Industry:** ~9% of category revenue
**Digital Adoption:** Low — usage dashboards exist and report the wrong thing
**Target Buyer:** Platform engineering and the finance function
**Automation Potential:** Very High — every minute is already attributed to a job, a step and a change

## What Makes This a Distinct Niche
Build compute has become a substantial line item and is attributed to nobody in particular, so it is optimised by whoever happens to notice the invoice. Usage dashboards exist at every vendor and show minutes by repository, which is not a unit anyone can act on: a repository is not a decision, and nobody can look at a number of minutes and know what to change. The actionable units are elsewhere and are all available — minutes by pipeline step, by test, by trigger type, by branch, by whether the run was a re-run of an identical change, by whether the work was redundant with a cached result. Each of those points at a specific change somebody could make this week. This is a distinct contest because the data is fully attributed already and the reporting stops one level above where action becomes possible.

## Current Tools & Gaps
Usage dashboards with minutes by repository and by workflow, plan limits, and cost allocation tags in cloud-hosted runners. The gaps: the reporting unit is not actionable; re-runs are not separated from first runs, although re-runs are a large and entirely avoidable cost in a flaky estate; queue time is billed in some models and is a vendor capacity problem rather than a customer one; cost per change or per merged pull request is never reported, though it is the unit that would let an organisation reason about it; and nobody attributes a cost increase to the commit that caused it, so increases are discovered as budget variances.

## Problems
- [[niches/ci-cd-platforms/build-spend-attribution/build|🔨 Build: Minutes by Repository Is Not a Decision]]
- [[niches/ci-cd-platforms/build-spend-attribution/buy|🛒 Buy: Cloud Cost Allocation, One Layer Down]]
- [[niches/ci-cd-platforms/build-spend-attribution/fix|🔧 Fix: Re-Runs Billed as First Runs]]
