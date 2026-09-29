# Freight Tech Platforms

## Profile
**Category:** Vertical SaaS
**Market Size:** ~$8B US freight technology (TMS, visibility, digital brokerage, carrier vetting)
**Tech Maturity:** High and brittle — McLeod and Trimble run the brokerage back office, project44 and FourKites sell visibility, Uber Freight and Loadsmart digitised load matching, and Highway and Carrier Assure emerged specifically because the industry discovered it could not reliably tell who it was giving freight to. The technology layer is dense and the identity layer underneath it is broken.
**Workforce:** Carrier vetting and compliance analysts, track-and-trace operations staff, integration engineers, pricing analysts, implementation consultants, customer success managers

## Key Pain Themes
The industry's defining current crisis is that a broker cannot reliably establish who is actually hauling a load. Double brokering, identity takeover of dormant carrier authorities and outright cargo theft have escalated sharply, the losses run to hundreds of millions annually, and the vetting infrastructure was designed for an era when a carrier's insurance certificate and authority number were sufficient. Below that sits the spot market, where rates move violently and every party — broker, carrier, shipper — is quoting from stale intuition. Two operational problems consume enormous labour and produce no differentiation: dock appointment scheduling, which every facility does differently and which drives detention costs the whole industry complains about; and document handling for proof of delivery and accessorial billing, where capture is solved and the shipper-specific rules that determine whether a charge gets paid are not. The people staffing all this — carrier sales reps and track-and-trace operators — spend their days on the phone repeating themselves.

## Current Tech Landscape
McLeod, Trimble and Revenova dominate brokerage operations; MercuryGate and Oracle serve shipper-side TMS. Load boards (DAT, Truckstop) remain the market's price discovery mechanism and its largest fraud surface. Visibility platforms have consolidated and now cover most of the truckload market with ELD and telematics integration. Carrier vetting has become a distinct and fast-growing category. Rate benchmarking is sold by DAT and Freightwaves. Digital brokerage as a category has retrenched sharply after Convoy's collapse, and the survivors have converged on the same operating model as the incumbents with better software.

## Problems
- [[problems/freight-tech-platforms/high-impact|🔴 High Impact: Carrier Identity and Double Brokering Fraud]]
- [[problems/freight-tech-platforms/low-impact-1|🟡 Low Impact: Dock Appointment Scheduling]]
- [[problems/freight-tech-platforms/low-impact-2|🟡 Low Impact: Accessorial Documentation and Billing Rules]]
- [[problems/freight-tech-platforms/worker-life-1|🟢 Worker Life: Carrier Sales Cover Scramble]]
- [[problems/freight-tech-platforms/worker-life-2|🟢 Worker Life: Track and Trace Check Calls]]
- [[problems/freight-tech-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/freight-tech-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
The platforms sit on the only cross-broker record of carrier behaviour that exists: which carriers accepted which loads at which rates, who showed up, who was late, who re-brokered, whose paperwork did not match, and which identities appeared and disappeared. Federal authority and insurance data is public and thin. Individual brokers see their own experience and are structurally reluctant to share it. The platform sees the network, and the network structure is exactly where fraud is visible and where nobody is looking.
