# Machine Learning Opportunities — Music Publishers

**Industry:** [[music-publishers|Music Publishers]]
**Derived from:** [[problems/music-publishers/high-impact|High Impact]], [[problems/music-publishers/low-impact-1|Low Impact 1]], [[problems/music-publishers/low-impact-2|Low Impact 2]], [[problems/music-publishers/worker-life-1|Worker Life 1]], [[problems/music-publishers/worker-life-2|Worker Life 2]]

---

## 1. Learning the Sync Rep's Brief-to-Song Match
#tacit-knowledge-ml #transformers #contrastive-learning #word-embeddings #evaluation-metrics #feature-engineering #revenue-impact #worker-facing

**Problem statement:** Experienced sync reps read a brief and know which five songs, out of tens of thousands, the supervisor will actually license, given what that supervisor has bought before, what "seventies soul feel" means from that agency, and which songs can be cleared at the budget. The ML problem is to learn that match from the team's own history of briefs, pitches, shortlists and licences, and rank the catalogue for the next brief the way a senior rep would.

**ML task:** Learning-to-rank over a dual-encoder retrieval stage (brief encoder against song encoder), conditioned on the recipient, plus a fee-band classifier for each suggested song
**Input data:** Brief emails and attachments (text, reference tracks, budget, media, term, territory); pitch playlists from DISCO or Synchtank; quote requests, licences and fees from the rights system; song audio, lyrics, writer, era and genre metadata; each song's licence and clearance history (co-publisher approvals, master restrictions).
**Target:** For each brief, the songs pitched, shortlisted (a quote was requested) and licensed, as graded relevance; and the fee band a licence closed at.
**Evaluation metric:** Recall at 10 of the eventually licensed or shortlisted song among the model's suggestions, against the songs the rep actually sent, measured on briefs held out by time. Report NDCG for the graded labels, and time from brief to pitch list. A suggestion that cannot be cleared for the use is a hard error that is never acceptable. Missing a good song costs a placement, while an unclearable suggestion costs the rep's trust in the tool.
**Scope:** The data-collection challenge comes first and is most of the work. Brief, pitch and outcome live in email, a pitch tool and a rights database with no shared key, so the first deliverable is a ledger that joins them automatically, without asking reps to fill in forms under deadline. The labelling challenge is that silence after a pitch is not a negative. Reps disagree with each other and with themselves about fit, so a sample of briefs should be re-ranked blind by two or three reps to measure agreement, which sets the ceiling the model is judged against. The deployment challenge is speed: the list must arrive within minutes, be shorter than the rep's own and explain itself in the rep's terms, or it will be ignored. Expect 2 ML engineers and a data engineer working with one sync team for 6–9 months. Value arrives first as retrieval ("songs this supervisor licensed that resemble this brief") before any ranker is trusted.
**Data availability:** Every publisher holds its own licences and fees. Briefs and pitch histories sit in email and pitch tools, usable once joined. Audio embeddings come from licensable models or vendors. A mid-size team accumulates a few thousand brief-outcome records a year (estimate), enough for retrieval and per-recipient re-ranking but thin for a model of each supervisor.

---

## 2. Song-Level Earnings Decay Forecasting for Catalogue Underwriting
#time-series-forecasting #survival-analysis #gradient-boosting #bayesian-inference #confidence-intervals #revenue-impact

**Problem statement:** Every catalogue price is a forecast of how each song's earnings decline, stabilise or revive, by income type, over ten years or more. Forecast song-level net publisher share by source from the song's earnings history and usage signals, with honest uncertainty, so a catalogue can be valued bottom-up rather than with a single multiple.

**ML task:** Hierarchical probabilistic forecasting of song-by-source earnings, pooled across songs of similar age, genre and income mix, with a hazard component for revival events (sync placements, covers, viral moments)
**Input data:** Song-level royalty histories by source and territory, quarterly, going back decades in a publisher's own records or a data room; streaming and airplay time series; sync licence history; release dates and the song's age; writer and performer attributes; rate changes (Phonorecords determinations, PRO rate settlements) as known regime shifts.
**Target:** Earnings per song and source for each of the next 40 quarters; catalogue-level totals with prediction intervals.
**Evaluation metric:** Out-of-time error on catalogue totals at 3- and 5-year horizons, measured on catalogues whose later history is known, and the coverage of the 80% intervals. A model whose intervals are too narrow is worse than a wider honest one. Overestimating earnings costs the buyer money and the asset-backed security its rating, so error should be reported separately for over- and under-forecasts.
**Scope:** Modest modelling with demanding data. The hard part is normalising decades of statements into song-by-source series and handling regime shifts, since rate changes are not decay. Expect 2 data scientists and a data engineer for 5–6 months for a first version, validated on the owner's own back catalogue.
**Data availability:** Large owners and valuers hold rich histories. A buyer sees a seller's data only under NDA in a data room, so a buyer-side model learns from the buyer's own catalogue and applies it to the target.

