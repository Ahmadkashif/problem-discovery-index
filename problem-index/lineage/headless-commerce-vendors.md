# Lineage: Headless Commerce Vendors

**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the commercetools platform — a commerce back end with no storefront at all, exposing products, prices, carts and orders only through a hosted API, launched 2013
**Builder:** commercetools
**Builder in vault:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Verification:** partial — see Sources

## The Problem That Came First

An ecommerce platform used to be a website that happened to have a database.

The suites large retailers ran in the 2000s shipped the catalogue, pricing, cart, checkout and page templates as one application. The storefront was rendered by the same system that held the prices. That was efficient while "online" meant one website.

It stopped being efficient when the same product had to appear in a mobile app, a marketplace feed, an in-store screen and a second country's site. **Every new channel meant either another copy of the platform or another team working around its templates**, and every change to the storefront risked the order logic sitting underneath it. commercetools' own account of why it exists names this directly: legacy platforms whose "rigid architectures made it difficult to expand globally, launch new channels and adapt."

## What Got Built

A commerce engine with the head cut off.

The commercetools platform, launched in 2013 after several years of development, holds the parts of commerce that have to be correct — product catalogue, price rules, carts, orders, customers, inventory — and exposes them through an API. It renders nothing. There is no template language and no default shop. A retailer, or the systems integrator it hires, builds every front end separately and calls the same back end from each.

Dirk Hoerig, the company's co-founder, is credited with coining the phrase **"headless commerce"** for this arrangement. The industry later formalised the idea as **MACH** — microservices, API-first, cloud-native, headless — the banner under which today's vendors certify one another's products.

## Who Built It, And Why Them

commercetools, founded in Munich by Dirk Hoerig and Denis Werner. The founding year is disputed between sources: Wikipedia gives 2006, the company's own about page says 2010. The 2013 platform launch is the date that matters here.

**The clearest evidence of whose problem it solved is who bought it.** In 2014 REWE Digital, the digital arm of the German retail group REWE, acquired the company outright. A grocer with many formats and channels did not want a vendor's storefront; it wanted a back end it could put its own front ends on. commercetools was later spun out again, with REWE remaining a significant shareholder.

That is the business case the artefact encodes. A large retailer already pays for design and front-end engineering, and the storefront is where it competes. What it wants from a vendor is the order logic nobody competes on — and it wants that logic to stay put while the storefronts change. A suite vendor selling templates could not offer this without undercutting its own product. A company that sold no storefront could.

The model found investors: $145 million from Insight Partners in 2019, and $140 million in 2021 at a $1.9 billion valuation. That November the company bought Frontastic — a front-end layer, filling the gap its own design had left open.

## What It Cost

**Nobody owns the page the customer sees.** The storefront is someone else's code, search is a separate service, content lives in a headless CMS, pricing and tax may be further vendors. The back end is correct by its own definition and the outcome is correct by nobody's.

The headless design also multiplies copies. Each service keeps its own view of catalogue and price for speed, and a customer can be shown one price and charged another. Checkout rules — tax, strong customer authentication, accessibility — land on whoever assembled the checkout, usually an integrator. The Frontastic purchase is the vendor quietly conceding part of the point.

## What You Still Touch

When a large retailer's app, website and in-store kiosk show the same basket, that is the back end commercetools separated from the page. When they disagree about the price, that is the same separation.

- [[problems/headless-commerce-vendors/high-impact|🔴 Nobody Owns the Composed Outcome]] — the direct cost of a back end that renders nothing
- [[problems/headless-commerce-vendors/low-impact-1|🟡 Catalogue and Pricing Consistency Across Services]]
- [[problems/headless-commerce-vendors/worker-life-2|🟢 On-Call During Peak Traffic]]
- [[niches/headless-commerce-vendors/cross-vendor-observability/profile|Cross-Vendor Observability]]
- [[niches/headless-commerce-vendors/enterprise-composable-platforms/profile|Enterprise Composable Platforms]]

**Sources:** Wikipedia, *Commercetools* (founders, Munich, 2006 founding, 2013 platform launch, 2014 REWE Digital acquisition and later spin-out, 2019 and 2021 funding, November 2021 Frontastic acquisition, Hoerig credited with coining "headless commerce"); commercetools.com/about (founders, "2010" founding, "rigid architectures" quotation); machalliance.org (expansion of MACH). ⚠️ **Not established:** WebSearch hit its session cap before this note was researched; all checks were WebFetch against known URLs. The founding year conflict (2006 vs 2010) is unresolved and both are reported. The platform's original product name and whether the founders first ran an agency could not be confirmed — web.archive.org was unreachable — so neither is asserted. MACH Alliance's founding date and founding members are not given because its site did not state them. REWE's internal reasons for the 2014 purchase are inferred from its position as a multi-format retailer, not from a stated rationale.
