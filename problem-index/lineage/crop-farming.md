# Lineage: Crop Farming

**Industry:** [[industries/crop-farming|Crop Farming]]
**Wave:** [[series/eras/wave-08-mobile-gps|8 — Mobile & GPS]]
**The tool:** StarFire — John Deere's wide-area differential GPS, a subscription correction signal broadcast over Inmarsat L-band to a receiver on the tractor or combine cab, first offered in 1998
**Builder:** Deere & Company
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A yield map was only as good as the position stamped on each reading, and in the mid-1990s the position was bad.

A grain-flow sensor on a combine, paired with a GPS receiver, could already log bushels against location — and so make a case for putting seed and fertiliser where they would pay. (The combine-side sensor has its own lineage: see [[lineage/agtech-platforms|Lineage: Agtech Platforms]].)

What was not built was a usable fix. Civilian GPS was then degraded deliberately under Selective Availability, and standard accuracy ran to roughly 15 metres. A combine header is narrower than that. **A map whose error is wider than the machine cannot say which pass produced which yield**, and so it cannot justify treating one strip of a field differently from the next. Several early yield-mapping ventures went bankrupt in those years on exactly this limitation.

Differential correction needed a reference receiver on a surveyed point and a radio link — surveying infrastructure, not farm equipment.

## What Got Built

A correction service delivered from orbit.

Ground reference stations measure GPS error; the corrections are uplinked from a US east-coast station and rebroadcast worldwide on Inmarsat's L-band frequencies. The receiver on the cab combines them with the GPS signal to resolve its position far more tightly.

The generations, as dated in the one source reached this session:

| Generation | Year | Stated accuracy |
|---|---|---|
| SF1 | 1998 | about 1 m, 1-sigma |
| SF2 | 2004 | about 4.5 cm absolute, 2.5 cm relative; GPS and GLONASS |
| SF3 | 2016 | slightly better than SF2; pull-in time cut 67%; 60 ground reference stations |

The jump from a metre to a few centimetres is the jump from *mapping* a field to *driving* in it: at SF2 accuracy the receiver can hold a machine on the same line pass after pass, which is what Deere's assisted-steering products are built on.

## Who Built It, And Why Them

Deere & Company, and the reason is that it sold the combine the map came from.

The system traces to a **1994 meeting of John Deere engineers** charting future product direction, who identified position accuracy as the thing holding yield mapping back. **In 1997 a team was formed** from Deere's engineering staff, a small project at Stanford University, and NASA engineers at the Jet Propulsion Laboratory. The result is described as developed by Deere's NavCom and precision-farming groups; NavCom Technology remains a Deere subsidiary in Torrance, California.

Why an equipment maker and not a GPS firm: a farm's yield data had value only if the whole chain worked — sensor, display, receiver and correction — and Deere owned every piece except the last. A satellite-delivered correction was the one form that needed no base station on the farm and no line-of-sight radio across rolling ground. It also tied positioning to Deere's own receiver.

## What It Cost

**Accuracy became a thing you rent from your tractor's manufacturer.** StarFire corrections are a proprietary signal, and the receiver that decodes them is Deere's. The shape of the business — equipment plus subscription — is the shape the farm-data platforms that followed still have.

The second cost is dependency: lose the correction and the machine's precision degrades toward what an operator can hold by eye.

## What You Still Touch

Every straight planter pass on a large row-crop farm is held on its line by a corrected GPS fix. Guidance took the steering off the operator; it did not take the hours off, and it left the watching — plugged rows, depth, hazards — with a tired human.

- [[problems/crop-farming/worker-life-1|🟢 Tractor Operator Fatigue During Extended Planting and Harvest]] — the operator the steering was taken from, still in the cab at hour sixteen
- [[problems/crop-farming/low-impact-1|🟡 Farm Management Software Data Entry Burden]] — positioned machine data that still does not flow into the records
- [[niches/crop-farming/variable-rate-prescription-management/profile|Variable-Rate Prescription Management]] — the zone-by-zone treatment the accurate map was meant to justify
- [[niches/crop-farming/large-scale-row-crop-operations/profile|Large-Scale Row Crop Operations]]

**Sources:** WebSearch was unavailable this session (session cap reached); research was by WebFetch on specific URLs only. Wikipedia, *StarFire (navigation system)* — source for the 1994 meeting, the 1997 Deere/Stanford/JPL team, NavCom's role, the Inmarsat L-band delivery, and the SF1 1998 / SF2 2004 / SF3 2016 accuracy figures; Wikipedia, *John Deere* — NavCom Technology as a Torrance, California subsidiary; Wikipedia, *Precision agriculture* — background only. The ~15 m pre-correction accuracy and the bankruptcies of early yield-mapping providers are as stated by the StarFire article; no primary source was reached. ⚠️ **Not established:** the introduction date of Deere's AutoTrac assisted-steering system (neither the Deere nor the precision-agriculture article dates it); the subscription pricing model at launch; the names of the Stanford project or its lead; the date Selective Availability was switched off (not re-verified this session, so not dated here). The Deere-owned-the-chain argument in "Who Built It" is analysis, not a sourced statement of Deere's motive.
