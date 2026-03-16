# Machine Learning Opportunities — Collections Agencies

**Industry:** [[collections-agencies|Collections Agencies]]
**Derived from:** [[problems/collections-agencies/high-impact|High Impact]], [[problems/collections-agencies/low-impact-1|Low Impact 1]], [[problems/collections-agencies/low-impact-2|Low Impact 2]], [[problems/collections-agencies/worker-life-1|Worker Life 1]], [[problems/collections-agencies/worker-life-2|Worker Life 2]]

---

## 1. Call Outcome Prediction from Early Conversation Signals
#gradient-boosting #bert #binary-classification #nlp #tabular-ml #tacit-knowledge-ml

**Problem statement:** Experienced collection agents develop an intuitive sense within the first 30 seconds of a call — based on tone, word choice, hesitation patterns, and greeting style — whether the debtor will engage meaningfully or resist. This tacit judgment determines how aggressively the agent negotiates, whether to pivot to a payment plan early, or whether to cut the call short and move on. New agents lack this instinct and waste 3-5 minutes on calls that a veteran would have redirected in 30 seconds.

**ML task:** Binary classification (will this call result in a payment arrangement: yes/no) from multimodal early-call features, with an extension to multiclass (payment arrangement / promise to pay / callback scheduled / hard refusal / hang-up).

**Input data:** First 30-60 seconds of call audio (prosodic features: pitch variance, speech rate, pause duration, interruption patterns), real-time transcription (word choice, sentiment markers, disclosure acknowledgment timing), and account-level tabular features (balance, days-past-due, prior contact attempts, prior promises kept/broken).

**Target:** Binary label: call resulted in a payment arrangement or verified promise-to-pay within 48 hours. Extended: 5-class disposition label assigned post-call and verified against payment system within 30 days.

**Evaluation metric:** AUC-ROC for binary; balanced accuracy for multiclass. Precision at the "will pay" class is critical — false positives waste agent time on optimistic calls. Recall on "hard refusal" is valuable for early call termination.

**Scope:** Requires partnership with a mid-to-large agency (200+ seats) to capture labeled call data. Audio feature extraction via pretrained speech models (wav2vec2 or Whisper embeddings) combined with gradient-boosted tabular features. 6-9 month build for a team of 2 ML engineers + 1 domain expert. The labeling challenge is significant: experienced agents may not agree with each other on "I knew this one was a waste," and ground truth (actual payment) has a 30-day lag.

**Data availability:** Call recordings exist at every agency (required for QA compliance). Disposition codes are logged in the collection platform. The challenge is linking call-level audio to account-level payment outcomes across systems, and getting consistent labeling from veteran agents on the "early signal" that triggered their judgment.

---

## 2. Optimal Contact Time Prediction
#gradient-boosting #regression #time-series-forecasting #tabular-ml #revenue-impact

**Problem statement:** Agencies dial accounts at times determined by campaign schedules and dialer pacing, not by individual debtor reachability patterns. The probability of reaching a specific debtor varies dramatically by day-of-week and time-of-day, and these patterns are debtor-specific (a night-shift worker is unreachable at 10 AM; a retiree is unreachable after 8 PM).

**ML task:** Regression / time-series forecasting: predict the probability of right-party contact for a given account at each hour of each day in the upcoming week.

**Input data:** Historical contact attempt logs (timestamp, outcome, phone number used), account demographics (age, zip code, employment status where available), phone type (mobile vs. landline), and prior successful contact timestamps.

**Target:** Probability of right-party contact at each candidate time slot (168 hourly slots per week). Output is a ranked list of optimal contact windows per account.

**Evaluation metric:** Normalized Discounted Cumulative Gain (NDCG) on the ranked time slots, measured against actual right-party contact events. Secondary: lift in right-party contact rate when the model's top-3 recommended slots are used vs. random scheduling.

