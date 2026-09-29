# Lineage: Payment Fraud Vendors

**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**The tool:** Falcon — HNC Software's neural-network card fraud detection system, which scores every authorisation against a stored profile of that cardholder's behaviour and queues the suspicious ones to a fraud workstation
**Builder:** HNC Software
**Builder in vault:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Verification:** partial — see Sources

## The Problem That Came First

Once a machine could read a card, every purchase could be asked about. That is not the same as judged.

The magnetic stripe — see [[lineage/payment-processors|Lineage: Payment Processors]] — made authorisation cheap, but the stripe is a static secret: a copy is indistinguishable from the original. The issuer could confirm an account had credit, not that the person holding the card owned it.

The defences an issuer had were blunt. HNC's own 1997 annual report lists what Falcon competed against: card activation programmes, cards carrying the holder's photograph, smart cards and "other card authorization techniques." Every one of them works on the *card*. None looks at the *behaviour*.

The information that could separate them — this cardholder never buys petrol at 3am in another state — was sitting in the issuer's transaction history, unread at the moment of decision.

## What Got Built

Falcon, which HNC's 1997 10-K calls "the Company's first predictive solution product": a credit and debit card fraud detection system "for monitoring individual credit card accounts."

The filing describes five parts, and the shape is the point: **an interface into the customer's legacy system, a decision engine, a cardholder profile database, a case management database and a fraud workstation.** The neural network examined "transaction, cardholder and merchant data." The profile database is what made it different from a rule: each account carried a running summary of its own normal, and each new transaction was scored against it.

The output was a score, not a verdict. A rules layer — Falcon Expert — let fraud managers "define and deploy rules... creating or reopening cases based on Falcon transaction fields and/or the Falcon score." Humans at the workstation worked the queue.

By mid-2000 HNC said Falcon was contracted to monitor over 300 million payment card accounts, with 16 of the world's top 25 card issuers as customers. First Data and EDS were licensed as service bureaus, so smaller issuers could reach it through their processor.

## Who Built It, And Why Them

HNC was a neural-network company looking for a market, not a payments company looking for a model.

Robert Hecht-Nielsen and Todd Gutschow met in 1983, wrote a business plan over lunch in March 1986, and founded Hecht-Nielsen Neurocomputing Corp. in October 1986 on $500,000 from an angel investor, by the company's own account. The early revenue was Department of Defense contract work on neural-network decision support. Venture funding followed in 1987, and Robert North, formerly head of a TRW group, became CEO.

**That is why it was HNC and not a bank.** Card fraud offered the three things a neural network needed: a large volume of labelled examples (every chargeback is a fraud label), a decision repeated millions of times a day, and a pattern too diffuse for a hand-written rule. Issuers had the data but no modelling capability; HNC had the modelling and a defence-contract habit of building to someone else's spec. Falcon became the template: the 1997 10-K says HNC built ProfitMax, its credit-authorisation product, "by adapting the core technology developed for Falcon," and that Falcon was the majority of 1995 installations. HNC went public in 1995; Fair Isaac acquired it in 2002.

## What It Cost

**The model learns only from transactions it let through.** A chargeback exists only when an approved transaction is disputed. A declined transaction is never charged back, so its true label never arrives. Every threshold the issuer tightened removed exactly the borderline cases from the training data.

The score also replaced a rule a manager could read with a number nobody could explain; Falcon Expert let the rules back in on top.

## What You Still Touch

A card declined abroad, then a text asking "was this you?" — that is Falcon's architecture: a profile, a score, a threshold, a case queue.

- [[problems/payment-fraud-vendors/high-impact|🔴 The Declines Nobody Ever Grades]] — the label Falcon's design never collects
- [[problems/payment-fraud-vendors/worker-life-1|🟢 The Manual Review Analyst at Forty Seconds a Case]] — the fraud workstation, still staffed
- [[niches/payment-fraud-vendors/counterfactual-labels/profile|Counterfactual Label Acquisition]]
- [[niches/payment-fraud-vendors/consortium-signal-sharing/profile|Consortium Signal Sharing]]
- [[niches/payment-fraud-vendors/good-customer-recovery/profile|Good-Customer Recovery]]

**Sources:** WebSearch was unavailable this session (session cap reached); research was by direct fetch. HNC Software Form 10-K for fiscal 1997 (SEC EDGAR, filed 17 Feb 1998, accession 0000936392-98-000260; read directly: "first predictive solution product," five-part architecture, competing methods, First Data/EDS service bureaus, 1986 founding, June 1995 Delaware reincorporation) and Form 10-K for fiscal 2000 (accession 0000936392-01-000032; neural networks on transaction, cardholder and merchant data); hnc.com via the Wayback Machine — "HNC History" page, Dec 2001 (founders, 1983 meeting, March/October 1986, $500,000 angel, DoD contracts, 1987 VC, Robert North, 1995 IPO; nine of top ten Visa/MasterCard issuers, "300 of 500 million cardholders") and Falcon product page, June/Sept 2000 (300 million accounts, 16 of top 25 issuers, Falcon Expert, a vendor-claimed 20–60% detection improvement not repeated above); Wikipedia, *Robert Hecht-Nielsen* (Fair Isaac acquisition, 2002). These are HNC's own statements, not independent corroboration. ⚠️ **Not established:** Falcon's launch year — commonly given as 1992 or 1993, but no fetched primary source dated it; HNC's 2001 page says only "over the last ten years." The first issuer customer was not found. Nothing is asserted here about an issuer data consortium behind Falcon's early models, because I could not source one.
