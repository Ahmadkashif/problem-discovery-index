# Machine Learning Opportunities — Film Distributors

**Industry:** [[film-distributors|Film Distributors]]
**Derived from:** [[problems/film-distributors/high-impact|High Impact]], [[problems/film-distributors/low-impact-1|Low Impact 1]], [[problems/film-distributors/low-impact-2|Low Impact 2]], [[problems/film-distributors/worker-life-1|Worker Life 1]], [[problems/film-distributors/worker-life-2|Worker Life 2]]

---

## 1. Learning the Acquisitions Executive's Read of a Festival Film
#tacit-knowledge-ml #gradient-boosting #bayesian-inference #transformers #confidence-intervals #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Experienced buyers watch a film once, in a festival room, and "know" whether it will play theatrically, travel internationally and carry an awards campaign. That judgement prices a minimum guarantee and a P&A commitment, and it leaves with the buyer. The ML problem is to learn it from the buyer's own dated reads and the outcomes that followed, and to return a calibrated range of outcomes by window with the nearest comparables, before the bid.

**ML task:** Multi-output regression of ultimates by window (domestic box office, premium VOD, subscription licence, international minimum guarantees, ad-supported revenue), with calibrated prediction intervals. Also passage-level classification of the buyer's voice notes into a fixed vocabulary of reads (festival film versus theatrical film, travels versus domestic, awards path, trailer-dependent).
**Input data:** The buyer's notes and voice memos per screening, structured into a bid ledger. Film metadata (genre, runtime, cast and director history, budget band, sales agent). Screening context: programme slot, festival section, audience response captured with consent, first-week critics' scores. Embeddings of the film's trailer, audio and dialogue. Comparable-title outcomes from public box office and the firm's own statements. Films passed on whose public performance is known.
**Target:** Window-level revenue over 24 to 36 months; whether the film expanded past a set screen count; whether it received major awards nominations; and agreement between the model's read labels and the buyer's.
**Evaluation metric:** Interval coverage and pinball loss on window revenue, measured strictly out of time by festival year: a random split leaks the market cycle. For the read labels, agreement with held-out buyer annotations, reported against the buyer's own test-retest agreement on re-watched films as the ceiling. Over-bidding costs more than under-bidding on most films, because a lost auction costs an opportunity and an overpaid guarantee costs cash. Report the over-prediction rate at the price actually paid as the headline business metric.
**Scope:** The data collection challenge comes first. The read must be captured while the buyer is in the festival, so the system needs a near-zero-effort capture surface: a voice note after each screening, drafted into a record for one-tap confirmation. Historical bids must be reconstructed from email and deal memos. The labelling challenge is that revenue confounds the bid with marketing spend, release dating and luck, and the films not bought are unobserved. The outcome therefore needs adjustment for P&A and release width, the passed-on films need inclusion from public data, and the buyer needs to re-rate a sample of films to estimate intra-rater reliability. The deployment challenge is that the output must arrive between the screening and the bid, faster than the buyer's own recall of comparables, so the first release is retrieval ("the five most similar films you saw, what you said, what they earned") before any forecast is trusted. 1 ML engineer and 1 data engineer embedded with an acquisitions team for 9 to 12 months, plus a festival season of capture, before forecasts are credible.
**Data availability:** Public box office and festival records are available. Window-level revenue sits in the distributor's own statements and licensee reports, scattered across formats. The decisive asset, the buyer's dated read, barely exists and must be built. A single mid-sized distributor buys ~10 to 30 films a year (estimate), so models need pooling across a consortium or heavy use of public comparables.

---

## 2. Rights Extraction and Avails Resolution From Contracts
#large-language-models #transformers #bert #sets-and-logic #evaluation-metrics #compliance #automation #data-integration

**Problem statement:** Convert acquisition agreements, sales-agent grants, licences, deal memos and amendments into a structured rights grid (title × territory × medium × window × term × exclusivity × language × holdback). Then answer avails queries and detect conflicts between a proposed grant and existing grants, citing the clause behind every answer.

**ML task:** Clause-level information extraction into a controlled rights schema; normalisation of media and territory definitions; amendment-chain resolution; rule-based interval and set logic for conflict detection over the extracted grid
**Input data:** Executed contracts in PDF and scanned form, deal memos in email, amendment letters, the distributor's existing rights spreadsheet as weak labels, and sales-agent avails sheets.
**Target:** Structured grant records with source clause spans and confidence; for queries, available / unavailable / conditional with the blocking grants listed.
**Evaluation metric:** Field-level precision and recall on a hand-labelled set of contracts, with recall on restrictive terms (holdbacks, exclusivity, reversion triggers) as the binding metric, because a missed restriction causes a double grant while a false one costs a lookup. Query-level accuracy against answers given by senior rights staff. Zero tolerance for an "available" answer without a cited source.
**Scope:** The schema and the media-definition mapping are the hard part; models extract clauses well once the vocabulary exists. 2 engineers and a rights specialist, 5 to 6 months to a production version for one distributor's library; the vocabulary transfers across firms.
**Data availability:** Every distributor holds its own contracts. Labels come from rights coordinators' existing spreadsheets, which are partial and sometimes wrong. A few hundred labelled contracts are enough to evaluate.

