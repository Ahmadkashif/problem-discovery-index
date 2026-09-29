# Lineage: BNPL Providers

**Industry:** [[industries/bnpl-providers|BNPL Providers]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** Afterpay's "pay in 4" — a purchase split into four interest-free instalments over six weeks, 25% at checkout, with the merchant paying the fee and the shopper paying nothing if on time
**Builder:** Afterpay
**Builder in vault:** [[industries/bnpl-providers|BNPL Providers]]
**Verification:** partial — see Sources

## The Problem That Came First

An online shop loses a large share of customers at the payment page, and a young customer without a credit card is often one of them.

Credit already existed for that customer, but it came with paperwork: Australia's National Credit Code, America's Regulation Z, and in both a regulated assessment and disclosure. A retailer wanting to offer "pay later" at checkout had to attach a lender, the lender had to run the regulated process, and the process cost time at the one moment in e-commerce when time costs the sale.

The question was how to lend small sums instantly, inside a checkout, without the paperwork.

## What Got Built

Four payments. The first, about a quarter of the price, is taken at checkout. The other three follow a fortnight apart, so the plan ends in six weeks. There is no interest. The merchant pays a fee on every sale. The shopper pays nothing more unless they miss a payment, and then pays a late fee.

Each number was chosen. **No interest and a term under 62 days** is what put Afterpay outside Australia's National Credit Code, which did not reach short-term credit carrying no interest charge. **Fortnightly** matches the pay cycle of the customers it was built for. **The merchant pays** because the merchant is the one buying something: a completed sale and a larger basket.

## Who Built It, And Why Them

Afterpay was founded in Sydney in 2014 by Nick Molnar and Anthony Eisen, neighbours in Rose Bay. Molnar sold jewellery online. Eisen had been chief investment officer at Guinness Peat Group.

**That pairing is why the product looks the way it does.** A merchant builds a lending product in which the lender's customer is the merchant: the shopper is the thing being delivered, and the fee is priced like a marketing cost, not an interest rate. An investment manager supplies the financing structure that makes a no-interest loan pay for itself from merchant fees. A bank prices lending on the borrower. This design removes exactly that price.

Afterpay reached the US in May 2018. There its four instalments met a line that had been drawn half a century earlier for a different reason. Regulation Z defines a creditor as a lender whose credit carries a finance charge *or* is payable in **more than four instalments**. The Federal Reserve Board wrote that four-instalment rule so merchants could not dodge disclosure by hiding interest inside the price. The Supreme Court upheld it in *Mourning v. Family Publications Service* (24 April 1973), a case about magazine subscriptions sold to a 73-year-old widow in 30 monthly payments. **Four instalments and no fee lands just under that line.** I found no source saying Afterpay designed for the US rule; the fit to Australian law is the documented reason.

## What It Cost

**Leaving out the lending process also left out the lending record.** A plan that avoids the regulated credit process also avoids most of what that process produces: the affordability assessment, the disclosures and, above all, the report to a credit bureau. Each provider sees its own plans. None sees the other five the same shopper opened that month.

The design also moved the risk to where it is hardest to price. With no interest income, losses have to be covered by merchant fees and late fees. That puts late fees and small-balance collections at the centre of the business, and it puts the provider between the shopper and the merchant whenever goods come back or never arrive.

## What You Still Touch

The four-payment button under a price is Afterpay's six-week, fortnightly schedule, now copied by its competitors. What it left behind is the record that was never kept.

- [[problems/bnpl-providers/high-impact|🔴 Underwriting Blind to Accumulation]] — every plan underwritten as if it were the only one
- [[problems/bnpl-providers/low-impact-2|🟡 Dispute and Refund Handling Under Reg Z]]
- [[problems/bnpl-providers/worker-life-1|🟢 The Collections Agent on a Ninety-Dollar Balance]] — the late fee as the business model's backstop
- [[niches/bnpl-providers/cross-provider-accumulation/profile|Cross-Provider Accumulation]]
- [[niches/bnpl-providers/the-consumer-with-six-plans/profile|The Consumer With Six Plans]]
- [[niches/bnpl-providers/returns-and-instalment-reconciliation/profile|Returns & Instalment Reconciliation]]

**Sources:** Wikipedia, *Afterpay* (founding October 2014, Molnar and Eisen, Rose Bay; four instalments over six weeks; merchant fees; late fees; exemption from the National Credit Code as no-interest credit repaid in under 62 days; US launch mid-May 2018; Block acquisition announced August 2021, completed 31 January 2022, A$39bn / US$29bn); 12 CFR § 1026.2(a)(17)(i), via Cornell LII (the "more than four installments" creditor definition); *Mourning v. Family Publications Service, Inc.*, 411 U.S. 356 (1973), via Cornell LII (decided 24 April 1973; the Board's evasion rationale; magazine subscriptions, $3.95 × 30). ⚠️ **Not established:** (1) whether Afterpay was the *first* to sell four fortnightly interest-free instalments. Klarna (founded 2005) and Affirm (2012) predate it with other products, and I did not check which pay-in-4 came first, so the note keys the builder of this specific schedule, not of BNPL. (2) Any evidence that Afterpay chose four instalments with Reg Z in mind. The fit is shown as a coincidence of two separately documented facts. (3) The dates of credit-bureau BNPL furnishing announcements and of the CFPB's 2024 BNPL interpretive rule and what happened to it. The session's web-search budget ran out before these could be checked, so the note does not date them.
