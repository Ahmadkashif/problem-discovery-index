# AI Agents & Platform Opportunities — Music Distribution Platforms

**Industry:** [[music-distribution-platforms|Music Distribution Platforms]]

---

## 1. Rights Matching Platform
#ai-platform #graph-neural-networks #bert #word-embeddings #k-nearest-neighbors #gradient-boosting #compliance #evaluation-metrics

**Concept:** A platform that links recordings to the compositions underneath them, which is the join the entire royalty system depends on and nowhere holds authoritatively. It resolves entities on a graph of writers, works, recordings, publishers and societies — using co-writing relationships, publisher affiliations, catalogue co-occurrence and recording metadata as corroborating edges, which is far stronger than the name matching current processes rely on. It identifies compositions from audio where metadata cannot, catching covers, live versions and re-recordings. It captures the link at upload, when the distributor is speaking to the one person who knows both sides, rather than reconstructing it years later. And it tiers by confidence with a claimant review path, replacing a binary matched-or-pooled outcome that sends every ambiguity straight to the pool.

**Inputs:** Recording metadata and ISRCs; composition registrations, ISWCs, writers, publishers and splits across societies; co-writing and catalogue graphs; audio for melodic identification; historical confirmed matches and rejections; unmatched pool contents.

**Outputs / Actions:** Confidence-scored recording-to-composition links with the corroborating evidence shown. Upload-time link capture and validation. A claimant review queue for the ambiguous middle band where the money actually sits. A searchable view of what is unmatched and why, so writers can find their own money — the simplest available remedy and the one that would be uncomfortable for exactly the reason it would work.

**Why now:** Hundreds of millions of dollars are misdirected by a matching failure that no participant is paid to fix, and whose eventual market-share distribution means the largest rights holders are its beneficiaries rather than its victims. The data required to fix it sits with distributors and societies in quantities that make the entity resolution tractable, and the cheapest intervention costs a better form.

**Market:** Distributors, publishers and publishing administrators, collecting societies and mechanical licensing bodies, and rights management platforms. The buyer is a distributor or administrator; the argument that travels furthest is that unmatched money is a reputational and regulatory exposure as much as an accounting one.

---

## 2. Catalogue Integrity Agent
#ai-agent #cnns #graph-neural-networks #bert #k-nearest-neighbors #k-means-clustering #worker-facing #compliance

**Concept:** An agent that guards the catalogue at the scale uploads actually arrive. It fingerprints every upload against the full catalogue robustly enough to catch pitch-shifted, tempo-adjusted and re-recorded infringement that exact matching misses. It disambiguates artist names as an entity resolution problem over existing artists, their catalogues, identifiers and audiences, turning a name similarity judgement into an evidenced one. It checks artwork for rights and policy issues by vision rather than by eye. Most importantly it detects at the account level rather than the release level, because fraud arrives as an account with a characteristic upload cadence, catalogue composition and payout destination — and it routes by risk, so low-risk uploads from established accounts pass with sampling and human attention concentrates where it matters.

**Inputs:** Catalogue and upload audio; existing artist entities and their catalogues; artwork; account creation, upload cadence and payout destination patterns; historical review decisions including reversals; evolving fraud pattern signatures.

**Outputs / Actions:** Transformation-robust match candidates with the evidence. Evidenced artist name conflict assessments reported in both directions with the asymmetry named. Artwork policy findings. Account-level risk with the contributing signals. Risk-based routing and sampling. Precedent retrieval including reversals, which is the only way this function accumulates knowledge rather than relearning it every few months.

**Why now:** Upload volumes grow every year and review capacity grows arithmetically at best, while the fraud patterns change faster than the heuristics that catch them. Both failure directions are costly — a wrongly rejected artist loses their release date and their trust, a wrongly approved one produces a takedown and a clawback — and the current process makes both decisions in seconds on thin evidence.

**Market:** Distributors, streaming services, rights management platforms and content identification vendors. The metric is uploads reviewed per person and the rate of escapes in both directions, with the account-level view being the change that actually moves either.

---

## 3. Artist Money Agent
#ai-agent #large-language-models #bert #gradient-boosting #k-nearest-neighbors #evaluation-metrics #worker-facing #workflow-orchestration

**Concept:** An agent that explains money. It traces any statement line into its components — service, territory, subscription tier, per-stream rate, stream count, split, withholding, currency conversion — and produces that decomposition on demand, which answers the single largest category of support ticket with a document instead of a conversation. It explains proactively: a rate change, a reporting lag, a split adjustment or a currency movement is knowable before the artist notices the shortfall, and telling them first removes the ticket entirely. It diagnoses metadata problems by identifying which identifier failed and which system holds the authoritative record, rather than reconstructing that per ticket. And it builds the structured escalation path that takedowns, penalties and account actions currently lack, so an artist contesting a third-party decision has evidence assembled rather than an apology.

**Inputs:** Royalty statements across services and their formats; rate cards and territory tiers; splits and withholding; currency conversions; release and metadata records with their identifiers; takedown, penalty and restriction records; historical tickets with resolutions; distributor-side manipulation signals.

**Outputs / Actions:** On-demand payout decompositions per statement line. Proactive explanations of expected variance before the artist asks. Metadata diagnoses naming the failed identifier and the corrective action. Evidence-assembled escalations for third-party actions, including the targeting-versus-participation assessment where a manipulation penalty is disputed. Prior-ticket retrieval that transfers tacit support knowledge to new agents.

**Why now:** For many artists this income is not supplementary, and the only human they can reach in a chain of automated systems is a support agent who can see part of the picture and must apologise for the rest. The tracing is mechanical, the variance is predictable, and the escalation path is a thing the distributor has standing to build and nobody has built.

**Market:** Distributors, labels and label services, publishing administrators and artist management platforms. The support cost argument opens the conversation; the retention argument closes it, since artists move distributors over exactly these experiences.
