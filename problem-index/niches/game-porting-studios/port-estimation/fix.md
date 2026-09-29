# Nobody Wrote Down What the Last Twenty Ports Cost

**Niche:** [[niches/game-porting-studios/port-estimation/profile|Port Estimation]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Fix (Pain Point)
**One-liner:** The studio has completed dozens of projects and cannot tell you which ones were over, by how much, or why.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #confidence-intervals #revenue-impact #data-integration #workflow-orchestration #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to quote a fixed price and a fixed date for work whose difficulty depends entirely on properties of a codebase they cannot see until after the contract is signed — and whoever estimates it accurately takes the account.

## The Problem
Ask a porting studio how accurate its estimates have been and there is no answer. Hours are tracked for invoicing, the original estimate is in a document somewhere, and nobody has ever put the two side by side across projects. The overruns are known anecdotally — everyone remembers the bad one — and the pattern across twenty projects, which is the actually informative thing, has never been looked at.

## Why It's Still Broken
Nobody joined the two numbers — an estimate and an actual that live in different systems and are never compared produce no learning at all, however many projects go by. Each project closes and attention moves on. Comparing implies judging the estimator. And there is no forcing event, since the margin absorbs it quietly.

## What a Fix Looks Like
Tabulate the history you already have. Put every past project's estimate against its actual in one table, which is the fix and usually takes a week of digging and changes the conversation permanently. Record the overrun by phase rather than in total, since the pattern is almost always concentrated in one or two phases. Note the specific cause of each overrun in a consistent vocabulary, which is what turns anecdote into a checklist. Compare across engines, platforms and client types, as the differences are usually large and unexamined. Identify the estimator-level pattern honestly and privately, which is uncomfortable and is where most of the improvement lives. Calculate the average contingency actually required, which is a number the business can price with immediately. Apply the resulting checklist at the next bid rather than waiting for a model. Keep the record going forward as a standing part of project close, which is the durable part. Include the projects that went well, since they are as informative as the failures. And separate estimation error from scope change, because conflating them hides both.

## Who Feels the Pain
Studios absorbing overruns out of margin; technical directors blamed for estimates nobody checked; producers managing dates set by a guess; and the business, which prices its core risk blind.

## Impact If Fixed
An estimate and an actual that live in different systems and are never compared produce no learning at all, however many projects go by. One table of the last twenty projects gives the business its first honest contingency number.
