# Machine Learning Opportunities — SMB Video Production

**Industry:** [[video-production-smb|SMB Video Production]]
**Derived from:** [[problems/video-production-smb/high-impact|High Impact]], [[problems/video-production-smb/low-impact-1|Low Impact 1]], [[problems/video-production-smb/low-impact-2|Low Impact 2]], [[problems/video-production-smb/worker-life-1|Worker Life 1]], [[problems/video-production-smb/worker-life-2|Worker Life 2]]

---

## 1. Footage Quality & Usability Scoring from Raw Clips
#cnn #lstm #binary-classification #computer-vision #tacit-knowledge-ml

**Problem statement:** Experienced editors and DPs review hours of raw footage and instantly assess which takes are usable — reading subtle cues like performance energy, eye-line consistency, focus accuracy, audio clarity, and continuity with adjacent shots. This tacit judgment, built over thousands of hours in the edit bay, is the bottleneck in post-production: an editor on a 2-day corporate shoot may have 8-12 hours of raw footage and needs 45-90 minutes of selects. Currently, logging and reviewing consumes 40-60% of total post-production time.

**ML task:** Binary classification (usable/unusable) with a continuous quality score for ranked selection across multiple assessment dimensions (visual sharpness, exposure consistency, audio signal-to-noise, performance quality, continuity compatibility).

**Input data:** Raw video clips (H.264/H.265/ProRes, typically 4K), segmented by take. Each clip includes embedded audio (boom/lav/on-camera mic mix), camera metadata (focal length, ISO, shutter speed, stabilization mode), and timecode. For continuity assessment, the preceding and following takes in the shot list are included as context.

**Target:** Per-take binary usability label (keep/reject) and a 0-100 quality score decomposed into sub-scores: focus accuracy (0-100), exposure consistency (0-100), audio usability (0-100), performance energy (0-100, most subjective), and continuity match (0-100 relative to adjacent shots). Labels derived from editor select decisions on completed projects.

**Evaluation metric:** Recall at 95%+ on the "keep" class is critical — missing a good take is far worse than including a marginal one. Secondary metric is Spearman rank correlation between predicted quality scores and editor rankings. Performance energy sub-score evaluated separately with inter-rater agreement as the ceiling.

**Scope:** This is a 12-18 month build requiring a team of 3-4 (CV engineer, audio ML engineer, full-stack engineer, domain advisor who is an active editor). The core challenge is data collection: you need partnership with 20-50 production companies willing to share raw footage alongside their final edit decision lists. Labeling is inherently noisy — two editors may disagree on performance energy ratings by 15-20 points. A multi-annotator approach with learned rater biases is necessary. Initial deployment should target the "obviously bad" takes (out of focus, clipped audio, wrong framing) which account for 30-40% of raw footage and have high inter-rater agreement, then progressively tackle the subjective quality dimensions.

**Data availability:** Raw footage is the most sensitive asset a production company owns — client NDAs often prohibit sharing. A federated learning approach or on-premise processing model may be necessary. The positive signal is that edit decision lists (EDLs/XMLs) are standardized and machine-readable, providing clean labels for which clips were actually used. Initial dataset target: 500+ hours of raw footage across 200+ projects spanning corporate, commercial, event, and social content.

---

## 2. Project Budget & Timeline Prediction
#gradient-boosting #regression #tabular-ml #revenue-impact

**Problem statement:** SMB video production companies price projects using intuition and rough comparables, leading to systematic underestimation of post-production costs, revision cycles, and deliverable complexity. A data-driven budget model could predict total project cost and timeline from initial project parameters.

**ML task:** Multi-output regression — predict total project cost (dollars), total hours by department (pre-production, production, post-production), number of revision rounds, and project duration (calendar days from kickoff to final delivery).

**Input data:** Project parameters at proposal stage: project type (corporate brand, event highlight, social campaign, training, testimonial), client industry, number of deliverables, target durations, estimated shoot days, number of locations, number of on-camera talent, client company size, whether legal/compliance review is required, and historical client data if returning. Post-hoc: actual invoiced hours, revision logs, communication volume, timeline milestones.

**Target:** Four continuous targets: total cost ($), total labor hours, revision round count, calendar duration (days). Trained on completed projects with full financial reconciliation.

**Evaluation metric:** Mean absolute percentage error (MAPE) on total cost, with asymmetric penalty — underestimation penalized 2x vs. overestimation (reflecting the real-world cost of under-bidding). Secondary: MAPE on revision round count.

