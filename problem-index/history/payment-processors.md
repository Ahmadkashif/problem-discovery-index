# History: Payment Processors

**Industry:** [[industries/payment-processors|Payment Processors]]
**Primary Wave:** [[series/eras/wave-01-mainframe-batch|1 — Mainframe & Batch]]
**Secondary Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**Origin Parent:** [[origins/retail-banking/profile|Retail Banking]]
**Episode Tier:** 1
**Transferable Pattern:** A real-time prediction layer bolted onto an inherited overnight batch clock will look, from the inside, like a configuration problem — because the architecture that separates the decision from its outcome was never built to join the two.

## Before

A merchant took a card on faith, a phone call, or a printed booklet. Diners Club (1950) and American Express (1958) proved a charge card could work as a product, but nothing about their early operations was computed in the sense this vault means it. A cashier pressed a card into a knuckle-buster imprinter, took an impression of the embossed numbers onto a paper slip, and — above a "floor limit" set by the merchant's own risk tolerance — telephoned an operator to check the account by hand. Merchants below the floor limit simply trusted the plastic. Above it, someone read the account number off a paper bulletin of stolen and delinquent numbers, updated every week or two and already out of date the day it arrived.

This is worth stating precisely because it is the exact shape of the constraint that opened [[series/eras/wave-01-mainframe-batch|Wave 1]] elsewhere: a business could not consult its whole customer file at the moment of a transaction, so it consulted a stale sample — a floor limit, a printed list — and ate the resulting fraud as a cost of doing business.

## The Origin Event

**Bank of America launched BankAmericard on 18 September 1958**, in Fresno, California, by mailing 65,000 unsolicited, already-active credit cards to residents — the so-called "Fresno Drop." By October 1959 California was saturated: over two million cards, accepted by 20,000 merchants. The programme first turned a profit in May 1961.

This is a card *product* launching, not a computing system, and the distinction matters for this file. BankAmericard's genuinely computational moment came later and in two separate places. First, the card itself had to become machine-readable — IBM engineer Forrest Parry's magnetic-stripe work from 1960 onward, refined through the decade, standardised by the American Bankers Association as Track 2 and folded into what became the ISO 7811 family of card standards by the early 1970s. This is the same manoeuvre [[origins/retail-banking/the-mechanism|MICR]] made for the cheque three years earlier: pre-print a machine-readable layer onto a document a customer physically handles, without asking the customer to change anything. Second, verifying a card had to move from a phone call and a paper bulletin to a query against a live file — the same "single authoritative copy, read by many distant terminals" problem [[origins/airlines/origin-story|SABRE]] solved for seat inventory in the same decade.

Bank of America relinquished direct control of the card programme in June 1970, spinning it out as the independent National BankAmericard Inc. (NBI). The international licensees unified under a new name on 16 December 1976: **Visa**. Interbank Card Association, the rival network that became Mastercard, was organised over the same years by a competing group of banks that did not want to license BankAmericard.

> **What I could not verify.** Payments-industry retrospectives commonly date NBI's first electronic authorisation system, BASE I, to 1973, and describe it as the moment card verification moved from telephone and paper to a real-time network query. I could not confirm this date against a primary source in this session. Treat 1973 as a widely repeated but unverified figure, not a fact to script from.

## What Became Cheap

**Knowing, in seconds, whether a card is good — without a phone call.** That is the entire authorisation layer this industry now runs, and it is a genuinely different achievement from anything Wave 1 elsewhere in this vault produced. Retail banking's ERMA and the airlines' SABRE both made an *internal* file consultable in real time. Card authorisation made an *external counterparty's* file — the issuing bank's, not the merchant's, not the network's — consultable in real time, across every merchant in the country, for a transaction that had to clear in the time a cashier stands at a till.

## How It Was Actually Solved — and Where the Split Was Built In

Here is the mechanism, and it is the reason this industry's own hub note reads the way it does.

Card **authorisation** became a real-time network query: the merchant's terminal or gateway asks the network, the network asks the issuer, the issuer's risk model answers in under a second, and the merchant is told yes or no. This is genuinely new infrastructure, built on top of Wave 1's foundations rather than inherited from them.

Card **settlement** — the actual movement of money from the cardholder's bank to the merchant's account — was not rebuilt. It rides the same overnight batch rails [[origins/retail-banking/the-mechanism|retail banking]] laid down for cheque clearing, because that infrastructure already existed and building a second national funds-movement network from scratch made no sense once one existed. Transactions authorised throughout the day are batched, submitted, and cleared that night or the next business day, through mechanisms that ultimately depend on the same Federal Reserve and ACH machinery [[origins/retail-banking/origin-story|retail banking's origin story]] describes.

**The result is a system with two clocks that were never designed to talk to each other.** The authorisation decision — should this specific decline be retried, through which route, on what schedule — happens in milliseconds. The record of what actually happened to the money lands in a settlement file one or two days later, in a different system, produced by an inherited batch process that has no concept of "decision" at all; it only has a concept of "transaction." This vault's own hub note for this industry states the consequence without needing to know the ancestry: *"the outcome of that prediction lands in a settlement file two days later in a different system."* [[origins/retail-banking/legacy|Retail banking's legacy file]] names this industry as the exemplar of the missing join it manufactured in 1959, and this file is the confirmation: the split was never a design decision made about card payments specifically. It is Wave 1's batch clock, still running, underneath a Wave 6 SaaS-era analytics layer that was built without knowing the clock was there.

