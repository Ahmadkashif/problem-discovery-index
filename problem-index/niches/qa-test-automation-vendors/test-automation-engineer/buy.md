# Exploratory Testing Practice, Unsupported by Tooling

**Niche:** [[niches/qa-test-automation-vendors/test-automation-engineer/profile|The Test Automation Engineer]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Exploratory testing has a developed practice with heuristics, charters and session-based management, and no tooling supports any of it because the category's products are built for automation.
**Tags:** #large-language-models #k-means-clustering #bert #descriptive-statistics #evaluation-metrics #confidence-intervals #worker-facing #tacit-knowledge-ml
**Contested on:** Every serious competitor that takes this seriously is fighting to return a test engineer's week from repair to design — and whoever does that takes the quality function, because repair is currently the job and design is what the role was created for.

## The Problem
Exploratory testing is a developed discipline: heuristics for where defects hide, charters that scope a session, session-based management that makes the work accountable, and a substantial practitioner literature about how to think about what could go wrong. It is the design half of the test engineer's job and it is supported by no tooling whatsoever, because the category's products automate execution and exploration is by definition not automated.

## What Already Exists
The exploratory testing literature with its heuristic catalogues and session management methodology; risk analysis frameworks; fault taxonomies from safety engineering; boundary and equivalence class analysis, which is teachable and is frequently not taught; and language models capable of proposing what could go wrong given a description of a system.

## The Customization Gap
The adaptation is to support judgement rather than replace it. It requires: (1) proposing rather than deciding, since the value of exploration is a human noticing something a machine would not, and a tool that generates a list of cases produces the same low-value volume the generation sub-niche describes — the useful form is a prompt that makes the engineer think of something; (2) grounding in this system's actual history, so the heuristics offered are the ones that have found defects in this codebase rather than a generic catalogue, which requires the escaped-defect record; (3) capturing the session, since exploratory work produces findings that are currently written up inconsistently or not at all, and structured capture makes the work accountable and reusable; (4) turning findings into automated tests where appropriate, which is the handoff between the two halves of the role and is manual; and (5) measuring the output honestly, since exploration's value is defects found and the practice has always struggled to demonstrate that against the visible activity of automation.

## Target Customer
Quality engineering functions, test management tool vendors, and the exploratory testing practitioner community whose methodology has no software behind it.

## Impact If Solved
A developed practice covering the valuable half of the role has no tooling at all, because the category automated the other half. Grounding the heuristics in this system's own defect history is what makes the prompts useful rather than generic.
