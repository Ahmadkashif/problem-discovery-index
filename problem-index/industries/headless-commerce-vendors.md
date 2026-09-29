# Headless Commerce Vendors

## Profile
**Category:** Digital Commerce
**Market Size:** ~$4B US composable and API-first commerce platform licensing and implementation
**Tech Maturity:** Architecturally advanced, operationally fragile — commercetools, Elastic Path, Shopify Hydrogen, BigCommerce, Saleor and Medusa let a retailer assemble commerce from independent services. The architecture is genuinely better for large complex retailers and it distributes responsibility for correctness across so many services that nobody owns the outcome.
**Workforce:** Solutions architects, implementation and integration engineers, developer advocates, support engineers, performance specialists, partner enablement staff

## Key Pain Themes
Composable architecture solves coupling and creates an accountability vacuum. When a product page loads slowly, the cause could be the commerce API, the content management system, the search service, the pricing engine, the inventory service, the personalisation layer or the front end, each owned by a different vendor and a different team. When the price shown differs from the price charged, the same list applies. Nobody owns the customer-visible outcome, and the incident that follows a peak-traffic failure is a conference call between six parties. Around it sit two persistent problems: keeping catalogue and pricing consistent across services that each hold their own copy, and checkout compliance, where tax calculation, strong customer authentication, accessibility and consumer protection requirements change by jurisdiction and land on whoever built the checkout. Solutions architects live inside multi-year replatforms and on-call engineers own an incident spanning systems they cannot see into.

## Current Tech Landscape
The MACH approach — microservices, API-first, cloud-native, headless — is the architectural consensus for large retailers, with commercetools as the reference implementation. Shopify's Hydrogen and Oxygen brought headless to its ecosystem with tighter integration. Content management is typically a separate headless CMS. Search, personalisation, pricing, tax, payments and inventory are each frequently separate vendors. Observability across the composed stack is the acknowledged weak point, with distributed tracing available and inconsistently implemented across vendor boundaries. Implementation is largely delivered by systems integrators, and the quality of a headless deployment depends more on the integrator than on the platform.

## Problems
- [[problems/headless-commerce-vendors/high-impact|🔴 High Impact: Nobody Owns the Composed Outcome]]
- [[problems/headless-commerce-vendors/low-impact-1|🟡 Low Impact: Catalogue and Pricing Consistency Across Services]]
- [[problems/headless-commerce-vendors/low-impact-2|🟡 Low Impact: Checkout Compliance by Jurisdiction]]
- [[problems/headless-commerce-vendors/worker-life-1|🟢 Worker Life: Solutions Architect in a Replatform]]
- [[problems/headless-commerce-vendors/worker-life-2|🟢 Worker Life: On-Call During Peak Traffic]]
- [[problems/headless-commerce-vendors/ml-opportunity|🧠 ML Opportunities]]
- [[problems/headless-commerce-vendors/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
The composable proposition is that a retailer assembles best-of-breed services and changes any of them independently. What it does not supply is the layer that would make that safe: continuous verification that the composed system produces correct prices, consistent inventory and acceptable performance across every service boundary. Monolithic platforms provided that implicitly by owning everything. Composable architecture removed the coupling and removed the guarantee with it, and no vendor in the category has stepped into the gap because doing so means taking responsibility for other vendors' components.
