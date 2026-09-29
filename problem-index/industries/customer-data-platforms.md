# Customer Data Platforms

## Profile
**Category:** Adtech & Martech
**Market Size:** ~$5B US for customer data infrastructure, split between packaged platforms and the warehouse-native tools that have been taking their place
**Tech Maturity:** Strong pipelines, unexamined core. Segment, mParticle, Tealium, Amperity, ActionIQ and Treasure Data move enormous volumes of customer events reliably and activate them into downstream tools. The function everything else depends on — deciding which records belong to the same person — is probabilistic, tuned by thresholds somebody set once, and measured by nobody.
**Workforce:** Data engineers and platform architects, identity and matching specialists, analytics and audience operations teams, privacy and compliance operators, solutions consultants

## Key Pain Themes
The unified customer profile is the product, and it is assembled by joining records that may or may not be the same person: an email, a device, a cookie, a loyalty number, a phone, an order from a household. Deterministic matches are safe and incomplete; probabilistic matches fill the gap and make two kinds of error. An over-merge combines two people into one profile, which means one person's history informs another's experience and, in the worst case, their data is exposed to them. An under-merge splits one person across several profiles, which breaks suppression, double-counts customers and understates lifetime value. Neither error is visible in any dashboard, and almost no organisation has ever measured its own rate.

The second theme is that the category's architecture has been overturned. The warehouse became the place customer data lives, and reverse-ETL tools activate from it directly, which removes the packaged CDP's central justification. The incumbents have repositioned toward identity, governance and activation breadth, which puts more weight on exactly the function that has never been validated.

The third is the event stream itself. A CDP is only as good as what product teams send it, and product teams ship code weekly. Event names change, properties disappear, a field's meaning drifts, a release stops firing an event entirely. Downstream, segments silently stop matching and journeys stop firing, and the cause is discovered weeks later by someone looking at a revenue chart.

## Current Tech Landscape
Twilio Segment and mParticle lead the packaged tier; Tealium holds enterprise tag and data management; Amperity and ActionIQ compete specifically on identity resolution at retail and enterprise scale. The composable stack — Snowflake or BigQuery plus dbt plus Hightouch or Census plus RudderStack — is where new builds increasingly go. Consent and privacy tooling from OneTrust and its peers sits alongside rather than inside. LiveRamp provides identity as a service for advertising activation. Tracking plan and schema tooling exists in Segment Protocols and Avo and is adopted unevenly.

## Problems
- [[problems/customer-data-platforms/high-impact|🔴 High Impact: Identity Resolution Is a Guess Nobody Measures]]
- [[problems/customer-data-platforms/low-impact-1|🟡 Low Impact: Audience Definitions and Segment Sprawl]]
- [[problems/customer-data-platforms/low-impact-2|🟡 Low Impact: Event Schema Governance]]
- [[problems/customer-data-platforms/worker-life-1|🟢 Worker Life: The Engineer Whose Tracking Plan Nobody Reads]]
- [[problems/customer-data-platforms/worker-life-2|🟢 Worker Life: Fulfilling a Deletion Request Against a Probabilistic Graph]]
- [[problems/customer-data-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/customer-data-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
Everything an organisation does with customer data — personalisation, suppression, lifetime value, audience activation, privacy request fulfilment — rests on the identity graph, and the identity graph is the one component with no accuracy metric. That is an unusual situation for a piece of infrastructure this consequential: a database would not ship without a consistency guarantee, and an identity graph ships with a threshold. The organisations running these systems cannot currently answer how often they merge two people, how often they split one, or which of those errors their configuration is trading against the other. Making that measurable, and letting the trade be chosen deliberately rather than inherited from a default, is the missing foundation beneath a category now competing on exactly this function.
