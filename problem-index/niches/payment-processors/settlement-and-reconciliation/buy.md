# Trade Reconciliation Practice

**Niche:** [[niches/payment-processors/settlement-and-reconciliation/profile|Settlement & Reconciliation]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Securities settlement reconciles to the cent daily with automated break management, and payment settlement reconciles in a spreadsheet.
**Tags:** #data-integration #workflow-orchestration #automation #compliance #evaluation-metrics #descriptive-statistics #confidence-intervals #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to prove that money moved across networks, currencies and fee schedules adds up — and whoever does that automatically removes the largest manual finance function in payments.

## The Problem
Post-trade reconciliation in securities is exact, automated and non-negotiable. Positions and cash are reconciled daily against custodians and clearing houses, breaks are raised automatically with an owner and an ageing clock, root causes are categorised, and the function is measured on break volume and resolution time. The infrastructure is mature and the discipline is enforced by regulation. Payment settlement reconciles comparable volumes across more counterparties with more fee complexity, largely manually.

## What Already Exists
Automated matching engines with configurable tolerance; break management with ownership and ageing; root cause categorisation and trending; exception workflow with escalation; and reconciliation control reporting.

## The Customization Gap
The adaptation is to counterparties who set their own formats and a fee structure of enormous complexity. It requires: (1) fee schedules with hundreds of qualification conditions that must be recomputed to verify, where securities reconciliation deals with simpler commission structures — independently recalculating interchange is the substantive addition and is where real money is found; (2) no common transaction identifier across counterparties, unlike a trade reference, so matching is probabilistic on attributes; (3) settlement timing that varies by network, market and product, making the timing dimension part of the matching rather than a fixed convention; (4) merchant-level sub-reconciliation, since the processor must also prove its own payouts to merchants are correct, which is a second layer securities does not have; and (5) no regulatory mandate forcing the discipline, so it must be justified commercially.

## Target Customer
Processor finance operations, platform acquirers, and reconciliation vendors for whom payments is a larger and less served market than securities.

## Impact If Solved
Securities reconciles to the cent daily under a regulatory mandate and payments does comparable volume in spreadsheets. Independently recomputing complex fee schedules is the addition that finds real money, and the absence of a common transaction identifier makes matching probabilistic.
