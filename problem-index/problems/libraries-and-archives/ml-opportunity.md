# Machine Learning Opportunities — Libraries & Archives

**Industry:** [[libraries-and-archives|Libraries & Archives]]
**Derived from:** [[problems/libraries-and-archives/high-impact|High Impact]], [[problems/libraries-and-archives/low-impact-1|Low Impact 1]], [[problems/libraries-and-archives/low-impact-2|Low Impact 2]], [[problems/libraries-and-archives/worker-life-1|Worker Life 1]], [[problems/libraries-and-archives/worker-life-2|Worker Life 2]]

---

## 1. Capturing the Selector's Read of Demand and Shelf Life
#tacit-knowledge-ml #gradient-boosting #survival-analysis #time-series-forecasting #feature-engineering #evaluation-metrics #worker-facing

**Problem statement:** Experienced selectors look at a pre-publication title and "know" how many copies each branch needs, whether an ebook licence will earn back its cost, and years later whether the book still earns its shelf space. The ML problem is to learn those reads from the selector's own past decisions and the copy-adjusted outcomes, and surface them in the cart and the weeding list with their track record.

**ML task:** Per-title, per-branch demand regression (first-90-day loans and peak holds per copy) plus survival modelling of time to last meaningful loan, conditioned on the selector's chosen quantity and placement
**Input data:** Order and licence history from wholesaler and OverDrive carts with quantities and dates; ILS circulation and holds aggregated to title-branch-week (never patron level); licence expiry and renewal events; title metadata (BISAC and LCSH subjects, format, series position, author's prior circulation); pre-publication signals such as review stars and publisher print run where available; weeding and withdrawal records.
**Target:** Copy-adjusted loans and holds ratio over fixed horizons; time from acquisition to last loan before withdrawal; and, for the ledger, whether the selector's stated demand band was met.
**Evaluation metric:** Out-of-time error on demand bands against a baseline of the selector's own historical quantities — a model that only matches the selector adds nothing. Concordance index for the survival model on withdrawals. For licences, the share of expired licences that would have been correctly flagged as not worth renewing, weighted by their price; under-forecasting a breakout title (a holds queue of months) costs more goodwill than over-buying a copy, so recall on high-demand titles is reported separately.
**Scope:** The data collection challenge comes first: the selector's decision and its reasons must be captured inside the cart in seconds, and the titles passed over must be logged too, or the model only ever sees bought titles. The labelling challenge is that circulation is shaped by the decision itself (more copies and display drive more loans), so labels need copy and placement adjustment and a held-out sample of titles re-judged by the same selector to measure their own consistency, which sets the ceiling. The deployment challenge is speed and trust: the suggestion must appear beside the title in the vendor cart faster than the selector's glance, and a library will only trust it after it has been shadow-scored against the selector for a season. 1 ML engineer and 1 data engineer working with two or three library systems' selectors, 6–9 months; value appears first as retrieval ("titles like this one, how many copies we bought, how they did") before any forecast is trusted.
**Data availability:** Circulation and order history sit in each library's ILS and vendor accounts and are clean at title level. Patron privacy statutes rule out person-level features, which is a constraint rather than a blocker. The decision rationale does not exist and must be captured prospectively; consortia that share an ILS offer pooled title-level history across many small libraries.

---

## 2. Cancellation Impact Modelling for E-Resource Packages
#causal-inference #linear-regression #time-series-forecasting #hypothesis-testing #confidence-intervals #data-integration

**Problem statement:** Before a journal package or database renews, estimate what cancelling it — or moving to title-by-title subscriptions — will actually cost readers, measured as the interlibrary loan, document delivery and lost access that follow, rather than as raw downloads.

**ML task:** Counterfactual demand estimation per title after cancellation, using libraries that already cancelled as natural experiments, plus open-access substitution modelling
**Input data:** COUNTER Release 5 / 5.1 title-level usage and turnaway reports; KBART holdings and perpetual-access entitlements; prices and multi-year caps; interlibrary loan and document delivery requests by title; open-access availability by article; publication and citation activity of the library's own faculty; cancellation histories from peer libraries and consortia.
**Target:** Post-cancellation requests per title per year and their cost; the share of prior downloads that open-access copies would have served.
**Evaluation metric:** Prediction error on post-cancellation request volume, back-tested on libraries that cancelled packages, with confidence intervals reported to the committee. Over-estimating the cost of cancelling locks a library into a package it does not need; under-estimating it produces faculty backlash, so the asymmetry depends on the library's appetite and should be shown as a range rather than a point.
**Scope:** The causal piece is the hard part: downloads overstate need because many are casual, and only cancellations reveal real demand. A consortium pooling several members' cancellation histories is the natural owner. 1 data scientist and 1 engineer, 4–6 months to a usable harness; each renewal thereafter in days.
**Data availability:** COUNTER reports are harvestable through SUSHI by every subscribing library. Interlibrary loan data sits in ILLiad, Tipasa or Rapido. Price data is often under confidentiality clauses, which limits pooling across libraries.

---

## 3. Sensitive-Content Triage for Digitised Collections
#bert #transformers #cnns #evaluation-metrics #compliance #automation

**Problem statement:** Classify every page of a digitised archival collection for personal and restricted information — identity numbers, student and patient records, information about living third parties, culturally sensitive material — so archivists review only the flagged pages before publication.

**ML task:** Page- and passage-level multi-label classification on OCR and handwriting-recognition output, with document-type classification (personnel file, transcript, medical form, correspondence) from page images
**Input data:** Page images and OCR text from digitised collections; finding aids and folder titles; donor agreements and restriction dates; archivists' past redaction and closure decisions where recorded.
**Target:** Per-page labels by restriction category and a folder-level recommendation (open, review, restrict until date).
**Evaluation metric:** Recall on pages an archivist would restrict is binding: a missed social security number or student record published online is a legal and ethical failure, while a false flag costs a minute of reading. Report reviewer pages read per collection against the full-read baseline, at a recall floor agreed with the archive.
**Scope:** OCR quality on typescript, carbon copies and handwriting drives most of the error, so the pipeline needs an image-quality stage first. Training labels are scarce because past closures were recorded at folder level; a few thousand page-level labels from two or three archives are enough for a usable first model with transfer learning. 1 ML engineer and an archivist lead, 4–5 months.
**Data availability:** Archives hold the images; labels must be created. Restricted material cannot leave the institution, so training happens on-premises or in the archive's own cloud tenancy.

---

## 4. Subject and Classification Suggestion for Original Cataloguing
#transformers #large-language-models #k-nearest-neighbors #word-embeddings #evaluation-metrics #automation #worker-facing

**Problem statement:** For items that have no usable shared record, propose Library of Congress Subject Headings, a classification number and matched name authorities from the item's title page, contents and any digital text, ranked with evidence for the cataloguer to accept or correct.

**ML task:** Extreme multi-label classification over the LCSH vocabulary plus hierarchical classification into LCC or Dewey, with nearest-neighbour retrieval of similar catalogued works
**Input data:** Millions of existing MARC records with subjects and call numbers (from a library's own catalogue or shared catalogue data under its licence terms); title-page images, tables of contents and abstracts; LCSH and name authority files, which the Library of Congress publishes openly.
**Target:** Ranked subject headings, a class number, and authority links per item.
**Evaluation metric:** Precision at the top three suggested headings and exact-match rate on class number at the level the library uses, measured against held-out cataloguer records — and against a second cataloguer on a sample, because cataloguers agree with each other on subjects far less than on description. Time per record before and after is the adoption metric.
**Scope:** The long tail of rare headings and non-English material is where help is needed and where training data is thinnest. Retrieval of similar records gives most of the early value. 2 engineers, 4 months to a pilot in one library's cataloguing editor.
**Data availability:** Authority files are public; bibliographic records are abundant but their reuse is governed by WorldCat's record-use policy and vendor licences, so training sets must be built from records the library or consortium has rights to.

---

## 5. Handwriting and Degraded-Text Recognition for Archival Description
#cnns #transformers #seq2seq #transfer-learning #evaluation-metrics #automation

**Problem statement:** Transcribe handwritten and degraded typescript archival pages well enough to support search, folder-level summaries for finding aids, and the sensitive-content triage above.

**ML task:** Handwritten text recognition (image-to-sequence) with layout analysis, fine-tuned per collection or hand
**Input data:** Page images at preservation resolution; existing transcriptions from crowdsourcing projects and earlier editorial work; collection-level metadata on dates, languages and creators.
**Target:** Line-level transcriptions with confidence, and folder-level keywords and summaries.
**Evaluation metric:** Character error rate on held-out pages per collection, plus retrieval success on a set of researcher queries — a transcript that is 85% accurate can still make a collection findable, so the search metric matters more than perfect text.
**Scope:** Off-the-shelf models handle modern print well and 19th-century hands poorly; a few hundred transcribed lines per hand fine-tune a usable model. 1 engineer, 3–4 months to integrate with a repository and the finding-aid workflow.
**Data availability:** Crowdsourced transcription projects at national and university archives provide training pairs; most collections have none, so the first transcriptions are human-corrected model output.
