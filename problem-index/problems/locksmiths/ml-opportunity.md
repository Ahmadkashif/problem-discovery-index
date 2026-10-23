# Machine Learning Opportunities — Locksmiths

**Industry:** [[locksmiths|Locksmiths]]
**Derived from:** [[problems/locksmiths/high-impact|High Impact]], [[problems/locksmiths/low-impact-1|Low Impact 1]], [[problems/locksmiths/low-impact-2|Low Impact 2]], [[problems/locksmiths/worker-life-1|Worker Life 1]], [[problems/locksmiths/worker-life-2|Worker Life 2]]

---

## 1. Diagnosing a Failing Opening from Photos and the Ticket
#tacit-knowledge-ml #cnns #object-detection #transfer-learning #large-language-models #evaluation-metrics #worker-facing

**Problem statement:** Senior commercial door technicians look at an opening that won't latch, lock or close and "just know" whether the cause is the closer, a hinge, the frame, the strike, the lock or exit device, or the electrified hardware, and which part to bring. The ML problem is to identify the hardware on an opening from photos and rank the likely causes and parts from visible wear signs, the ticket text and the opening's history, graded by whether the job closed without a callback.

**ML task:** Object detection and fine-grained classification of door hardware (closer, exit device, lock body, trim, hinge type, electric strike, fire label) and of wear signs (rub marks, hinge gap, strike wear, arm geometry); then multi-label cause ranking with a calibrated probability per cause and a recommended parts list
**Input data:** Two to four phone photos per opening at the start of each visit, a short voice note transcribed to text, the client's ticket text, invoice line items (parts and labour), the opening's prior visits, and manufacturer catalogue images for hardware identification.
**Target:** Hardware identity at model level where visible; cause labels from a fixed hierarchy (closer adjustment, closer failure, hinge wear or sag, frame spread, strike alignment, latch or device wear, electrified component or power, other); parts used; callback within 30 and 90 days.
**Evaluation metric:** Top-3 cause recall against the cause that ended callbacks, measured strictly on later jobs, reported against the agreement between senior technicians on the same photo sets as the ceiling. Parts-list recall matters more than precision: a missing part costs a second trip, a spare part costs nothing but truck space. Hardware identification is scored by top-1 and top-5 model accuracy, with "unknown" preferred to a confident wrong model.
**Scope:** The data collection challenge comes first. The expert's read must be captured at the door while they work, so the capture has to take seconds: three photos and a voice note, with everything else drafted from the invoice. Callbacks must be linked to the opening, not the address, which is a data-model change most firms' job systems need before any training. The labelling challenge is disagreement. Causes chain (slamming closer → worn hinge → sagging door → strike rub), and experts favour different fixes, so a sample of openings needs repeated annotation by two or three senior technicians to measure intra- and inter-rater agreement, and the no-callback outcome decides contested labels. The deployment challenge is speed: the technician already has an answer at a glance, so the first useful product is pre-dispatch (load the truck from last visit's photos), not on-site diagnosis. Hardware identification can transfer from catalogue images, but painted-over and decades-old hardware is the hard tail. Team: 2 ML engineers, 1 data engineer and a senior door technician as domain lead, 9–12 months with a commercial door specialist running several thousand openings a year.
**Data availability:** None exists in usable form today. Photos sit in technicians' camera rolls, and causes are implicit in invoice lines. A firm with multi-site contracts can generate thousands of labelled openings a year once capture is built into the job. Manufacturer catalogues (Allegion, ASSA ABLOY, dormakaba brands) supply reference imagery for identification.

---

## 2. Quoting the Lockout From the Call
#large-language-models #gradient-boosting #feature-engineering #evaluation-metrics #automation #revenue-impact

**Problem statement:** An honest lockout business loses the call if it can't give a firm price, and loses money if the price is wrong. Predict the job type, time on site and fair total price from the first minute of the call, so the dispatcher can quote a binding price and the technician arrives knowing what to bring.

**ML task:** Information extraction from call transcripts (property type, lock type, vehicle year, make and model, key type, location, urgency), then gradient-boosted regression of minutes on site and total billed, plus classification of job type and of whether the job will need a different method than quoted (for example drilling rather than picking)
**Input data:** Call recordings or transcripts; dispatch records with timestamps; invoice totals and line items; technician notes; vehicle data decoded from year, make and model; time of day and travel distance.
**Target:** Minutes on site; billed total; job-type class; a "quote miss" flag where the billed total exceeded the quote by more than an agreed tolerance.
**Evaluation metric:** Share of jobs completed within the quoted price band. This is the customer-facing promise and the measure that separates an honest operator from a bait-and-switch one. Then mean absolute error on minutes. Underquoting is worse than overquoting for the business, and overquoting loses calls, so the band is tuned on the conversion and margin trade-off rather than accuracy alone.
**Scope:** The extraction is a solved pattern with current language models. The regression needs a few thousand completed jobs per firm or pooled across firms. 1 ML engineer for 3–4 months on top of an existing call-recording and field-service stack.
**Data availability:** Call recordings exist where firms use cloud phone systems; invoices exist in field-service software. Recording consent rules vary by state and must be followed. Pooling across firms requires a platform or [[answering-services|answering service]] as the aggregator.

---

## 3. Automotive Key Programming Success Prediction
#gradient-boosting #survival-analysis #logistic-regression #feature-engineering #data-integration #evaluation-metrics

**Problem statement:** Predict, before the locksmith leaves the shop, whether a key-programming job on a given vehicle will succeed with the tools and software versions they own, how long it will take, and whether a bench read of the immobilizer module will be needed.

**ML task:** Binary classification of success per tool and procedure, with time-to-completion modelled as a survival problem (jobs abandoned are censored), conditioned on decoded VIN attributes
**Input data:** VIN-decoded attributes (make, model, year, plant, immobilizer generation where known), key type (transponder, remote head, smart proximity), job type (add a key or all keys lost), tool, firmware and software version, procedure used, outcome, minutes, and errors. Contributed by locksmiths or logged by online tools.
**Target:** Success or failure; minutes to success or abandonment; module-damage events.
**Evaluation metric:** Calibration (Brier score) of the success probability by vehicle family, because the locksmith uses it to quote and decide; recall on failures for vehicle variants recently changed by the automaker, where the cost of a wrong "yes" is highest. Concordance index for the time model.
**Scope:** Small-data and long-tailed: thousands of vehicle variants, few jobs each. Hierarchical pooling across trim and year, plus fast updating when a manufacturer changes security mid-year, matters more than model sophistication. 1 data scientist and 1 engineer for 4–6 months, if a tool vendor or a large locksmith network supplies the outcome logs.
**Data availability:** The best data is in tool vendors' online logs and their support tickets, which is their own product telemetry. Locksmith-contributed logs are possible through a community platform. NASTF rules forbid storing the security codes themselves; the outcome log must exclude them, and that is easy to enforce because the model doesn't need them.

---

## 4. Master-Key System Design and Cross-Keying Audit
#combinatorics-and-counting #graph-theory #optimization-fundamentals #compliance #data-integration

**Problem statement:** Given an existing master-key system and a requested change (a new wing, a lost master, a reorganised department), find the minimal-cost rekey and extension plan that introduces no unintended cross-keying, respects the manufacturer's cut rules and preserves capacity for future growth.

**ML task:** Constraint satisfaction and combinatorial optimisation over bitting assignments, with a graph model of keys and cylinders (a key opens a cylinder if its bitting fits the cylinder's shear-line set); an auxiliary model extracts existing systems from scanned bitting charts and key-issue logs
**Input data:** Bitting charts and pinning records (often scanned paper), keyway and manufacturer specifications (depths, maximum adjacent cut), key-issue logs, door schedules and floor plans, and the client's request.
**Target:** A new bitting assignment and pinning list per cylinder; the set of doors exposed by any given key; a costed list of cylinders to re-pin or cores to change.
**Evaluation metric:** Zero unintended cross-keys (a hard constraint, verified exhaustively); cylinders touched and total cost against a locksmith's manual plan; remaining expansion capacity at each level of the hierarchy.
**Scope:** The optimisation is tractable with standard solvers for systems up to tens of thousands of cylinders. The hard part is getting systems out of binders: digitising charts and reconciling them with what is actually installed. 1 engineer with OR background and 1 locksmith with master-keying certification, 4 months to a usable tool.
**Data availability:** Every master-keyed client has a chart somewhere; few have it digitally. Factory keying services at lock manufacturers hold registered systems for patented keyways. Records are usually treated as confidential to the client and the designing locksmith.

---

## 5. Decoding Key Bitting From a Photograph
#cnns #transfer-learning #loss-functions #evaluation-metrics #compliance

**Problem statement:** Estimate the keyway and cut depths of a key from one or two phone photos, both to duplicate keys and to audit key control (does a photographed key match a system key, and could it be copied from a picture?).

**ML task:** Keyway classification plus per-position regression of cut depth (or classification over the manufacturer's depth increments), with geometric normalisation from a reference card or the key's own blade width
**Input data:** Photos of keys against a plain background at varied angles and lighting; ground-truth bittings from code-machine decodes; manufacturer depth and spacing tables.
**Target:** Keyway; depth code at each cut position; confidence per position.
**Evaluation metric:** Exact-bitting accuracy (every position correct). A key with one wrong cut does not work, so position-level accuracy overstates usefulness. Report it by keyway and wear level, and cap acceptance on confidence.
**Scope:** Kiosk networks have shown image-based duplication works at scale for common residential keyways. The locksmith use is narrower: auditing restricted systems and decoding worn originals. 1 ML engineer, 3–4 months, with a code machine to generate labelled data.
**Data availability:** Labels can be produced quickly: photograph keys, decode them on a machine. Restricted and patented keyways are deliberately hard to source, and any public tool that decodes them would undercut the key control it is meant to protect. Deployment should be limited to credentialed locksmiths.
