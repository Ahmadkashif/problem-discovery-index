# Self-Managed & Enterprise CI

**Parent Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor here is fighting to give an organisation hosted-grade pipelines inside its own boundary — with the evidence, the hardware and the control it requires — and whoever does that takes the enterprise, because the alternative is that they keep operating it themselves.

## Profile
**Market Size:** ~$610M US self-managed and enterprise CI
**Share of Parent Industry:** ~15% of category revenue
**Digital Adoption:** Medium — deep, customised and old in large enterprises
**Target Buyer:** Enterprise platform engineering under compliance and control constraints
**Automation Potential:** High for evidence generation and migration; the constraints are structural

## What Makes This a Distinct Niche
A substantial population cannot use hosted execution, for reasons that are not preferences. Source code may not leave a boundary. Builds may need hardware the hosted runners do not offer — specific processor architectures, graphics hardware, devices under test, licensed operating systems. Regulated environments need change control evidence, segregation of duties and an auditable record of what was built from what by whom. Air-gapped networks need the whole toolchain inside them. These organisations frequently run a heavily customised legacy server that everyone dislikes and nobody will replace, because the migration risk exceeds the pain and because the alternatives do not address the constraints that put them there. The contest is being adoptable inside those constraints, against the incumbent option of continuing to operate it themselves.

## Current Tools & Gaps
Long-established self-managed servers with deep plugin customisation; self-hosted runners attached to hosted control planes; enterprise distributions of the hosted products; and internally built platforms. The gaps: compliance evidence is assembled by hand at audit time from logs that were not designed for it; migration off legacy servers is blocked by thousands of accumulated jobs nobody can inventory or translate; specialised hardware is attached through self-hosted runners with little management around them; air-gapped operation is supported awkwardly and updated rarely, so these environments run old and vulnerable software; and the platform teams operating all of this are doing work that is nobody's product.

## Problems
- [[niches/ci-cd-platforms/self-managed-enterprise-ci/build|🔨 Build: The Server Nobody Will Replace]]
- [[niches/ci-cd-platforms/self-managed-enterprise-ci/buy|🛒 Buy: Compliance Evidence the Pipeline Already Produces]]
- [[niches/ci-cd-platforms/self-managed-enterprise-ci/fix|🔧 Fix: Air-Gapped Means Out of Date]]
