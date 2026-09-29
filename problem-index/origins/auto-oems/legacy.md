# Legacy: What Auto OEMs Bequeathed

**Origin:** [[origins/auto-oems/profile|Auto OEMs]]

## The Direct Inheritance

| Child | What it inherited |
|---|---|
| [[industries/contract-manufacturing|Contract Manufacturing]] | The ERP/MES stack running mid-to-large shops (Epicor, Infor, SAP for BOM and costing; Plex and QAD purpose-built for the floor) is MRP's direct descendant, running the same explosion logic against the same class of bill-of-materials problem — for someone else's product instead of a single OEM's. |
| [[industries/metal-fabrication|Metal Fabrication]] | Job-shop ERP (JobBOSS, Prodsmart) inherited MRP's planning logic scaled down to shops too small to have ever run the original mainframe systems — and, per this vault's own notes, the quality-inspection judgement that MRP never touched is exactly what still resists automation. |
| [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]] | MES and ERP are near-universal here (Aegis FactoryLogix, Valor, SAP/Oracle/Epicor) — but this vault's own analysis notes no platform yet does predictive BOM risk scoring, which is MRP's original question — "will this plan actually execute?" — still unanswered by prediction rather than static rule. |
| [[industries/food-manufacturing|Food Manufacturing]] | ERP and MES are widespread, but this vault records that batch-to-batch yield variance is absorbed by operator judgement the systems don't capture — the same gap between "the plan" and "what actually happened on the floor" that MRP's push logic has carried since 1964. |
| [[industries/auto-dealers-independent|Independent Auto Dealers]] | A thin, consumer-grade descendant: budget dealer-management systems handle basic vehicle inventory but, per this vault's own note, offer "no analytics, no lead scoring" — the computerised-inventory idea survived; the optimisation layer that made MRP worth building did not travel with it downstream. |
| [[industries/auto-repair-shops|Auto Repair Shops]] | Received the parts-sourcing problem MRP was built to solve, with none of the tooling: shops juggle NAPA, O'Reilly, AutoZone and dealer parts networks by hand, and this vault's own `low-impact-2` problem note for the industry — Parts Sourcing Optimization — is, structurally, Orlicky's 1964 question asked again for an industry that never got the 1975 answer. |

## The Second Inheritance: the hybrid that actually shipped

Neither lineage won cleanly. What spread through this vault's manufacturing industries is the compromise NUMMI-era Detroit eventually adopted: **push-based ERP for planning and procurement, pull-based signals for execution on the floor.** An FDE meeting a contract manufacturer running SAP with kanban bins on the shop floor is looking at both halves of this origin's fight, coexisting because neither one alone was sufficient.

## The Third Inheritance: computability as a false signal of quality

The single most transferable lesson from this origin is not about manufacturing at all: **the fact that a method can be computerised and sold as software says nothing about whether it is the better method.** MRP spread to 8,000 companies by 1981 because IBM's sales force could install it. Kanban spread to almost none outside Toyota's own supply chain in the same period, because it could not be shrink-wrapped — and it was, by the industry's own eventual judgement at NUMMI, the more important discipline. Anyone evaluating why an industry runs on the tool it runs on should ask whether the tool won because it was better, or because it was the one that could be sold.

## What an Episode Should Take From This

1. **Two solutions to one problem is not a contradiction to smooth over — it's the whole lesson.** MRP and TPS are not the same idea in different clothes; teaching them as one erases the most useful comparison in the file.
2. **Detroit's first response — GM's ~$90B automation programme — is the clean counter-example to "just add computing power."** NUMMI, with less capital and the same workforce, beat it.
3. **The infrastructure/discipline gap here has its own timeline, like SABRE's twenty-five-year wait for DINAMO:** MRP was buyable in 1975; the discipline Toyota had proved by 1963 wasn't seriously absorbed by a major US automaker until NUMMI, 1984 — a twenty-year gap most retellings compress to nothing.

**Sources:** See [[origins/auto-oems/the-mechanism|The Mechanism]] and [[origins/auto-oems/the-fight|The Fight]] for full citations; this vault's `industries/contract-manufacturing.md`, `industries/metal-fabrication.md`, `industries/electronics-contract-mfg.md`, `industries/food-manufacturing.md`, `industries/auto-dealers-independent.md`, `industries/auto-repair-shops.md` and their problem notes.
