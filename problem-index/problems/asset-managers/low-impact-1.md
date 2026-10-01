# RFP, DDQ and Consultant Database Responses

**Industry:** [[asset-managers|Asset Managers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every institutional search asks the same few hundred questions in a different order and wording, and the answers must agree with what the firm told every consultant database last quarter.
**Tags:** #large-language-models #bert #word-embeddings #k-nearest-neighbors #evaluation-metrics #compliance #workflow-orchestration #automation

## The Problem
An institutional mandate is won through a process the manager does not control. A pension fund's investment consultant screens the universe on a consultant database — eVestment, Mercer's GIMD, Callan's or Aon's — then issues an RFP to a shortlist, often with a due diligence questionnaire attached, and gives the managers two to four weeks. A mid-sized manager answers a few hundred of these a year across its strategies, plus quarterly database updates, plus ad hoc consultant information requests.

The questions overlap massively — team, process, risk management, ESG integration, cybersecurity, business continuity, fees, performance, holdings characteristics — but each is worded differently, wants a different length, and asks about a different strategy, vehicle or share class. The numeric answers (AUM by strategy, performance, characteristics, headcount, turnover) change every quarter. An answer that disagrees with the firm's eVestment profile, or with an answer given to the same consultant last year, is noticed.

## What Already Exists
RFP content libraries — Loopio, Responsive (formerly RFPIO), Upland Qvidian — store approved answers and offer search and, increasingly, generative drafting. Consultant databases have their own upload templates. Some managers run data feeds from their performance system into the database uploads.

## The Customisation Gap
The generic tools treat an RFP as a search over a library of approved prose. In asset management the hard part is not the prose; it is that answers are strategy-specific, vehicle-specific and date-specific, and that numbers must tie to the performance book of record and to what each consultant database currently shows. The library needs to understand that "the Global Equity strategy" and "the Global Equity CIT" have different fee schedules and the same team, that a GIPS composite's performance must be presented with the required disclosures, and that marketing-rule constraints apply to how performance is shown.

It also needs the consistency check nobody runs: has the firm described its ESG integration, its headcount or its risk limits differently to two consultants this year? Generic tools answer each RFP in isolation; the risk sits across them.

## Impact If Solved
RFP and database work occupies a sizeable team at every institutional manager and is a gating step for every new mandate. An answer layer that is aware of strategy, vehicle and quarter, and tied to the book of record, removes most of the re-writing and the reconciliation, and closes the cross-consultant inconsistency that currently surfaces only when a consultant points it out.
