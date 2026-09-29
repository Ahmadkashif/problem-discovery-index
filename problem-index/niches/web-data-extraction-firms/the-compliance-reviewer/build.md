# Unsettled Law, No Tooling, Commercial Pressure

**Niche:** [[niches/web-data-extraction-firms/the-compliance-reviewer/profile|The Compliance Reviewer]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A compliance reviewer approves or refuses collection requests against a legal landscape that is genuinely unsettled, with no tooling, no precedent library and commercial pressure on one side of every decision.
**Tags:** #compliance #large-language-models #evaluation-metrics #worker-facing #descriptive-statistics #data-integration #graph-theory #automation
**Contested on:** Every serious competitor in this niche is fighting to give the reviewer a precedent library and a framework instead of an unsettled legal landscape and a deadline — and whoever does that takes the account, because this decision gates every collection the firm runs.

## The Problem
A request arrives: collect listing data from a large marketplace, for a customer who describes the purpose as market research. The reviewer needs to know what the site's terms say, whether its robots directives address this, whether the content is likely copyrighted, whether personal data is exposed, which jurisdictions' residents are involved, whether the customer's stated purpose is the real one, and what the firm decided on the four similar requests it has seen. They have a form, a browser and two days. The sales team needs an answer by Thursday. They approve with caveats nobody will read.

## Why Nobody Has Built This
The legal questions are genuinely unsettled, which makes a tool that gives an answer feel inappropriate — and has been used to justify building nothing, including the parts that are purely mechanical. Legal functions are small and do not build software. The firm's own precedent is scattered across emails. And a reviewer with better tooling would refuse more clearly, which is not universally welcome internally.

## What to Build
Give the reviewer evidence, precedent and a way to say something other than yes or no. Automate the evidence gathering — the target's current and historical terms, robots directives, whether personal data appears in the fields requested, the jurisdictions implicated, whether the site is in known litigation — which is mechanical, takes the reviewer a day, and would take a system minutes. Build a precedent library of the firm's own decisions with their reasoning, indexed by the features that mattered, which the fix note develops and which is the largest single improvement available. Provide a structured intake capturing the features a decision actually turns on: target, fields, rate, purpose, customer, jurisdictions, output use including model training. Support graduated outcomes — approve with field exclusions, with a rate cap, with a jurisdiction exclusion, with a purpose restriction, with a review date — since the binary form pushes toward approval and most real answers are conditional. Record uncertainty explicitly, because on several of these questions the honest position is that it is unsettled, and a record that says so is more defensible than one that implies confidence. Track the legal landscape and flag affected past decisions when something changes. Report approval and refusal rates and their commercial consequences, which makes the pressure visible rather than personal. And give refusals standing, since a reviewer who can be overridden without record is not a control.

## Target Customer
Legal and compliance functions at extraction firms, the reviewers themselves, the firms' leadership, and the customers whose risk position depends on these decisions.

## Impact If Built
The unsettledness of the law has been used to justify building nothing, including the mechanical parts. Automated evidence gathering turns a reviewer's day into minutes, and graduated outcomes let them express the conditional answer that the binary form currently pushes into an approval.
