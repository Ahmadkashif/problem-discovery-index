# Lineage: Edge & CDN Providers

**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** Akamai FreeFlow — racks of cache servers placed free inside other networks' data centres, reached through DNS-based request mapping and "Akamaized" URLs (ARLs), commercial from April 1999
**Builder:** Akamai
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Every copy of a popular web page came from one place.

A 1990s website ran on servers in one building. When a page became popular, every request crossed the internet to that building, through peering points and long-haul links that the site did not own. Load grew at the origin and congestion grew in the middle. Adding servers at the origin fixed the first problem and not the second.

In early 1995, by Akamai's own account, Tim Berners-Lee challenged colleagues at MIT to invent a fundamentally better way to deliver content. Tom Leighton, a professor of applied mathematics who led the Algorithms Group at MIT's Laboratory for Computer Science, had an office down the hall.

The obvious answer — cache copies near users — had a hard part. With thousands of caches and objects constantly added and removed, which cache should hold which object, and how could the assignment survive caches joining and failing without reshuffling everything?

## What Got Built

First a paper, then a product.

**Consistent hashing** was introduced in a 1997 Symposium on Theory of Computing paper by David Karger, Eric Lehman, Tom Leighton, Matthew Levine, Daniel Lewin and Rina Panigrahy, subtitled "distributed caching protocols for relieving hot spots on the World Wide Web." It maps objects to caches so that when a cache is added or lost, only a small share of objects move.

The product was **FreeFlow**. An industry white paper from 1999 describes it: thousands of servers, each with 1 GB of RAM and two 18 GB disks, installed in groups of about five at network providers, universities and corporate campuses. Akamai used DNS to steer each request: when a resolver asked for an Akamai hostname, Akamai looked at where the resolver was and answered with the best nearby server, recomputing continuously from measured load and link conditions. Customers rewrote the URLs of the objects they wanted delivered into Akamai Resource Locators, typically keeping the HTML page on their own servers.

Akamai was incorporated on **20 August 1998**, delivered its first live traffic in February 1999 — a pixel on a Disney site — and launched commercially in **April 1999**, with Yahoo! as a charter customer.

## Who Built It, And Why Them

**Akamai**, founded by Leighton, his graduate student Daniel Lewin and others after entering the 1998 MIT $50K competition with a business plan based on consistent hashing.

Why an algorithms group and not a carrier: the white paper states plainly that Akamai's network "is not a facilities-based network." It owned no links. Its advantage was the mathematics of deciding which of thousands of machines should serve a given object to a given user, and that problem is algorithmic, not physical.

That shaped the commercial deal. Lacking facilities, Akamai needed space inside other people's. Through its Accelerated Network Program it gave servers to network providers **at no cost**; the provider supplied rack space, power and a connection, and saved on upstream traffic. Content companies paid. Internet service providers hosted for free.

## What It Cost

The CDN sat between two parties and controlled neither.

It could cache only what the customer let it cache. In the original design that meant the objects whose URLs the customer chose to rewrite; the customer's application decided what was cacheable and for how long. The CDN served whatever that application said, correctly or not.

Configuration therefore became a negotiation made during onboarding, encoded per customer and rarely reopened. The network was built to optimise *where* to serve from continuously. *What* to serve from cache was left as a customer decision frozen in rules.

## What You Still Touch

Every request that resolves to a CDN edge server near you is FreeFlow's DNS mapping, and every cache miss caused by a customer's own header is the division of responsibility it started with.

- [[problems/edge-cdn-providers/high-impact|🔴 Cache Configuration Decided by Rules Nobody Revisits]] — routing re-optimised in near real time; cacheability decided once
- [[problems/edge-cdn-providers/worker-life-1|🟢 Support Engineer on Cache Misses and Origin Errors]] — explaining that the customer's application decided
- [[niches/edge-cdn-providers/cache-configuration/profile|Cache Configuration]]
- [[niches/edge-cdn-providers/the-configuration-owner/profile|The Configuration Owner]]

**Sources:** Akamai, *Company History* (Berners-Lee's early-1995 challenge; Leighton and Lewin; incorporation 20 August 1998; first live traffic February 1999 on a Disney pixel; ESPN and Star Wars trailer March 1999; commercial launch April 1999 with Yahoo! as charter customer) — company's own account; Wikipedia, *Akamai Technologies* (five co-founders; 1998 MIT $50K competition entry based on consistent hashing; IPO 29 October 1999); Karger, Lehman, Leighton, Levine, Lewin and Panigrahy, *Consistent Hashing and Random Trees*, STOC 1997 (via Semantic Scholar and Wikipedia, *Consistent hashing*); Internet Research Group, *The ISP Business Case for Internet Content Delivery* (1999; FreeFlow server specification; DNS-based mapping; Accelerated Network Program servers at no cost; "not a facilities-based network"; Open Cache Interface with Cisco); search-result summaries of Akamai's IPO prospectus and Encyclopedia.com (FreeFlow as the first product; ARLs pointing browsers at embedded objects while customers kept serving HTML). ⚠️ **Not established:** the ARL's internal field structure and how the 1999 system handled freshness and invalidation — I did not reach a primary technical description; the section on configuration describes the division of responsibility, not a dated rule-set mechanism. Leighton's office "down the hall" from Berners-Lee is from Akamai's own history, not independently checked.
