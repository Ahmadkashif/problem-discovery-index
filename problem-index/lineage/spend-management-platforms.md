# Lineage: Spend Management Platforms

**Industry:** [[industries/spend-management-platforms|Spend Management Platforms]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the Brex corporate card — a card issued to a company on its EIN, with no personal guarantee, whose limit is set from the company's cash balance, amount raised or revenue rather than a founder's credit score
**Builder:** Brex
**Builder in vault:** [[industries/spend-management-platforms|Spend Management Platforms]]
**Verification:** partial — see Sources

## The Problem That Came First

A new company could not get a company card.

Corporate cards were underwritten the way lending is underwritten: on a credit history. A venture-funded startup twelve months old has none. It may hold millions in the bank from its last round, but a bank's small-business card process looks for years of filed accounts, and where those are missing it falls back on the founder — a personal guarantee and a personal credit file behind a business card.

So the fastest-growing small companies in the economy paid for software, ads and travel on founders' personal cards and reimbursed through expense reports, or took a business card with a limit too small to be useful. **The constraint was not risk. It was that the data used to measure risk did not exist yet for this kind of company**, while the data that did exist — a large, visible cash balance — was not what the card issuers underwrote on.

## What Got Built

A corporate card that underwrites on the balance sheet it can see.

Brex applies against the company's EIN, requires no personal guarantee, and states that founders' personal credit "isn't used or reported." The limit is set "based on your company's financial profile, including revenue, amount raised, or cash balance, rather than a personal FICO score." Around the card the company later layered expense software — Brex Empower, launched April 2022, to help employees comply with expense policies — which is where the category now competes.

## Who Built It, And Why Them

Brex, founded on January 3 2017 by Henrique Dubugras and Pedro Franceschi, both 22 and both Brazilian.

**The founders were payments people before they were card people.** They had built and in 2016 sold Pagar.me, a Brazilian online payments company, to Stone. They entered Y Combinator's Winter 2017 batch with a different idea and, three weeks in, pivoted to credit cards for venture-funded startups with limited credit history.

That setting explains the artefact. Y Combinator is a factory for exactly the customer the banks could not underwrite: young companies with fresh funding and no history. Sitting inside it, the founders could see the whole population at once, and could see that its most reliable signal was the one a card programme could read directly — money in the bank, raised from named investors. An incumbent issuer had the balance sheet but a credit process built for established firms and personal guarantees; changing it for a small, new segment was not worth the risk to them. A startup with payments experience and a ready-made customer base could build the process around that one segment.

The model scaled into a spend platform, peaked at a $12.3 billion valuation in 2021, and in January 2026 Capital One acquired Brex for $5.15 billion.

## What It Cost

**A limit set from a cash balance moves with the cash balance.** Underwriting on current funds rather than on repayment history means the lender learns whether the customer pays only later, when a company burns down its round. The data that would correct the model arrives in collections, not in the underwriting system.

The segment itself proved costly: in June 2022 Brex exited the small and midsize business market to focus on enterprise customers. The card built for companies with no history became, a few years on, a product for companies that had one.

And because the card is monetised through interchange, control arrived as rules bolted around the card — limits, merchant categories, receipt thresholds — rather than as judgement.

## What You Still Touch

A startup employee who never fronted a flight on a personal card is using this design; so is the credit analyst setting a five-figure limit from a bank connection and a pitch deck.

- [[problems/spend-management-platforms/worker-life-2|🟢 The Credit Analyst Setting Limits on Twelve Months of History]] — the direct descendant of underwriting on cash
- [[problems/spend-management-platforms/high-impact|🔴 Policy That Never Learns From Its Own Exceptions]] — the rules layered around the card
- [[niches/spend-management-platforms/credit-underwriting/profile|Credit Underwriting]]
- [[niches/spend-management-platforms/spend-policy-and-control/profile|Spend Policy & Control]]

**Sources:** Wikipedia, *Brex* (founding January 3 2017, founders and ages, Pagar.me sale 2016, YC Winter 2017 and three-week pivot, Brex Empower April 2022, June 2022 SMB exit, 2021 peak valuation, January 2026 Capital One acquisition for $5.15 billion); ycombinator.com/companies/brex (batch, Pagar.me sold to Stone); brex.com/product/corporate-card (no personal guarantee, EIN, limit basis — quoted). ⚠️ **Not established:** WebSearch hit its session cap before this note was researched; checks were WebFetch only, and two TechCrunch and Brex support URLs tried returned 404. The public launch date of the card itself is not given — Wikipedia does not state it and I could not confirm the commonly cited 2018 month. A widely repeated story that the founders built the card because they could not get one themselves as foreign founders without US credit was not confirmed and is not used. The account of why incumbent issuers did not serve this segment is inference, not a sourced statement. The interchange-and-rules description draws on this vault's `industries/spend-management-platforms.md` (vault material, not independent corroboration).
