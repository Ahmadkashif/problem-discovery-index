# Field Service Software

## Profile
**Category:** Vertical SaaS
**Market Size:** ~$5B US field service management software
**Tech Maturity:** High at the workflow layer — ServiceTitan, Jobber, Housecall Pro, FieldEdge, ServiceMax and Salesforce Field Service have won scheduling, dispatch, invoicing and payments for the trades. Dispatch itself, the decision that determines the economics, is still a person moving cards on a board.
**Workforce:** Onboarding specialists, price book content teams, integration engineers, dispatch product specialists, trade advisory staff, customer success managers

## Key Pain Themes
Field service platforms have digitised everything around the visit and left the visit's central question untouched: which technician, with which parts, at which time, for this specific job. First-time fix rate is the number that determines whether a service business makes money — a return visit consumes a slot, a drive, and a customer's patience — and it is decided by a dispatcher matching a vague customer description against a mental model of who is good at what. Beneath that sit two content burdens the vendors carry permanently: flat-rate price books, which must be maintained per trade, per region and per equipment type and are the single most-cited reason contractors switch platforms; and equipment asset history, where the platform records that a unit was serviced but not enough about it to be useful the next time. The technician, meanwhile, does an hour of unpaid administration a day, and the dispatcher spends the day in a state of continuous re-planning.

## Current Tech Landscape
ServiceTitan dominates the larger residential trades with deep vertical functionality; Jobber and Housecall Pro serve smaller operators well; ServiceMax and Salesforce Field Service handle the enterprise and OEM side. Routing and scheduling optimisation is offered by all of them and adopted by few, because the constraints that matter are informal. Price book content is licensed (Profit Rhino, Callahan) or maintained in-house. Payments, financing and consumer lending have become major revenue lines. IoT and remote equipment monitoring is real in commercial HVAC and refrigeration and largely absent in residential.

## Problems
- [[problems/field-service-software/high-impact|🔴 High Impact: First-Time Fix and the Dispatch Match]]
- [[problems/field-service-software/low-impact-1|🟡 Low Impact: Flat-Rate Price Book Maintenance]]
- [[problems/field-service-software/low-impact-2|🟡 Low Impact: Equipment Asset History Capture]]
- [[problems/field-service-software/worker-life-1|🟢 Worker Life: Dispatcher Continuous Re-Planning]]
- [[problems/field-service-software/worker-life-2|🟢 Worker Life: Technician Administration at the Truck]]
- [[problems/field-service-software/ml-opportunity|🧠 ML Opportunities]]
- [[problems/field-service-software/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
The vendor holds a service history corpus that no manufacturer and no contractor can match: millions of visits, across every equipment make and model, with the reported symptom, the diagnosis, the parts used, the resolution and whether anyone had to come back. Manufacturers see warranty claims on their own equipment during the warranty period. Contractors see their own few thousand jobs. The platform sees the full service life of the installed base across brands, and uses it to print an invoice.
