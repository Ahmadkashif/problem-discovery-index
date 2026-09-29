# The Contemporaneous Record That Says Nothing Useful

**Niche:** [[niches/construction-tech-platforms/daily-report-automation/profile|Daily Report & Field Capture]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Daily reports are written to be filed rather than read, so two years of them describe the weather accurately and the project's actual problems not at all — and then a claim depends on them.
**Tags:** #large-language-models #descriptive-statistics #evaluation-metrics #hypothesis-testing #compliance #automation #worker-facing #quick-win
**Contested on:** Every serious competitor in field capture is fighting to assemble the daily report from the day's own photos, messages, timecards and deliveries so the superintendent confirms rather than types — and whoever gets the accepted-unedited share highest takes the account.

## The Problem
A dispute arises eighteen months after a delay. Counsel pulls the daily reports for the relevant period, which is exactly what they are for. The reports say "continued work on level 3" for eleven consecutive days, record the weather correctly, and never mention that the area was inaccessible for six of those days because another trade had not finished. The superintendent knew. He wrote what he always writes, because the report is a compliance ritual nobody reads and writing about another trade's failure feels like starting a fight. The contemporaneous record that the entire claim depends on is contemporaneous and empty.

## Why It's Still Broken
Nobody reads daily reports until a dispute, so there is no feedback on their quality and no incentive to improve them. Writing about a problem in a permanent record also has social cost on a jobsite where the parties have to work together the next morning, and superintendents are sensitive to it — the omission is a judgment, not laziness. And the forms ask for what is easy to record rather than what is evidentially valuable: there is a field for weather and no field for "this area was not available and here is why."

## What a Fix Looks Like
Ask for impact explicitly and make it cheap and neutral. Add a structured impact entry — area, cause category, duration, responsible party if known, photo — that is a tap and a dropdown rather than a paragraph, and make it a normal part of every day's report rather than an exception that signals conflict. Cross-check the narrative against the day's own evidence and prompt where they disagree: if the schedule shows an activity that no photograph or timecard supports, ask. Score report specificity — repeated identical entries, absence of area detail, missing impacts on days the data suggests something happened — and report it to project leadership, because the first useful thing here is knowing that eleven consecutive reports were identical. None of this requires the superintendent to write more; it requires the form to ask better and the platform to notice when the record and the evidence diverge.

## Who Feels the Pain
Superintendents asked years later to explain a record they wrote in five minutes; contractors losing recoverable claims for want of contemporaneous documentation; and project executives who believed the reports were a record and discover they are a ritual.

## Impact If Fixed
Structured impact capture converts the daily report from a filed formality into the evidence it is supposed to be, and the difference shows up entirely in disputes — where the amounts are large and the record is the whole argument. The specificity score is free to compute and is the fastest way for a contractor to discover that its most important contemporaneous record currently says nothing.
