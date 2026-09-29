# Legacy: What Process Manufacturing Bequeathed

**Origin:** [[origins/process-manufacturing/profile|Process Manufacturing]]

## The Direct Inheritance

| Child | What it inherited |
|---|---|
| [[industries/food-manufacturing|Food Manufacturing]] | The control loop itself, wearing regulatory clothing. This vault's own notes describe HACCP's Critical Control Point monitoring — continuous measurement against a defined limit, with a documented response when the limit is approached — which is [[origins/process-manufacturing/origin-story|the DCS's]] control-and-alarm discipline, mandated by the FDA rather than chosen for cost. |
| [[industries/contract-manufacturing|Contract Manufacturing]] | The ERP fit. Formulas, batches, recipes, co-products, by-products and lot traceability map cleanly onto a transactional and financial engine, because the accounting and planning logic for one chemical product is not fundamentally different from another's — the same reason SAP's client-server architecture, [[series/eras/wave-04-client-server-erp|Wave 4]]'s founding event, scaled across chemically diverse process businesses in a way discrete manufacturing's more bespoke routings resisted. |
| [[industries/medical-device-mfg|Medical Device Manufacturing]] | The validation burden as a permanent tax on automation. This vault's own notes describe near-zero ML adoption specifically because any model influencing a quality decision must be validated under 21 CFR Part 820 — the descendant of process manufacturing's own hard-won lesson that a control system's output is only as trustworthy as the validation behind it. |
| [[industries/metal-fabrication|Metal Fabrication]] | A weaker, adjacent line, stated honestly rather than stretched: nesting software optimising cutting layouts against material and machine constraints echoes [[origins/process-manufacturing/the-mechanism|DMC's]] constraint-pushing logic, but metal fabrication is discrete, job-shop production, not a continuous process — the resemblance is in the shape of the optimisation, not shared lineage. |
| [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]] | The tuning discipline in miniature. This vault's own notes describe NPI yield ramp as empirically tuning reflow-profile and placement parameters against a live process over weeks — exactly the empirical step-response tuning [[origins/process-manufacturing/the-mechanism|DMC]] formalised for a continuous chemical process, done here per new product, by hand, without the closed-loop optimisation layer process manufacturing built fifty years earlier. |

## The OT/IT Inheritance

**Every one of these five children runs shop-floor systems — MES, SCADA-descended data collection, vision inspection lines — that inherited process manufacturing's original assumption along with its control discipline: that the network is isolated and therefore safe.** [[origins/process-manufacturing/the-fight|Stuxnet]] proved that assumption fails specifically at the human and removable-media layer, not the network layer, and every one of these industries' plant-floor systems carries that exact exposure today, usually without anyone on the floor having heard the word "Stuxnet."

## The Deeper Inheritance: infrastructure before the weapon, a third time

The Data Hiway shipped in 1975. DMC had already been running at Shell for two years by then and did not become a broadly commercialised, industry-standard product until DMC Corporation's founding in **1984** — nearly a decade after the platform that made it practical. This is the same gap this series has now found three times: [[origins/airlines/legacy|SABRE to DINAMO]], [[origins/railroads/legacy|TOPS to PSR]], and here, the DCS to DMC. The infrastructure that makes a capability possible tends to sit unexploited for the better part of a decade before someone builds the thing that actually uses it.

## What an Episode Should Take From This

1. **A control system and its human interface are not the same trust boundary, and an attacker only needs to compromise one of them.** Stuxnet's falsified HMI readings are the single most important technical detail in this file — the plant was not blind, it was lied to.
2. **Regulatory mandate and cost-driven automation can produce the identical-looking control loop for entirely different reasons.** Food manufacturing's CCP monitoring and a chemical plant's DMC loop look alike and were adopted for opposite reasons — one compelled, one chosen.
3. **"Our systems aren't connected to the internet" is a claim about the network, not about the humans who operate on both sides of it.**

**Sources:** See [[origins/process-manufacturing/the-mechanism|The Mechanism]] and [[origins/process-manufacturing/the-fight|The Fight]] for full citations; this vault's `industries/food-manufacturing.md`, `industries/contract-manufacturing.md`, `industries/medical-device-mfg.md`, `industries/metal-fabrication.md`, `industries/electronics-contract-mfg.md`.
