# Machine Learning Opportunities — Recording Studios

**Industry:** [[recording-studios|Recording Studios]]
**Derived from:** [[problems/recording-studios/high-impact|High Impact]], [[problems/recording-studios/low-impact-1|Low Impact 1]], [[problems/recording-studios/low-impact-2|Low Impact 2]], [[problems/recording-studios/worker-life-1|Worker Life 1]], [[problems/recording-studios/worker-life-2|Worker Life 2]]

---

## 1. Learning the Engineer's Translation of Client Notes
#tacit-knowledge-ml #transformers #contrastive-learning #large-language-models #feature-engineering #evaluation-metrics #worker-facing #revenue-impact

**Problem statement:** Senior mix engineers turn vague client notes ("warmer", "more punch", "the chorus feels small") into concrete mix moves that get approved, a judgement built over thousands of revisions that they cannot specify. The ML problem is to learn, per engineer and per client, which moves answer which notes in which musical context, and to rank candidate moves when a new note arrives.

**ML task:** Retrieval and ranking: given a note (text plus timestamp) and the audio around it, rank candidate parameter-change sets from the engineer's history; plus a calibrated probability that a proposed change set is approved without a further round
**Input data:** Revision ledgers built from DAW sessions: parameter-level diffs between bounces (track, plug-in, parameter, magnitude), bounced audio before and after, client notes with song timestamps from email and review tools, and the client's response; reference tracks the client supplied; per-client note histories.
**Target:** The change set the engineer made in response to each note; whether the next bounce was approved or drew a repeat of the same note.
**Evaluation metric:** Recall@5 of the engineer's actual change family (for example "vocal presence cut" or "bus compression eased") on held-out notes, measured per engineer and reported against that engineer's own consistency on repeated notes as the ceiling. Then first-round approval rate in a live trial against the engineer's unassisted baseline. A wrong suggestion costs a second of attention; a missed one costs nothing beyond the status quo, so precision matters less than coverage of the engineer's repertoire.
**Scope:** The data collection challenge dominates. The expert must be captured while they work, so the system needs a DAW-side extension that snapshots parameter state at every bounce and a near-zero-effort way to tie a change to a note; historical sessions saved over each other yield only partial ledgers. The labelling challenge is that approval is noisy (fatigue, deadlines, A&R overruling the artist) and engineers answer the same note differently on different days, so a sample of notes must be re-presented blind to estimate intra-engineer agreement, and approvals within 24 hours of a release deadline should be down-weighted. The deployment challenge is speed: the suggestion has to appear in the session in seconds, faster than the engineer's own instinct, and start as retrieval from their own history ("last time this artist said warmer you did X") before any model proposes novel moves. Two ML engineers, one audio DSP engineer and three to five partner mixers; 6–9 months to a useful retrieval tool, longer to anything trusted to propose.
**Data availability:** Nobody holds this today. Session files exist on engineers' drives, but the stems inside them belong to the artist's or label's project, so training requires consent written into mix agreements. Notes are scattered across email, text and review tools. The first asset is the ledger itself, built engineer by engineer.

---

## 2. Vocal Take Ranking and Comp Assist
#cnns #contrastive-learning #transfer-learning #evaluation-metrics #feature-engineering #worker-facing #automation

**Problem statement:** A producer records eight to twenty takes of a lead vocal and builds a composite phrase by phrase, choosing by ear for pitch, timing, tone and feel; it takes one to three hours a song (estimate). Learn the producer's own phrase-level preferences from past comps and propose a first comp.

**ML task:** Pairwise ranking of aligned phrase candidates across takes, with a learned embedding of the producer's preferences
**Input data:** All takes of each vocal with phrase segmentation from alignment to lyrics; the comp lanes or playlists in past sessions showing which take segment was chosen for each phrase; pitch, timing, loudness and spectral features; the producer and artist identity.
**Target:** The selected take for each phrase.
**Evaluation metric:** Top-1 and top-2 agreement with the producer's held-out choices per phrase, and the number of phrases the producer changes in the proposed comp. A pitch-perfect but lifeless take is the typical wrong answer, so agreement must be reported separately for phrases where the producer chose a less accurate take, which is where feel overrides correctness.
**Scope:** Unusually clean labels: Pro Tools and Logic store comp selections in the session, so every past song is a labelled example. Alignment across takes is solved technology. One ML engineer and one audio engineer, 4–6 months, per-producer fine-tuning on as few as ~30 songs (estimate).
**Data availability:** In producers' and studios' session archives; the same stem-ownership consent question as entry 1, but simpler because only selection metadata and features need leave the session.

