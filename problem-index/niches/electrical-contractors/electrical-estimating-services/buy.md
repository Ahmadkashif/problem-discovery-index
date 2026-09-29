# Drawing Takeoff Adapted to Electrical Scope Inference

**Niche:** [[niches/electrical-contractors/electrical-estimating-services/profile|Electrical Estimating Service Bureaus]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Takeoff software counts the symbols an estimator clicks; the expensive judgment is everything the drawings do not show — the routing, the conditions, and the work implied but not drawn.
**Tags:** #cnns #object-detection #semantic-segmentation #transformers #transfer-learning #evaluation-metrics #feature-engineering #tacit-knowledge-ml #automation #data-integration

## The Problem
Counting devices is the visible part of a takeoff and the smaller part of the value. Electrical drawings show devices and panel schedules; they generally do not show conductor routing, and the estimator infers run lengths, pathway, and installation conditions from the architectural and structural sheets — whether a run goes through finished space, above an accessible ceiling, or through a concrete deck, each with completely different labour. That inference is where the estimate is made or lost, it is done from experience, and it is the part software has not touched.

## What Already Exists
Digital takeoff is a mature category. Accubid, ConEst, PlanSwift, and Stack all provide symbol counting, measurement tools, assembly application, and increasingly automated symbol recognition on electrical drawings. Recognition accuracy on standard symbol sets is good and improving.

## The Customization Gap
All of it accelerates counting what is drawn. The estimator's actual work is inferring what is not — and that requires reasoning across sheet types, which no takeoff tool does, since they treat each sheet as a page to be measured. The adaptation is a scope inference layer that reads the electrical sheets together with the architectural, structural, and mechanical sets: routing candidates derived from building geometry and pathway availability, installation condition classified per run segment from what the architectural sheets show about finishes and access, and coordination conflicts flagged where the mechanical set occupies the space the electrical run would use. Output should be proposed runs with conditions and explicit uncertainty for the estimator to confirm rather than an automated quantity, because the liability sits with the person signing the bid. Trained on the bureau's own completed takeoffs, the system learns how its estimators actually make these calls, which is the firm's accumulated craft.

## Target Customer
Chief estimators and operations leaders at estimating bureaus, and the takeoff technicians who currently spend most of their time on inference rather than on counting.

## Impact If Solved
Attacks the part of the takeoff that consumes the time and carries the risk, rather than the part software has already addressed. Training on the firm's own completed work also captures estimator judgment as a by-product, which is the succession problem underneath the whole trade.
