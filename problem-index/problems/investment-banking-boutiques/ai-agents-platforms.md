# AI Agents & Platform Opportunities — Investment Banking Boutiques

**Industry:** [[investment-banking-boutiques|Investment Banking Boutiques]]

---

## 1. Process Memory Platform
#ai-platform #gradient-boosting #graph-theory #k-nearest-neighbors #evaluation-metrics #data-integration #revenue-impact #tacit-knowledge-ml

**Concept:** A platform that turns every sell-side and capital-raising process the firm has run into one institutional ledger of buyer behaviour. It ingests historical buyer trackers, CRM records and data room engagement exports, resolves buyers to canonical entities across sponsors, funds and portfolio companies, and records each buyer's path through each process. On a new mandate it proposes a ranked buyer universe with every name annotated by the firm's own history with that buyer, and during the process it updates buyer engagement scores from live data room and Q&A activity.

**Inputs:** Historical Excel buyer trackers; DealCloud or Salesforce exports; data room activity and Q&A logs; licensed buyer attributes from PitchBook or Capital IQ; MD overrides on proposed lists.

**Outputs / Actions:** Canonical buyer profiles with full interaction history; ranked buyer lists with evidence; in-process engagement alerts (a bidder whose data room activity has collapsed before the bid date); post-process grading of how the list performed.

**Why now:** Entity resolution and extraction from messy spreadsheets is now cheap with language models, and DealCloud adoption has standardised enough of the recent record to anchor the backfill. Banker mobility makes institutional memory a retention issue for firm leadership.

**Market:** Mid-market and elite boutiques — several hundred firms in the US alone running repeated processes. Sold to the head of the M&A group or the COO on outcome and franchise protection, not on productivity.

---

## 2. Pitch Assembly Agent
#ai-agent #large-language-models #word-embeddings #k-nearest-neighbors #transformers #worker-facing #automation

**Concept:** An agent that drafts a first pitch book from a one-line brief. It retrieves the firm's best recent pages for the sector and page type, refreshes comps and precedents from licensed data, filters credentials to the relevant sector and size, drafts the situation overview from filings and news, and assembles the deck in the firm's template — then records every MD and VP markup as preference data for the next draft.

**Inputs:** The brief; the firm's indexed archive of past books; licensed market data; the firm template; markup history.

**Outputs / Actions:** A formatted draft deck with every number linked to its source; a change log; a short list of pages the analyst should verify by hand.

**Why now:** Language models can now draft credible narrative pages and operate Office formats through plug-ins, and several vendors (Rogo, Hebbia and the data terminals' own assistants) have made banks comfortable piloting generative tools inside their perimeter.

**Market:** Every boutique and middle-market bank; the buyer is the COO or head of the analyst programme. Competes with the terminals' own assistants, so the firm-archive retrieval is the differentiator.

---

## 3. Tie-Out and Consistency Agent
#ai-agent #large-language-models #transformers #object-detection #evaluation-metrics #compliance #quick-win

**Concept:** An agent that checks every number in a board book, fairness presentation or CIM against the model and source financials, flags mismatches and stale pastes, verifies internal arithmetic, and produces a marked-up review copy. On revision it explains which numbers moved and whether the model change accounts for it.

**Inputs:** Deck and CIM drafts (PowerPoint, PDF); the Excel model; audited financials and quality-of-earnings schedules; prior versions.

**Outputs / Actions:** A review copy with every figure marked tied, mismatched or unresolved; a discrepancy list; a version-to-version numeric diff.

**Why now:** Multimodal models read slides and charts well enough to extract figures; the residual hard part (matching to model cells) is tractable with structure the firm already has.

**Market:** Boutiques, fairness-opinion committees, and the law firms and valuation firms that review the same documents. Bought on risk reduction, which survives budget cycles.

---

## 4. Origination Signal Agent
#ai-agent #survival-analysis #gradient-boosting #large-language-models #time-series-forecasting #revenue-impact #automation

**Concept:** A research agent that monitors the coverage universe for the conditions that precede a transaction — a sponsor's hold period passing four or five years, a fund nearing the end of its life, a debt maturity approaching, a founder's succession signals, a management change, a carve-out hint in an earnings call — and drafts a weekly briefing per MD of the companies most likely to transact, with the evidence.

**Inputs:** PitchBook or Capital IQ ownership and fund data; debt maturity schedules; news and filings; earnings call transcripts; the firm's CRM relationship history.

**Outputs / Actions:** Ranked transaction-likelihood list per coverage MD with reasoning; suggested outreach; CRM tasks created.

**Why now:** Cheap summarisation of filings and transcripts at scale, plus structured ownership data that was not available to mid-market firms a decade ago.

**Market:** Coverage teams at boutiques and middle-market banks; overlaps with sponsor-side sourcing tools but tuned to the banker's question — who will need an adviser — rather than the investor's.
