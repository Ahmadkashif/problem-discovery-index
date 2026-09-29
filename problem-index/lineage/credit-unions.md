# Lineage: Credit Unions

**Industry:** [[industries/credit-unions|Credit Unions]]
**Wave:** [[series/eras/wave-01-mainframe-batch|1 — Mainframe & Batch]]
**The tool:** the share draft — a withdrawal order drawn on a share account and *payable through* a commercial bank
**Builder:** Credit Union National Association
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A credit union member could save and borrow. They could not pay anybody.

Into the early 1970s a credit union held shares and a loan book and nothing in between. The instrument households transacted with was the cheque, and a cheque is a draft on a *demand deposit* — which a federal credit union had no authority to accept. So the member kept two relationships: a credit union for saving, a bank for living. The payroll landed at the bank, the bills were paid from it, and the balance sat there in between.

**The constraint was definitional, not technical.** Nothing about writing a cheque is difficult. What a credit union lacked was standing — authority to hold the deposit, and a position in the interbank arrangement that moves paper items between institutions.

## What Got Built

A cheque that is legally not a cheque.

The **share draft** is an order to withdraw from a share account, printed and encoded to clear like a cheque, and — the load-bearing phrase — **payable through** a named commercial bank rather than at the credit union itself. The bank supplies the clearing position and the routing digits; the credit union keeps the member and the pay-or-return decision.

Every feature of its shape is a fact about what a credit union was not permitted to be. It is not drawn on the credit union, because the credit union has no place in the clearing chain. The balance behind it stays a *share* — equity in a cooperative, not a deposit — which is why what protects it is share insurance.

**NCUA approved the first share draft programmes in October 1974, on a pilot and experimental basis, for three federally chartered credit unions.** Approval then spread on individual application until federal credit unions in all fifty states had them.

## Who Built It, And Why Them

CUNA — through its wholly owned subsidiary I.C.U. Services Corporation, which developed the prototype programmes the regulator approved.

Why the trade association: **no single cooperative could have assembled it.** The design only functions if a correspondent bank agrees to stand as the payable-through party, if the drafts are printed to one specification the clearing system will accept, and if the regulator will bless a template rather than adjudicate thousands of applications. Those are three negotiations, and the median credit union in 1974 had a few thousand members and a handful of staff.

The capability was designed once, centrally, and distributed — the first instance of the pattern governing credit union technology ever since: **what the industry needs is built by an entity the industry collectively owns, and rented back.** Core processing, shared branching and the card rails all arrived the same way, for the same reason.

## What It Cost

The banks sued, and briefly won. **On 20 April 1979 the DC Circuit held that the NCUA, the Federal Home Loan Bank Board and the Federal Reserve had exceeded their statutory authority** in permitting share drafts and the parallel bank and thrift products, staying the effect to 1 January 1980. It did: the Consumer Checking Account Equity Act, inside the Depository Institutions Deregulation and Monetary Control Act signed 31 March 1980, wrote share draft authority into the Federal Credit Union Act and authorised NOW accounts nationwide.

Five years of holding a transaction product at the regulator's pleasure was the visible price. The architectural price was quieter: the payable-through design put a commercial bank permanently inside the cooperative's payment path. Credit unions later obtained their own routing numbers, but the sector entered electronic payments as somebody else's correspondent traffic.

## What You Still Touch

Your credit union "checking account" is a share draft account and your balance is a share. You are an owner, not a depositor — vocabulary chosen in 1974 to route around a word the statute reserved for banks.

- [[problems/credit-unions/low-impact-1|🟡 Digital Banking Feature Parity with Neobanks]] — buying the transaction layer again, for the same reason
- [[niches/credit-unions/core-banking-vendor-data/profile|Core Banking Platform Data Teams]] — where the rented capability lives now
- [[niches/credit-unions/member-onboarding-automation/profile|Member Onboarding & Cross-Sell Automation]]
- [[niches/credit-unions/deposit-loan-pricing-data/profile|Deposit & Loan Pricing Benchmark Data]] — pricing a share, not a deposit

**Sources:** NCUA, Share Insurance Fund history; Washington State Attorney General opinion and Michigan insurance-bureau declaratory ruling (1974–77) on the legality of share draft programmes — both describe the October 1974 NCUA pilot approval for three federal credit unions and attribute the prototype to CUNA's wholly owned subsidiary I.C.U. Services Corporation; Wikipedia, *Depository Institutions Deregulation and Monetary Control Act*; *Fordham Law Review* 46(6), "The Legality of Credit Union Share Accounts Under Federal Law"; DC Circuit ruling of 20 April 1979 and the stay to 1 January 1980, as reported in contemporaneous legislative and policy commentary; this vault's `history/credit-unions.md` and `industries/credit-unions.md` (cited as vault material, not independent corroboration — and note that the history note covers the *field-of-membership* fight, a different contest from the one here). ⚠️ **Not established:** which three credit unions ran the October 1974 pilot, and the name of the first payable-through correspondent bank. Both were searched and neither is named in any source reached this session. ⚠️ **Read at second hand:** the 1979 DC Circuit holding and the Consumer Checking Account Equity Act's text were confirmed through secondary summaries, not the opinion or the statute itself.
