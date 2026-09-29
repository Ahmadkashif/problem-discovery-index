# Address Attribution & Taint Propagation

**Parent Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this niche is fighting to say who actually controls an address and how far illicit taint legitimately travels through a public ledger — and whoever attributes most accurately, with a confidence they can defend, owns the input every downstream decision consumes.

## Profile
**Market Size:** ~$2.0B US
**Share of Parent Industry:** ~13% of category revenue
**Digital Adoption:** Medium — vendor graphs and heuristics
**Target Buyer:** Exchange compliance and data leadership
**Automation Potential:** Very High — a graph inference problem

## What Makes This a Distinct Niche
This contest is inference about the chain. An address is a string. Deciding that it belongs to a particular exchange, mixer, darknet market or sanctioned entity is an inference built from clustering heuristics, behavioural signatures and off-chain evidence. Deciding that funds three hops downstream are still tainted is a second inference, governed by propagation rules that are contested, largely undocumented and differ between vendors. Both are graph problems over public data, and neither is evaluation or adjudication.

## Current Tools & Gaps
Blockchain analytics vendors, clustering heuristics, address labels sold as a feed, and graph interfaces for tracing. The gaps: attribution bought rather than modelled; confidence not expressed; propagation rules opaque; the exchange's own deposit-and-withdrawal evidence — the ground source of most labels — not used; and no disagreement signal when vendors differ.

## Problems
- [[niches/crypto-exchanges/address-attribution/build|🔨 Build: Attribution With a Confidence]]
- [[niches/crypto-exchanges/address-attribution/buy|🛒 Buy: Entity Resolution and Graph Inference]]
- [[niches/crypto-exchanges/address-attribution/fix|🔧 Fix: Taint That Never Decays]]
