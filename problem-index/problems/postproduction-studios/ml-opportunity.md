# Machine Learning Opportunities — Postproduction Studios

**Industry:** [[postproduction-studios|Postproduction Studios]]
**Derived from:** [[problems/postproduction-studios/high-impact|High Impact]], [[problems/postproduction-studios/low-impact-1|Low Impact 1]], [[problems/postproduction-studios/low-impact-2|Low Impact 2]], [[problems/postproduction-studios/worker-life-1|Worker Life 1]], [[problems/postproduction-studios/worker-life-2|Worker Life 2]]

---

## 1. Learning the Supervisor's Read of Shot Difficulty
#tacit-knowledge-ml #cnns #transformers #gradient-boosting #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** An experienced VFX supervisor looks at a plate and a breakdown line and "knows" how many artist-days a shot will take by department, reading camera motion, motion blur, hair and fine edges, occlusion and lighting complexity that the shot category does not capture. The ML problem is to learn that read from the vendor's own bid history and recorded actuals, and give an estimate with an uncertainty band at bid time.

**ML task:** Multi-output quantile regression of artist-days per department (matchmove, roto, paint, FX, lighting, comp) from plate-level visual features, breakdown and script text, and shot metadata, plus nearest-neighbour retrieval of similar past shots with their actuals
**Input data:** Sample plates or reference frames per shot; extracted features from pretrained vision models (camera motion from optical flow, blur and fine-edge density, segmentation of regions to replace); breakdown text and script pages; shot category, length in frames and resolution; client, director and show; the supervisor's original bid per department; artist time logs from Autodesk Flow Production Tracking or ftrack; version counts and client note history per shot.
**Target:** Actual artist-days per department, split where possible into intrinsic effort (versions to first client approval) and note-driven rework (versions after a scope-changing note); plus the supervisor's bid as a second target, to measure where model and expert disagree.
**Evaluation metric:** Pinball loss at the 50th and 80th percentiles, and calibration of the 80% interval, measured on whole shows held out by time. Random shot-level splits leak show-specific effects and overstate accuracy. The business metric is error on the costliest decile of shots, because underbidding a hero shot costs far more than overbidding a cleanup shot. Report error against the supervisor's own bid as the baseline the model must beat on at least some shot types to be useful.
**Scope:** The data collection challenge comes first: bid lines must be linked to delivered shots across edit changes, shot splits and renames, which is a record-linkage project in its own right, and the plates the supervisor saw at bid time must be recovered or approximated by the final plates. The labelling challenge is that hours are a noisy label for difficulty. Client indecision, artist seniority and render outages all inflate them, so labels need the note history to separate rework from intrinsic effort, and supervisors should re-bid a held-out sample blind to estimate how consistent the expert is with themselves. The deployment challenge is speed and trust: estimates must come from whatever the supervisor has during a two-to-five-day bid window, appear in the bid template, and explain themselves with the nearest past shots. 2 ML engineers and 1 pipeline engineer embedded with a bidding team, 6–9 months. Value shows first as retrieval ("the last twelve shots like this took 2.1x category average") before any regression is trusted.
**Data availability:** Only mid-size and large vendors have enough history: a few thousand shots a year with time logs. Bid spreadsheets are kept but unstructured. Plates and footage belong to clients under NDA and TPN security rules, so the model must be trained and run inside each vendor's secure environment; no cross-vendor pooling is realistic.

---

## 2. QC Rejection Risk for Outgoing Deliverables
#gradient-boosting #autoencoders #feature-engineering #evaluation-metrics #compliance #automation

**Problem statement:** Predict, before upload, which deliverables (IMF packages, mixes, timed-text files, DCPs) are likely to be rejected by the receiving platform, and which check they will fail, so human QC time goes to the riskiest packages.

