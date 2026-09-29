# Regulated & Constrained Platforms

**Parent Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Category:** Low Digitized
**Contested on:** Every serious competitor here is fighting to give a regulated or air-gapped organisation a platform that produces the control evidence as a by-product of shipping — and whoever does that takes those estates, because the compliance burden is where their engineering time actually goes.

## Profile
**Market Size:** ~$290M US attributable to platforms in regulated and constrained environments
**Share of Parent Industry:** ~15% of category revenue
**Digital Adoption:** Very Low — the tooling assumes a permissive environment
**Target Buyer:** Platform engineering in banking, healthcare, government and defence
**Automation Potential:** High — evidence generation is mechanical and is done by hand

## What Makes This a Distinct Niche
A platform in a regulated organisation has a different job. Alongside making deployment easy it must enforce segregation of duties, produce evidence that every change was reviewed and approved by the right people, restrict what can be deployed where, maintain an auditable record, and frequently operate without internet access. These are precisely the environments where a platform's value is largest, because the compliance overhead that a platform could absorb is otherwise carried by every team individually — and they are the environments the category's tooling serves worst, because it assumes a permissive network, a continuous delivery posture and an approval model that regulated change control does not permit. The result is that these organisations build their own, badly, and their engineers spend a large share of their time on control evidence rather than on software.

## Current Tools & Gaps
General platform tooling with permission models, change management systems from the service management world, and a great deal of internally built glue. The gaps: the platform and the change management system are separate, so the evidence that the platform produced must be re-entered into the system that records it; controls are implemented as approval gates that slow delivery without improving assurance, because a human approving a change they cannot evaluate is theatre; air-gapped operation is supported awkwardly, which leaves these estates running old versions as the CI niche describes; evidence is assembled at audit time from logs designed for operations; and the platform's own compliance posture is not demonstrable, which blocks its adoption.

## Problems
- [[niches/internal-developer-platforms/regulated-and-constrained-platforms/build|🔨 Build: Evidence as a By-Product Rather Than a Project]]
- [[niches/internal-developer-platforms/regulated-and-constrained-platforms/buy|🛒 Buy: Policy as Code, Applied to Change Control]]
- [[niches/internal-developer-platforms/regulated-and-constrained-platforms/fix|🔧 Fix: The Approval That Nobody Can Evaluate]]
