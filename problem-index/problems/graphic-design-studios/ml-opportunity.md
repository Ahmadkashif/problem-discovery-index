# Machine Learning Opportunities — Graphic Design Studios

**Industry:** [[graphic-design-studios|Graphic Design Studios]]
**Derived from:** [[problems/graphic-design-studios/high-impact|High Impact]], [[problems/graphic-design-studios/low-impact-1|Low Impact 1]], [[problems/graphic-design-studios/low-impact-2|Low Impact 2]], [[problems/graphic-design-studios/worker-life-1|Worker Life 1]], [[problems/graphic-design-studios/worker-life-2|Worker Life 2]]

---

## 1. Learning the Creative Director's Redline
#tacit-knowledge-ml #transformers #cnns #object-detection #contrastive-learning #transfer-learning #large-language-models #worker-facing

**Problem statement:** A creative director scans a draft and, in seconds, knows which regions will be redlined and which concepts a given client will reject — judgement built over thousands of reviews that they cannot specify and that leaves with them. The ML problem is to learn that review from the director's own captured critiques and the subsequent client and print outcomes, and to pre-review drafts before they reach the director.

**ML task:** Multi-label region detection of critique categories on a rendered artboard (hierarchy, typography, colour and print, brand consistency, legibility and accessibility, client fit), plus a calibrated per-draft probability that the client requests changes in each category in the next round
**Input data:** Rendered artboards at several scales paired with their layer structure (Figma file JSON, Illustrator and InDesign/IDML exports); version histories; the director's markup from PDF annotations, Figma comments and transcribed voice notes, pinned to regions; client feedback by round from Ziflow, Filestage or email; approval dates; printer preflight reports and reprint records; the client's own historical feedback.
**Target:** Critique category × bounding region per draft; next-round client change requests by category; rounds remaining to approval.
**Evaluation metric:** Recall@3 of the director's actual redlines on held-out drafts, reported against the director's own test–retest agreement on a re-reviewed sample as the ceiling. Precision matters more than usual for a tacit tool: a junior who sees five wrong flags stops reading, so the system shows at most three per draft and is judged on whether those three are right. For the print-defect class (minimum stroke, trap, rich black in small type) recall dominates, because a miss costs a plate remake. The client-risk probability is judged by Brier score and calibration, strictly out of time.
**Scope:** The data collection challenge comes first: the director's critique must be captured while they review, at near-zero extra effort — pen markup on a tablet, a push-to-talk voice note transcribed and pinned to where the stylus was — because they will not type structured critiques. Historical PDF markups can be mined for a starter set. The labelling challenge is that directors disagree with themselves on the taste classes; re-presenting ~200 past drafts blind and measuring intra-rater agreement separates the categories with ground truth (print and legibility defects) from those with only agreement, and the model should only be trusted where the director is consistent. The deployment challenge is speed and placement: under five seconds, inside Figma, Illustrator or InDesign as a plugin, never a separate app, or the director's own glance stays faster. A shared vision-language base model fine-tuned per studio keeps client files inside each studio. 2 ML engineers and 1 design technologist with 3–5 pilot studios, 6–9 months; value appears first as retrieval ("the last three times you redlined this pattern") before any learned flag is trusted.
**Data availability:** Studios hold every file and version, and proofing tools hold client comments by round. The decisive asset — the director's reasons, pinned to regions — barely exists and must be captured prospectively. Public template corpora used in layout-generation research help pre-train the visual encoder but carry no critique labels.

---

## 2. Packaging Copy-Deck-to-Artwork Verification
#cnns #transformers #seq2seq #object-detection #large-language-models #compliance #automation

**Problem statement:** Verify that each SKU's packaging artwork matches the client's copy deck and the applicable labelling rules, when the artwork's text has been converted to outlines and set on rotated, curved and folded panels.

**ML task:** Panel detection and text-region detection on rendered dielines, optical character recognition on outlined and stylised type, alignment of recognised text to copy-deck fields by SKU, and rule checks (allergen statement consistent with ingredient list, required panels present, net quantity placement) with barcode decoding
**Input data:** Print-ready PDFs and Illustrator files with dielines; copy decks in Excel or Word; the SKU matrix; prior approved versions; regulatory rule tables (21 CFR 101 for food, Supplement Facts, cosmetics labelling); assigned UPCs.
**Target:** Per field per SKU: match, mismatch with location, or missing; per rule: pass or fail with reason; barcode decoded value and grade.
**Evaluation metric:** Recall on seeded and historical discrepancies is the binding metric — a missed mismatch costs a reprint or a recall — at a fixed ceiling of false flags per panel that a proofreader will tolerate (around one). Character-level accuracy on outlined text reported separately for condensed, script and reversed type, where recognition fails most.
**Scope:** Recognition on rendered vectors is tractable because the files can be rendered at any resolution; the hard parts are dieline geometry, multi-language panels and keeping the rule library current. 2 engineers, 4–5 months to a studio-grade tool, then ongoing rule maintenance — which is a content business as much as software.
**Data availability:** Studios and clients hold copy decks and artwork; genuine error examples are rare, so training and evaluation rely on synthetic error injection (swapped values, dropped allergens, wrong UPC) into real artwork.

