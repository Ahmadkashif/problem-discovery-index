# The Abstraction That Leaks Under Pressure

**Niche:** [[niches/internal-developer-platforms/provisioning-and-abstraction/profile|Provisioning & Abstraction]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Application developers learn what the platform supports by attempting something and failing, because the abstraction hides the underlying system right up until the moment it leaks.
**Tags:** #graph-theory #descriptive-statistics #k-means-clustering #logistic-regression #evaluation-metrics #confidence-intervals #worker-facing #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to hide infrastructure complexity in a way that does not collapse the first time a team needs something the abstraction cannot express — and whoever does that takes the platform, because the leak is what determines adoption.

## The Problem
A team is close to a deadline and needs a particular configuration on a resource the platform provisions. The abstraction does not expose it. The documentation does not say so; they discover it by trying. Their options are to accept a worse configuration, to file a request with the platform team and wait a week, or to provision the resource themselves outside the platform and accept that it will not be managed — and under deadline the third is chosen. The platform team learns none of this. The next four teams encounter the same limitation and make the same choice, and the platform's coverage silently declines while its reported adoption stays flat.

## Why Nobody Has Built This
Abstractions are designed from the cases the platform team knows about, which is the estate as it was when they started, and the long tail of genuine requirements is discovered by encountering it. The escape route is either absent, which forces the routing-around, or completely open, which means the abstraction guarantees nothing — and the intermediate design, where a team can escape in a bounded and visible way, has not been articulated by anybody. The escapes are invisible because they happen outside the platform. And the platform team's information about coverage comes from requests, which are filed only by the teams who chose to wait.

## What to Build
Make the escape bounded, visible and informative. Provide a supported escape path: a way for a team to specify something the abstraction does not express, recorded and attributed, without leaving the platform's management — which converts an invisible routing-around into a visible gap and is the design decision the whole niche turns on. Record every escape with what was needed and why, which is the requirement backlog the platform team cannot currently obtain and is the most valuable output. Detect the unsupported escapes too, by reconciling infrastructure that exists against infrastructure the platform provisioned, which finds the teams who left entirely. Report coverage as a measured property: what proportion of resource configurations in the estate the abstraction can express, which is computable and tells the platform team where they actually are. Warn at the point of attempt rather than at the point of failure, so a team discovers the limitation before they have built around it. Prioritise abstraction work by escape frequency rather than by request volume, since requests come from the patient and escapes come from everybody. And make the exception path fast, because its latency is what determines whether teams use it or route around.

## Target Customer
Platform engineering teams, the abstraction and provisioning tooling vendors, and the application teams currently choosing between a worse configuration and leaving the platform.

## Impact If Built
The leak under pressure is the moment that decides adoption and is invisible to the platform team. A bounded, recorded escape path converts a silent departure into a requirement, which is the input the abstraction's roadmap has never had.
