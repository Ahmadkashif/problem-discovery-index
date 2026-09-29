# Provisioning & Abstraction

**Parent Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor here is fighting to hide infrastructure complexity in a way that does not collapse the first time a team needs something the abstraction cannot express — and whoever does that takes the platform, because the leak is what determines adoption.

## Profile
**Market Size:** ~$350M US provisioning and abstraction tooling
**Share of Parent Industry:** ~18% of category revenue
**Digital Adoption:** Medium — widely attempted and frequently routed around
**Target Buyer:** Platform teams choosing how much to hide
**Automation Potential:** High — the escape patterns and the abstraction's coverage are both observable

## What Makes This a Distinct Niche
The provisioning layer is where a platform makes its central bargain: developers give up direct control of infrastructure in exchange for not having to understand it. The bargain holds until a team needs something the abstraction does not express — a configuration option, a resource type, a behaviour under a specific condition — at which point the abstraction leaks and the team must either accept a worse outcome, obtain an exception, or route around the platform entirely. How that moment is handled determines whether the platform is adopted, and it is the moment no vendor's evaluation covers because it does not arise during a trial. The competitors are the infrastructure tooling the team would otherwise use directly, which is mature, well understood and always available, and which is a stronger alternative than any vendor in this market.

## Current Tools & Gaps
Infrastructure-as-code module registries, abstraction layers over container orchestration, and internal wrappers written by platform teams. The gaps: the escape hatch is either absent, which forces routing around, or unrestricted, which makes the abstraction meaningless — and the middle position is a design problem nobody has articulated; the abstraction's coverage is unmeasured, so nobody knows what proportion of needs it expresses; the leak is discovered by a team under time pressure, which is the worst moment; a team that escapes is invisible, so the platform team never learns what was missing; and the abstraction's own maintenance grows with the number of cases it accumulates.

## Problems
- [[niches/internal-developer-platforms/provisioning-and-abstraction/build|🔨 Build: The Abstraction That Leaks Under Pressure]]
- [[niches/internal-developer-platforms/provisioning-and-abstraction/buy|🛒 Buy: Escape Hatch Design From Language and Framework Practice]]
- [[niches/internal-developer-platforms/provisioning-and-abstraction/fix|🔧 Fix: Nobody Records What the Abstraction Could Not Express]]
