# Embedded Finance Platforms

## Profile
**Category:** Fintech
**Market Size:** ~$8B US banking-as-a-service and embedded finance infrastructure revenue, reshaped since 2023 by supervisory action against the sponsor bank layer
**Tech Maturity:** Strong APIs on top of a compliance model that was never engineered — Unit, Treasury Prime, Synctera, Marqeta, Lithic, Galileo, Stripe Treasury and Increase expose accounts, cards, ledgers and payments as clean developer primitives, and sit between a fintech programme that owns the customer and a sponsor bank that owns the regulatory obligation. The platform is accountable for conduct it observes only as API calls.
**Workforce:** Platform and payments engineers, compliance and BSA analysts, programme risk managers, solutions engineers and implementation specialists, bank partnership managers, support engineers

## Key Pain Themes
The structural problem is a three-party arrangement in which responsibility, visibility and control are held by different parties. The programme designs the product, writes the marketing, and speaks to the end customer. The bank holds the charter, carries the BSA and consumer compliance obligation, and is the entity a regulator examines. The platform builds the rails, sees every transaction, and has neither the customer relationship nor the charter.

When the 2023–24 consent orders landed — Blue Ridge, Choice, Lineage, Evolve, and the Synapse collapse that left end users unable to reach their own deposits — the supervisory conclusion was that banks must oversee programmes they had not been overseeing. That obligation is now pushed onto the platform layer, which must monitor programme behaviour it can only infer, produce evidence for banks that each want it differently, and reconcile ledgers across for-benefit-of accounts where the sub-ledger is the only record of who owns what.

Around it sit programme launch configuration, which is bespoke every time, and a support and implementation function serving developers building regulated products they have often not built before.

## Current Tech Landscape
Card issuing runs through Marqeta, Lithic, Galileo or the platform's own processor connection. Ledgers are internal, sometimes built on Modern Treasury or a homegrown double-entry core. KYC and KYB come from Persona, Alloy, Socure or Middesk. Transaction monitoring uses Unit21, Hummingbird or Sardine. Sponsor bank oversight is a mixture of portals, workbooks and scheduled file drops. The industry has consolidated toward platforms that own more of the compliance stack, because the alternative — a thin API layer over a bank that is not equipped to supervise — is the configuration regulators objected to.

## Problems
- [[problems/embedded-finance-platforms/high-impact|🔴 High Impact: Programme Oversight Without Programme Visibility]]
- [[problems/embedded-finance-platforms/low-impact-1|🟡 Low Impact: Programme Launch Configuration]]
- [[problems/embedded-finance-platforms/low-impact-2|🟡 Low Impact: FBO Ledger Reconciliation]]
- [[problems/embedded-finance-platforms/worker-life-1|🟢 Worker Life: The Compliance Analyst Watching Forty Programmes]]
- [[problems/embedded-finance-platforms/worker-life-2|🟢 Worker Life: The Implementation Engineer Launching Someone Else's Bank]]
- [[problems/embedded-finance-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/embedded-finance-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
An embedded finance platform occupies a position nobody else in banking has: it sees the full transaction and customer behaviour of dozens or hundreds of distinct financial products simultaneously, built by different teams for different populations, on identical infrastructure. That is a natural comparison set of a kind no individual bank possesses — the same primitive, deployed a hundred ways, with outcomes attached. It makes questions answerable that the industry currently treats as unanswerable: which programme designs produce disputes, which onboarding flows produce abandonment concentrated in particular populations, which product configurations precede a compliance failure. The platforms hold this and use it for billing and for incident response, which is to say they use it after the fact.
