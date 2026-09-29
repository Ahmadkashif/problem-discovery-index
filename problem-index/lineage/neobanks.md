# Lineage: Neobanks

**Industry:** [[industries/neobanks|Neobanks]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the Durbin Amendment's small-issuer exemption, 15 U.S.C. § 1693o-2: debit cards issued by a bank with under $10 billion in assets are exempt from Regulation II's interchange cap of 21 cents plus 0.05%
**Builder:** US Congress
**Builder in vault:** **ABSENT**
**Verification:** verified for the statute and Chime's filings; partial on intent — see Sources

## The Problem That Came First

A bank earns on a deposit account by lending the deposits or charging the customer. A company without a charter can do neither.

It cannot lend deposits it does not hold. And the customers it was built for, people living paycheck to paycheck and tired of overdraft and minimum-balance fees, are the ones who leave when they are charged. What remains is the fee the *merchant* pays every time a customer swipes a debit card: interchange, set by the card networks and split among the banks in the transaction.

So whether a phone-first checking account can survive comes down to one number: how much interchange a debit swipe earns. From October 2011 federal law set that number, differently for different banks.

## What Got Built

Section 1075 of the Dodd-Frank Act, signed 21 July 2010, is the amendment Senator Dick Durbin added. It ordered the Federal Reserve Board to cap debit interchange at a level "reasonable and proportional" to the issuer's cost. The Board's Regulation II, final on 29 June 2011 and effective 1 October 2011, set the cap at **21 cents plus 0.05% of the transaction**, plus a one-cent fraud-prevention adjustment.

The statute also drew a line. **An issuer that, with its affiliates, has less than $10 billion in assets is exempt.** Its debit cards still earn the unregulated network rate.

Put the two halves together. A small bank's debit swipe earns the market rate. A large bank's earns the capped rate. A company that can bring millions of cardholders to a *small* bank can share the difference.

## Who Built It, And Why Them

The builder is Congress, with the Federal Reserve Board writing the rule. The carve-out exists because the target was the largest issuers, and the $10 billion line kept smaller banks and credit unions out of the cap. Nobody drafting it was thinking about app-based checking accounts, and I found no evidence that anyone was.

**The neobank did not build this tool. It found it.** Chime, founded in 2012 by Chris Britt and Ryan King, has partnered with The Bancorp Bank since 2013. Today its accounts are provided by The Bancorp Bank, N.A. and Stride Bank, N.A. Chime's 2025 IPO prospectus is plain about the economics. Interchange-based "payments revenue" was 80% of revenue in 2022 and 2023 and 76% in 2024. Debit interchange alone was 63%, 61% and 55%. And the business depends "in part on the maintenance of our bank partners' qualification for the small issuer exemption."

That is why the sponsor-bank model has the shape it does. It is not mainly a licensing shortcut. It is how a technology company gets an exempt bank's interchange rate onto its own card.

## What It Cost

**The exemption rewards the bank for staying small, and the neobank's success makes it bigger.** Chime's prospectus admits that its own growth "could itself put pressure on our bank partners' ability to qualify." A neobank that succeeds pushes its sponsor toward the $10 billion line. So it spreads across several banks, each with its own compliance regime and reporting format.

It also fixed the unit of revenue as the *swipe*. A neobank is paid only when a customer spends, so it competes for primary accounts, where paychecks arrive and wages are spent. It opens them by the million, through a phone, with no branch visit. The account that must be won quickly is also the account that must be frozen quickly when it looks wrong. A company earning cents a swipe cannot pay a person to look closely at every freeze.

## What You Still Touch

The line "Banking services provided by The Bancorp Bank, N.A. or Stride Bank, N.A.; Members FDIC" at the bottom of a neobank's app is the Durbin exemption made visible. It names the small bank whose rate the product runs on.

- [[problems/neobanks/low-impact-1|🟡 Sponsor Bank Compliance Reporting]] — one pack per sponsor, because one sponsor is never enough
- [[problems/neobanks/high-impact|🔴 The Account Freeze Nobody Grades]]
- [[niches/neobanks/deposit-and-interchange-economics/profile|Deposit & Interchange Economics]]
- [[niches/neobanks/sponsor-bank-compliance/profile|Sponsor Bank Compliance]]
- [[niches/neobanks/ongoing-account-risk/profile|Ongoing Account Risk]]

**Sources:** Wikipedia, *Durbin amendment* (15 U.S.C. § 1693o-2; enacted with Dodd-Frank 21 July 2010; Regulation II final 29 June 2011, effective 1 October 2011; 21¢ + 0.05% cap, one-cent fraud adjustment; $10 billion exemption); Chime Financial, Inc., Form S-1 filed with the SEC 13 May 2025 (founded 2012; co-founders Christopher Britt and Ryan King; Bancorp partnership since 2013; bank partners Bancorp and Stride; payments-revenue and debit-interchange shares for 2022–2024; small-issuer-exemption risk factors, quoted); 15 U.S.C. § 1693o-2 via Cornell LII (text checked for "reasonable and proportional" and the $10,000,000,000 threshold; source credit Pub. L. 111–203, title X, § 1075, 21 July 2010). ⚠️ **Not established:** the legislative record of *why* the line was drawn at $10 billion. The "protect small banks" reading is the conventional one and follows from the text, but I did not check it against the Congressional Record or Durbin's floor statements; the session's web-search budget was exhausted. The link from interchange economics to freeze volume in *What It Cost* is my inference, grounded in the vault's own problem notes, not in any source.
