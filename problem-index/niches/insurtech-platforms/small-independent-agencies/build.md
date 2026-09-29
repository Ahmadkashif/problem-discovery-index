# One Submission, Six Markets

**Niche:** [[niches/insurtech-platforms/small-independent-agencies/profile|Small Independent Agencies]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Shopping a commercial renewal means entering the same account into six carriers' submission processes by hand, and the account data is already structured in the agency system that the service representative is copying from.
**Tags:** #data-integration #bert #large-language-models #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #worker-facing
**Contested on:** Every serious competitor selling to small agencies is fighting to let a service representative shop a renewal to six markets without rebuilding the submission six times — and whoever makes application data reusable across carriers takes the agency.

## The Problem
A commercial account renews in sixty days and the incumbent carrier has indicated a significant increase. The right thing for the client is to shop it. Shopping it means the service representative entering the business description, the location schedule, the vehicle schedule, the payroll and sales figures, the loss history and a dozen supplemental questions into six different carrier portals, each asking for the same facts in a different order with a different vocabulary, over most of a day. On an account whose commission does not justify a day, the account is not shopped, and the client pays the increase.

## Why Nobody Has Built This
ACORD forms were designed for exactly this and are honoured inconsistently, because carriers want their own questions answered in their own systems and each of them individually has no incentive to accept a standard submission. That collective action problem is the whole reason this persists. The agency management system vendors have not solved it either, since they sell to agencies and the integration effort lies with carriers. Any workable answer has to operate without the carriers' cooperation for a long time, which means automating their portals rather than integrating with them.

## What to Build
A submission engine that maps the agency's structured account data onto each carrier's process, whatever that process is. Where a carrier accepts an ACORD submission, use it. Where it requires a portal, drive the portal. Where it wants a supplemental, generate the answers from the account data and flag the genuinely new questions for the representative — which is the key insight, because most supplemental questions are restatements of facts already known and only a few are new. The agency's own answer history accumulates, so a question answered for this class last month is proposed rather than asked. Carrier appetite filtering comes first, so the six markets are chosen rather than defaulted. And the whole flow is measured in what matters to the agency: minutes per market, and how many accounts got shopped that previously would not have been.

## Target Customer
Small and mid-size independent agencies, agency management system vendors, and the wholesale brokers and aggregators who serve small agencies and face the same friction at larger scale.

## Impact If Built
Remarketing capacity directly determines how many clients get a market check, which is the core value an independent agency offers over a direct writer. An agency that can shop an account in an hour rather than a day shops more accounts, retains more clients on better terms, and earns commission it currently forgoes — and the client, who is the party that actually bears the increase, benefits most.
