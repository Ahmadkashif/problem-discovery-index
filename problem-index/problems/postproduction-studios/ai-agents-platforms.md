# AI Agents & Platform Opportunities — Postproduction Studios

**Industry:** [[postproduction-studios|Postproduction Studios]]

---

## 1. Bid Memory Platform for VFX Vendors
#ai-platform #gradient-boosting #cnns #tacit-knowledge-ml #evaluation-metrics #revenue-impact

**Concept:** A platform that links every bid line a vendor has ever priced to the shot it became, the hours it took and the notes that changed it, then puts that history in front of the supervisor and producer on the next bid. It drafts per-department estimates from plates and breakdowns, shows the nearest past shots with their actuals, and flags shot types the vendor systematically underbids. After award, it tracks burn against bid shot by shot and warns while there is still time to raise a change order.
**Inputs:** Bid spreadsheets and breakdowns, sample plates, Flow Production Tracking or ftrack time logs and versions, review notes, edit change history, accepted change orders.
**Outputs / Actions:** Draft bids with uncertainty bands; bid-versus-actual reports by shot type, client and supervisor; burn alerts during production; post-mortems written from data rather than memory.
**Why now:** Pretrained vision models can describe plate difficulty without hand-built features, and the 2023–2025 contraction (strikes, fewer series, Technicolor's collapse) has made bid accuracy a survival question for mid-size vendors.
**Market:** VFX vendors with roughly 50 to 1,000 artists, a few hundred worldwide (estimate). Production trackers are the natural incumbents but record actuals without grading bids.

---

## 2. Delivery Pre-Flight Agent
#ai-agent #gradient-boosting #autoencoders #compliance #automation #workflow-orchestration

**Concept:** An agent that sits between finishing and upload. It reads the target platform's current spec, runs the studio's automated QC and loudness checks, risk-ranks the package against the studio's own rejection history, and writes a fix list for the department that has to act. It classifies every incoming rejection notice, links it to the component and export path that caused it, and updates the rules so the same failure is caught next time.
**Inputs:** Platform specs and error-code documentation; QC and loudness reports; Dolby Vision metadata; IMF CPLs; rejection emails and portal notices; the show's delivery schedule.
**Outputs / Actions:** Pass, review or hold per package; department-addressed fix lists; a classified rejection log; spec-change alerts when a platform revises its requirements.
**Why now:** Language models can parse spec documents and rejection notices that were never structured, and platforms' strict whole-package rejection makes each avoided failure worth an overnight shift.
**Market:** Finishing and mastering facilities and in-house deliverables teams at studios. Adjacent to QC tool vendors, who sell the checks but not the memory of which checks this studio fails.

---

## 3. Turnover and Change-List Agent
#ai-agent #large-language-models #seq2seq #worker-facing #workflow-orchestration #automation

**Concept:** An agent for editorial departments that diffs every new version of the cut against the last turnover and produces each downstream department's change package: updated VFX pull lists with new, omitted and retimed shots; conform EDLs; sound change lists with sync offsets; music timing updates. It tracks which vendor holds which version and drafts the change notes for the assistant editor to send.
**Inputs:** Avid bins and AAF or EDL exports per version, VFX shot lists, vendor delivery logs, sound and music turnover records.
**Outputs / Actions:** Department-specific change lists and exports; a version ledger per vendor; draft notifications; alerts when a vendor is working from a stale cut.
**Why now:** Agents can now operate across file formats and email reliably enough to take on reconciliation work, and recut volume has grown as streamers test and re-edit more.
**Market:** Editorial teams on scripted series and features, paid by productions or post houses. No incumbent owns cross-vendor version tracking; editorial software owns the timeline only.

---

## 4. Delivery Schedule Closer
#ai-agent #large-language-models #cnns #compliance #data-integration #automation

**Concept:** An agent for the delivering side (the post house or producer closing a distributor's ~80–200-item acquisition schedule, estimate) that turns the PDF delivery schedule into a live checklist, links each item to the file or document that satisfies it, generates the music cue sheet from the locked cut and the licence log, drafts credits checks against contracts, and chases the missing items (E&O certificate, chain-of-title documents, licences) until the schedule closes.
**Inputs:** Delivery schedules, AAF or EDL and music stems, licence logs, contracts and credit obligations, E&O and chain-of-title documents.
**Outputs / Actions:** Item-by-item delivery status; draft cue sheets in each distributor's and PRO's format; licence-mismatch flags; requests to the people who owe each document.
**Why now:** Document understanding and audio event detection are both good enough to draft what coordinators retype, and distributors' holdbacks on final payments make every missing item a cash problem.
**Market:** Post supervisors, post houses' deliverables departments and independent producers; music cue sheet services and rights platforms are adjacent sellers. The distributor's own re-servicing of licensees is a separate agent under [[film-distributors|Film Distributors]].
