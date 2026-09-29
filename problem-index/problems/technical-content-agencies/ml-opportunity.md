# Machine Learning Opportunities — Technical Content Agencies

**Industry:** [[technical-content-agencies|Technical Content Agencies]]
**Derived from:** [[problems/technical-content-agencies/high-impact|High Impact]], [[problems/technical-content-agencies/low-impact-1|Low Impact 1]], [[problems/technical-content-agencies/low-impact-2|Low Impact 2]], [[problems/technical-content-agencies/worker-life-1|Worker Life 1]], [[problems/technical-content-agencies/worker-life-2|Worker Life 2]]

---

## 1. Reader Failure Detection From Search, Support and Community Signal
#bert #word-embeddings #k-means-clustering #large-language-models #gradient-boosting #contrastive-learning #evaluation-metrics #data-integration

**Problem statement:** Documentation is measured by pageviews while the direct evidence of failure — zero-result searches, rephrasing sequences, tickets whose answer exists in the docs, pages visited immediately before a ticket — sits unjoined across three systems.

**ML task:** Join and cluster failure signals into a ranked backlog, and classify each cluster by failure mode: missing content, findability, accuracy, or comprehension
**Input data:** Site search queries with result sets and click-through; query rephrasing sequences within a session; support tickets with their resolutions and any documentation links used; community questions and the answers given; page visits preceding ticket creation; the documentation corpus itself.
**Target:** The failure mode as adjudicated by a writer reviewing a sample, and whether remediation reduced the recurrence of the cluster.
**Evaluation metric:** The operational test is whether fixing a top-ranked cluster reduces its signal recurrence over the following quarter — retrospective clustering quality is easy to achieve and proves nothing. Classification accuracy on failure mode matters because the four modes need entirely different remedies, and misrouting a findability problem as a content gap produces a new page that is also not found.
**Scope:** Most of the value here requires no modelling at all — joining the signals and ranking by volume produces an evidence-based backlog immediately, and the clustering refines it. Agencies cannot access these signals after handover, which makes the contracting change the precondition. 1-2 engineers, 4-6 months.
**Data availability:** Search logs, support systems and community platforms all hold this data continuously and nobody joins them.

---

## 2. Documentation-Code Dependency Extraction and Drift Detection
#bert #transformers #large-language-models #change-point-detection #gradient-boosting #evaluation-metrics #automation #workflow-orchestration

**Problem statement:** Prose documentation has semantic dependencies on code — parameter names, configuration keys, endpoint paths, version constraints — that no tooling tracks, so drift is discovered by readers and destroys trust in the whole corpus rather than in one page.

**ML task:** Extract code references from prose, link them to the codebase, detect invalidation on change, and rank pages by drift risk; separately, detect interface changes that invalidate documented screenshots
**Input data:** Documentation source with prose and examples; the codebase with its symbols, signatures, configuration schema and API definitions; commit and pull request history; page traffic and task criticality; current interface captures against documented screenshots.
**Target:** Whether a documentation statement is currently inaccurate with respect to the code, verified by writer review.
**Evaluation metric:** Precision at the flag threshold governs adoption — a drift checker producing many false alarms will be ignored, and documentation teams are small enough that a single bad week kills it. Recall on invalidating changes is the value, so report both separately and measure the proportion of reader-reported drift that the system had already flagged, which is the honest test of coverage.
**Scope:** Change-triggered routing is the intervention that prevents drift rather than detecting it: when a pull request renames a configuration key, the referencing pages are computable and should surface in that review. Risk ranking — drift probability weighted by traffic and criticality — is what makes a large corpus maintainable by a small team. 2 engineers, 6 months.
**Data availability:** Excellent under docs-as-code, since documentation and code sit in the same repositories.

---

## 3. Vocabulary Mapping and Retrieval Across the Published Corpus
#contrastive-learning #bert #word-embeddings #k-nearest-neighbors #graph-neural-networks #dimensionality-reduction #evaluation-metrics #data-integration

**Problem statement:** Documentation is written in the system's vocabulary and searched in the reader's, answers are fragmented across reference, guides, blog posts, release notes and community threads, and version mismatches produce accuracy complaints that were actually navigation failures.

**ML task:** Learn mappings between reader language and system vocabulary from the site's own failed queries, and build unified retrieval across every surface the organisation has published with currency and version awareness
**Input data:** Zero-result and rephrasing queries with eventual resolutions; the full published corpus across documentation, blog, release notes and community; version metadata and product context signals; observed navigation paths; support ticket language as a source of reader vocabulary.
**Target:** Whether the reader found what they needed, approximated by click-through followed by no further search and no subsequent ticket.
**Evaluation metric:** Zero-result rate and rephrasing rate are the direct measures and should fall. The more meaningful one is downstream: support tickets whose answer existed in the corpus, which is the clearest possible findability failure and is countable. Report version-mismatch arrivals separately, since those masquerade as accuracy problems and are fixed differently.
**Scope:** Error messages and symptoms are the highest-value vocabulary to map, because that is what readers search when something is broken and it is almost never what the documentation is organised around. Architecture evaluation against observed navigation replaces card sorts with eight participants with evidence from every reader. 2 engineers, 4-6 months.
**Data availability:** Search logs are complete and almost universally unanalysed; this is the most underused asset in the category.

---

## 4. Grounded Drafting With an Explicit Uncertainty List
#large-language-models #bert #transformers #gradient-boosting #evaluation-metrics #confidence-intervals #worker-facing #automation

**Problem statement:** Writers depend on engineer availability for both information and review, both requests lose to sprint commitments, and the compressed pre-launch window is when engineering availability is lowest and documentation accuracy matters most.

**ML task:** Assemble a grounded draft from code, pull requests, design documents, issue threads and tests, and — the central output — produce the list of claims that could not be established from the source material
**Input data:** Source code and signatures; pull request discussions and commit messages; design documents and RFCs; issue threads; test cases as behavioural specification; existing documentation for style and structure; prior feature documentation as precedent.
**Target:** Whether a drafted claim is accurate, as confirmed by an engineer during targeted review.
**Evaluation metric:** The uncertainty list is what this stands or falls on, so the metric is calibration: claims the system asserted confidently that turned out wrong are the dangerous failure, and they must be counted and reported rather than absorbed into an aggregate accuracy figure. Measure engineer review time before and after, since converting a thirty-minute document review into confirming four highlighted claims is the entire operational benefit.
**Scope:** The system must be conservative about asserting behaviour it inferred rather than found, because a confidently wrong tutorial is worse than a missing one and readers cannot evaluate it. Mechanical verification — examples that compile, parameters that exist, configuration keys that are real — should run in CI and be removed from human review scope entirely. 2 engineers, 6 months.
**Data availability:** Strong in any organisation practising docs-as-code with code and documentation co-located.
