# Consent Withdrawn and Nobody Downstream Knows

**Niche:** [[niches/data-marketplace-brokers/provenance-and-consent-evidence/profile|Provenance & Consent Evidence]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** An individual withdraws consent or exercises a deletion right at the original collector, and the copies already sold to eleven buyers carry on being used because nothing propagates the withdrawal.
**Tags:** #compliance #data-integration #graph-theory #automation #workflow-orchestration #evaluation-metrics #quick-win #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to replace a contractual warranty about lawful collection with evidence a buyer can rely on — and whoever does that takes the account, because the buyer now carries the regulatory risk and a warranty does not discharge it.

## The Problem
A person exercises a deletion right with the company that collected their data. That company removes them. The dataset containing their record was sold eleven times over two years, licensed onward by three of those buyers, and incorporated into two derived products. None of those copies change. The obligation the original collector discharged is not discharged anywhere else, every downstream holder is now processing data they should not be, and none of them know. The market's copying model has no reverse channel, and the regulatory framework assumes one exists.

## Why It's Still Broken
Propagating a withdrawal requires knowing who holds copies, which requires a chain nobody maintains. It also requires downstream holders to act, which costs them and benefits them not at all. Delivery is one-directional by design, and adding a reverse channel means maintaining a relationship after the transaction. The regulatory expectation is clear in principle and unenforced in practice against downstream holders, which removes the pressure. And nobody wants to be the party that builds the mechanism that then demonstrates how often it is needed.

## What a Fix Looks Like
Build the reverse channel. Maintain a downstream register of who holds which dataset version, which is the precondition and is a natural by-product of the chain-of-custody work — without it no propagation is possible at all. Publish suppression lists that downstream holders check, using hashed identifiers so the list itself discloses nothing, which is the mechanism that makes propagation practical and is already understood from adjacent marketing practice. Make suppression checking a contractual obligation with a defined cadence, since voluntary checking will not happen. Propagate through derived products, which is the hardest case and the one where the individual's data persists longest. Report propagation rates, so a provider can tell a regulator what fraction of downstream holders actually suppressed and the number stops being an assumption. Support record-level provenance so a withdrawal can be traced to every copy rather than invalidating a whole dataset. Handle the model training case honestly, since a model trained on withdrawn data cannot be untrained and the correct response is disclosure and a retraining commitment rather than silence. And make the obligation flow with the data in the licence terms, so onward licensing does not break the chain.

## Who Feels the Pain
The individuals whose exercised rights stop at the first company; downstream holders processing unlawfully without knowing; and the providers whose compliance evaporates the moment their data is resold.

## Impact If Fixed
The market's copying model has no reverse channel and the regulatory framework assumes one. Hashed suppression lists with a contractual checking cadence make propagation practical, and reported propagation rates turn an assumption into a measurement.
