# Occurrence Monitoring Across a Fragmenting Media Landscape

**Niche:** [[niches/news-media-local/political-ad-tracking/profile|Political Advertising Tracking]]
**Industry:** [[industries/news-media-local|Local News Media]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The product is complete coverage, and the places political advertising runs multiply every cycle.
**Tags:** #computer-vision #ocr #anomaly-detection #data-integration #automation

## The Problem
The claim is completeness: every political spot, everywhere. That was tractable when political advertising meant broadcast and cable in identifiable markets. It now means broadcast, cable, connected television, digital video, social platforms, streaming audio, and direct mail — each with different observability and some with essentially none.

Broadcast monitoring is a mature operation of signal capture and matching. Digital is a different problem entirely: ads are targeted, so what any observer sees is a sample from an unknown distribution, and platform ad libraries vary enormously in completeness and detail.

Every cycle, spending shifts toward the channels that are hardest to see, and the product's core claim erodes unless the collection keeps up.

## What Already Exists
Broadcast monitoring technology is mature. Audio and video fingerprinting is commodity. Web scraping and platform API integration are standard. Media monitoring services exist across many verticals.

## The Customization Gap
The generic capabilities cover collection. The domain problems are attribution and estimation.

**Sponsor attribution is adversarial.** Spending routes through committees and intermediaries with names designed not to be informative, and connecting a spot to the interest actually behind it is entity resolution over a deliberately obscured network — the single most valuable thing the product does and the least automated.

**Digital coverage is a sampling problem, not a collection problem.** Targeted advertising cannot be observed comprehensively by any outside party, so digital spend must be estimated from partial observation with a stated method and an honest uncertainty — which is a statistical product, not a monitoring feed.

**Rate data is public, structured badly, and decisive.** Broadcast political files disclose what was actually paid, in scanned documents of varying quality, and they are the ground truth that anchors every estimate. Extracting them reliably is unglamorous and load-bearing.

**Creative matching across variants.** Campaigns run dozens of versions of a spot with small changes, and the analytically meaningful unit is the message, not the file. Clustering variants into messages is a domain requirement no monitoring platform provides.

**Coverage must be reported, not claimed.** With channels multiplying, the product needs to say what it observes comprehensively, what it estimates, and how well — and being the first to do so is a differentiator rather than an admission.

## Target Customer
Chief Technology Officer or VP of Data at a political tracking firm, where coverage completeness is the product claim and the landscape moves under it every two years.

## Impact If Solved
Buyers make allocation decisions worth billions on the assumption that the tracking is complete, and it is decreasingly true in exactly the channels where spending is growing fastest. Honest estimation with stated coverage — and better sponsor attribution — improves both the product and the public record of who is paying for political speech.