**Scope:** 6-9 month build, 2-person team (ML engineer + full-stack). Requires integration with invoicing/project management tools to ingest historical data. The cold-start problem is real — a new shop may have only 30-50 completed projects. Transfer learning from an aggregate model across shops, fine-tuned per company, is the likely architecture. Feature engineering around "client profile" (revision patterns, response latency, stakeholder count) is where most predictive power will come from.

**Data availability:** Moderate. Project financials are in QuickBooks/FreshBooks, hours are in Toggl/Harvest, project specs are in proposals (PDF/Google Docs — requires extraction). A structured onboarding flow that helps shops tag 50+ historical projects with standardized features is the critical adoption step. Target: 2,000+ completed projects across 40+ shops for the base model.

---

## 3. Client Satisfaction Prediction from Revision Patterns
#random-forest #binary-classification #tabular-ml #revenue-impact

**Problem statement:** Production companies are blindsided by client churn — a project wraps, the producer thinks it went well, and the client never returns. Revision patterns, communication sentiment, and response latency during a project contain strong signals about client satisfaction that go unnoticed in the daily grind.

**ML task:** Binary classification (client will return for another project within 12 months: yes/no), with a continuous satisfaction risk score updated at each project milestone.

**Input data:** Per-project features: number of revision rounds, average time between feedback submission and response, sentiment scores from client emails/messages (extracted via NLP), ratio of "additive" feedback (new requests) vs. "corrective" feedback (fixing mistakes), whether the project went over budget, whether deadlines were missed, client stakeholder count and turnover during the project, and payment promptness. Historical: number of past projects with this client, trend in project value, referral history.

**Target:** Binary label: did the client commission another project within 12 months? Secondary: 1-5 satisfaction score (if post-project surveys are collected).

**Evaluation metric:** AUC-ROC for the return prediction. Precision at the low-satisfaction end is more valuable — correctly identifying at-risk clients enables intervention (producer check-in call, discount on next project).

**Scope:** 4-6 month build, 1-2 person team. The NLP component for email sentiment analysis can use pre-trained models (fine-tuned BERT or GPT-based classification). Main engineering effort is the data pipeline connecting email, project management, and invoicing systems. Smallest viable training set: 200+ client relationships with known return/churn outcomes.

**Data availability:** Good for structured data (invoices, timelines), moderate for communication data (requires email/Slack integration with client consent). The labeling is natural — you simply look at whether the client came back.

---

## 4. Crew Availability & Demand Forecasting
#gradient-boosting #time-series-forecasting #tabular-ml #worker-facing

**Problem statement:** Producers book freelance crew reactively, often 3-7 days before a shoot, leading to availability conflicts and suboptimal crew composition. Predicting demand patterns and freelancer availability windows would enable proactive booking and reduce day-of cancellations.

**ML task:** Time-series forecasting — predict crew demand by role (camera operator, gaffer, sound recordist, PA, makeup) for the next 4-6 weeks, and predict individual freelancer availability probability for specific dates.

**Input data:** Historical booking data: dates, roles, rates, confirmation lead time, cancellation events. Seasonal signals: month, week-of-year, proximity to major holidays, local event calendar. Project pipeline data: proposals in progress with estimated shoot dates and crew needs. Per-freelancer: historical acceptance rate by day-of-week, average response time, cancellation rate, concurrent booking count from other sources (if shared).

**Target:** Per-role demand count for each day in the forecast window (regression). Per-freelancer binary availability prediction (will accept a booking offer for date X: yes/no) with a probability score.

**Evaluation metric:** Weighted MAPE on demand forecasts, with heavier penalty on underestimation during peak periods (missing demand means scrambling for crew). For individual availability: log-loss, optimized for calibration — the probability score must be reliable, not just discriminative.

**Scope:** 6-8 month build, 2-person team. Requires a lightweight freelancer-facing app or integration (calendar sync, availability toggle) to capture real-time supply signals. The cold-start problem for individual freelancers is significant — default to role-level demand patterns until 20+ booking interactions are logged per freelancer. Seasonal patterns are strong and learnable quickly (Q4 corporate rush, spring wedding/event season, summer slowdown in corporate).

**Data availability:** Currently poor — most booking data lives in text messages and phone calls. The product must create the data collection layer as a core feature (scheduling platform that logs every offer, acceptance, rejection, and cancellation). Within 6 months of adoption by 30+ shops, sufficient data exists for meaningful forecasting.
