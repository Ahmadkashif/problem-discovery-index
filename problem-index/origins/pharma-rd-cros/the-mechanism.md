# The Mechanism: Validation, and the AI Hype Gap

**Origin:** [[origins/pharma-rd-cros/profile|Pharma R&D and CROs]]
**Tags:** #compliance #data-integration #workflow-orchestration #hypothesis-testing #survival-analysis #evaluation-metrics #causal-inference

> This is the file to read twice if the pitch in front of you is "AI is transforming drug discovery." The honest version of that claim is much narrower than the pitch.

## Part One: What Part 11 Actually Made Systems Do

The regulation described in [[origins/pharma-rd-cros/origin-story|the origin story]] translates into concrete engineering requirements that still shape every EDC/eCRF platform:

- **An immutable, computer-generated audit trail.** Every change to a record must log who changed it, when, and what the prior value was — permanently, not optionally.
- **Access controls tied to identity**, not to a shared credential — the system must know which specific person made which specific change.
- **Validation that the electronic signature is bound to its record** such that the signature cannot be copied onto a different record or the record altered after signing without breaking the binding.
- **A documented, defensible process (computer system validation, CSV) proving the software itself does what it claims** — tested, versioned, and re-validated on every meaningful change.

None of this is exotic computer science. What makes it expensive is that **every control has to be demonstrated to a regulator's satisfaction, potentially years later**, by people who were not in the room when the system was built. The validation package routinely costs more than the software it validates. The teaching point: **in a regulated-computing regime, "does it work" is a smaller question than "can you prove to a regulator that it worked."**

## Part Two: Where AI Actually Helps — and Where It Does Not

As of sources checked in 2026, AI in drug discovery has a well-documented **hype gap**, and this file states it plainly rather than hedging it into meaninglessness.

**Where the gains are real:** almost entirely **preclinical** — compound screening, target identification, and structural prediction (protein-folding-adjacent work being the clearest, most externally validated success class in the broader field). These are genuine wins in the part of the pipeline furthest from the patient.

**Where the gains have not materialised:** the clinical pipeline itself. **Roughly 90% of drug candidates entering clinical trials still fail** — essentially unchanged by a decade of AI investment — because the bottleneck sits in human biology and trial endpoint design, not compound search. One tracked figure puts industry-wide AI-drug-discovery investment above **$100 billion**, against **zero FDA approvals attributable specifically to an AI-discovered molecule** as of sources checked here; a separate estimate puts **$8.9 billion in AI-drug-discovery-specific hype capital** against the same zero-approval count.

Compounding the gap: **published machine-learning drug-discovery papers have a documented pattern of reproducibility and external-validation failures** — models that perform well on the original authors' held-out set and considerably worse when an independent group tries to reproduce the result on new data.

## Why the Gains Cluster Where They Do

This is not mysterious once the validation burden from Part One is taken seriously. **Preclinical screening is where you can iterate fast and fail cheaply** — a wrong prediction about a candidate compound costs a few weeks of wet-lab time. **Clinical trials are where the Part 11 apparatus, ICH-GCP inspection regimes, and the sheer cost of patient recruitment make an unvalidated shortcut catastrophic** — an AI model's confident wrong answer at trial-design or endpoint-selection stage can cost years and hundreds of millions of dollars, and no regulator will accept "the model said so" as the underlying evidence for a decision affecting patient safety.

**AI is genuinely useful exactly where the cost of being wrong is low, and genuinely unproven exactly where the cost of being wrong is the entire budget of the origin.** That is not a coincidence; it is the direct consequence of what Part 11 and the CSV regime were built to enforce.

## The Transferable Pattern

> **Frame any "AI is revolutionising X" claim in a regulated-computing domain as hype pending a named, sourced counterexample — and specifically ask which stage of the pipeline the claimed gain sits in, because the validation cost is not evenly distributed across stages.**

An FDE meeting a pharma or med-device prospect pitching an AI product should ask, before anything else: **which regulatory stage does this touch, and who has to sign off that it works?** The answer usually explains the entire sales cycle.

**Sources:** US FDA, 21 CFR Part 11 and associated CSV guidance; industry-tracked figures on AI-drug-discovery capital investment and FDA approval counts attributable to AI-discovered molecules (as reported in pharma-industry analyses circulating through 2025–26; treated as directionally reliable order-of-magnitude figures rather than audited totals); published commentary on reproducibility failures in machine-learning drug-discovery literature.