---

## 3. Expected-Versus-Received Income Gap Detection
#gradient-boosting #linear-regression #hypothesis-testing #feature-engineering #data-integration #revenue-impact

**Problem statement:** Estimate what each work should have earned from each source and territory in each period, from usage evidence, and flag shortfalls large enough to be a missing registration, an unresolved conflict or a society failing to pay. Prioritise them by recoverable value and by the deadline after which the money is shared out by market share.

**ML task:** Regression of expected income per work, source, territory and period from usage features, with residual-based anomaly flags and a classifier for the likely cause
**Input data:** Streams by country from DSP and consumption data; airplay and broadcast detections from monitoring vendors; sync and cue sheet data; received statement lines by source; registration status by society; known rate tables and conversion factors.
**Target:** Expected income and its interval; whether a flagged gap was later recovered after a claim, and how much.
**Evaluation metric:** Precision of flagged gaps confirmed as recoverable, and dollars recovered per analyst hour, against the current practice of checking top earners by hand. Recall matters most for gaps facing a deadline: the MLC's first market-share distribution in April 2027 and the three-year non-distributable rule for EU societies.
**Scope:** Usage-to-income conversion differs by society and source, so expect a model per source family. Expect 2 data scientists and an analyst for 4–5 months. The first useful output is a ranked claim list for the top few territories.
**Data availability:** Statements are the publisher's own. Usage data needs licensed consumption and monitoring feeds. Recovery outcomes must be logged going forward to train the cause classifier.

---

## 4. Share Conflict Triage and Evidence Retrieval
#large-language-models #random-forests #k-nearest-neighbors #evaluation-metrics #workflow-orchestration #automation

**Problem statement:** Classify each incoming conflict or counterclaim by its likely cause, retrieve the agreements and documents that settle it, predict whether the publisher is likely to prevail, and rank the queue by money in suspense.

**ML task:** Multi-class cause classification plus a resolution-outcome classifier; nearest-neighbour retrieval of similar past conflicts; language-model extraction of relevant clauses from scanned agreements
**Input data:** Conflict notices from the MLC, PROs, foreign societies and YouTube; the publisher's registrations and deal records; scanned agreements and letters of direction; past conflict files and outcomes.
**Target:** Cause category (duplicate work, expired term, successor assignment, split error, bad-faith claim); prevail or concede; days to resolution.
**Evaluation metric:** Accuracy of the cause label, and the precision of "concede" recommendations. Conceding a share that was the publisher's loses income permanently, so concede predictions need high precision, while a wrongly contested case only costs time. Measure coordinator time per resolved conflict before and after.
**Scope:** Expect 1 ML engineer, 1 data engineer and a senior coordinator as subject expert for 4 months. Past outcomes are recorded thinly and must be reconstructed for a training sample.
**Data availability:** Conflict notices and outcomes sit in portals and email. Agreements need scanning and OCR at older publishers.

---

## 5. Agreement Extraction for Termination and Reversion Windows
#large-language-models #transformers #seq2seq #evaluation-metrics #compliance #automation

**Problem statement:** Extract from publishing agreements the facts that decide when a song can be terminated under Sections 203 or 304 or will revert by contract, compute the windows and deadlines, and source each to a page and clause.

**ML task:** Document field extraction (grant date, parties, whether the author executed the grant, work-for-hire language, works covered, territory, term, reversion and retention clauses) followed by rule-based window computation
**Input data:** Scanned and digital agreements, schedules of works, Copyright Office registration and recordation records, publication dates from release data.
**Target:** Structured fields with clause citations; termination windows, service and recordation deadlines per work and grant.
**Evaluation metric:** Field-level accuracy against lawyer-reviewed samples. Recall on terminable grants is the binding metric, because a missed window is a lost copyright or an overpaid acquisition, while a false flag costs a lawyer's reading time.
**Scope:** Expect 1 ML engineer and a music lawyer reviewing samples for 3–4 months. Old typed agreements and handwritten amendments are the hard tail.
**Data availability:** Each publisher holds its own agreements. Sharing a labelled set across publishers is unlikely, so each model is trained per catalogue with a shared extraction schema.