---

## 3. Revision-Round and Effort Forecasting for Fixed-Fee Quotes
#gradient-boosting #survival-analysis #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Predict, at quote time and again after round one, how many revision rounds and how many hours a deliverable will take, so the studio can price, staff and enforce scope on evidence rather than on the principal's optimism.

**ML task:** Quantile regression of total hours (P50 and P80) and time-to-approval survival modelling, both updated as rounds accumulate
**Input data:** Job and time records from Harvest, Toggl, Function Point, Workamajig or Productive; deliverable type and size; number of client stakeholders; brief length and specificity; client history (prior jobs' rounds and overruns); proofing-tool comment counts and sentiment per round; whether the decision-maker attended the kickoff.
**Target:** Total hours; rounds to approval; time to approval in days with censoring for stalled jobs.
**Evaluation metric:** Pinball loss at P50 and P80 on held-out jobs; calibration of P(more than three rounds); concordance index for time-to-approval. The asymmetric cost is under-forecasting — an under-quoted job loses money silently — so P80 coverage is reported prominently.
**Scope:** Modest modelling on small data: a single studio has hundreds of jobs, not thousands, so a pooled model across studios with studio-level effects is the realistic design. 1 data scientist, 3 months, delivered as a quoting aid inside the job system.
**Data availability:** Time and job data exist wherever a studio tracks time at all; client feedback history sits in proofing tools; many small studios track nothing, which limits the market to the better-run ones.

---

## 4. Font, Image and Provenance Identification for Rights Audits
#contrastive-learning #cnns #k-nearest-neighbors #transfer-learning #compliance #data-integration

**Problem statement:** Inventory every font, stock image and generated element inside a delivered file — including type converted to outlines and images flattened into composites — and match each to a licence, so the handoff carries a rights bill of materials.

**ML task:** Font family identification from glyph outlines and rasters via metric learning; near-duplicate and partial-match retrieval of image regions against the studio's licensed stock and marketplace downloads; reading C2PA Content Credentials and file metadata; a weak classifier flagging likely AI-generated regions for human review
**Input data:** Delivered PDFs, AI, INDD and PSD files; the studio's font licence records and stock download histories; foundry specimen glyphs; C2PA manifests where present.
**Target:** Per element: identified asset, licence held, scope, conflict flag (desktop font in web template, stock image in a logo, unprovenanced generated element in a mark).
**Evaluation metric:** Top-5 font family accuracy on outlined text; recall of stock matches at a fixed false-match rate; for AI-generated detection, report precision and recall honestly and treat the output as a prompt for review, never a determination, because detectors are unreliable.
**Scope:** Font recognition and image retrieval are mature techniques; the work is in the licence-record integration and the conflict rules. 2 engineers, 4 months.
**Data availability:** Studios hold their files and licence receipts, usually scattered across email; foundry specimens are public; ground truth for AI-generated elements is scarce.

---

## 5. Constraint-Aware Layout Adaptation for Versioning
#transformers #autoregressive-models #optimization-fundamentals #worker-facing #automation

**Problem statement:** Generate size, format and language variants of an approved master layout that follow the studio's own adaptation habits and never violate hard rules (logo clear space and minimum size, legal copy present and legible, platform safe zones).

**ML task:** Conditional layout generation — predicting element positions, scales and line breaks for a target canvas as an autoregressive sequence of element boxes — followed by a constraint solver that enforces hard rules and resolves overlaps
**Input data:** Pairs of masters and hand-built variants from past jobs (layer trees with element roles), target format specs, brand rules from guidelines, translated copy lengths.
**Target:** Element boxes and text breaks per variant.
**Evaluation metric:** Share of variants accepted by the production artist without edits; minutes of edits per variant; constraint violations on legal copy and logo rules must be zero, enforced by the solver rather than learned.
**Scope:** Learned layout generation is an active research area; the practical system leans on the solver and learns only the soft preferences. 2 engineers, 5–6 months; per-studio fine-tuning needs a few hundred master–variant pairs.
**Data availability:** Studios that do campaign work hold years of master–variant pairs in their archives, but layer naming is inconsistent and element roles must be inferred or labelled.
