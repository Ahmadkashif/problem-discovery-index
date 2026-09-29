# The Process Is Already Written Down, in Formulas

**Niche:** [[niches/no-code-app-builders/spreadsheet-process-migration/profile|Spreadsheet Process Migration]]
**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A team's process is fully specified in a spreadsheet's columns, formulas, validation lists and colour rules, and every migration path asks them to describe it again from nothing.
**Tags:** #graph-theory #large-language-models #bert #decision-trees #evaluation-metrics #confidence-intervals #automation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to turn an existing spreadsheet-and-email process into a working application without the owner rebuilding it from scratch — and whoever does that takes the department, because the rebuild is the only reason the process is still a spreadsheet.

## The Problem
A claims team runs on a spreadsheet with nineteen columns, a validation list of eight statuses, three formulas computing ageing and priority, conditional formatting that turns a row amber at five days, a pivot that is the weekly report, and a convention that a comment in column S means escalated. Around it are an email alias where claims arrive and a rule that anything over a threshold gets forwarded for approval. Everything about the process is written down. Moving to an app means a person re-entering all of it into a builder, plus the data, plus the training — a week of work for a process that functions, which is why it has been a spreadsheet for six years.

## Why Nobody Has Built This
Import features were built to move data, because data has an obvious representation and process does not, and nobody attempted the harder half. Extracting process from a spreadsheet requires parsing formulas into a dependency graph and interpreting conventions that are idiosyncratic to each team — colour meaning status, a column used as a flag, a blank meaning not started — which needed language-model-grade interpretation to be feasible and was therefore out of reach until recently. The email side has never been touched by anyone. And vendor onboarding is optimised for time-to-first-app rather than time-to-replaced-process, which are different targets and lead to different products.

## What to Build
Migration that reads the process, not just the rows. Parse the workbook into its dependency graph and classify what each element is doing: a status field, a computed ageing metric, a validation list that is an enumeration, a lookup that is a relationship to another entity, a pivot that is a report, a colour rule that encodes a state transition. Interpret the conventions with a model and confirm them with the owner in their own language — "it looks like a row turns amber after five days and that means it needs chasing; is that right?" — which is a conversation the owner can have and a specification they could never write. Read the email half where it is available: the alias that receives work, the forward that is an approval, the reply that is a completion, which supplies the workflow the spreadsheet cannot express. Generate the app with its data, its rules, its views and its automations, and then run both in parallel with a comparison — the same inputs producing the same outputs — which is the verification that makes the owner willing to switch and which nothing currently offers. And keep a reversible path for a period, since the fear of being unable to go back is what stops the decision more often than the effort.

## Target Customer
Operations and departmental managers running real processes on spreadsheets, no-code vendors whose growth depends on reaching beyond people who already want to build apps, and the implementation partners doing this by hand today for the customers who can afford them.

## Impact If Built
The rebuild cost is the entire reason this population has not moved, and the process specification they would have to rewrite already exists in machine-readable form. Parallel-run verification is what converts a risky migration into a safe one, and reversibility is what makes the decision easy.
