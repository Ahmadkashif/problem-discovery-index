# Tax Engines Wired to the Trust Ledger

**Niche:** [[niches/trust-companies/fiduciary-tax-compliance/profile|Fiduciary Tax Compliance]]
**Industry:** [[industries/trust-companies|Trust Companies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Fiduciary tax software computes the return correctly once the numbers are in; getting the numbers from the trust ledger, under each instrument's allocation rules, is where the hours go.
**Tags:** #feature-engineering #large-language-models #data-integration #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to file every trust's 1041 and K-1s correctly by the April deadline despite late and corrected tax information, and whoever finishes the most returns without an amendment takes the account.

## The Problem
Trust ledgers separate income and principal under state law and the instrument; tax returns need income, deductions and distributions classified for distributable net income. The mapping is configured once and then patched by hand for every unusual trust.

## What Already Exists
Fiduciary modules of tax software from CCH and Thomson Reuters, with import routines from trust accounting systems such as FIS, SEI and SS&C Innovest.

## The Customization Gap
The adaptation needs: instrument-aware treatment of capital gains (whether they are allocated to distributable net income under the instrument, state law or consistent practice), fee allocation between income and principal, specific bequests and terminating-year rules, grantor and non-grantor status changes during the year, state residency of trustees and beneficiaries for state returns, and an automatic tie-out from return to ledger with exceptions explained.

## Target Customer
Fiduciary tax units already licensing a tax engine who want fewer manual adjustments per return.

## Impact If Solved
Fewer adjustments per return and a tie-out that runs itself, so preparers review exceptions rather than rebuild each trust.
