# The Template Nobody Validated

**Niche:** [[niches/spend-management-platforms/policy-design/profile|Policy Design]]
**Industry:** [[industries/spend-management-platforms|Spend Management Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every new customer is configured from the same default policy template, which was written by an implementation team three years ago.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #automation #workflow-orchestration #confidence-intervals #compliance #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to say which spend policies actually produce better outcomes rather than merely more exceptions — and whoever can answer that across thousands of companies sells policy instead of a rule builder.

## The Problem
Implementation configures the new customer from a default template: standard limits, standard categories, standard receipt threshold, standard approval chain. The template came from what early customers asked for and has been copied ever since. Every customer therefore starts from the same unvalidated configuration, adjusts it only when something becomes painful, and lives with it for years. The platform has years of data on how those configurations performed and has never looked.

## Why It's Still Broken
The template was a speed tool for implementation, so it was optimised for getting live quickly rather than for being right — and once it worked for that purpose nobody revisited its content. Implementation teams are measured on time to launch. Nobody owns the template. And its effects are diffuse, delayed and invisible without the comparison nobody runs.

## What a Fix Looks Like
Look at what the template produced. Report exception rates and approval rates for customers on the default template, which is the fix and is one query that will show whether it generates workable policy or noise. Compare against customers who diverged from it, since their configurations were chosen deliberately and their outcomes are informative. Vary the template by company size and sector, as one default for a twenty-person startup and a two-thousand-person company is obviously wrong and is what currently ships. Review the template on a schedule with a named owner, because an artefact nobody owns decays silently. Set starting thresholds from observed distributions rather than round numbers, since round numbers are guesses and the data has better ones. Flag new customers whose early exception rate is abnormally high, which catches a bad configuration in week two rather than year two. Tell existing customers how their configuration compares to peers, as that is useful, easy and a differentiator. Track how many customers ever change their configuration, which will show how sticky the initial choice is. Make adjustment easy and reversible, so change is not a project. And feed the template updates back to implementation, since that is where the compounding happens.

## Who Feels the Pain
New customers inheriting an unvalidated configuration; employees hitting thresholds set for a different company; controllers managing exceptions caused by a default; and a platform whose most influential product decision is unowned.

## Impact If Fixed
The template was optimised for getting live quickly and nobody revisited its content once it served that purpose. Reporting what the default actually produces across the customer base is one query and makes the most influential configuration in the product visible.