> **Corrected here explicitly, because the vault has recorded this myth being caught before:** the settlement lag in payments is not "T+2." T+2 is a securities-settlement term (US equities moved to T+1 in May 2024) and has never applied to card or ACH timing. The lag here is the overnight batch window, inherited, not chosen, for this transaction type specifically.

## The Binding Constraint

**Regulation II**, the Federal Reserve's rule implementing the **Durbin Amendment** (signed into Dodd-Frank on 21 July 2010, effective 1 October 2011), caps the interchange fee a bank can collect on a debit transaction at roughly 21–24 cents on a typical purchase, down from an industry average nearer 44 cents — a reduction estimated at $9.4B a year in bank revenue. It also did something with more lasting architectural consequence: it required that every debit transaction be routable over **at least two unaffiliated networks**, so a merchant's acquirer, not the card's issuer alone, gets to choose the cheaper path.

This is not a technical limit. It is a number and a rule, set by Congress and the Fed, and it is why "routing and network optimisation" exists as a commercial discipline at all rather than a fixed wire between merchant and issuer. A processor's routing engine is not free to pick the fastest or most reliable path; it is choosing among paths Congress mandated must exist, at a fee Congress mandated must be capped. No amount of modelling moves the 21-cent figure. It only decides how a fixed pool of routing options gets used inside it.

## The Graveyard

**Wirecard.** Founded in 1999 as a payment processor for online vendors (early clients included adult-content and gambling sites before a broader pivot from 2002), it reached the DAX — Germany's blue-chip index — in September 2018, reporting €2.02B in 2018 revenue and 5,300 staff. Financial Times reporting had questioned its accounting since 2015 and documented specific fraud allegations from 2016; the company denied all of it for years.

**On 18 June 2020, Wirecard disclosed that €1.9 billion supposedly held in escrow accounts in the Philippines did not exist.** The Philippine banks named confirmed they held no such funds. The stock fell 72% in two days. CEO Markus Braun resigned on 19 June and was arrested on fraud charges on 22 June. The company filed for insolvency on 25 June 2020. Santander bought the core European business out of the wreckage for €100M that November.

This is not a competitive fight in the American Airlines/People Express sense — nobody out-computed Wirecard. It is the payments industry's own instance of the vault's **declined join**: a company reporting numbers that a competent, independent audit would have caught years earlier, in an industry where the technical capability to reconcile a balance sheet against real cash positions has existed since Wave 1. The failure was not technological. Nobody built the check.

## What's Still Open

- [[problems/payment-processors/high-impact|🔴 Authorisation Rate as an Unmeasured Decision]] — the missing join this file traces to 1959
- [[niches/payment-processors/authorisation-performance/profile|Authorisation Performance]]
- [[niches/payment-processors/decline-recovery/profile|Decline Recovery]]
- [[niches/payment-processors/network-outcome-intelligence/profile|Network Outcome Intelligence]] — the cross-merchant signal no single issuer or merchant can see alone
- [[niches/payment-processors/routing-and-network-optimisation/profile|Routing & Network Optimisation]] — operating inside Regulation II's mandated choice set
- [[niches/payment-processors/fee-and-interchange-optimisation/profile|Fee & Interchange Optimisation]]
- [[niches/payment-processors/settlement-and-reconciliation/profile|Settlement & Reconciliation]] — proving the two clocks agree
- [[niches/payment-processors/merchant-underwriting/profile|Merchant Underwriting]] — every acquirer re-solving the same KYB problem alone

## The Transferable Pattern

> **Find the clock the industry inherited before it had a reason to choose one, then find the newer decision that was bolted on top of it without changing it. The gap between the two clocks is where the money leaks, and it will present itself as a data problem when it is actually an architecture problem nobody was empowered to fix.**

An FDE arriving at a payments business should ask, before anything else, which parts of the pipeline are real-time by design and which are still riding the overnight rail because nobody has had a reason — or the standing — to replace it. Authorisation answers in a second. Settlement answers tomorrow. The entire commercial opportunity in this industry lives in that gap, and it has lived there since 1959.

**Sources:** Wikipedia, *BankAmericard*, *Visa Inc.*, *Magnetic stripe card*, *Durbin Amendment*, *Wirecard*; American Bankers Association Track 2 / ISO 7811 standard history; Federal Reserve, Regulation II final rule (29 June 2011, effective 1 Oct 2011); Financial Times Wirecard investigation coverage (2015–2020); this vault's `industries/payment-processors.md` and `origins/retail-banking/` (origin-story, the-mechanism, legacy).
