# History: Payment Fraud Vendors

**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Primary Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**Secondary Wave:** [[series/eras/wave-01-mainframe-batch|1 — Mainframe & Batch]]
**Origin Parent:** [[origins/credit-bureaus/profile|Credit Bureaus]] *(see "The Origin Parent, Made Explicit," below — this link is not in `origins/credit-bureaus/legacy.md`'s own inheritance table, and this file adds it on the strength of a direct, named technical lineage rather than treating the absence as final)*
**Episode Tier:** 1
**Transferable Pattern:** Whenever a model's two error types are paid for out of two different budgets, the organisation will drift toward whichever error is invisible to the person making the call — not because anyone chose that outcome, but because nobody is accountable for the loss they cannot see.

## Before the Merchant Carried the Risk Alone

**Fair Isaac Corporation**, founded in 1956 by engineer Bill Fair and mathematician Earl Isaac, sold its first credit scorecards to lenders in 1958 and debuted the general-purpose, bureau-wide consumer FICO score in 1989 — the full lineage is [[origins/credit-bureaus/profile|this vault's own credit-bureaus origin]]. The same company built the next generation of the same idea for a different decision: **Falcon**, one of the earliest market entrants in automated card-fraud detection, applying neural-network scoring to card-present transactions from the early 1990s, per the sources checked for this file. This is the same institution, the same underlying statistical technology — a scorecard trained on outcomes to rank a decision by risk — retargeted from "will this person repay a loan" to "is this specific card transaction fraudulent."

What Falcon and its issuer-side peers did not cover is the harder half of the problem. Falcon scored transactions on behalf of **card issuers**, who could draw on the cardholder's own credit history, prior transaction pattern and account tenure. A **merchant** selling goods online had none of that. It saw a card number, a shipping address and a device, and if the transaction it approved turned out to be fraudulent, the network's rules left the loss with the merchant — chargeback fees, the cost of goods already shipped, and, past a threshold, enrolment in a card network's excessive-chargeback monitoring programme. **The entire commercial existence of the "chargeback guarantee" product this file describes below only makes sense against that liability allocation** — nobody would buy a guarantee against a cost they did not already bear.

## The Origin Event — a Displacement, Not a Single Founding

There is a real, dated trigger here, though it did not create the merchant-side vendors so much as force a decade of scaling on them. **EMV chip liability shifted in the United States on 1 October 2015** — Visa, Mastercard and American Express all moved to the same effective date for point-of-sale terminals — pushing the liability for **card-present** counterfeit fraud onto whichever party (issuer or merchant) had not upgraded its hardware. Chip cards are cryptographically much harder to counterfeit at a physical terminal, and fraud that had run through cloned magnetic stripes did not disappear; per the sources checked, it **migrated to card-not-present channels** — online, phone and mail order — which EMV does nothing to protect, and which the same sources describe as already accounting for at least half of all documented card fraud even before the shift completed.

**Signifyd, founded in 2011 by Raj Ramanand and Mike Liberty — both former PayPal risk specialists** — and **Forter, founded in 2013 by Michael Reitblat, Liron Damri and Alon Shemesh**, both predate the 2015 liability shift. Neither vendor was created by EMV. What EMV did was hand both companies, and the category generally, an accelerant: a large, sudden, well-documented redirection of fraud into precisely the channel — online, card-not-present, no chip to read — that only a merchant-side, behavioural-and-device-signal vendor could address at all, because there was no physical card present for a chip to protect in the first place.

## What Became Cheap

**Running a large statistical ensemble over device, behavioural and network signals, in real time, at the price a small-to-mid-sized online merchant could afford.** Before this category existed as a bought product, that capability lived only inside issuers and the largest card networks, built on infrastructure that took decades to accumulate. [[series/eras/wave-07-big-data|Wave 7's]] general story — commodity storage and compute making population-scale modelling affordable outside the institutions that used to have exclusive access to it — plays out here as literally as anywhere in this vault: a merchant with no data-science team and no bureau relationship can now buy, by the transaction, a decision that FICO-grade modelling used to require owning outright.

## How It Was Actually Solved

This is worth explaining precisely, because the mechanism is a genuinely hard, genuinely well-taught modelling problem, not a marketing abstraction.

A fraud-decisioning model scores a transaction using device fingerprinting, behavioural biometrics (typing cadence, mouse movement, session velocity), email and phone intelligence, IP and proxy detection, and — the durable moat in this category — **consortium data**: the same device, email or card fingerprint appearing across many unrelated merchants who share signal through the vendor, which no single merchant could ever assemble alone. The model outputs a risk score; a merchant-configurable rule layer sits above it for hard blocks and allow-lists; and, above a confidence threshold neither side is fully certain of, a **manual review analyst** makes the final call, in this vault's own words for the industry, "in under a minute."

The training label is where the honesty of this mechanism actually lives, and it is structurally compromised in a specific, teachable way. A model only receives a label — fraud, or not fraud — for transactions that were **approved**. A declined transaction produces no outcome at all: the merchant never learns whether that customer would have paid, gone elsewhere, or was in fact the fraudster the model suspected. And even the labels that do arrive are a lagging, imperfect proxy: a chargeback can mean genuine fraud, or it can mean a legitimate customer who forgot a recurring subscription and disputed it rather than cancelling it. **The model is trained on approvals, labelled by chargebacks, and then evaluated on exactly that same self-selected population** — which makes every accuracy figure a vendor publishes a true statement about a population the model itself chose, not a statement about the transactions it declined.

## The Trade-Off, Properly Named

The decision a fraud model makes has two error types, and — this is the part worth teaching carefully — **the two costs are paid by different people, which is why the trade-off persists uncorrected.**

A **false positive** — a good customer wrongly declined — costs the merchant a sale, and per this vault's own analysis of the category, false declines are estimated to exceed actual fraud losses by a wide margin across card-not-present commerce generally, "largely without being measured directly." That cost lands on **revenue and marketing**: a customer who does not return, invisible in any fraud report, because a decline produces no fraud-team ticket.

A **false negative** — fraud wrongly approved — costs the merchant a chargeback, a fee, and, past a threshold, exposure to a card network's chargeback-monitoring programme. That cost lands on **risk and finance**, is booked, dated, and appears on a dashboard the same afternoon.

**One error is counted and owned. The other is uncounted and owned by no one.** A risk strategist tuning the model's threshold is, structurally, tuning against the visible cost and not the invisible one, because only the visible cost will ever generate a complaint. This vault's own note on the industry names the honest fix directly: a small, continuously run randomised approval allowance on transactions the model would otherwise decline would produce unbiased labels in exactly the region the model is weakest, and would let an organisation see, for the first time, the true rate and cost of its own false declines. **Almost nobody runs it, for the same reason few institutions in this vault's other files ever measure their own declined join: the cost of finding out is immediate and visible, and the bias it would correct is permanent and invisible — and an organisation under no external pressure to look will not volunteer to.**

## Why There Is No Graveyard Here

Unlike Wirecard in [[history/payment-processors|payment processors]] or the Hadoop distributions in Wave 7's own file, this category records no comparable corpse in the sources checked for this file. Signifyd's own funding history — from a $2M seed round in 2012 to a $205M round in 2021 at a $1.34B valuation — describes sustained growth, not a shakeout. **This is a category that has consolidated by acquisition and by scale rather than by anyone's documented collapse**, and this file records that absence rather than inventing a fight to fill it.

## The Origin Parent, Made Explicit

`origins/credit-bureaus/legacy.md` lists lending marketplaces, BNPL providers, collections agencies, mortgage brokers, credit unions and independent insurance agents as its direct children. Payment fraud vendors are not on that list. **This file adds the connection anyway, on the strength of a link the legacy file's own inheritance table does not need to spell out because it is closer than inheritance: Fair Isaac Corporation is the same institution behind both the 1956 lending scorecard and the early-1990s Falcon fraud model.** The technique — a statistical score trained on historical outcomes, standing in for a human's individual judgement of a stranger — travelled from "will this person repay" to "is this transaction real" inside one company, not across an industry boundary. Where the credit-bureau lineage differs, and differs sharply, is the label: a lender eventually learns whether a loan was repaid. A fraud model, as this file's own mechanism section describes, frequently never learns anything about the transactions it was least sure of.

## What's Still Open

- [[problems/payment-fraud-vendors/high-impact|🔴 The Declines Nobody Ever Grades]] — the missing counterfactual this file traces to the training label itself
- [[problems/payment-fraud-vendors/worker-life-2|🟢 The Risk Strategist Tuning Blind]]
- [[problems/payment-fraud-vendors/worker-life-1|🟢 The Manual Review Analyst at Forty Seconds a Case]]
- [[niches/payment-fraud-vendors/counterfactual-labels/profile|Counterfactual Labels]] — the randomised-approval fix this file names and almost nobody runs
- [[niches/payment-fraud-vendors/good-customer-recovery/profile|Good Customer Recovery]] — the false-positive side nobody's dashboard shows
- [[niches/payment-fraud-vendors/consortium-signal-sharing/profile|Consortium Signal Sharing]] — the durable moat this file's mechanism section names
- [[niches/payment-fraud-vendors/decision-modelling/profile|Decision Modelling]]
- [[niches/payment-fraud-vendors/merchant-onboarding-cold-start/profile|Merchant Onboarding & Cold Start]]

## The Transferable Pattern

> **Find the two error types a decision can make, then find out who is billed for each one. If the two bills go to different people or different teams, the decision will be biased toward whichever error its own owner cannot see — and no amount of model improvement fixes that, because the model is not the thing that is miscalibrated. The accounting is.**

This is the sharpest version, in this whole vault, of a shape that recurs constantly and is rarely named this cleanly: [[history/dental-practices|dental practices]] found a governing number nobody had standing to revisit; [[history/payment-processors|payment processors]] found two clocks nobody had reason to join. Here, the two things that need joining are not systems or dates — they are two ledgers, held by two different teams, both correct in isolation, and the joining of them is the entire unsolved problem. An FDE who proposes a better fraud model without first asking who owns the false-decline number is proposing to improve a system whose actual defect is organisational, not statistical.

**Sources:** Wikipedia, *FICO* (1956 founding, Bill Fair and Earl Isaac; first scorecards 1958; general-purpose FICO score 1989); Wikipedia, *Credit card fraud* (Falcon as an early-1990s market entrant in neural-network card-fraud detection; card-not-present fraud share); Wikipedia, *EMV* (US liability shift, 1 October 2015, Visa/Mastercard/Amex; CNP fraud migration post-EMV); Wikipedia, *Signifyd* (2011 founding, Raj Ramanand and Mike Liberty, ex-PayPal; funding history 2012–2021); Wikipedia, *Forter* (2013 founding, Michael Reitblat, Liron Damri, Alon Shemesh); Wikipedia, *Chargeback* (dispute mechanism, reason codes, ~21% of chargebacks decided for the merchant globally); this vault's `origins/credit-bureaus/profile.md`, `the-mechanism.md`, and `legacy.md`; this vault's `history/payment-processors.md`; this vault's `industries/payment-fraud-vendors.md`.
