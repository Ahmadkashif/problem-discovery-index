# Six Copies That Disagree

**Niche:** [[niches/headless-commerce-vendors/catalogue-price-consistency/profile|Catalogue & Price Consistency]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every service in the stack keeps its own copy of the catalogue for performance, synchronisation is a solved engineering problem, and the copies still disagree in ways that charge customers the wrong price.
**Tags:** #data-integration #change-point-detection #evaluation-metrics #confidence-intervals #automation #compliance #descriptive-statistics #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to make every service's copy of the catalogue agree about the price a customer will be charged — and whoever does that removes the category's most visible failure, because the copies disagree and the customer notices.

## The Problem
A price is updated in the commerce platform. The search index picks it up in four minutes, the content platform's cache holds the old one for an hour, the personalisation service refreshes nightly, and the front end caches at the edge for ten minutes. For a period whose length nobody has calculated, a customer can see three different prices in one session depending on which surface they look at, and be charged a fourth. Each service is behaving exactly as configured. Nobody has asked what the composed system's consistency window actually is, because that question belongs to no service owner.

## Why Nobody Has Built This
Consistency is a property of the composition and every participant owns only their own copy, so it falls between them. Cache settings were chosen for performance by whoever configured each service, without anybody computing their combined effect. The divergence is intermittent and hard to reproduce, which makes it look like a mystery rather than an arithmetic consequence of the configuration. And the complaint arrives as a customer service issue.

## What to Build
Compare the copies continuously. Sample products and query every service that holds a copy, comparing prices, availability and key attributes, which detects divergence directly and is the build — the comparison is mechanical, cheap, and is not run anywhere. Compute and publish the composition's consistency window from the actual observed propagation, rather than from the cache settings, so the retailer knows how long a price change takes to be true everywhere. Designate an authoritative source for the customer-facing price and verify every surface against it, since without a designated authority the question of which price is correct has no answer. Detect stale copies by comparing update timestamps against the authority's, which catches a broken synchronisation before any customer does. Model promotions explicitly, which the fix note develops and which is the largest contributor. Alert on divergence with the responsible service named, so it becomes a ticket rather than an investigation. Report the customer impact — how many sessions could have seen an inconsistent price — which makes an abstract correctness property a business number. Hold the checkout price as authoritative and reconcile display prices to it, or the reverse, but decide, since the failure is frequently that no decision exists. And feed the divergence signal into the composed verification work, since this is its most common finding.

## Target Customer
Data and commerce engineering at retailers, the platform vendors whose services hold copies, and the integrators who configured the caches.

## Impact If Built
Consistency is a property of the composition and every participant owns only their copy, so the question belongs to nobody. Continuously comparing the copies is mechanical and cheap, and computing the observed consistency window turns an intermittent mystery into an arithmetic fact.
