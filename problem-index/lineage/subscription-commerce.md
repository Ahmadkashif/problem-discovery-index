# Lineage: Subscription Commerce

**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** Recharge — the Shopify app that turns a one-off product into a recurring order on a fixed cadence, with a stored payment method and a subscriber portal for skip, swap and cancel
**Builder:** Recharge
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A store built on Shopify could sell a box once. It could not sell it every month.

The platform that small direct-to-consumer brands adopted in their thousands was built around a single checkout producing a single order. Recurring billing — keep the card, charge it again in thirty days, create the next order, ship it — was not something its checkout did. A brand wanting to sell coffee, razors or a curated box by subscription had three options: move to a billing system built for software companies and bolt a store to it, build the recurring logic itself, or not sell subscriptions.

**The constraint was that the store and the recurring charge lived in different systems.** A subscription is an order plus a promise of future orders, and the store only understood the first half.

## What Got Built

An app that supplies the second half.

Recharge sits on top of a Shopify store. A shopper chooses "subscribe" on a product page, the payment method is stored, and on each cycle Recharge charges it and creates the next order in Shopify, where the brand's normal fulfilment picks it up. The subscriber gets a portal to change the date, skip a delivery, swap a product or cancel. The brand gets a list of active subscribers, upcoming charges and failed payments.

That last list matters: cards expire, and a subscription business loses customers who never decided to leave. Dunning retries and card-updater services, now standard across the category, exist to recover them.

Recharge says it is used by more than 20,000 businesses and processes over $30 billion in recurring revenue on Shopify — the company's own figures.

## Who Built It, And Why Them

Recharge, founded in 2014 in Santa Monica, California, by Oisin O'Connor, now CEO, and Mike Flynn, now CTO.

**The opening was structural: Shopify had the merchants and no recurring checkout, and it let outside developers sell apps into that gap.** An app developer did not need to win the merchant, host the store or process the one-off sale. It needed only to add the part the platform left out, and every subscription brand on Shopify became a prospective customer at once. A general recurring-billing company built for software contracts would have had to rebuild a store around its billing; an app on the platform started where the merchants already were.

That position also dictated the shape. For years such apps ran their subscription checkout alongside Shopify's rather than inside it — Shopify's developer documentation still carries a guide for "migrating a legacy subscriptions app to one that is integrated to Shopify Checkout," and tells new apps to use its Subscription APIs.

I could not establish how O'Connor and Flynn came to build it — whether for their own store, for a client, or as a product from the start.

## What It Cost

**The subscription was modelled as a recurring order, not as a relationship.** The system knows cadence, next charge and status. It records that a subscriber cancelled; it does not know why.

The fixed cadence produces a fixed wave. When most subscribers are charged on the same cycle, fulfilment arrives in the same few days, and the planner absorbs a peak the billing schedule created. And because skip, pause and swap sit in a portal next to cancel, brands that fear lost revenue bury them — so a customer who wanted to miss one month leaves altogether.

## What You Still Touch

The "subscribe and save" toggle on a small brand's product page, and the email saying your next box ships in three days, are this app's shape.

- [[problems/subscription-commerce/high-impact|🔴 Diagnosing Early-Cycle Churn]] — a system that records cancellations but not reasons
- [[problems/subscription-commerce/low-impact-2|🟡 Skip, Pause and Swap Flexibility]]
- [[problems/subscription-commerce/worker-life-1|🟢 Fulfilment Planner on the Monthly Wave]]
- [[niches/subscription-commerce/involuntary-churn-recovery/profile|Involuntary Churn Recovery]]
- [[niches/subscription-commerce/subscription-lifecycle-platforms/profile|Subscription Lifecycle Platforms]]

**Sources:** getrecharge.com/about (founding 2014, Santa Monica, O'Connor and Flynn and their titles, 20,000 businesses, $30 billion — company claims); shopify.dev, *Migrate to Subscription APIs* and *Subscriptions* guides (the "legacy subscriptions app" wording and the instruction that new apps use the Subscription APIs). Recharge's dominance on Shopify, and dunning and card updater as standard, come from this vault's `industries/subscription-commerce.md` (vault material, not independent corroboration). ⚠️ **Not established:** WebSearch hit its session cap before this note was researched; checks were WebFetch only. There is no Wikipedia article on Recharge, its blog carries no founding history, and the Shopify Unite 2020 newsroom URL returned 404 — so the date Shopify's Subscription APIs launched and the founders' origin story are both left out. The description of Shopify's checkout before those APIs is inferred from the "legacy" migration guide, not from a dated Shopify statement. The characterisation of the app's mechanics is general and not tied to a specific release.
