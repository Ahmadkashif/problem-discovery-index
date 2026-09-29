# Conversion Optimization Firms

## Profile
**Category:** Digital Professional Services
**Market Size:** ~$2.5B US in conversion rate optimisation services and experimentation programmes, alongside the testing platform market that supports them
**Tech Maturity:** Excellent tooling attached to weak statistical practice. Testing platforms make it trivial to launch an experiment, monitor it continuously and declare a winner, and the ease of all three is precisely the problem — the industry's standard workflow contains several practices that inflate false positive rates severely, and its case studies are full of reported wins that do not replicate.
**Workforce:** CRO strategists and experimentation leads, front-end developers building variants, analysts and data scientists, UX researchers, programme managers

## Key Pain Themes
The discipline sells uplift and mostly reports it wrong. Experiments are run on traffic that cannot detect the effect sizes being claimed, monitored continuously with a decision made the moment significance appears, stopped early when the result is favourable, and segmented after the fact until something is significant. Each of these inflates the false positive rate on its own and they are frequently combined. The reported wins are therefore a mixture of real effects and noise, weighted toward noise because noise is what gets stopped early.

Nobody finds out. A declared win is implemented and the uplift is assumed; the business metric moves for a hundred reasons and nobody returns to check whether the sum of the year's reported uplifts bears any relationship to the actual change. Practitioners who have checked — and a few have published on this — find the gap embarrassing.

The third theme is that the programme's value is bounded by test capacity and that capacity is spent badly. Most tests are small variations on low-traffic pages that could never have produced a detectable effect, chosen because they were easy to build rather than because they addressed a plausible mechanism.

## Current Tech Landscape
Testing platforms — Optimizely, VWO, AB Tasty, Convert, and increasingly server-side and feature-flag tooling from LaunchDarkly, Statsig and Eppo — handle assignment, delivery and reporting. Statsig and Eppo in particular have brought sequential testing and more careful statistics into the commercial tier, which is a genuine improvement. Behavioural tooling from Hotjar, FullStory, Contentsquare and Clarity supplies hypothesis input. Bayesian reporting is offered by several platforms and is frequently used to justify exactly the peeking behaviour it does not license. Personalisation engines sit adjacent and share the measurement problems.

## Problems
- [[problems/conversion-optimization-firms/high-impact|🔴 High Impact: The Reported Wins Do Not Add Up and Nobody Checks]]
- [[problems/conversion-optimization-firms/low-impact-1|🟡 Low Impact: Hypothesis Generation From Behavioural Data]]
- [[problems/conversion-optimization-firms/low-impact-2|🟡 Low Impact: Variant Implementation and Test Quality]]
- [[problems/conversion-optimization-firms/worker-life-1|🟢 Worker Life: The Strategist Reporting a Win They Privately Doubt]]
- [[problems/conversion-optimization-firms/worker-life-2|🟢 Worker Life: The Developer Building Variants Against a Site That Moves]]
- [[problems/conversion-optimization-firms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/conversion-optimization-firms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
This is a discipline with an unusually clean opportunity to fix itself, because unlike most of this cluster its outcome data is not on the other side of a wall — it runs the experiments, it holds the results, and the validation it needs is a holdout it could implement tomorrow. Reserving a permanent randomised holdback from every implemented winner, and comparing the accumulated actual effect against the sum of reported uplifts, would tell any firm within a year how much of its claimed value is real. Almost nobody does it, because the answer is likely to be uncomfortable and the client is currently satisfied with the reported number. The firm that runs it and survives the finding has the only credible position in a market where every competitor's case studies say the same thing.
