# Machine Learning Opportunities — Court Reporting Firms

**Industry:** [[court-reporting-firms|Court Reporting Firms]]
**Derived from:** [[problems/court-reporting-firms/high-impact|High Impact]], [[problems/court-reporting-firms/low-impact-1|Low Impact 1]], [[problems/court-reporting-firms/low-impact-2|Low Impact 2]], [[problems/court-reporting-firms/worker-life-1|Worker Life 1]], [[problems/court-reporting-firms/worker-life-2|Worker Life 2]]

---

## 1. Learning the Reporter's Read of an Unrecoverable Passage
#tacit-knowledge-ml #transformers #lstms-and-grus #seq2seq #feature-engineering #evaluation-metrics #worker-facing

**Problem statement:** Experienced stenographers sense, within a second, which passages their writing or the audio will not survive, and decide whether to interrupt the proceeding or write through. Learn that judgement from their own stroke streams, audio and certified transcripts, so it can be given back to them in realtime and to digital reporters who have no stroke signal at all.

**ML task:** Sequence labelling over the aligned stroke-and-audio stream: per-token probability that the realtime translation differs from the certified text, plus a passage-level classifier of whether the error is recoverable from audio (multi-channel signal quality, overlap, speaker change). A secondary head predicts the reporter's interrupt decision from colloquy markers.
**Input data:** CAT job files with stroke codes, timestamps, raw translations and edit histories (Case CATalyst, Eclipse); synchronised multi-channel audio; the final certified transcript; colloquy lines marking reporter interruptions and readbacks; the reporter's dictionary; exhibit lists and case vocabulary.
**Target:** Token-level "changed in edit" labels with error type (untranslate, mistranslate, misattributed speaker, missed word); passage-level recoverable/unrecoverable; interrupt/no-interrupt where a colloquy exists.
**Evaluation metric:** Recall of passages that required substantive correction, at a precision the reporter tolerates in realtime (false flags cost attention while writing). Measure separately on unrecoverable passages, where a miss leaves a permanent gap. Report per-reporter results against the reporter's own re-edit consistency on a blind sample as the ceiling, and edit minutes per transcript page before and after.
**Scope:** The data collection challenge comes first: reporters must opt in to preserving raw translations and audio before editing, and the interrupt decisions that did not happen leave no trace, so a sample of jobs needs the reporter to mark "should have stopped" passages afterwards. The labelling challenge is that the certified transcript is both output and ground truth, and reporters resolve the same stroke differently on different nights. That means a repeated blind re-edit sample to estimate intra-rater agreement, and errata and readbacks as sparse independent labels. The deployment challenge is the one-second window: a flag that arrives late or clutters the writing screen will be switched off, so the first release is the post-job ranked edit queue and realtime flags follow only once precision is proven. Roughly 2 ML engineers and a reporter-in-residence, 9–12 months, starting with a cohort of 20–50 reporters on one CAT platform.
**Data availability:** Rich but scattered. Every job produces stroke-level files, but they sit on contractors' laptops under personal dictionaries, and agencies cannot pool them without each reporter's consent. A CAT vendor or a large agency with an opt-in programme is the realistic data holder.

---

## 2. Forced Alignment of Transcript to Video and Audio
#hidden-markov-models #dynamic-programming #transformers #evaluation-metrics #automation #quick-win

**Problem statement:** Video depositions must be synchronised to the certified transcript line by line so trial teams can cut clips by page and line. Align the certified text to the recording automatically and flag lines where the alignment, or the transcript, is doubtful.

**ML task:** Forced alignment of known text to audio (acoustic model plus dynamic-programming alignment), with confidence per line and detection of off-record segments, overlaps and gaps.
**Input data:** Certified transcript with page-line structure and timestamps from the CAT realtime feed where available; deposition video and multi-channel audio; on/off-record markers.
**Target:** Start and end time per transcript line; confidence; flagged regions where text and audio disagree.
**Evaluation metric:** Share of lines aligned within 0.5 seconds of human-synchronised reference, and recall of transcript-audio disagreements. A clip that starts mid-answer in front of a jury is the costly failure.
**Scope:** Mature techniques; the work is legal formatting, page-line fidelity and edge cases (interpreters, exhibits read aloud, crosstalk). 1–2 engineers, 3–4 months. Overlaps with the videographer's own sync tools; the reporting firm's advantage is the stroke timestamps.
**Data availability:** Agencies hold synchronised video and transcripts for past jobs as reference pairs; the recordings belong to the case, so training should use opt-in or synthetic sets.