**Scope:** Moderate difficulty. Feature engineering from contact attempt logs is straightforward. A gradient-boosted model on tabular features (hour, day, phone type, prior contact patterns) can be trained on 6 months of historical data. 3-4 month build for 1-2 ML engineers. The main challenge is integration with the dialer — most predictive dialers don't accept per-account time preferences natively.

**Data availability:** Contact attempt logs with timestamps and disposition codes are standard in every collection platform. Phone type data is available from carrier lookup APIs. Employment/demographic data is available through credit bureau headers where permissible.

---

## 3. Settlement Amount Optimization
#gradient-boosting #regression #tabular-ml #revenue-impact

**Problem statement:** When a debtor is willing to settle for less than the full balance, the agent must decide what settlement percentage to offer. Too high and the debtor walks away; too low and the agency leaves money on the table. Currently this is guided by static rules (e.g., "offer 40% on accounts over 180 days") that ignore debtor-specific willingness-to-pay signals.

**ML task:** Regression: predict the maximum settlement percentage a debtor will accept, conditional on account characteristics and conversation features.

**Input data:** Account attributes (original balance, current balance, days-past-due, debt type, creditor), debtor demographics (age, income estimate, state), prior negotiation history (offers made, counteroffers, rejected amounts), and conversation-level features from current call (sentiment, stated hardship indicators extracted via NLP).

**Target:** Accepted settlement percentage (final agreed amount / original balance), with training labels from historically completed settlements.

**Evaluation metric:** Mean Absolute Error (MAE) on settlement percentage. Business metric: total dollars recovered per portfolio, comparing model-guided offers vs. static rules. The cost function is asymmetric — overestimating willingness-to-pay loses the deal entirely, while underestimating leaves 5-15% on the table.

**Scope:** 4-6 month build for 2 ML engineers. Requires historical settlement data with full negotiation context (not just final accepted amount). The main challenge is that settlement negotiations are partially strategic — the debtor's true willingness-to-pay is never observed, only the outcome of a bargaining process. The model must account for agent skill as a confound.

**Data availability:** Settlement records exist in collection platforms. Negotiation transcripts are available from call recordings but require NLP extraction. The dataset is biased toward successful settlements; failed negotiations (debtor hung up, refused all offers) have censored outcomes.

---

## 4. Right-Party Contact Scoring from Phone Number Portfolios
#gradient-boosting #binary-classification #tabular-ml #data-integration

**Problem statement:** Each debtor account may have 5-15 associated phone numbers from skip tracing vendors, credit headers, and prior collection attempts. Agents or dialers must choose which number to try first, and the wrong choice wastes one of the limited daily contact attempts allowed under Reg F (7 attempts per 7-day period per phone number).

**ML task:** Binary classification: for a given (account, phone number) pair, predict whether dialing this number at the proposed time will result in a right-party contact.

**Input data:** Phone number attributes (type: mobile/landline/VoIP, carrier, area code match to debtor address, number age, source vendor, number of other accounts sharing this number), account attributes (days-past-due, prior contact attempts on this and other numbers, last successful contact date), and temporal features (hour, day-of-week, days since last attempt on this number).

**Target:** Binary: right-party contact achieved (yes/no). Positive class defined as debtor identity confirmed on the call.

**Evaluation metric:** Precision-Recall AUC, optimized for precision at recall=0.3 — the goal is to identify the top 30% of phone numbers that account for 70%+ of successful contacts. Reg F contact attempt limits make false positives costly (wasted attempt that counts against the cap).

**Scope:** 3-4 month build for 1-2 ML engineers. Feature engineering is the bulk of the work — joining phone metadata from carrier APIs, skip trace vendor feeds, and historical attempt logs. A well-tuned gradient-boosted model on these tabular features should significantly outperform the current approach of dialing numbers in the order returned by the skip trace vendor.

**Data availability:** Historical contact attempt logs with per-phone-number outcomes are available in every collection platform. Phone metadata requires carrier lookup API integration (Twilio Lookup, Telnyx). Skip trace vendor confidence scores are available but often poorly calibrated.
