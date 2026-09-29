# Lineage: Embedded Finance Platforms

**Industry:** [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** Marqeta's Just-in-Time (JIT) Funding — a payment card that holds a zero balance until the moment of use, when the card network's authorisation request is forwarded to the program's own endpoint to approve and fund in real time
**Builder:** Marqeta
**Builder in vault:** [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
**Verification:** partial — see Sources

## The Problem That Came First

A software company that wanted to put a card in someone's hand could not decide what the card was allowed to buy.

A conventional card program was made by a bank and a processor. The bank decided at issuance who got a card and how big the balance or limit was. After that, every authorisation was the processor's call against that balance. The company paying for the spending, whether a delivery marketplace or an expense platform, had no part in the decision at the moment of purchase.

For some businesses that made the card impossible. A grocery-delivery shopper paying at a till needs exactly the amount of one customer's order, at one store, now, and nothing afterwards. Loading money onto thousands of workers' cards in advance ties up cash and invites misuse. Not loading them means the card is declined at the till.

## What Got Built

A card with nothing on it. When it is swiped, the authorisation travels from the merchant through the card network to Marqeta. Marqeta runs the program's spend controls (merchant, category, amount, time) and then sends a **funding request to an endpoint the customer runs**. The customer's system approves, declines or partially approves. If approved, Marqeta moves funds from the customer's funding source into the card account, and the approval goes back to the till.

The authorisation decision becomes an API call to the business paying for the spending. If the customer's endpoint cannot answer, a fallback Marqeta calls "Commando Mode" decides on preset rules.

Marqeta's 2021 prospectus gives the canonical case. Instacart shoppers carry zero-balance Marqeta cards, and each in-store transaction is checked against the customer's order and the store before any funds move.

## Who Built It, And Why Them

Marqeta was incorporated in 2010 and is headquartered in Oakland. Jason Gardner, its founder, tells the origin in his prospectus letter. At dinner in San Francisco in December 2009, shortly after leaving MoneyGram (which had acquired a company he co-founded), a friend holding a pocketful of Groupon coupons told him: "You're a payment nerd; find a way to put these on a card."

**That origin explains the shape.** The first problem was a merchant-specific offer that should be spendable in one place and not another. Solving it meant owning the authorisation step, not just printing cards. A bank had no reason to hand that step to its customers. A payments-processing specialist did: it could sell the decision as a feature.

The commercial proof was concentrated. Square accounted for 60% of Marqeta's net revenue in 2019 and 70% in 2020, and about 96–97% of its payment volume in those years settled through one issuing bank, Sutton Bank. The platform was infrastructure for a few large software companies, on a bank most of their users never heard of.

## What It Cost

**The card program stopped being the bank's product, and the bank stopped seeing it whole.** The issuing bank's name is on every card, but the spending rules, the approval logic and often the ledger of who owns which funds live in the program's code and the platform's. Gateway JIT customers, in Marqeta's own documentation, "manage your own ledger balances".

That split was tolerable while nothing broke. When the middleware provider Synapse filed for bankruptcy in April 2024, its partner bank Evolve froze withdrawals from the affected apps, and even after reconciliation tens of millions of dollars could not be accounted for. In June 2024 the Federal Reserve took enforcement action against Evolve. JIT Funding did not cause that. But it created the arrangement in which the rules, the money and the record of the money can sit in three different companies.

## What You Still Touch

A delivery driver's card that works only at the right restaurant, for the right amount, is a JIT authorisation.

- [[problems/embedded-finance-platforms/high-impact|🔴 Programme Oversight Without Programme Visibility]] — the bank sees API calls, not decisions
- [[problems/embedded-finance-platforms/low-impact-2|🟡 FBO Ledger Reconciliation]] — the Synapse failure mode
- [[niches/embedded-finance-platforms/ledger-integrity/profile|Ledger Integrity]]
- [[niches/embedded-finance-platforms/programme-configuration/profile|Programme Configuration]]
- [[niches/embedded-finance-platforms/bank-partnership-and-charter/profile|Bank Partnership & Charter Access]]

**Sources:** Marqeta, Inc., Form S-1 filed with the SEC 14 May 2021 (incorporated 2010, Oakland; founder letter with the December 2009 origin; JIT Funding definition and "industry-first" claim; Instacart zero-balance example; Square at 60% and 70% of net revenue in 2019 and 2020; Sutton Bank at ~97% and 96% of TPV); Marqeta developer documentation, *About JIT Funding* (gateway flow, "Commando Mode", customer-managed ledger balances); Wikipedia, *Evolve Bank & Trust* (Synapse bankruptcy April 2024, withdrawal freeze, unreconciled funds, Federal Reserve enforcement June 2024). ⚠️ **Not established:** the year JIT Funding launched, and whether any processor offered real-time program-controlled funding before Marqeta. The prospectus calls it "industry-first", which is the company's own claim. Marqeta has no Wikipedia article, and the session's web-search budget was used up before other sources could be checked. The friend's surname and the company Gardner co-founded that MoneyGram bought are not named in the prospectus, and I have not supplied them.