---

## 3. Errata Classification: Reporter Correction or Changed Testimony
#bert #transformers #logistic-regression #evaluation-metrics #compliance #automation

**Problem statement:** Witness errata sheets mix reporter errors (spellings, misheard words) with substantive changes to testimony. Classify each change so the reporter's quality record captures her own errors, and counsel sees substantive changes immediately.

**ML task:** Pair classification over (original line, proposed change, reason given), labelling each change as transcription correction, clarification or substantive change, with a calibrated probability.
**Input data:** Errata sheets (often scanned, needing OCR), the transcript passages they reference, and audio snippets for disputed lines.
**Target:** Change type; whether the audio supports the original or the change.
**Evaluation metric:** Recall on substantive changes (a missed reversal of testimony is the costly error), with macro-F1 across types; agreement with an experienced reporter and a litigator on a labelled sample.
**Scope:** A few thousand labelled errata pairs would support a fine-tuned encoder; audio verification adds value only where errata claim the reporter misheard. 1 ML engineer, 3 months, inside a read-and-sign workflow.
**Data availability:** Every firm handling read-and-sign holds errata; they are part of the record in each case and sit in agency repositories and reporters' files.

---

## 4. Booking Fill and Cancellation Forecasting
#gradient-boosting #time-series-forecasting #survival-analysis #optimization-fundamentals #revenue-impact

**Problem statement:** Predict, for each booked deposition, the probability it goes ahead as scheduled, and for each open job, the probability a qualified reporter accepts, so schedulers can hold standby capacity where fill risk is highest.

**ML task:** Binary classification of go-ahead versus cancel or continue, time-to-cancellation survival modelling, and reporter-acceptance prediction feeding an assignment optimiser.
**Input data:** Booking history with notice dates, case type, noticing firm, witness type (expert, party, corporate designee), venue, remote or in-person, add-ons; cancellation and continuance timestamps; reporter offers, acceptances and declines; court calendars where available.
**Target:** Go-ahead flag; hours-before-start of cancellation; acceptance per offer.
**Evaluation metric:** Brier score of go-ahead probability by lead time; fill rate and dropped jobs per thousand bookings in a back-test of the standby policy against actual outcomes.
**Scope:** Standard tabular modelling; the value is in the assignment policy and getting schedulers to trust it. 1 data scientist and 1 engineer, 4 months, for a regional or national agency with several years of bookings.
**Data availability:** Agencies hold booking logs in their scheduling systems; small firms keep them in calendars and texts, which limits this to firms with real systems.

---

## 5. Session Vocabulary Preparation for CART Captioners
#large-language-models #word-embeddings #k-nearest-neighbors #evaluation-metrics #worker-facing

**Problem statement:** Turn a course's or meeting's published materials into a ranked list of terms, names and phrases a captioner is likely to meet and likely to mistranslate, with suggested dictionary entries, before each session.

**ML task:** Term extraction and ranking from documents, scored by expected frequency in speech and by the captioner's historical error rate on similar terms (nearest neighbours in an embedding space of her past mistranslations).
**Input data:** Syllabi, slides, reading lists, prior session transcripts, speaker lists; the captioner's past session files with edits or flagged errors; her dictionary.
**Target:** Ranked term list with suggested briefs; after the session, which suggested terms appeared and how they were written.
**Evaluation metric:** Recall of technical terms that appeared in the session among the top-k suggestions, and error rate on those terms in prepared versus unprepared sessions.
**Scope:** Small and shippable: 1 engineer, 2–3 months, as a plug-in to the captioner's CAT software. The hard part is getting materials from instructors, so the tool should work from whatever is public.
**Data availability:** Course materials are usually available to enrolled students and the disability office; past session files are the captioner's own. Instructors' intellectual-property rules sometimes restrict sharing CART transcripts, so prior sessions stay with the captioner.
