# Lineage: Crypto Exchanges

**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the Chainalysis address cluster: Bitcoin addresses grouped into one entity by the common-input-ownership heuristic, labelled with the service behind them and scored for risk, sold to exchanges to screen deposits
**Builder:** Chainalysis
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

An exchange takes deposits from strangers and has to answer for where the money came from.

On 18 March 2013 FinCEN's guidance FIN-2013-G001 said that anyone who buys or sells convertible virtual currency is a money transmitter. That brought exchanges under the Bank Secrecy Act, with its duty to know customers and report suspicious activity. A bank can meet that duty because a wire arrives carrying a sending institution and a name. A Bitcoin deposit arrives carrying an address: a hash with no name, no institution and no history the exchange can read.

The paradox is that the whole history is public. Every transaction since January 2009 sits in the ledger. The missing thing was never data. It was a way to turn millions of anonymous addresses into a smaller number of *parties*.

## What Got Built

Two moves, one on top of the other.

**Clustering.** Satoshi Nakamoto's whitepaper admitted the weakness itself: multi-input transactions "necessarily reveal that their inputs were owned by the same owner." Merge every address ever spent together in one transaction, and a scatter of addresses collapses into one wallet.

**Labelling.** A cluster is still anonymous until one of its addresses is tied to a known service. Then the label spreads to the whole cluster. The academic proof came at IMC 2013 in Barcelona, in *A Fistful of Bitcoins* by Sarah Meiklejohn and colleagues at UC San Diego and George Mason. They bought goods and made deposits at services including Mt. Gox and Silk Road to learn their addresses, then clustered outward: "if we labeled one public key as belonging to Mt. Gox, we can now transitively taint the entire cluster."

Chainalysis turned that method into a product: a continuously updated database of clusters and labels, with a risk score on each deposit address, which a compliance team can call before crediting a customer.

## Who Built It, And Why Them

Chainalysis was founded in 2014 by Michael Gronager, Jan Møller and Jonathan Levin. It grew out of the Mt. Gox collapse.

Mt. Gox suspended trading on 24 February 2014 and filed for bankruptcy in Tokyo four days later, having lost about 850,000 bitcoins. Gronager was then chief operating officer of Kraken, and Kraken was later appointed by the bankruptcy trustee to help process the claims of Mt. Gox's roughly 127,000 creditors. **The first job was forensic: follow stolen coins through a public ledger to where they ended up.**

That is why the builder came from inside an exchange rather than from a bank-compliance vendor. The people who knew how exchanges' wallets actually behaved (hot wallets, deposit-address rotation, the change outputs that clustering relies on) were exchange operators. And one fact made it a business: **the places where criminal coins become cash are the same few exchanges.** A label on one exchange's deposit addresses is worth something to every other exchange, and to the FBI, DEA and IRS Criminal Investigation, which became customers too.

## What It Cost

The heuristic gives a guess of ownership, not proof of it. A shared-spend transaction such as a CoinJoin merges strangers into one "entity", and a missed change address splits one owner into two. Every error spreads through the label.

The larger cost is structural. **An exchange that freezes a deposit on a vendor's score almost never finds out whether the funds were really criminal.** The customer disputes it or disappears. Law enforcement rarely reports back. The score is never graded against an outcome. The exchange has bought a label it cannot audit, and the vault's own problem note records that the precision of this control has never been measured.

## What You Still Touch

Every deposit screen at a US exchange starts from the question Chainalysis made answerable: *whose cluster is this address in?* The answer still comes back as a score, not a verdict.

- [[problems/crypto-exchanges/high-impact|🔴 Deposit Screening Without Ground Truth]]
- [[problems/crypto-exchanges/worker-life-1|🟢 The Transaction Monitoring Analyst Tracing Hops]] — Gronager's 2014 forensic job, now a daily queue
- [[niches/crypto-exchanges/address-attribution/profile|Address Attribution & Taint Propagation]]
- [[niches/crypto-exchanges/screening-decision-quality/profile|Screening Decision Quality]]
- [[niches/crypto-exchanges/cross-exchange-attribution/profile|Cross-Exchange Attribution]]

**Sources:** FinCEN, FIN-2013-G001, *Application of FinCEN's Regulations to Persons Administering, Exchanging, or Using Virtual Currencies* (18 March 2013); S. Nakamoto, *Bitcoin: A Peer-to-Peer Electronic Cash System*, §10 Privacy (quotation checked against bitcoin.org/bitcoin.pdf); Meiklejohn, Pomarole, Jordan, Levchenko, McCoy, Voelker, Savage, *A Fistful of Bitcoins: Characterizing Payments Among Men with No Names*, IMC '13, Barcelona, 23–25 October 2013 (quotation checked against the UCSD PDF); Wikipedia, *Chainalysis* (founded 2014; Gronager, Møller, Levin; origin in Gronager's Mt. Gox investigation while at Kraken; federal agency customers); Wikipedia, *Mt. Gox* (suspension 24 February 2014, filing 28 February, ~850,000 BTC, Kraken's appointment reported January 2015, 127,000 creditors); chainalysis.com company page (2014 founding only). ⚠️ **Not established:** launch dates for Chainalysis Reactor and for its deposit-screening product KYT ("Know Your Transaction"). Neither Wikipedia nor the company page gives them, and the session's web-search budget was used up before other sources could be checked. The note therefore describes the product's function but does not date it. Also not established: who first applied the multi-input heuristic in print before 2013. The IMC paper cites earlier clustering work, which I did not trace.
