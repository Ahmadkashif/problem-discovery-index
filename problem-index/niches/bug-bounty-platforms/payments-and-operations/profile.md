# Payments & Programme Operations

**Parent Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Category:** Highly Automatable
**Contested on:** Whether the administrative shell around a programme — payouts across jurisdictions, budget control, tax handling, sanctions screening — runs itself or consumes staff attention every cycle.

## Profile

**Market Size:** ~$30M
**Share of Parent Industry:** ~2%
**Digital Adoption:** Moderate — the mechanics are largely solved
**Target Buyer:** Platform operations, finance and compliance functions
**Automation Potential:** Very high — it is repeatable process

## What Makes This a Distinct Niche

Around the marketplace sits an operational layer: paying independent individuals in many countries, screening them against sanctions lists, handling tax documentation across jurisdictions, managing programme budgets and accruals, and running the administrative machinery of launching, scoping and closing programmes.

The platforms have built this reasonably well — cross-border payment is genuinely one of the things they do best, and it is a real barrier to a programme running independently. But it is the smallest niche in the industry and the one where the remaining friction is most obviously mechanical rather than conceptual.

The contest, such as it is, is about whether this layer is invisible. Every hour a programme manager spends on payout approvals, budget reconciliation or tax paperwork is an hour not spent on scope, triage quality or researcher relations. And the friction falls hardest on the researcher, for whom payment delay and tax complexity are a real cost of participation that platforms treat as solved because the money eventually arrives.

## Current Tools & Gaps

Platform payment infrastructure with multiple rails, currency handling and payout scheduling. Sanctions and jurisdiction screening. Tax documentation collection at the platform level. Programme configuration for scope, reward tables and budgets. Budget tracking with accruals. Invoicing to programmes.

The gaps are small individually and add up. Payout timing is opaque to researchers — approved and paid are different events separated by an unpredictable interval nobody reports. Tax support ends at issuing a form, leaving researchers with irregular international income to work out their own position. Budget controls are coarse, so a programme cannot easily express a spending policy beyond a total. Programme launch is a manual configuration exercise repeated per programme. And reward tables are set once and rarely revisited against what the programme actually pays, which is a reconciliation nobody performs.

## Problems

- [[niches/bug-bounty-platforms/payments-and-operations/build|🔨 Build: The Invisible Operations Layer]]
- [[niches/bug-bounty-platforms/payments-and-operations/buy|🛒 Buy: Global Contractor Payments, Already Solved]]
- [[niches/bug-bounty-platforms/payments-and-operations/fix|🔧 Fix: Approved Is Not Paid]]
