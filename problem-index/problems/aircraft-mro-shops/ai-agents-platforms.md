# AI Agents & Platform Opportunities — Aircraft MRO & FBO Shops

**Industry:** [[aircraft-mro-shops|Aircraft MRO & FBO Shops]]

---

## 1. Work-Card AD and SDR Checker
#ai-agent #large-language-models #transformers #compliance #automation #quick-win

**Concept:** An agent that sits between the work package and the inspector's signature. It reads the draft work cards and engineering orders for an aircraft, works out which airworthiness directives apply from the aircraft's configuration, checks that each card cites the current revision and an approved method or AMOC, recomputes recurring intervals, and attaches the Service Difficulty Reports filed on the same part number. Every flag carries the AD paragraph or SDR behind it, so the inspector reviews findings instead of re-reading the library. This is the owner's MVP. The rules side is public (FAA ADs in DRS and the Federal Register, plus the yearly SDR files), but the aircraft's configuration, embodied service bulletins, AD status and work cards are customer records, so a first demo runs on public ADs and SDRs against a synthetic aircraft and work package.
**Inputs:** Work cards and engineering orders (PDF or maintenance-system export); aircraft configuration and AD status from the tracking system; FAA ADs, AMOC letters on file; SDR CSVs; licensed service bulletins where available.
**Outputs / Actions:** A per-package compliance report (applies / doesn't / can't determine, with reason), flagged cards, corrected interval calculations, a list of related SDRs per card, and an audit trail of what was checked and when.
**Why now:** Language models can turn the fixed Federal Register structure of an AD into checkable rules. SDRs come as free yearly CSV downloads, but ADs do not: no bulk download or API for the FAA's Dynamic Regulatory System was found, so an AD library has to be built from the Federal Register API (317 final ADs in 2025), which does not carry every emergency AD, plus DRS lookups. SDRs are also ~93% air-carrier submissions (Cessna has 1,348 of 2025's 67,652), so the SDR signal is thin for the business and general aviation shops most likely to buy first. The vendors that would sell this are hiring engineers now: Zymbly (YC W26) lists a Forward Deployed Engineer in San Francisco or London at $120K–$180K plus 0.5–1.25% equity, on-site in hangars, building connectors to legacy ERPs; Fleetcraft lists a Founding Engineer in London only; CAMP Systems lists a Senior Software Engineer in Merrimack, New Hampshire (checked on their own boards or YC job pages, 24 October 2026).
**Market:** Every Part 145 station, FBO maintenance shop and IA signing general aviation annuals, plus airline engineering departments. Tracking vendors (CAMP, Traxxall, Veryon) are the natural incumbents but stop at the due list. A checker is either a module they buy or a wedge for an AI entrant.

---

## 2. Technician Voice-to-Record Assistant
#ai-agent #large-language-models #seq2seq #worker-facing #automation #compliance

**Concept:** An assistant that lets a mechanic describe the work in their own words at the aircraft, then drafts the 43.9-compliant entry with the right manual reference and ATA code, reads part data from a tag photo, and posts the same record to the work order, the operator's tech log and the tracking system. It also answers "how was this fixed last time?" from the shop's own history and the manuals. It flags whatever a QA reviewer would reject before the mechanic signs.
**Inputs:** Voice or text notes, photos of tags and data plates, the work order, the aircraft's maintenance manual and fault isolation manual, the shop's past write-ups and QA rejections.
**Outputs / Actions:** Draft logbook and work-order entries for sign-off; parts records; suggested troubleshooting steps with sources; QA pre-check results.
**Why now:** Speech recognition is accurate in a noisy hangar, and language models can map plain speech to a shop's house style and approved-data references. Zymbly's posting (San Francisco or London) describes "an AI-native operating system for airline operations" that guides mechanics through repairs and inspections, and claims three of the top 10 airlines in Europe and the US as customers (company claim). Fleetcraft, hiring in London only, says it turns technician input into compliant records and quotes from RFQs.
**Market:** Airline line maintenance, MROs and FBO shops, paid per technician seat. Competes with Veryon's AIRE and the maintenance-system vendors' own mobile apps. Wins where the draft passes QA without a callback.

---

## 3. Engine Shop Visit Workscope and Turn-Time Planner
#ai-platform #gradient-boosting #survival-analysis #feature-engineering #revenue-impact #workflow-orchestration

**Concept:** A planning platform for engine and component shops that turns an incoming engine's records, borescope findings and LLP status into a recommended workscope (module by module: restore, repair, replace with new or used serviceable material) and a turn-time quote with a range. It then tracks the shop visit against parts and repair-vendor lead times and re-forecasts the release date daily.
**Inputs:** Engine records and LLP status, on-wing borescope findings, engine trend data, the shop's historical workscopes and findings by module, parts availability and quotes (including used serviceable material offers from distributors), repair-vendor turn times, test-cell schedule.
**Outputs / Actions:** Workscope options with cost and expected on-wing life; a quoted turn time with confidence range; daily critical-path updates and customer status drafts; alerts when a parts or repair-vendor delay will move the release date.
**Why now:** Engines are the largest MRO segment ($14.8B of North America's $31.8B in 2026, Oliver Wyman), shop turn times are far above pre-pandemic levels, and operators now choose shops on a believable date as much as on price. Gradient-boosting and survival models on a shop's own history can produce the honest ranges planners don't have today.
**Market:** Independent engine shops (StandardAero, with about 8,000 staff and $6.06B 2025 revenue, describes itself as the largest independent pure-play engine aftermarket provider), airline engine shops and component repair shops. Engine OEM networks are both competitors and customers. Used-serviceable-material trading itself belongs to the queued aviation parts distributors industry.

---

## 4. Records Transition Agent
#ai-agent #large-language-models #graph-theory #data-integration #compliance #automation

**Concept:** An agent that ingests an aircraft's or engine's scanned records ahead of a shop visit, sale or lease return. It builds the back-to-birth history for every life-limited part, the AD compliance history and the major repair and alteration file, then produces the gap list a buyer's records auditor would raise, with the source page for every number and drafted requests for the missing documents.
**Inputs:** Scanned log books, LLP sheets, shop visit reports, 8130-3 and EASA Form 1 tags, operator utilisation statements, AD records, 337 forms and repair approvals.
**Outputs / Actions:** Structured part-history graph, LLP status with remaining cycles, AD compliance matrix, gap report, document request drafts, and a delivery-ready records index.
**Why now:** Document AI reads handwritten and mixed-format records well enough to draft a first pass, and buyers have read every page since the AOG Technics forgeries (over 60,000 suspect parts, sentenced February 2026). Soji AI, which announced a records partnership with Active Partners in May 2026, lists a senior Forward Deployed Engineer (Aviation) in Hamburg only (hybrid, not a US role) to embed with airline, MRO and lessor customers for one to two years. JSSI, Traxxall's parent, lists a Director of Data Engineering in Chicago.
**Market:** MRO records departments and engine shops at induction; operators preparing redeliveries; lessors, whose side of the transition belongs to the queued aircraft and railcar lessors industry. Records platforms (flydocs, Bluetail) and records consultancies are the incumbents.
