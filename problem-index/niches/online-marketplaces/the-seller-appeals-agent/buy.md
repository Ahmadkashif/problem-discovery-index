# Due Process and Explainability Practice

**Niche:** [[niches/online-marketplaces/the-seller-appeals-agent/profile|The Seller Appeals Agent]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Credit decisioning has been required to give applicants specific reasons for adverse decisions for decades, and marketplace suspensions cite a policy section.
**Tags:** #compliance #logistic-regression #evaluation-metrics #worker-facing #confidence-intervals #descriptive-statistics #automation #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to give the person handling an appeal the reason for the suspension and the authority to act on it — and whoever does that takes the account, because this conversation is where a marketplace's relationship with its sellers is decided.

## The Problem
Telling somebody specifically why an automated decision went against them, in a form they can act on, is a legal requirement in credit decisioning and a developed practice in employment and insurance. Adverse action notices name the principal reasons. Appeals processes have defined timelines and an independent reviewer. Regulated decisions carry a record of the basis. Marketplace suspensions, which stop a person's income with the same immediacy as a credit refusal, cite a policy number and invite the seller to review it.

## What Already Exists
Adverse action notice requirements with specific-reason obligations; reason code generation from scoring models; appeal processes with defined timelines and independent review; model explainability methods producing per-decision attributions; and the documentation practice regulated decisioning carries.

## The Customization Gap
The adaptation is to a decision where explanation can aid evasion. It requires: (1) an explicit separation of explanatory signals from evasion-sensitive ones, since not every signal is sensitive and treating them all as such is the reason nothing is explained — making this distinction per signal is the enabling step; (2) per-decision attribution from the detection model, which the explainability methods provide directly and which nobody surfaces; (3) appeal timelines proportionate to consequence, since a stopped income is a materially different urgency from a listing removal and the queue treats them the same; (4) an independent review step for contested cases, which regulated decisioning requires and which prevents the appeal being decided by the same logic that made the decision; and (5) a record of the basis, since a suspension that cannot be justified afterwards is a regulatory exposure in several jurisdictions now moving on platform accountability.

## Target Customer
Seller support and risk organisations, sellers, regulators increasingly interested in platform decision accountability, and the explainability tooling ecosystem.

## Impact If Solved
Credit decisioning has given specific reasons for decades and marketplace suspensions cite a policy number. Separating explanatory from evasion-sensitive signals per signal is the enabling step, and it unblocks explanations that currently do not exist because everything is treated as sensitive.
