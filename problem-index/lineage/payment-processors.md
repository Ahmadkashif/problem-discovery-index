# Lineage: Payment Processors

**Industry:** [[industries/payment-processors|Payment Processors]]
**Wave:** [[series/eras/wave-01-mainframe-batch|1 — Mainframe & Batch]]
**The tool:** the magnetic stripe on a payment card, and the ABA Track 2 record encoded on it
**Builder:** IBM
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Asking whether a card was good cost a phone call.

Through the 1960s a merchant ran a card through a manual imprinter, pressing the embossed digits onto a paper slip. That captured the number. It did not say whether the account had money, or had been stolen the previous week.

So the networks set a **floor limit** — typically around $50. Below it the merchant took the card on faith. Above it a clerk phoned a toll-free number and waited for a human at the issuing bank while the customer stood there.

**An authorisation therefore had a marginal cost measured in minutes of two people's time.** Below the floor limit the cost of asking exceeded the expected loss from not asking, so nobody asked — and organised card fraud lived underneath the threshold, one $49 purchase at a time.

## What Got Built

A strip of magnetic tape, hot-stamped onto the back of a plastic card, carrying a machine-readable copy of the account number.

**Track 2 — the track the American Bankers Association specified for financial transactions — is tiny and numeric-only:** roughly 40 characters at 75 bits per inch, five bits per character. Primary account number, expiry, service code, discretionary data, nothing else. That parsimony is not aesthetic. It is the price of a 1970s leased line and of a terminal cheap enough to sit on a counter.

The stripe alone is inert. What made it matter was the **cheap terminal that could read it and dial out** — a card a machine could read, paired with a network that could answer. Visa's predecessor, National BankAmericard Inc., brought its electronic authorisation system up in the mid-1970s, and together the two halves drove the cost of asking "is this card good?" from a phone call toward a fraction of a cent.

## Who Built It, And Why Them

IBM, and the reason is manufacturing rather than finance.

Forrest Parry, an IBM engineer, made the first working card in 1960 for a US government identity-badge project. The origin story is well attested and slightly domestic: his adhesive kept warping the tape until his wife Dorothea suggested pressing it on with a clothes iron.

But a prototype is not a product. The real work ran at **IBM's Information Records Division in Dayton, New Jersey, from 1969** — roughly two years on how to hot-stamp a stripe onto plastic so it survived a wallet, and how to encode it reproducibly at volume.

**That is why it was IBM and not a bank.** The binding constraint was never the idea; it was tolerances, adhesion and yield across hundreds of millions of identical units. Banks had the problem and the distribution. Only a manufacturer with magnetic-media expertise had the process.

## What It Cost

**The stripe authenticates nothing.** It is a static secret that the card broadcasts to any reader that asks, and a copy of it is indistinguishable from the original.

That was an acceptable trade when the reader had to cost almost nothing and the alternative was a phone call. It became the foundation of card-present fraud for the next forty years, and EMV chips exist to undo precisely this decision — replacing a replayable constant with a per-transaction cryptogram.

The subtler cost: Track 2's fields were so cheap to carry that they became the permanent vocabulary of payments. Message formats still negotiate around a record designed for a leased line nobody uses.

## What You Still Touch

Your $2 coffee gets authorised. Every transaction now asks the issuer regardless of size, because the floor limit died the moment asking became free and nothing replaced it.

That is also why authorisation is a *rate* rather than a yes: once every transaction is a question, the share coming back wrongly refused becomes a business problem nobody owns.

- [[problems/payment-processors/high-impact|🔴 Authorisation Rate as an Unmeasured Decision]] — the direct descendant of making the question free
- [[niches/payment-processors/authorisation-performance/profile|Authorisation Performance]]
- [[niches/payment-processors/decline-recovery/profile|Decline Recovery]]
- [[niches/payment-processors/fraud-and-chargeback-decisioning/profile|Fraud & Chargeback Decisioning]] — the bill for the stripe's missing authentication

**Sources:** Wikipedia, *Forrest Parry*, *Magnetic stripe card*, *Floor limit*; historyofinformation.com on IBM's first magnetic-stripe transaction tests and the Information Records Division's 1969 industrialisation programme; this vault's `history/payment-processors.md` and `origins/retail-banking/` (cited as vault material, not as independent corroboration). ⚠️ **Not established:** a precise date for the ABA's adoption of Track 2 — widely given as 1971, but I could not confirm it against a primary ABA or ISO source this session; treat the year as unverified. NBI's electronic authorisation system is dated here only to "the mid-1970s" for the same reason — secondary accounts place it around 1973–1975 and disagree.
