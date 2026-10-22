# Overpayments Recovered From Widows Months After a Death

**Niche:** [[niches/pension-funds/payee-verification-overpayment/profile|Payee Verification & Overpayment Prevention]]
**Industry:** [[industries/pension-funds|Pension Funds]]
**Type:** Fix (Pain Point)
**One-liner:** When a retiree's death is reported late, the plan has paid several months too many and asks the grieving spouse to repay them.
**Tags:** #k-nearest-neighbors #logistic-regression #workflow-orchestration #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to stop payments to dead or impersonated payees before each monthly payroll runs, and whoever stops the most improper payments before the cutoff without holding a living retiree's check takes the account.

## The Problem
Death audits run on a schedule, often monthly or quarterly against vendor files. A death that the family does not report, and that the match misses because a name or date differs, can go unnoticed for months. The plan then reverses deposits where the bank allows and sends repayment letters to the survivor, who may also be the beneficiary now due a survivor benefit.

## Why It's Still Broken
Death matching and survivor benefit processing are separate workflows. Fuzzy matches below the vendor's threshold are discarded rather than reviewed, and nobody offsets an overpayment against the survivor benefit due.

## What a Fix Looks Like
Match against death data before every payroll, and route probable matches with name or date discrepancies to review. When a death is confirmed, start the survivor benefit and net any overpayment against it automatically, with a plain-language letter, instead of sending a repayment demand.

## Who Feels the Pain
Surviving spouses; the staff who make the recovery calls; plans writing off unrecoverable amounts.

## Impact If Fixed
Fewer overpayments arise, and those that do are resolved within the survivor's benefit rather than as a debt.
