# Embedded Analytics

**Parent Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in embedded analytics is fighting to serve thousands of a software vendor's customers their own data, fast, inside a product that is not theirs — and whoever holds latency and isolation at that scale takes the deal, because the buyer is an engineering team that will otherwise build it.

## Profile
**Market Size:** ~$2.6B US embedded and customer-facing analytics
**Share of Parent Industry:** ~16% of category revenue
**Digital Adoption:** Medium-High — most software products ship some form of it
**Target Buyer:** Product and engineering leadership at software companies, not data teams
**Automation Potential:** High for authoring and provisioning; the hard constraints are performance and isolation

## What Makes This a Distinct Niche
Embedded analytics is a different business from internal business intelligence, and the only thing the two share is the rendering. The buyer is a product manager or an engineering lead at a software company, not a head of data. The users are that company's customers, who never chose the tool, have no training and no patience, and will judge the host product by it. The scale is thousands of tenants rather than hundreds of employees, which makes multi-tenant isolation a security requirement rather than a permissions preference and makes query performance a product-quality issue rather than an inconvenience — a dashboard an analyst waits nine seconds for is annoying, and a customer-facing page that takes nine seconds is a defect. The commercial model differs too: the host company pays per tenant or by consumption and its margin depends on the analytics vendor's cost structure, which is why so many of them build it themselves and regret it.

## Current Tools & Gaps
Embedded offerings from the major BI vendors, specialist embedded analytics vendors, charting libraries for teams building it themselves, and warehouse-native approaches. The gaps: isolation is enforced through configuration that is easy to get wrong, and a cross-tenant leak is an existential incident rather than a bug; performance at tenant scale requires pre-aggregation and caching strategies each team invents privately; white-labelling is usually superficial, so the embedded experience visibly belongs to another vendor; per-tenant customisation — the customer who wants one different chart — forces either a fork or a refusal; and the build-versus-buy calculation is dominated by a total cost of ownership nobody has measured properly.

## Problems
- [[niches/bi-analytics-platforms/embedded-analytics/build|🔨 Build: Nine Seconds Is a Defect, Not an Inconvenience]]
- [[niches/bi-analytics-platforms/embedded-analytics/buy|🛒 Buy: Multi-Tenant Query Optimisation as a Product]]
- [[niches/bi-analytics-platforms/embedded-analytics/fix|🔧 Fix: The Customer Who Wants One Different Chart]]
