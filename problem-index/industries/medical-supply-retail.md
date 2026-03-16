# Medical Supply Retail

## Profile
**Category:** Retail & E-Commerce
**Market Size:** ~$55B US durable medical equipment (DME) and medical supply market including independent DME suppliers, home medical equipment stores, respiratory equipment providers, mobility device dealers, and wound care supply shops
**Tech Maturity:** Low — Brightree and ResMed dominate DME-specific software for billing and inventory, but AI adoption is near-zero; most prior authorization work, equipment fitting, and clinical documentation is manual and paper-driven
**Workforce:** DME fitters/technicians, customer service reps, delivery drivers, billing/insurance specialists, respiratory therapists, rehab technology suppliers, store managers

## Key Pain Themes
Insurance eligibility verification and prior authorization consume the largest share of staff time and create the most revenue cycle friction: a single wheelchair or CPAP order can require 45–90 minutes of phone calls, fax submissions, and portal navigation before a payer confirms coverage, and denials for documentation insufficiency run 20–35% on first submission. DME fitting is a skill-intensive process where experienced fitters develop an intuitive read on a patient's body habitus, mobility limitations, and home environment that informs equipment selection — this tacit knowledge is nearly impossible to transfer to new hires and leaves with every retiring technician. Product catalog complexity is extreme: thousands of HCPCS codes map to overlapping product lines, and matching a patient's clinical indication to the correct billable item requires both clinical knowledge and payer-specific coverage rules that vary by state and plan. Delivery logistics are uniquely constrained by patient mobility — a bariatric bed delivery to a second-floor apartment with no elevator is a fundamentally different operation than a standard walker drop-off, and current scheduling tools do not account for these access variables.

## Current Tech Landscape
Brightree (owned by ResMed) is the dominant vertical ERP handling order intake, inventory, billing, and delivery for mid-to-large DME suppliers, but its prior auth workflow is essentially a structured form that still requires human phone calls and fax follow-ups. Smaller shops use general-purpose tools (QuickBooks for billing, Google Sheets for inventory, paper CMN forms) with no integration between them. Bonafide and Parachute Health have digitized some of the physician-to-DME ordering workflow, but the insurance verification and fitting steps remain almost entirely manual. No existing platform uses ML to predict prior auth outcomes, recommend equipment based on patient characteristics, or optimize delivery routes with patient-access constraints.

## Problems
- [[problems/medical-supply-retail/high-impact|🔴 High Impact: Insurance Eligibility Verification and Prior Authorization for DME]]
- [[problems/medical-supply-retail/low-impact-1|🟡 Low Impact: Product Catalog Search by Clinical Need and Payer Coverage]]
- [[problems/medical-supply-retail/low-impact-2|🟡 Low Impact: Delivery Scheduling with Patient Mobility and Access Constraints]]
- [[problems/medical-supply-retail/worker-life-1|🟢 Worker Life: DME Fitter Documentation Burden]]
- [[problems/medical-supply-retail/worker-life-2|🟢 Worker Life: Customer Service Rep Insurance Denial Appeal Processing]]

## Analysis
- [[problems/medical-supply-retail/ml-opportunity|🧠 ML Opportunities]]
- [[problems/medical-supply-retail/ai-agents-platforms|🤖 AI Agents & Platforms]]