---

## 3. Manuscript-Aligned Audiobook Proofing and Spec Check
#transformers #seq2seq #hidden-markov-models #cnns #evaluation-metrics #automation #worker-facing

**Problem statement:** Detect missed, added and misread words, mispronunciations, mouth noise, breaths and room-tone breaks in audiobook narration against the manuscript, and verify every file against the retailer's technical spec before delivery.

**ML task:** Speech recognition with forced alignment to the manuscript and word-level discrepancy classification; event detection for non-speech artefacts
**Input data:** Narration audio per chapter; the final manuscript; pronunciation guides; historical proofers' notes and pickup lists; retailer specs such as ACX (-23 to -18 dB RMS, peaks below -3 dB, noise floor below -60 dB).
**Target:** Word-level labels (correct, missed, added, substituted, mispronounced) with timestamps; artefact events; per-file pass or fail with the failing measurement.
**Evaluation metric:** Recall on discrepancies a human proofer flagged is the binding metric, because a misread that reaches a listener draws a public review and a publisher return. Precision is managed by reviewer minutes per finished hour. Character names, invented words and deliberate dialect are the hard tail and need separate reporting.
**Scope:** Strong off-the-shelf recognition makes this mostly an alignment and workflow project. Pozotron already sells part of it. The open work is mispronunciation against a pronunciation guide and tone matching for pickups. One ML engineer and one product engineer, 4 months.
**Data availability:** Production houses and publishers hold years of narration with proofers' notes; manuscripts are under publisher licence, so training happens inside the production house's own environment.

---

## 4. Console and Outboard Recall From Photos
#cnns #object-detection #semantic-segmentation #transfer-learning #worker-facing #quick-win

**Problem statement:** Read the position of every knob, switch and fader on an analog console and outboard rack from photos or video, store it as a recall file, and guide the assistant through resetting each control that differs.

**ML task:** Unit identification, control detection and angle or position regression per control; image-to-image comparison against the stored state
**Input data:** Photos and short videos of consoles and outboard units under studio lighting; manufacturer panel layouts; paired ground-truth settings captured during collection.
**Target:** Unit model and position; per-control value (angle, switch state, fader position) with confidence.
**Evaluation metric:** Per-control accuracy within a tolerance that is audibly irrelevant (a few degrees on a rotary control), and the share of recalls that need no correction by ear. A confident wrong reading is worse than a flagged uncertain one, so confidence calibration is reported alongside accuracy.
**Scope:** A finite catalogue of popular units covers most racks, and synthetic renders of panel layouts can bootstrap training. The hard cases are glare, dark rooms, chicken-head knobs without markings and custom gear. Two engineers, 4–5 months, offline on a phone.
**Data availability:** No public dataset. Collection with partner studios, photographing units at known settings, is straightforward and cheap.

---

## 5. Hold Conversion and No-Show Prediction for Bookings
#gradient-boosting #logistic-regression #time-series-forecasting #survival-analysis #revenue-impact #quick-win

**Problem statement:** Predict which first and second holds will convert to paid sessions and which confirmed sessions will cancel, start late or run over, so the studio can release, over-hold or reprice dates.

**ML task:** Binary classification of hold conversion and cancellation; time-to-confirmation survival modelling; demand forecasting by room and week
**Input data:** Booking and hold history with timestamps, client and producer identity, project type, deposit status, lead time, season, release dates where known, and actual start and stop times.
**Target:** Converted or released; cancelled within 72 hours; overtime hours.
**Evaluation metric:** Brier score and calibration of conversion probability, and booked utilisation against a rule-based baseline. Wrongly releasing a hold that would have converted loses a client relationship, while keeping a dead hold loses one day, so the decision threshold should be set per client tier.
**Scope:** Modest data per studio means pooled models across studios on a shared booking platform. One data scientist, 2–3 months once the booking system records holds properly, which most don't.
**Data availability:** Inside booking tools and calendars; holds are rarely recorded as structured data today, which is the first fix.
