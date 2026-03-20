# Legal Research for Common Charge Types

**Industry:** [[public-defenders|Public Defenders]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** General legal research platforms like Westlaw and Lexis are built for attorneys who have 2-3 hours to research a question — public defenders handling 200+ cases need jurisdiction-specific, charge-specific research delivered in 5 minutes, not a search engine that returns 500 cases.
**Tags:** #bert #transfer-learning #attention-mechanisms #transformers #word-embeddings #evaluation-metrics #entropy-cross-entropy-kl-divergence #loss-functions #quick-win

## The Problem

A public defender handling a DUI case needs to know: the specific suppression case law in their jurisdiction for traffic stops, the mandatory minimum and maximum sentences for the charge level, the available diversion programs and eligibility criteria, the judge's historical sentencing patterns for this charge type, and the prosecution's typical plea offer structure. On Westlaw, assembling this information takes 1-3 hours of research across multiple databases. A private attorney doing 10-20 DUI cases per year invests that time. A public defender handling 50 DUI cases per year while simultaneously managing 150 other cases does not — the research simply doesn't happen for the majority of cases.

The consequence is that defenders rely on institutional memory (asking the senior attorney in the hallway) or personal recollection (what worked last time) rather than systematic legal research. This means defensible legal issues go unraised, applicable case law goes uncited, and clients receive a lower quality of representation simply because their attorney doesn't have time to look things up.

## What Already Exists

Westlaw and LexisNexis provide comprehensive legal research with AI-assisted search. Casetext's CoCounsel offers AI-powered legal research that can answer questions in natural language. Google Scholar provides free case law search. All of these tools are general-purpose — they serve every practice area, every jurisdiction, and every attorney type equally. None are optimized for the public defense context: high-volume, charge-specific, jurisdiction-specific, with emphasis on defense-relevant issues (suppression, sentencing alternatives, procedural defenses) rather than the prosecution-favorable framing that dominates reported case law.

## The Customisation Gap

The needed tool is a charge-specific research engine for public defenders that pre-compiles the defense-relevant legal landscape for common charge types in the defender's jurisdiction. When a defender opens a new DUI case, the system immediately surfaces: (1) the top 5 suppression cases for traffic stops in this jurisdiction from the last 3 years, (2) the statutory sentencing range with any mandatory minimums, (3) available diversion programs with eligibility checklist, (4) judge-specific sentencing data for this charge type, and (5) a motion template library with jurisdiction-specific language.

The customization is threefold: jurisdiction-specific (the law differs by state, county, and sometimes judge), defense-oriented (filtered for defendant-favorable holdings and defensive theories rather than the prosecution-favorable cases that general search tools tend to surface), and charge-specific (pre-organized by the 20-30 charge types that constitute 80% of a PD's caseload: DUI, drug possession, theft, assault, domestic violence, probation violations, etc.).

## Impact If Solved

Reduces per-case legal research time from 1-3 hours to 5-15 minutes for common charge types, recovering 200-500 hours/year per attorney. Increases the percentage of cases receiving substantive legal research from an estimated 20-30% to 70-80%, directly improving representation quality. Identification of applicable suppression case law or diversion eligibility on even 5% more cases (10 cases per year for a 200-case caseload) could lead to dismissals or reduced charges that collectively prevent dozens of months of unnecessary incarceration.