**ML task:** Package-level binary classification of rejection risk plus multi-class classification of likely failure category; unsupervised anomaly detection on essence-level measurements (loudness curves, black-frame and freeze detection, Dolby Vision metadata statistics) against the studio's history of accepted deliverables
**Input data:** Automated QC reports from BATON, Pulsar or Vidchecker; loudness and true-peak logs; Dolby Vision XML metadata; IMF CPL and packaging metadata; the conform and export path used; spec version targeted; the department and operator who produced each component; platform rejection reports and error codes.
**Target:** Rejected or accepted at first submission; rejection category (video, audio, metadata, timed text, packaging).
**Evaluation metric:** Recall at a fixed human review budget. If QC operators can check the top 30% of packages in depth, what share of eventual rejections fall inside that 30%? A missed rejection costs an overnight redelivery against a premiere; a false alarm costs an operator an hour. Track first-submission acceptance rate before and after.
**Scope:** Rejections are rarer than acceptances, so the first months are spent classifying the backlog of rejection emails and portal notices into categories. 1 ML engineer and 1 media engineer, 4–5 months, for a facility delivering hundreds of episodes a year.
**Data availability:** QC reports and rejection notices are held by the studio, but unstructured and scattered across inboxes. Platform error codes are documented publicly by some platforms (Netflix's Backlot help pages). The essence measurements are already computed by existing QC tools.

---

## 3. Classifying Client Notes as Revision or Change Order
#large-language-models #bert #transformers #evaluation-metrics #revenue-impact #workflow-orchestration

**Problem statement:** On fixed-bid work, each client note is either a revision inside the awarded scope or a change that should be priced. Classify every note on every shot at arrival, and link it to the awarded shot description, so producers can raise change orders while the client still remembers asking.

**ML task:** Text classification of review notes (in-scope fix, creative change, new work, omit) conditioned on the awarded shot description and prior notes, with extraction of the changed element (new asset, extended frame range, added element)
**Input data:** Frame.io, ShotGrid/Flow and email review notes with timestamps and annotated frames; awarded bid lines and shot descriptions; prior version history; historical change orders raised and accepted or refused by the client.
**Target:** Note category; whether a change order was raised and whether the client accepted it; the scope element added.
**Evaluation metric:** Precision on the "change order" class at a recall the producers accept. A change order raised wrongly damages the client relationship, so precision matters more than recall here. Value metric: change-order revenue recovered per show versus prior shows.
**Scope:** Historical labels are weak, because many real scope changes were never raised. Producers will need to re-label a sample of past shows. 1 ML engineer, 1 VFX producer part-time, 3–4 months.
**Data availability:** Notes and versions are in the vendor's tracker and review tool. Accepted change orders are in finance. Client tone and contract terms vary by studio, so the model should be tuned per client.

---

## 4. Music Event Detection for Cue Sheet Generation
#cnns #feature-engineering #seq2seq #large-language-models #evaluation-metrics #automation #compliance

**Problem statement:** From the locked cut's final mix stems and AAF or EDL, detect every music event with in and out times, identify the cue, classify its usage type, and produce a draft cue sheet reconciled against the licence log.

**ML task:** Frame-level music detection on audio spectrograms (music versus dialogue and effects, using the music stem where available); cue identification by matching to the composer's delivered cues and commercial fingerprint libraries; usage-type classification (background instrumental, background vocal, visual vocal, theme) from audio and picture context; LLM-assisted reconciliation of detected cues against licence and cue logs
**Input data:** Final mix and music stems; AAF or EDL clip names and timecodes; the composer's cue list and stems; the music supervisor's licence log; past cue sheets for the show as labelled examples.
**Target:** Cue sheet rows (title, timecodes, duration, usage, writers, publishers, PRO), and a list of licence mismatches.
**Evaluation metric:** Event-level F1 with a timing tolerance of about one second, plus row-level exact match on usage type. Missed cues matter more than spurious ones, because a missing cue is unpaid royalties and a delivery defect, while a spurious one is deleted in review.
**Scope:** Detection on separate music stems is close to solved. The hard parts are recut score cues that no fingerprint library holds, and usage type, which needs picture context. 1 ML engineer and 1 audio engineer, 4 months.
**Data availability:** Every studio and music editor holds past cue sheets paired with their mixes, which is a ready supervised dataset. Licence logs are held by music supervisors and production.

---

## 5. Temporally Consistent Mattes With Edge Confidence
#semantic-segmentation #cnns #transformers #transfer-learning #evaluation-metrics #worker-facing #automation

**Problem statement:** Produce roto mattes for actors and objects that hold on hair, fingers and motion blur across a whole shot, with a per-frame, per-edge confidence map that tells the artist exactly where to intervene.

**ML task:** Video object segmentation and alpha matting with temporal propagation from user keyframes, fine-tuned from foundation segmentation models; calibrated uncertainty estimation on edges
**Input data:** Plates at full resolution; artist-finished roto and alpha from past shows (spline shapes and final mattes); keyframe corrections recorded during artist sessions.
**Target:** Per-frame alpha mattes and editable spline shapes; an edge-level confidence score.
**Evaluation metric:** Boundary F-measure and alpha error on held-out shots, measured on hair and motion-blur regions separately because whole-frame metrics hide the failures that matter. Production metric: artist minutes per shot to reach final approval, compared against manual roto on matched shots.
**Scope:** Foundation models give a strong start; the work is fine-tuning on the studio's finished mattes, temporal stability, and integration into Nuke or Silhouette as editable output. 2 ML engineers and 1 pipeline TD, 6 months.
**Data availability:** Every VFX vendor holds years of finished roto, but it belongs to clients under contract and security rules, so training must happen inside the vendor's environment and contracts may need to allow it.
