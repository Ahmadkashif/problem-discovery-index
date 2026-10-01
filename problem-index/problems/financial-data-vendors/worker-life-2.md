# The Data Specialist Asked Why the Numbers Differ

**Industry:** [[financial-data-vendors|Financial Data Vendors]]
**Type:** Worker Life Changing
**One-liner:** Client data specialists spend their day reconstructing how a number was derived — because the vendor stored the number and not the derivation — for a client whose model broke an hour before a meeting.
**Tags:** #large-language-models #bert #word-embeddings #k-nearest-neighbors #evaluation-metrics #worker-facing #workflow-orchestration #data-integration

## The Problem
The ticket says: your EBITDA for this company is 4% lower than Capital IQ's, lower than the company's own press release, and different from what your platform showed last month — which is right? Sometimes the question comes from a portfolio manager by chat, sometimes from a banker building a comp table due at 7 a.m.

The specialist has to answer it. That means finding which filing the figure came from, whether it is as-reported or standardised, which adjustments were applied under which policy, whether a restatement superseded the prior value, how the competitor defines the same field (inferred, since nobody publishes it), and whether the company's own figure is a non-GAAP measure with its own exclusions. The answer lives across the collection tool's audit log, the methodology documents, the restatement history and the specialist's memory of having answered something similar for another client.

## Why It Matters to the Worker
The specialist absorbs the cost of an architectural choice: the vendor kept the number and discarded the reasoning. Every explanation is archaeology under a clock someone else set, and the client's patience is short because their model is broken now.

The work is skilled — it requires understanding accounting, the vendor's methodology and the competitor's — and it is measured as ticket handle time. When the investigation reveals a genuine error, the specialist must route it to content operations and wait, and the client blames the person on the phone. The same explanation is written from scratch dozens of times a quarter because no one has collected the answers.

## What a Solution Looks Like
Lineage on demand. Every value carries its derivation: source document and page, as-reported components, adjustments applied and the policy version, restatement history. The specialist opens the lineage instead of reconstructing it.

A reconciliation view against the obvious comparators: the company's press-release figure with its stated exclusions, and the vendor's own prior value, with the difference decomposed into named items.

Precedent retrieval over resolved tickets, so the specialist starts from how the same question about the same field was answered last time.

A clean path to content operations when the answer is "we are wrong," with the client told when the fix lands.

## Impact If Solved
Discrepancy questions are among the most frequent and most time-consuming client interactions at every vendor, and they are disproportionately raised just before high-stakes deadlines. Lineage that already exists makes most of them a two-minute answer, gives the specialist back their judgement for the hard cases, and turns their resolved tickets into labelled data for the collection models upstream.
