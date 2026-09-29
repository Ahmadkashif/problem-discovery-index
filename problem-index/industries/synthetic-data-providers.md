# Synthetic Data Providers

## Profile
**Category:** Data & AI Economy
**Market Size:** ~$1.5B US synthetic data generation, split between tabular privacy use cases and simulation for perception
**Tech Maturity:** Strong generation, absent certification — Gretel, MOSTLY AI, Tonic, Hazy and the open SDV ecosystem generate convincing tabular data; Parallel Domain, Rendered.ai and the autonomous vehicle simulation groups generate convincing sensor data. Nobody can certify that a given synthetic dataset is simultaneously useful enough to train on and private enough to release, which is the only claim customers are buying.
**Workforce:** Generation engineers, privacy researchers, solutions engineers running proofs of concept, domain data scientists, compliance and legal reviewers

## Key Pain Themes
The entire value proposition rests on a trade-off that nobody can measure well in both directions at once. Turn up fidelity and the synthetic records begin to memorise real individuals; turn up privacy and the data stops supporting the models it was generated for. Customers ask for a guarantee and receive a set of summary statistics comparisons and a differential privacy epsilon they do not understand. Below that sit two structural gaps: relational and constraint preservation, where multi-table data with referential integrity, temporal ordering and business rules degrades in ways single-table metrics do not reveal; and domain-specific generation, where healthcare, finance and industrial data each require constraints that generic generators do not know about. Solutions engineers spend proofs of concept manually demonstrating fidelity, and privacy officers are asked to sign off on a mathematical guarantee whose practical meaning is genuinely contested.

## Current Tech Landscape
Tabular synthesis is dominated by GAN and diffusion approaches plus increasingly large language model based generation, with the open Synthetic Data Vault library serving as a common baseline. Differential privacy provides the only formal guarantee available and is applied inconsistently, with epsilon values often chosen for utility rather than for meaningful protection. Membership inference and attribute inference attacks are the standard empirical privacy evaluations and are run inconsistently. For perception, simulation platforms generate labelled sensor data at scale, with the sim-to-real gap as the persistent limitation. Regulatory acceptance of synthetic data as de-identified is unsettled in both the US and EU.

## Problems
- [[problems/synthetic-data-providers/high-impact|🔴 High Impact: Certifying the Privacy-Utility Trade-Off]]
- [[problems/synthetic-data-providers/low-impact-1|🟡 Low Impact: Relational and Constraint Preservation]]
- [[problems/synthetic-data-providers/low-impact-2|🟡 Low Impact: Domain-Specific Generation Constraints]]
- [[problems/synthetic-data-providers/worker-life-1|🟢 Worker Life: Solutions Engineer Proving Fidelity]]
- [[problems/synthetic-data-providers/worker-life-2|🟢 Worker Life: Privacy Officer Signing Off]]
- [[problems/synthetic-data-providers/ml-opportunity|🧠 ML Opportunities]]
- [[problems/synthetic-data-providers/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
This is a category selling a guarantee it cannot yet issue. The customer's real question — can I release this without exposing anyone, and will a model trained on it work — has two answers that trade off against each other, and the industry reports them separately using metrics chosen by the vendor. The providers hold thousands of generation runs paired with fidelity evaluations, privacy attack results and, occasionally, downstream model performance. That corpus is the empirical basis for a certification standard the field lacks, and no vendor has assembled it, partly because the results would constrain what they are able to claim.
