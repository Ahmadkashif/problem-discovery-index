# Telematics Has the Sensors, the Maintenance System Has the Outcomes, and Nothing Joins Them

**Niche:** [[niches/auto-repair-shops/fleet-maintenance-analytics/profile|Fleet Maintenance Management Analytics]]
**Industry:** [[industries/auto-repair-shops|Auto Repair Shops]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Fleet telematics, maintenance management software and predictive maintenance products are all mature and all sit on one side of the join — the sensor stream without repair outcomes, or the work order without the sensor stream.
**Tags:** #time-series-forecasting #gradient-boosting #feature-engineering #data-integration #evaluation-metrics

## The Problem
A fleet management company runs a large maintenance operation and buys heavily to support it. Telematics on the vehicles. A fleet maintenance information system for work orders and authorisations. Parts and labour rate databases. Business intelligence for client reporting. Increasingly, predictive maintenance offerings sold on the promise of catching failures before they happen.

Each product is competent and each is built around a partial view. The telematics vendor sees engine hours, fault codes, idling, harsh events and location, and has no idea what was subsequently repaired. The maintenance system holds the repair with no sensor context. The predictive maintenance product was trained on a manufacturer's own fleet, on one platform, and generalises poorly to a mixed book. The BI layer reports cost, which is the only field everything agrees on.

## What Already Exists
Telematics platforms are mature, widely deployed and rich in vehicle data. Fleet maintenance information systems handle work orders, authorisation workflow, PM scheduling and vendor management. Standardised labour operation and parts catalogues exist and are widely used. Predictive maintenance products exist from manufacturers, telematics vendors and specialists. Data warehouses and BI tools handle the reporting.

## The Customization Gap
**The join is the whole product and nobody sells it.** A fault code with no repair outcome is an alert. A repair with no preceding sensor history is a cost record. The pair — this code, on this platform, at this mileage, followed by this component replacement — is a labelled training example, and the fleet manager is the only party holding both sides. Integration platforms move the data; they do not resolve it to the same vehicle, the same event and the same component, which is where the difficulty actually lives.

**Coding standards standardise the form, not the meaning.** Labour operation codes and parts catalogues give a shared vocabulary, and shops still record the same repair differently, bundle operations inconsistently, and use free text where the code does not fit. Any cross-shop analysis rests on normalising this, and no vendor does it because no vendor has the cross-shop volume.

**Predictive models assume one platform.** Manufacturer-built predictive maintenance is trained on that manufacturer's telemetry and validated on their fleet. A mixed fleet book spans every brand, several telematics vendors and twenty years of vehicles. Transferring a model across platforms is the actual problem and it is not what the products were built to do.

**Duty cycle is the variable nobody carries.** The same van on urban parcel delivery and on regional service calls is two different reliability problems. Telematics can characterise duty cycle precisely; the maintenance system does not record it; the benchmark report averages across it. Every cost-per-mile comparison in the industry is confounded by this and it is fixable with data already collected.

**Authorisation is a workflow step, not a decision support surface.** The FMIS routes the shop's request to an authoriser and records the outcome. It does not tell the authoriser what this repair usually costs on this vehicle at this mileage in this market, which is the one thing that would make the decision better — and the history to compute it is in the same system.

**Client reporting is built for finance.** BI tooling delivers spend, variance and budget. The questions that would change a client's behaviour — which platform to buy, which interval to run, which shop is reliable — are analytical rather than financial and fall outside what the reporting layer was scoped to answer.

## Target Customer
Director of Maintenance Services or VP of Fleet Analytics at a fleet management company. The adaptation is specific: keep telematics, the FMIS and the reporting layer, and build the entity resolution and normalisation layer that joins sensor history to repair outcome at component level — which is the asset, and the only part no vendor can supply.

## Impact If Solved
Every party in fleet maintenance holds half the data and buys tools built for their half. The organisation authorising the repairs holds both halves and has never joined them.
