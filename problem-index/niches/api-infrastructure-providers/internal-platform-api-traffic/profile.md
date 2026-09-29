# Internal Platform API Traffic

**Parent Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor here is fighting to carry service-to-service traffic with negligible latency cost and negligible friction for the teams deploying behind it — and whoever does that takes the platform account, because the alternative is that teams route around the layer entirely.

## Profile
**Market Size:** ~$940M US internal API and service traffic infrastructure
**Share of Parent Industry:** ~23% of category revenue
**Digital Adoption:** High — every organisation of size runs something here
**Target Buyer:** Platform engineering, measured on reliability and on imposing little friction
**Automation Potential:** Very High — dependency structure and failure behaviour are both observable

## What Makes This a Distinct Niche
Internal traffic is an operations problem with an organisational dimension. The platform team owns a layer that every other team's service passes through, which gives them enormous leverage and an equally large obligation: every millisecond they add is paid by every call in the company, and every configuration step they require is friction imposed on teams trying to ship. The contest is therefore fought on two axes simultaneously — technical cost and adoption cost — and losing either one loses the account, because a platform layer that teams route around provides none of the value it was deployed for. The competitors are service meshes, hyperscaler-native networking and the option of building nothing at all, which is a genuine and frequently chosen alternative.

## Current Tools & Gaps
Service meshes, internal gateways, hyperscaler service networking, and client libraries. The gaps: the operational cost of the mesh layer is significant and is frequently discovered after adoption; configuration surface is large enough that most organisations use a fraction of it; the dependency graph derivable from the traffic is not surfaced, so architecture and change management run on diagrams; failure attribution between the platform layer and the services it fronts is genuinely hard and is not helped by the tooling; and the friction imposed on service teams is not measured by anyone, although it determines adoption.

## Problems
- [[niches/api-infrastructure-providers/internal-platform-api-traffic/build|🔨 Build: Every Millisecond Paid by Every Call]]
- [[niches/api-infrastructure-providers/internal-platform-api-traffic/buy|🛒 Buy: Dependency Graphs the Mesh Already Computes]]
- [[niches/api-infrastructure-providers/internal-platform-api-traffic/fix|🔧 Fix: Nobody Measures the Friction the Platform Imposes]]
