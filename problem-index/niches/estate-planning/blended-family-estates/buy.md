# Beneficiary Designation Audit Platform

**Niche:** [[niches/estate-planning/blended-family-estates/profile|Blended Family Estates]]
**Industry:** [[industries/estate-planning|Estate Planning]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Account aggregation tools pull balances and transactions from financial institutions — but none pull beneficiary designations, the one piece of data that actually determines who inherits retirement accounts and life insurance.
**Tags:** #large-language-models #feature-engineering #evaluation-metrics #data-integration #compliance

## The Problem
The single most important fact in blended family estate planning is who is named as beneficiary on each retirement account and life insurance policy. These designations override the will and trust — a $1M IRA naming the ex-spouse passes to the ex-spouse regardless of what the trust says. Yet there is no systematic way for attorneys to verify current beneficiary designations across a client's accounts. Attorneys ask clients to check, clients say "I'll get to it," and designations go unverified. When a client dies with an outdated designation, the family faces costly litigation (if permitted by state law) or simply loses the asset to the wrong person.

## What Already Exists
Account aggregation platforms (Plaid, Yodlee, MX) connect to financial institutions and pull account balances, transactions, and holdings. Financial planning tools (eMoney, RightCapital) use these feeds to build comprehensive net worth pictures. But none of these tools pull beneficiary designation data — it's not exposed through standard aggregation APIs. Insurance verification services (Verisk, LIMRA) track policy existence but not beneficiary information. The beneficiary designation is locked inside each financial institution's records, accessible only through the institution's website or by calling customer service.

## The Customization Gap
The missing tool creates a beneficiary designation audit workflow: (1) for each retirement account and life insurance policy in the client's asset inventory, generate a designation verification request (pre-filled letter or form for the institution), (2) track which designations have been verified and which are outstanding, (3) compare verified designations against the estate plan's intended distribution, (4) flag misalignments with specific remediation instructions ("Update IRA beneficiary at Fidelity from Jane Smith to the John Smith QTIP Trust — here is Fidelity's beneficiary change form"). For blended families specifically, the system should flag designations that name a prior spouse, designations that name a current spouse outright (which may defeat QTIP trust planning), and designations that omit stepchildren the client intends to benefit.

## Target Customer
Estate planning attorneys and their paralegals who currently manage beneficiary designation verification through email reminders, phone calls, and manual tracking spreadsheets — often giving up after 2-3 follow-ups and leaving designations unverified.

## Impact If Solved
Increases beneficiary designation verification completion from ~30% (current industry average) to 80-90% through systematic tracking and pre-filled forms. Prevents $50K-$500K+ per case in misaligned asset transfers. Creates a documented audit trail that reduces attorney malpractice exposure for designation-related estate plan failures.
