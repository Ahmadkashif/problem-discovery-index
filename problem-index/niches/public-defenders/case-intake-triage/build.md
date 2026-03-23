# Intelligent Case Assignment Engine

**Niche:** [[niches/public-defenders/case-intake-triage/profile|Case Intake & Triage]]
**Industry:** [[industries/public-defenders|Public Defenders]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool optimizes case assignment by matching case complexity, charge type, and legal issues to attorney experience, skill set, and current caseload capacity — cases are assigned by rotation or geography, not fitness.
**Tags:** #gradient-boosting #ranking #tabular-ml #workflow-orchestration #automation

## The Problem
A DUI case with a constitutional search issue gets assigned to a new attorney who has never filed a suppression motion. A sex offense case goes to an attorney who has only handled misdemeanors. A case requiring Spanish-language client communication is assigned to an English-only speaker. These mismatches happen daily because case assignment in public defender offices is based on rotation (next name on the list) or geography (the attorney assigned to that courtroom), not case-attorney fit. The supervising attorney who makes assignments knows 10% of the relevant factors — the rest is buried in case files they haven't read.

## Why Nobody Has Built This
Intelligent case assignment requires three data inputs that don't currently exist in structured form: (1) case complexity and legal issue classification (from the charging document and discovery), (2) attorney skill profiles (experience by charge type, motion practice history, language capabilities, trial record), and (3) real-time caseload capacity (not just case count, but weighted by complexity). Building the assignment engine is straightforward once these inputs exist, but creating the data infrastructure is the hard part — it requires classifying every incoming case and maintaining dynamic attorney profiles.

## What to Build
A case assignment optimization engine with three layers. First, an NLP classifier that reads the charging document and produces a case profile: charge severity, likely legal issues (search and seizure, identification, self-defense, mental health), estimated complexity, and required attorney capabilities (language, trial experience, specialized knowledge). Second, a dynamic attorney capacity model that tracks each attorney's current caseload weighted by case complexity, upcoming trial dates, and historical performance by case type. Third, an assignment optimizer that matches cases to attorneys based on fit, capacity, and development goals (stretching newer attorneys with mentored assignments).

## Target Customer
Public defender offices with 20+ attorneys where case volume makes manual assignment optimization impossible. The buyer is the Chief Public Defender or the supervising attorney responsible for assignments.

## Impact If Built
Reduces case-attorney mismatch by an estimated 40-60%. Improves case outcomes by routing complex cases to experienced attorneys and ensuring specialized cases (sex offenses, death penalty-eligible, immigration-sensitive) reach attorneys with relevant expertise. Distributes caseload more equitably, reducing burnout.
