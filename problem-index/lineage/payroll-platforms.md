# Lineage: Payroll Platforms

**Industry:** [[industries/payroll-platforms|Payroll Platforms]]
**Wave:** [[series/eras/wave-01-mainframe-batch|1 — Mainframe & Batch]]
**The tool:** the ACH file — a fixed-width 94-character record set, carrying payroll as PPD credit entries
**Builder:** Nacha
**Builder in vault:** **ABSENT**
**Verification:** verified — see Sources

## The Problem That Came First

Paying people meant manufacturing objects.

On Friday an employer produced one piece of paper per employee, signed each, handed it over, and then waited while every one travelled back through the banking system independently — presented at a teller window, endorsed, bundled, driven to a clearing house, sorted, and charged against the account days apart, in no predictable order.

The employer's cost was visible: stationery, a signature machine, a clerk chasing which cheques had cleared and which sat in somebody's coat pocket. **The larger cost fell on the banks.** Payroll is the most synchronised batch in the economy — tens of millions of pieces of paper created on one afternoon — and by the late 1960s the clearing houses could see the curve and could not staff it.

## What Got Built

A file, in place of a stack.

The ACH format is a **fixed-width ASCII file in which every line is exactly 94 characters**. A `5` batch header names the originator and effective date; each `6` entry detail record is one person — account, amount, name, trace number — with optional `7` addenda; an `8` record closes the batch with a count, a dollar total and a hash total. A paycheque travels as a **PPD** entry, the Prearranged Payment and Deposit class for consumer accounts.

What matters is not the field layout. It is that **payroll becomes one object rather than N transactions.** The employer hands one file to one bank, and the network fans it out to every institution in the country.

## Who Built It, And Why Them

The clearing houses built it, because the clearing houses were the ones paying for the paper.

**In 1968 a group of check clearing house associations formed SCOPE — the Special Committee on Paperless Entries — specifically out of concern about the volume of cheques being cleared for payrolls.** In 1972 the California Automated Clearing House Association became the first operational ACH association in the country, and on **20 June 1974** the regional associations combined to form NACHA to govern a national network.

That is the whole explanation of *why them*. An employer's marginal cost for one more cheque is a sheet of paper. A clearing house's is transport, sorting and presentment, rising with every employee hired in its region. The payroll service bureaus, a mature business by 1968, never built this: their cost was **computing** the pay, not **moving** it, so they had every reason to plug into a settlement layer and none to build one.

Demand came from the largest employer available: the **US Air Force was the first major employer to adopt direct deposit for payroll**, and federal volume made the network worth building against.

## What It Cost

A file is not a conversation, and the ACH never acquired one.

The card networks spent the 1970s making *"is this account good?"* answerable in seconds — see [[lineage/payment-processors|Lineage: Payment Processors]]. ACH asks nothing. You submit ahead of an effective date, get no confirmation anything landed, and learn about a closed or mistyped account from a **return code arriving a couple of banking days later**, by which time the employee has already not been paid.

Batch settlement also imposed the clock. Pay on Friday means a file out Wednesday, so the close is Tuesday — which is why payroll is an industry with a deadline rather than a workflow. **Same Day ACH — credits from 23 September 2016, debits from 15 September 2017, 5pm funds availability from 16 March 2018** — shortened the wait without changing the shape. A faster batch is still a batch.

## What You Still Touch

Your pay appears at an hour on Friday nobody can tell you in advance, and if it does not, there is no one to ask and nothing to query.

- [[problems/payroll-platforms/worker-life-1|🟢 Payroll Specialist Friday Close]] — a deadline manufactured by a settlement window
- [[problems/payroll-platforms/worker-life-2|🟢 Support During a Missed Deposit]] — the missing acknowledgement
- [[problems/payroll-platforms/low-impact-2|🟡 Garnishment Order Processing]] — third parties riding the same file
- [[niches/payroll-platforms/disbursement-failure-recovery/profile|Disbursement & Failure Recovery]] — a practice built around return codes
- [[niches/payroll-platforms/worker-facing-pay-tools/profile|Worker-Facing Pay Tools]] — earned-wage access exists because the batch does not
- [[niches/payroll-platforms/payroll-operations-practitioners/profile|Payroll Operations Practitioners]] — the people holding the clock

**Sources:** Nacha, *History of Nacha and the ACH Network*, and Wikipedia, *NACHA* / *ACH Network*, for SCOPE's formation in 1968 out of concern over payroll cheque volume, CACHA as the first operational ACH association in 1972, and NACHA's founding on 20 June 1974. Nacha's ACH Developer Guide and multiple bank-published NACHA file specifications (Hancock Whitney, First Citizens, Bank of California) for the 94-character fixed-width record structure, the 1/5/6/7/8/9 record types, batch hash totals and the PPD entry class. Nacha rules pages for Same Day ACH Phases 1–3 (23 September 2016, 15 September 2017, 16 March 2018). ⚠️ **Partially established:** the US Air Force as the first major employer to adopt payroll direct deposit is consistently reported in secondary accounts but is given here **without a date**, because I could not pin one to a primary source this session. ⚠️ **Deliberately not claimed:** a founding date for any individual payroll bureau. The "already a mature business by 1968" characterisation is a general one and is not sourced to a company history. Return-code timing is stated as "a couple of banking days," matching the general rule for most return reasons rather than any specific R-code deadline.
