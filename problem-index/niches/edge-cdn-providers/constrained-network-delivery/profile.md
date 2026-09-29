# Constrained Network Delivery

**Parent Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Category:** Low Digitized
**Contested on:** Every serious competitor here is fighting to deliver acceptably to users on expensive, slow and intermittent connections — and whoever does that takes the markets where growth actually is, because the category's defaults assume conditions those users do not have.

## Profile
**Market Size:** ~$720M US-headquartered spend attributable to delivery into constrained markets
**Share of Parent Industry:** ~8% of category revenue
**Digital Adoption:** Very Low — the tooling and the defaults assume good connectivity
**Target Buyer:** Companies with mobile-first and emerging-market user bases
**Automation Potential:** High — adaptation to network conditions is measurable and automatable

## What Makes This a Distinct Niche
The category's defaults were designed around well-connected users: assume bandwidth, assume stability, assume the user is not paying per megabyte. A very large and growing population meets none of those assumptions — mobile connections with high and variable latency, data plans where a page's weight is a real cost to the user, networks that drop for seconds at a time, and devices several generations behind. For these users the difference between a well-adapted delivery strategy and the default one is the difference between a usable product and an unusable one, and it is where the delivery network's value is genuinely largest. It is also where measurement is weakest, because the tooling's vantage points are in well-connected locations and the users who cannot load the page never appear in the analytics that measure page loads.

## Current Tools & Gaps
Compression, image optimisation, adaptive media, and network information interfaces exposed by browsers. The gaps: adaptation is configured statically rather than driven by the observed connection, so a user on a poor connection receives the same payload as one on fibre; the users who fail entirely are absent from the measurement, which makes the problem invisible in exactly the way that matters; data cost to the user is never considered although it determines whether they return; intermittent connectivity is treated as failure rather than as a normal condition to be designed for; and the network's own vantage points are concentrated where connectivity is good.

## Problems
- [[niches/edge-cdn-providers/constrained-network-delivery/build|🔨 Build: The Users Who Never Appear in the Analytics]]
- [[niches/edge-cdn-providers/constrained-network-delivery/buy|🛒 Buy: Adaptive Delivery Techniques That Already Exist]]
- [[niches/edge-cdn-providers/constrained-network-delivery/fix|🔧 Fix: Measured From Places With Good Connectivity]]
