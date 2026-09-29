# Instrumentation Coverage

**Parent Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to make tracking work on the training code an organisation actually runs rather than on the frameworks the vendor supports — and whoever does that takes the account, because the unsupported code is where the important models live.

## Profile
**Market Size:** ~$240M US in licence displacement and integration cost
**Share of Parent Industry:** ~8% of category revenue
**Digital Adoption:** Low — one line for the supported set, a project for everything else
**Target Buyer:** Platform engineering, with the researchers as the blocked users
**Automation Potential:** High — capture can be made passive

## What Makes This a Distinct Niche
A tracking vendor's integration is genuinely excellent for the frameworks they have built adapters for, and for everything else it is a bespoke engineering project: a bank's twenty-year-old scoring pipeline, a research group's custom training loop, a modelling stack in a language the vendor does not support, an acquired company's system, a job running inside a scheduler the vendor has not integrated with. Large organisations run mostly that. The result is a platform with a coverage figure nobody publishes, showing beautiful dashboards for the newest projects and nothing for the models carrying the most risk. The contest is passive capture — getting useful tracking from code the vendor has never seen and nobody will rewrite.

## Current Tools & Gaps
Framework auto-logging for the major supported libraries, generic logging clients requiring explicit instrumentation, and manual integration services. The gaps: nothing captures a run that was never instrumented; legacy and bespoke pipelines are excluded by cost rather than by decision; no organisation knows its own tracking coverage; and the models least likely to be covered are frequently the oldest, most business-critical and least understood.

## Problems
- [[niches/mlops-platforms/instrumentation-coverage/build|🔨 Build: One Line for the Supported, a Project for the Rest]]
- [[niches/mlops-platforms/instrumentation-coverage/buy|🛒 Buy: Auto-Instrumentation From the Observability World]]
- [[niches/mlops-platforms/instrumentation-coverage/fix|🔧 Fix: The Untracked Model Carrying the Most Risk]]