---

## 3. Platform-Release Expansion and Run-Length Forecasting
#gradient-boosting #time-series-forecasting #survival-analysis #bayesian-inference #feature-engineering #revenue-impact

**Problem statement:** For a specialty film opening in a handful of theatres, forecast each candidate theatre's weekly gross and the number of weeks it will hold, so the distributor decides which markets to expand into, when, and whether an Academy-qualifying or Best Picture expanded run is achievable within the rules' windows.

**ML task:** Hierarchical forecasting of theatre-week grosses with partial pooling across films and theatres; survival modelling of run length; expansion recommendation under a print-and-advertising budget
**Input data:** Theatre-level daily grosses from box office reporting; the firm's own historical engagements and settlements; theatre attributes (market, circuit, arthouse versus commercial, screen count); film attributes; reviews and word-of-mouth exit-poll scores; competing releases by week.
**Target:** Weekly gross per theatre-week; weeks to drop below the holdover threshold.
**Evaluation metric:** Weighted absolute percentage error on second- and third-week grosses for theatres not yet played, out of time by release, against a per-screen-average heuristic baseline. Calibration of run-length survival curves. Report decision value separately: grosses captured per P&A dollar for the recommended expansion against what the team actually did.
**Scope:** Modest modelling and a real dataset problem. Theatre-level history is licensed, and the firm's own settlements have to be cleaned. 1 data scientist, 4 months.
**Data availability:** Box office data is licensable at theatre level. Settlement histories sit in the distributor's accounting system. Specialty releases are few per firm, so cross-film pooling is essential.

---

## 4. Shot-Level Search Over Archival Footage
#contrastive-learning #transformers #cnns #transfer-learning #evaluation-metrics #automation

**Problem statement:** Make a digitised archive of film and tape searchable at the level of the individual shot, by natural-language request and by example, so a researcher finds a clearable clip in minutes rather than hours.

**ML task:** Shot boundary detection, vision-language embedding and retrieval, fine-tuned with the library's own request-to-licensed-clip history; period and location classification as auxiliary heads
**Input data:** Digitised footage with existing reel-level metadata; past research requests and the clips eventually licensed against them; transcripts; catalogue rights flags.
**Target:** A ranked list of shots with timecodes per request.
**Evaluation metric:** Recall@20 of the clip the researcher ultimately licensed, on historical requests, and median researcher time to a sent screener. Period accuracy matters more than generic object accuracy, because a 1970s car in a "1960s" request costs the licence.
**Scope:** Off-the-shelf vision-language models get most of the way. Fine-tuning on the library's own licensing history is the differentiator, and so is compute to index tens of thousands of hours. 2 engineers, 4 months, plus indexing compute.
**Data availability:** The library owns the footage and its request and licence history, which is the training signal nobody else has. Legacy footage quality (scratches, monochrome, interlacing) degrades off-the-shelf models and needs fine-tuning data.

---

## 5. Statement Reconciliation and Unusual-Deduction Detection
#large-language-models #gaussian-mixture-models #feature-engineering #evaluation-metrics #compliance #data-integration

**Problem statement:** Ingest licensee, platform, sub-distributor and exhibitor statements in their native formats, map every line to the distributor's waterfall, reconcile receipts against contracts, and flag deductions, fees and expense allocations that are unusual for that counterparty or that title. This is the same work a producer's auditor does by hand later.

**ML task:** Document understanding and line-item mapping to a fixed chart of revenue and expense categories; density modelling of deduction rates by counterparty, window and territory to surface outliers
**Input data:** Quarterly statements in PDF, spreadsheet and portal export; licence contracts and their fee and expense terms; historical statements per counterparty.
**Target:** Mapped statement lines; reconciliation status per contract; outlier flags with the expected range.
**Evaluation metric:** Line-mapping accuracy on a labelled sample; precision of outlier flags at a review budget of a fixed number of flags per quarter, because reviewers will ignore a noisy queue; dollars of confirmed discrepancies recovered.
**Scope:** Format variety is the cost driver: dozens of counterparties, each with their own layout. 1 engineer and 1 royalty accountant, 4 months to cover the top counterparties.
**Data availability:** The distributor holds its inbound statements. Labels come from accountants' existing reconciliations. Outlier ground truth is thin and should be built from resolved disputes going forward.
