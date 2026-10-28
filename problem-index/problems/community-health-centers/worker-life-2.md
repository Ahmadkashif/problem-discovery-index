# The Front Desk Asking for Income Proof at Every Visit

**Industry:** [[community-health-centers|Community Health Centers]]
**Type:** Worker Life Changing
**One-liner:** A health center receptionist must ask each uninsured or underinsured patient for household size, income proof, housing status and other UDS demographics, photocopy what they bring and set the sliding-fee discount, so she gets back her dignity at the window and the line moves.
**Tags:** #large-language-models #transformers #cnns #feature-engineering #worker-facing #compliance #automation

## The Problem
Health centers must offer a sliding fee discount to patients at or below 200% of the federal poverty guidelines, with a full discount or nominal charge at or below 100%. They must base each discount on documented household income and size and re-check it on a schedule set by board policy (HRSA Compliance Manual, chapter 9, recalled). In 2025, 5.6M health center patients were uninsured and 67.7% of patients with known income were at or below the poverty line (UDS).

The front desk does this at check-in. A patient services representative asks who lives in the household and what they earn, then asks for pay stubs, a tax return, an unemployment letter or a signed self-declaration for cash income. She photocopies what the patient brings, keys the numbers into a registration screen and picks the discount tier. In the same conversation she asks for race, ethnicity, preferred language, housing status, agricultural work and veteran status, all of which feed UDS. She does this with a line behind the patient, often in two languages, and repeats it when the documentation expires.

## Why It Matters to the Worker
It is the most uncomfortable part of the job. She asks a stranger at a window, in front of others, to prove how poor they are. Patients are embarrassed, angry or afraid of where the information goes, and some walk out rather than answer. If she accepts weak documentation, the center risks a finding at HRSA's operational site visit. If she insists, she loses the patient. The rules for what counts as income, who counts as household and when proof expires are in a policy binder she rarely has time to open. When an auditor or a billing error later shows the wrong discount, it is traced back to her entry.

## What a Solution Looks Like
Let the patient do the private part privately. A text-message link before the visit, or a tablet in a quiet corner, asks the household and income questions in the patient's language. It explains why they are asked and lets the patient photograph documents. A document model reads the pay stubs and letters and proposes household income, size and the sliding-fee tier with the supporting evidence attached. It flags anything it cannot read, as well as documentation about to expire. The representative confirms in one click and only talks about money when something is unclear. The record is ready for the site visit.

## Impact If Solved
Cutting a sliding-fee check from ~10 minutes at the window to ~2 minutes of review (estimate) frees ~1.5 hours a day for a representative who handles ~12 sliding-fee checks a day (estimate). Fewer patients will walk away from the conversation, and the center keeps its sliding-fee file intact for the next site visit.
