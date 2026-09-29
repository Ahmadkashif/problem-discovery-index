# Nobody Measures the Friction the Platform Imposes

**Niche:** [[niches/api-infrastructure-providers/internal-platform-api-traffic/profile|Internal Platform API Traffic]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Fix (Pain Point)
**One-liner:** A platform layer's adoption is determined by how much work it imposes on the teams deploying behind it, and no platform team measures that or is measured on it.
**Tags:** #descriptive-statistics #survival-analysis #hypothesis-testing #confidence-intervals #evaluation-metrics #worker-facing #quick-win #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to carry service-to-service traffic with negligible latency cost and negligible friction for the teams deploying behind it — and whoever does that takes the platform account, because the alternative is that teams route around the layer entirely.

## The Problem
A platform team reports uptime, request volume and policy coverage. All three look good. What they do not report is that onboarding a new service takes a team two days, that the configuration requires understanding four concepts nobody documented well, that three teams have exemptions and two more have asked, and that the most common message in the platform support channel is a question about the same configuration field. The platform's real adoption problem is entirely in those numbers and none of them exists.

## Why It's Still Broken
Platform teams are measured on availability, which is the traditional infrastructure metric, and friction is the cost their internal customers pay rather than a cost they experience. Measuring it requires instrumenting the onboarding path and reading the support channel, neither of which anybody has been asked to do. And a platform team surfacing evidence that their layer is hard to use is volunteering criticism, which requires a leadership posture that invites it.

## What a Fix Looks Like
Measure the internal customer's experience as a first-class platform metric. Time from a service existing to being correctly onboarded, per service, which is the headline number and is a join between the deployment record and the platform's own registration. Steps required and how many teams complete each one, which localises where the friction is. Support requests by topic, classified from the platform channel, which names the confusing concepts directly and is a text classification task over a corpus already sitting there. Exemption and opt-out rate, which is the strongest available signal that the cost exceeds the value for somebody. Configuration surface actually used, since a platform offering ninety options where teams set six has a documentation and defaults problem rather than a capability gap. And publish all of it alongside availability, because a platform team held to both numbers builds a different product from one held to availability alone.

## Who Feels the Pain
Service teams spending days on platform onboarding; platform teams whose adoption stalls for reasons they cannot see; and organisations whose central infrastructure is quietly routed around.

## Impact If Fixed
Onboarding time and support-topic classification are both straightforward and produce the friction picture immediately. Reporting them alongside availability changes what the platform team optimises, which is the whole point.
