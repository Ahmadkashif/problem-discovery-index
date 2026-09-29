# The Claim Coded Wrong at Intake

**Niche:** [[niches/neobanks/disputes-and-reg-e/profile|Disputes & Reg E Operations]]
**Industry:** [[industries/neobanks|Neobanks]]
**Type:** Fix (Pain Point)
**One-liner:** The member's description was ambiguous, the analyst picked the wrong claim code under time pressure, and the claim was refused on a technicality that had nothing to do with its merits.
**Tags:** #large-language-models #evaluation-metrics #compliance #workflow-orchestration #quick-win #confidence-intervals #automation #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to turn a member's description of what went wrong into a coded claim before a regulatory clock expires — and whoever does that handles volume growth without either breaching deadlines or writing off valid claims.

## The Problem
A member describes a problem with a transaction. The description could mean an unauthorised charge, a cancelled subscription that kept billing, or goods not received — three claim types with different rules, different evidence and different success rates. The analyst picks one in a few seconds under queue pressure. If they pick wrong, the claim fails for a reason unrelated to whether the member was owed money, and the institution either absorbs the loss or asks the member to start again after a deadline has passed. The classification is the most consequential decision in the process and is made fastest and with the least support.

## Why It's Still Broken
Classification is treated as a data entry step rather than as a decision, so it receives the tooling data entry receives — a dropdown and no guidance. The analyst is measured on cases closed, which prioritises speed at exactly the moment accuracy matters most. The failure appears as a refused claim attributed to the network's rules. And nobody measures how often a claim failed on its coding rather than on its merits.

## What a Fix Looks Like
Support the classification and measure it. Suggest the claim type from the member's description with the reasoning shown, which is the fix, is reliable with current language models, and turns a guess under pressure into a review. Ask the member the one disambiguating question at intake, since the ambiguity is usually resolvable with a single follow-up and the member is the only one who knows. Show the analyst what each classification requires and implies, so the choice is informed rather than habitual. Flag low-confidence classifications for a second look rather than treating all cases as equal. Measure the failure-on-coding rate, which is the diagnostic and which nobody computes despite being derivable from refusal reasons. Allow reclassification before filing, with a clear window, since the error is frequently caught by the analyst gathering evidence and there is currently no route back. Learn from outcomes which descriptions map to which successful classifications, connecting to the corpus work, which is a straightforward supervised problem with abundant labels. Remove the throughput measure's dominance at intake, since measuring the analyst on closure rate at the most consequential step is the incentive error underneath this. Give the member a plain explanation when a claim is refused, because a technical refusal with no explanation is the complaint that reaches the regulator. And report claims refused for reasons unrelated to their merits, since that number is the cost of the current design.

## Who Feels the Pain
Members refused on a technicality; analysts making the most consequential decision fastest; and institutions absorbing losses caused by their own intake process.

## Impact If Fixed
Classification is treated as data entry and given a dropdown, while being the decision that determines the outcome. Suggesting the type from the member's own words with reasoning, and asking one disambiguating question at intake, turns a pressured guess into a review.
