# Lineage: Agtech Platforms

**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the on-the-go combine yield monitor — Ag Leader's first product, marketed in 1992, which records grain yield and moisture continuously while the combine harvests
**Builder:** Ag Leader Technology
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Before the monitor, a field had one yield.

A grower knew how many bushels came off a field because the grain went across a scale — at the elevator, on a weigh wagon, in a bin whose volume he could estimate. Divide by acres and that was the number. It told him how the field did. It could not tell him how any *part* of the field did.

That mattered because every input decision is made against variation inside the field. Soil changes across a few hundred feet; a wet corner, a sandy knoll and a strip of old fence line all yield differently. Researchers had begun to act on it — the University of Minnesota varied lime rates within fields in 1985, and grid soil sampling followed — but the payoff side of the ledger stayed blank. You could vary what went *in*; you had no way to see what came *out*, place by place.

Measuring it by hand meant harvesting test strips separately and weighing each one. That is what research plots do, which is why evidence lived on research farms and not on the farm that had to make the decision.

## What Got Built

A monitor in the combine cab that measures the grain as it is harvested. Wikipedia's summary of the technique is plain: sensors track grain flow, elevator and combine speed, and moisture, and — once paired with GPS — each measurement is stamped with a position, producing a yield map.

The first half arrived before the second. Ag Leader's founder, Al Myers, began developing an on-the-go yield monitor in 1986, and by his own account "it wasn't until 1992 that I was satisfied with a marketable product." The company, in Ames, Iowa, was founded around it. Mapping needed a usable civilian position signal, and that constraint lifted in stages; the largest single step was the switch-off of GPS Selective Availability on 2 May 2000, which gave civilian receivers undegraded accuracy.

## Who Built It, And Why Them

Ag Leader Technology, and the business case is that of an independent add-on, not a combine maker.

Ag Leader describes the product as something Myers pursued beyond his regular job, over six years, before a company existed — so this is a named-individual build that became a firm at launch. The company still describes itself as prioritising farmer needs over equipment-manufacturer preferences, which is the tell: the monitor was sold as something a grower put *into* a combine, not a feature a manufacturer chose to ship.

What I could not establish is why the combine makers did not get there first, or what Myers' day job was. Both are the obvious questions, and I have no source for either; I am not going to guess.

## What It Cost

The monitor made yield measurable, not trustworthy. Grain takes time to travel from the header to the sensor, so every reading belongs to a spot the combine has already left; header width is keyed in by the operator; moisture calibration drifts through a day; headland turns produce junk. The vault's own problem note lists exactly these errors — flow delay, header width, moisture drift, headland behaviour — as the reason naive strip comparisons "produce confident nonsense."

The deeper trade: the yield map was built as a *picture*. It answered "where was yield low?" and never "what caused it?" A continuous outcome measurement arrived decades before anyone built the treatment-assignment half of an experiment around it.

## What You Still Touch

Every agtech platform ingests yield files as the season's ground truth, and every one inherits the monitor's position lag and calibration drift. The randomised trial the monitor makes possible — strips in the prescription, yield at harvest — is still almost never assembled.

- [[problems/agtech-platforms/high-impact|🔴 Yield Attribution and On-Farm Trial Design]] — the experiment the monitor made cheap and nobody runs
- [[problems/agtech-platforms/low-impact-1|🟡 Cross-Brand Machine Data Reconciliation]] — the monitor's files, multiplied across colours of equipment
- [[niches/agtech-platforms/row-crop-farm-management/profile|Row Crop Farm Management]]
- [[niches/agtech-platforms/machine-data-interoperability/profile|Machine Data Interoperability]]

**Sources:** Ag Leader, "About" and history pages (agleader.com/about/, agleader.com/about/history/) — founding 1992, Al Myers, development from 1986, Ames, the "marketable product" quote, the equipment-manufacturer statement; Wikipedia, *Yield monitoring* (sensor set, 1990s development) and *Precision agriculture* (University of Minnesota lime trials, 1985; grid sampling); Wikipedia, *Global Positioning System* (Selective Availability discontinued 2 May 2000); this vault's `problems/agtech-platforms/high-impact.md` for the error list (vault material, not independent corroboration). WebSearch was unavailable this session (budget exhausted); research was by WebFetch on known URLs. ⚠️ **Not established:** the product's model name — secondary recollection calls it the "Yield Monitor 2000", but Ag Leader's own timeline as fetched was ambiguous about when that name applies, so it is not used here; the sensor mechanism (impact plate vs. other mass-flow designs) in the 1992 unit; Myers' employer while developing it; whether Ag Leader's was the first commercial yield monitor (the company claims "first commercially successful", which I could not check against rivals); why combine manufacturers did not build it first. Extension pages from Purdue and K-State on yield-monitor mechanics returned 404.
