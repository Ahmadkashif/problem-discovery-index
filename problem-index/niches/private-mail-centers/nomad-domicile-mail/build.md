# An Address-Acceptance Map by Agency and Bank

**Niche:** [[niches/private-mail-centers/nomad-domicile-mail/profile|Domicile Mail for Full-Time Travellers]]
**Industry:** [[industries/private-mail-centers|Private Mail Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A traveller cannot tell in advance whether a DMV, an election office, an insurer or a bank will accept their mail-service address, and finds out by being turned away.
**Tags:** #large-language-models #logistic-regression #feature-engineering #evaluation-metrics #compliance #data-integration
**Contested on:** Every serious competitor in this niche is fighting to keep a traveller's address legally usable for a driver's licence, vehicle registration, voting and banking while their mail reaches them wherever they are, and whoever's address keeps passing the state DMV, the election office and the bank takes the account.

## The Problem
Acceptance of a mail-service address varies by state, by agency, by county office, by bank and by insurer, and changes when a rule or a verification vendor changes. The traveller's whole legal identity rests on an address that some institution may reject.

## Why Nobody Has Built This
The knowledge is scattered across forum posts, club newsletters and each mail service's staff, and no single operator sees enough outcomes to keep it current.

## What to Build
A crowd-sourced, verified acceptance map: for each address (or address class) and institution, the outcome of recent attempts, the documents that worked, and the date. Mail services contribute customers' reports; a language model extracts rule changes from agency pages and forum threads for human review; a simple model estimates acceptance likelihood for a new institution from similar ones.

## Target Customer
Specialist mail services serving RVers and expatriates, who would offer it to members as a retention feature.

## Impact If Built
Travellers prepare the right documents before a DMV visit or bank application instead of making a second trip across a state, and the mail service whose address passes most often can prove it.
