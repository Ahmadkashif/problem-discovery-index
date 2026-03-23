# Real-Time Margin Calculator with Full Burden Estimation

**Niche:** [[niches/staffing-agencies/backoffice-billing-margin/profile|Back Office Billing, Payroll & Margin Management]]
**Industry:** [[industries/staffing-agencies|Staffing Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool gives a recruiter or account manager an accurate margin estimate at quote time that accounts for state-specific SUTA rates, workers' comp class codes, ACA eligibility, overtime patterns, and client payment behavior.
**Tags:** #gradient-boosting #regression #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
An account manager receives a call: "I need 10 assemblers in Juarez, Texas, $18/hour pay, what's your bill rate?" The AM must calculate a bill rate that covers pay, FICA (7.65%), FUTA ($42/worker/year), Texas SUTA (variable, 0.31%-6.31% depending on the agency's experience rating), workers' comp class code 3632 (electronic equipment assembly, ~$1.50/$100 payroll), ACA eligibility (if the worker will exceed 30 hours/week for 12+ months), PTO accrual (if applicable), and a target gross margin of 20-25%. A senior AM does this calculation in their head in 30 seconds — drawing on years of experience with burden components. A junior AM guesses, under-quotes, and the agency discovers the true margin only when the placement closes. Margin leakage of 1.5-3 percentage points on 20-30% of job orders quietly erodes $200K-$500K annually at a mid-size agency.

## Why Nobody Has Built This
The calculation itself is deterministic, but the inputs are dynamic and fragmented: SUTA rates change annually and vary by state and employer experience rating, workers' comp rates vary by class code and carrier, ACA eligibility depends on hours patterns that cannot be known at quote time, and overtime exposure depends on the client's historical patterns (some clients consistently run 45-hour weeks). Building an accurate calculator requires real-time access to current SUTA rates, workers' comp rate tables, and historical client patterns — data that lives across payroll systems, insurance policies, and ATS records.

## What to Build
A margin estimation engine that takes job order inputs (state, pay rate, job classification, expected hours, contract duration) and calculates: gross margin at the proposed bill rate with fully loaded burden, sensitivity analysis (margin impact of 5-hour overtime per week, ACA threshold crossing, SUTA rate change), break-even bill rate (minimum to achieve target margin), and comparison to historical realized margins on similar placements. The system pulls current SUTA rates, workers' comp rates from the carrier's rate table, and historical overtime/payment patterns from the ATS/payroll system.

## Target Customer
Account managers and CFOs at staffing firms quoting 50+ job orders per month, where the difference between a 20% and 23% gross margin compounds into hundreds of thousands in annual profit.

## Impact If Built
Eliminates margin leakage on under-quoted placements ($200K-$500K annually at a mid-size firm), enables junior AMs to quote with the accuracy of a 20-year veteran, and provides management with real-time visibility into portfolio-level margin health.
