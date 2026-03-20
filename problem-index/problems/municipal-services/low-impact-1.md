# 311/Citizen Request Intelligent Routing

**Industry:** [[municipal-services|Municipal Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic ticketing systems handle citizen requests but cannot distinguish a pothole complaint that needs streets from a drainage complaint that needs utilities — so clerks manually triage hundreds of requests daily.
**Tags:** #bert #transfer-learning #attention-mechanisms #word-embeddings #evaluation-metrics #loss-functions #entropy-cross-entropy-kl-divergence #gradient-descent #workflow-orchestration

## The Problem
Municipalities receive 50-500 citizen service requests per day through 311 calls, web forms, email, and mobile apps. Each request must be classified by department (streets, water, parks, code enforcement, animal control, planning), priority level, and geographic zone before being dispatched. Current 311 platforms like SeeClickFix provide dropdown menus, but citizens routinely miscategorize ("there's water on the street" could be a water main break, a storm drain blockage, or an irrigation runoff issue), and free-text descriptions contain the actual diagnostic information that clerks must read and interpret.

## What Already Exists
SeeClickFix, PublicStuff (now Accela Citizen Relationships), and CitySourced provide intake and basic category routing. These systems use static dropdown menus and keyword matching. They handle volume but not ambiguity — a request mentioning "smell near the manhole" gets routed to sewer when it might be a gas leak requiring a completely different emergency response. The routing logic is rule-based and cannot learn from correction patterns.

## The Customisation Gap
Municipal service taxonomies are hyperlocal — one city's "Streets Division" handles what another city splits between "Transportation" and "Stormwater." A fine-tuned BERT classifier trained on a specific municipality's historical request-to-resolution data (typically 3-5 years of 311 records with department assignments and resolution codes) could learn the local taxonomy, flag ambiguous requests for human review, auto-escalate safety-critical keywords, and predict resolution time based on similar past requests. The model also needs to handle multilingual input (Spanish, Vietnamese, Mandarin depending on the municipality) and code-switch between formal complaints and colloquial descriptions.

## Impact If Solved
Reduces clerk triage time by 60-70% on routine requests (which are 80% of volume), cuts average response time by routing directly to the correct crew on first assignment instead of bouncing between departments, and surfaces patterns (e.g., 15 sewer complaints in the same grid square this month) that indicate systemic issues rather than one-off maintenance needs.
