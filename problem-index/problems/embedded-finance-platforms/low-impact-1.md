# Programme Launch Configuration

**Industry:** [[embedded-finance-platforms|Embedded Finance Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every new programme is configured by hand across accounts, cards, limits, compliance rules and bank-specific constraints, and the same twenty programme archetypes are rebuilt from scratch each time.
**Tags:** #large-language-models #bert #k-nearest-neighbors #gradient-boosting #evaluation-metrics #data-integration #workflow-orchestration #automation

## The Problem
Launching a programme means deciding several hundred things. Account structure and whether balances are pooled or individually titled. Card product, network, BIN, and the fee and interchange arrangement. Transaction limits by type, velocity rules, permitted merchant categories. KYC flow, document requirements, step-up conditions, sanctions screening thresholds. Dispute handling and provisional credit policy. Statement and disclosure content. Which bank partner, and therefore which of that bank's specific constraints apply.

Most of these are not independent. A bank partner's risk appetite constrains permissible merchant categories, which interacts with the fraud rules, which interacts with the dispute policy. A consumer product and a business product diverge in ways that touch every layer.

The configuration is done by a solutions engineer working with the programme's team, largely in conversation, against documentation and precedent. It takes weeks to months. Then it is tested, corrected, and put live, and the parts that were wrong surface as production incidents.

The archetypes repeat. A payroll advance product, a business spend card, a consumer deposit account with a debit card, a marketplace payout wallet, a health savings product — the platform has launched each many times, and each launch starts from a template if it is lucky and from a blank configuration if it is not.

## What Already Exists
Platforms ship configuration APIs, sandbox environments and documentation. Some maintain templates per programme type. Bank partners publish constraint matrices. Testing frameworks exist. Implementation is staffed with solutions engineers.

## The Customisation Gap
Nothing derives configuration from the product description. A programme describing what it wants to build — in a sales call, a requirements document, or a product spec — is describing something the platform has configured before, and mapping that description to a configuration with the precedent attached is a retrieval and generation task on a corpus the platform holds.

Constraint conflicts are found by testing rather than by checking. A configuration that violates a bank partner's constraint, or that combines settings in a way that broke a previous programme, is statically detectable. Platforms discover these in the sandbox or in production.

Nothing learns from launch outcomes. Some programmes launch clean; others generate a month of incidents. The configuration differences between them are recorded and never analysed, so the platform cannot say which configuration choices predict a difficult launch.

And bank-specific constraints live in documents and in individuals' heads. A solutions engineer who knows what a particular bank partner will and will not accept holds commercially important knowledge informally, and it is re-learned by the next hire.

## Impact If Solved
Time to launch is the main thing programmes evaluate platforms on and the main constraint on how many programmes a platform can carry. Deriving configuration from the product description, checking constraints statically and learning which choices predict incidents compresses an engineering-led process into a reviewed one, and captures the bank-specific knowledge that currently leaves with the individual.
