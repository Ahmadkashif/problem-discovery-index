# Edge & CDN Providers

## Profile
**Category:** Developer Tools & Infrastructure
**Market Size:** ~$9B US content delivery, edge compute and network security
**Tech Maturity:** Extremely mature at delivery, immature at everything built on top — Akamai, Cloudflare, Fastly, AWS CloudFront and their peers operate global networks that move an enormous share of internet traffic reliably. Caching configuration, bot classification and edge compute economics are all decided by rules people wrote once.
**Workforce:** Solutions engineers, network operations staff, security researchers and bot analysts, support engineers, edge platform developers, capacity planners

## Key Pain Themes
Cache configuration is the category's oldest unsolved problem and its most consequential: what to cache, for how long, keyed on what, and when to invalidate — decided by hand in rule sets that accumulate for years and are never revisited, while the traffic that would show what is actually cacheable flows past continuously. Bot management is the second, and it is an adversarial classification problem where the cost of a false positive is a blocked customer and the cost of a false negative is scraping or fraud, run largely on signature and heuristic rules that adversaries adapt to within days. Edge compute added a genuinely new problem — where should this run, and does moving it help — that nobody can answer empirically. Support engineers spend their days on cache misses and origin errors that belong to the customer's application, and the customers themselves cannot tell whether the CDN is helping or hiding a problem.

## Current Tech Landscape
Cloudflare has expanded aggressively from delivery into security, edge compute and developer platform; Akamai retains the largest enterprise footprint; Fastly competes on programmability and instant purge; the hyperscalers bundle competent delivery. Edge compute runtimes are now standard across the category and their programming models differ substantially. Bot management is offered by everyone and is a meaningful differentiator. Real user monitoring is available and rarely joined to configuration decisions. Origin shielding and tiered caching are standard. HTTP/3 and modern transport are widely deployed.

## Problems
- [[problems/edge-cdn-providers/high-impact|🔴 High Impact: Cache Configuration Decided by Rules Nobody Revisits]]
- [[problems/edge-cdn-providers/low-impact-1|🟡 Low Impact: Bot Classification Under Adaptation]]
- [[problems/edge-cdn-providers/low-impact-2|🟡 Low Impact: Edge Compute Placement Economics]]
- [[problems/edge-cdn-providers/worker-life-1|🟢 Worker Life: Support Engineer on Cache Misses and Origin Errors]]
- [[problems/edge-cdn-providers/worker-life-2|🟢 Worker Life: The Engineer Who Cannot Tell If It Is Working]]
- [[problems/edge-cdn-providers/ml-opportunity|🧠 ML Opportunities]]
- [[problems/edge-cdn-providers/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These providers see a substantial fraction of internet traffic in real time — request patterns, response characteristics, client behaviour, attack campaigns and performance under every network condition. That vantage point is unique and is monetised as delivery capacity and as security rules. What it could support — knowing what is genuinely cacheable, recognising an adversary's adaptation as it happens across thousands of customers, and measuring whether any configuration change actually improved anything — is largely unbuilt, because the category sells bandwidth and rulesets rather than decisions.
