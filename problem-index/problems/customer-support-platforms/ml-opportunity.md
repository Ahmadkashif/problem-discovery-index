# Machine Learning Opportunities — Customer Support Platforms

**Industry:** [[customer-support-platforms|Customer Support Platforms]]
**Derived from:** [[problems/customer-support-platforms/high-impact|High Impact]], [[problems/customer-support-platforms/low-impact-1|Low Impact 1]], [[problems/customer-support-platforms/low-impact-2|Low Impact 2]], [[problems/customer-support-platforms/worker-life-1|Worker Life 1]], [[problems/customer-support-platforms/worker-life-2|Worker Life 2]]

---

## 1. Knowledge Staleness Detection from Behavioural Signal
#bert #word-embeddings #large-language-models #change-point-detection #hypothesis-testing #confidence-intervals #evaluation-metrics #transformers

**Problem statement:** Generative answering made the knowledge base the substrate of every automated answer, and the corpus was already decaying silently as the product changed. An article does not know it has become wrong, and the signals that would reveal it — customers reading it and then opening a ticket, agents contradicting it, generated answers being escalated — are all observable and none are used.

**ML task:** Ranking articles by probability of being stale, from behavioural evidence plus semantic comparison against product change artefacts
**Input data:** Article view events joined to subsequent ticket creation by the same customer on the same topic; agent reply text compared semantically against the article the ticket was tagged to; generative answer events with customer rejection, follow-up or escalation; release notes, changelogs and configuration change feeds; article edit history.
**Target:** Articles that a knowledge manager subsequently edited for accuracy, as distinct from stylistic edits.
**Evaluation metric:** Precision@k against a manageable weekly review queue — the knowledge manager can review perhaps twenty articles a week, so what matters is whether the top twenty contain the genuinely wrong ones. Compare against the age-ordered backlog, which is the current method and a fair baseline.
**Scope:** View-then-ticket is the single strongest signal and requires only session joining, no modelling. Semantic contradiction between agent replies and the cited article is the second and needs an entailment-style comparison. Mapping release notes to affected articles is mechanical and high value. 2 ML engineers plus a knowledge manager, 4-5 months.
**Data availability:** Behavioural events are complete in the platforms and almost never joined across the article and ticket boundary. Article edit history exists but does not distinguish accuracy fixes from rewording, so the label needs derivation.

---

## 2. Generative Answer Correctness Measurement
#large-language-models #hypothesis-testing #confidence-intervals #evaluation-metrics #bert #descriptive-statistics #compliance

**Problem statement:** Companies are shipping automated answers at scale and reporting deflection rate. Nobody reports answer correctness, because verifying it requires knowing the truth. A confidently wrong automated answer often generates no ticket at all, which means the failure mode is invisible in every metric currently collected.

**ML task:** Sampled adjudication with human labelling to establish a factual error rate, plus a learned predictor of which generated answers are likely wrong, used to route them for review
**Input data:** Generated answers with the retrieved source passages; the questions asked; subsequent customer behaviour (follow-up, escalation, repeat contact, none); human adjudications of factual correctness on a sampled basis; the knowledge base and its staleness signals.
**Target:** Factual correctness of the answer as adjudicated by a human against current ground truth.
**Evaluation metric:** The headline deliverable is the error rate itself with a confidence interval — a number the organisation currently does not have and needs. For the predictor, recall on adjudicated errors at a fixed review budget, since the purpose is to concentrate scarce human review where it pays.
**Scope:** The uncomfortable part is organisational rather than technical: this produces a number nobody wants. Sampling design matters — errors concentrate in topics with stale articles and in questions with thin retrieval support, so stratified sampling beats uniform. Silent failures, where a wrong answer generates no downstream signal, are the reason behavioural proxies alone are insufficient and human adjudication is unavoidable. 2 ML engineers plus a QA function, 4 months, ongoing thereafter.
**Data availability:** Generated answers and retrieval traces are complete. Adjudication labels must be created deliberately and continuously; there is no existing corpus.

---

## 3. Ticket Difficulty Estimation for Fair Agent Measurement
#gradient-boosting #bert #word-embeddings #hypothesis-testing #confidence-intervals #cross-validation #evaluation-metrics #worker-facing

**Problem statement:** Agents are measured on handle time and a satisfaction score. Handle time rewards closing without solving; satisfaction at individual volume is dominated by noise and by whether the answer was yes. Tickets are not assigned randomly, so raw comparisons across agents are meaningless, and everyone who has looked at the distribution knows it.

**ML task:** Regression on expected handling effort from ticket characteristics, used as an adjustment; plus resolution modelling defined as absence of repeat contact
**Input data:** Ticket text at creation, channel, customer tier and history, product area, prior contacts on the topic, attachments; realised handle time, transfers, reopens and repeat contacts; agent identity and tenure; satisfaction responses with response indicator.
**Target:** Handling effort as realised, and resolution defined as no repeat contact on the same issue within a window.
**Evaluation metric:** For difficulty, explained variance in handle time and — more importantly — whether adjusted agent comparisons are stable across periods, since an unstable ranking is measuring noise. For satisfaction, report the width of the interval at typical individual response volumes, which is itself the finding.
**Scope:** The deployment risk is entirely about framing. This is a fairness correction to an existing measurement, and it will be received as either a defence of agents or a more sophisticated surveillance system depending on how it is introduced. Resolution as a metric is the substantive change and is directly observable; difficulty adjustment is what makes it fair. 2 ML engineers plus support operations, 4 months.
**Data availability:** Complete and abundant. Repeat contact linkage requires identifying that two tickets concern the same issue, which is a text similarity problem rather than a lookup.

---

## 4. Translation Risk Estimation for Support Content
#transformers #large-language-models #bert #word-embeddings #transfer-learning #confidence-intervals #evaluation-metrics #compliance

**Problem statement:** Machine translation is cheap and good, and most companies still support two languages, because a manager cannot verify a translation in a language they do not read. Support text is disproportionately full of the constructs translation handles worst — conditionals, obligations and negations — and an error there is a written commitment to a customer.

**ML task:** Quality estimation per segment without a reference translation, combined with detection of high-risk constructs and terminology violations
**Input data:** Source support text and its machine translations; a maintained product and legal terminology glossary; historical human post-edits as quality labels; segment features including negation, conditional and obligation markers; content type (policy, troubleshooting, marketing).
**Target:** Whether a human post-editor materially changed the meaning of the segment.
**Evaluation metric:** Recall on meaning-changing edits at a review budget covering a small fraction of segments — the whole point is concentrating limited review. Report separately for policy and legal content, where the tolerance is different and the routing should be by rule rather than by score.
**Scope:** Round-trip comparison catches reversed negations and dropped conditions cheaply and is the practical technique nobody productises. Terminology enforcement resolves most of the genuine risk and is a glossary problem before it is a model. Content with legal effect should route to human review by policy, not by confidence, and that boundary should be explicit. 2 ML engineers plus a localisation lead, 4 months.
**Data availability:** Post-edit histories exist at companies already doing human review and are the natural label source. Companies not yet localising have no such data, which is a bootstrapping problem solved by starting with a reviewed pilot language.
