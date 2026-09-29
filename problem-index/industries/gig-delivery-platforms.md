# Gig Delivery Platforms

## Profile
**Category:** Platform Labour & Digital Work
**Market Size:** ~$90B US gross order value across food, grocery and local delivery; DoorDash, Uber Eats, Instacart and Grubhub hold the large majority, with several million people delivering on them in any given year
**Tech Maturity:** Very high on dispatch, routing and demand forecasting; deliberately opaque on everything the courier needs. Offer construction, pay calculation, batching decisions and account deactivation are all algorithmic, consequential and unexplained to the person they govern.
**Workforce:** Couriers and shoppers classified as independent contractors in most US jurisdictions; dispatch and marketplace engineers; support and deactivation review agents; merchant operations; safety and fraud teams

## Key Pain Themes
The offer a courier sees states a guaranteed amount and an estimated time. How that amount was constructed — base pay, distance, expected effort, any promotional component, and in some historical configurations the customer's tip — is not disclosed, and the industry has been through public controversy and regulatory action over pay models that used tips to offset base pay. Couriers therefore make accept-or-decline decisions dozens of times a shift against a number whose basis they cannot see.

Unpaid time is the structural economics problem. Waiting at a restaurant for a late order, driving to a pickup, and idling between offers are all working time in any ordinary sense and are largely uncompensated, so the headline per-delivery rate and the realised hourly rate after vehicle costs diverge substantially. Independent estimates of net hourly earnings vary widely, which is itself a symptom — nobody outside the platforms can compute it, and the platforms do not publish it.

Deactivation is the third. An account can be deactivated for customer complaints, low ratings, alleged fraud or policy violations, frequently with a generic reason and a limited appeal. For a full-time courier this is the loss of a job, delivered by an automated system, with no employment protections because the classification is contractor — a classification that remains genuinely contested in law and varies by jurisdiction.

## Current Tech Landscape
Dispatch and batching run on large real-time optimisation systems with demand forecasting and dynamic incentives. Routing uses standard mapping infrastructure with platform-specific adjustments. Courier apps expose offers, navigation, earnings summaries and support chat. Deactivation combines automated triggers with human review at varying depth. Background checks run through third-party vendors. Some jurisdictions now impose minimum earnings standards, pay transparency requirements or deactivation protections, and the platforms have built compliance systems for those markets specifically.

## Problems
- [[problems/gig-delivery-platforms/high-impact|🔴 High Impact: The Offer Shows a Number and Not What It Is Made Of]]
- [[problems/gig-delivery-platforms/low-impact-1|🟡 Low Impact: Batching, Routing and Wait Time]]
- [[problems/gig-delivery-platforms/low-impact-2|🟡 Low Impact: Order Accuracy and Substitution Decisions]]
- [[problems/gig-delivery-platforms/worker-life-1|🟢 Worker Life: The Courier Waiting Unpaid]]
- [[problems/gig-delivery-platforms/worker-life-2|🟢 Worker Life: The Agent Reviewing a Deactivation Appeal]]
- [[problems/gig-delivery-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/gig-delivery-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These platforms run some of the most sophisticated real-time allocation systems in commercial use and point almost none of that capability at the courier's own economics. The platform knows the expected wait at each merchant by hour, the realised net earnings per hour by market and time, and the probability that a given offer will turn out worse than its estimate — all of it computed continuously and none of it shown to the person deciding whether to accept. The asymmetry is the business model rather than an oversight, and it is increasingly the subject of legislation: minimum earnings standards, pay composition disclosure and deactivation protections have arrived in several jurisdictions and the compliance systems built for them demonstrate that the underlying computation is entirely feasible. The open question is whether transparency arrives as a product or as a statute.
