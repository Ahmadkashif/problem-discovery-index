# Contingency Reported as a Balance

**Niche:** [[niches/construction-tech-platforms/owner-side-project-controls/profile|Owner & Developer-Side Project Controls]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every owner report shows contingency as money remaining, which tells the owner nothing about whether it is enough, and the question of sufficiency is answered by whether the number still looks big.
**Tags:** #monte-carlo-methods #bayesian-inference #confidence-intervals #descriptive-statistics #evaluation-metrics #hypothesis-testing #revenue-impact #compliance
**Contested on:** Every serious competitor selling to owners is fighting to produce a cost-to-complete and a completion date that do not originate with the contractor being measured — and whoever makes the owner's number independent takes the account.

## The Problem
A project carries $2.1M of contingency, of which $900K has been drawn at the 55% completion point. The monthly report shows $1.2M remaining. The board is reassured. Whether $1.2M is enough depends entirely on what risk remains, and nobody has said: the drawdown so far has been dominated by design clarifications that are mostly behind the project, or alternatively by unforeseen conditions that will keep recurring. A balance is a fact about the past presented as comfort about the future, and it is how contingency is reported on essentially every project in the industry.

## Why It's Still Broken
Reporting a balance is easy and reporting sufficiency requires a forward view, which requires attributing past draws to causes and having a basis for forecasting the remaining ones. Neither is hard, and neither is anyone's job: the cost reporter reports cost, the scheduler reports schedule, and risk management on most projects is a register maintained separately and reviewed quarterly. There is also a reporting culture problem — a report that says "there is a 30% chance the contingency is insufficient" invites a difficult conversation, and a balance does not, so the balance survives.

## What a Fix Looks Like
Classify every contingency draw by cause — design clarification, unforeseen condition, owner-directed scope, market and escalation, coordination error — which is a small amount of work per draw and is the thing that makes everything else possible. Then forecast the remaining draw by cause, using the project's own drawdown pattern to date and the owner's portfolio history for how each cause behaves by phase. Report sufficiency as a probability with the drivers named, alongside the balance rather than instead of it. Make the by-cause breakdown visible, because it is immediately actionable in a way a balance is not: contingency going to coordination errors says something different about the project than contingency going to escalation, and the responses are different. The classification also compounds, since an owner with three years of cause-coded draws across a portfolio has the best possible basis for setting contingency on the next project.

## Who Feels the Pain
Owners reassured by a number that does not mean what it appears to; project executives who sense the contingency is thin and cannot demonstrate it; and boards approving capital on reports that describe the past.

## Impact If Fixed
Cause-coded drawdown with a forward forecast converts contingency from a comfort blanket into a managed reserve, and it typically reveals that sufficiency is either much better or much worse than the balance suggested. The coding effort is minutes per draw and is the cheapest structural improvement available in owner-side reporting.
