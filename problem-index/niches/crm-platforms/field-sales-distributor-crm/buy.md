# Retail Execution Tooling for Distributor Field Teams

**Niche:** [[niches/crm-platforms/field-sales-distributor-crm/profile|Field Sales & Distributor CRM]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Consumer goods companies have mature retail execution software with shelf recognition, planogram compliance and store-visit workflows, and distributors doing structurally identical work use a customised enterprise CRM.
**Tags:** #cnns #object-detection #semantic-segmentation #evaluation-metrics #confidence-intervals #automation #data-integration #worker-facing
**Contested on:** Every serious competitor in field sales software is fighting to capture what happened on a call from a vehicle in under a minute without typing — and whoever the representatives actually use takes the account.

## The Problem
A large consumer goods manufacturer's field team photographs a shelf and receives an automatic assessment: which products are present, whether the planogram is being followed, what share of shelf the brand holds, whether the competitor has gained facings. A distributor's representative standing in front of a comparable shelf writes "competitor has more space in the cooler" in a text field. The capability gap is entirely one of who bought software and who did not.

## What Already Exists
Retail execution platforms with image-based shelf recognition are a mature commercial category serving large consumer goods manufacturers, with product recognition, share-of-shelf computation, out-of-stock detection and planogram compliance all deployed at scale. The underlying vision capability — fine-grained product recognition from a shelf photograph — is well developed. Store visit workflows, task management and territory tooling are standard within those platforms. Everything exists and is priced for enterprise manufacturers.

## The Customization Gap
The adaptation is to a distributor's economics and product range. It requires: (1) a product catalogue built from the distributor's own range rather than from a manufacturer's brand set, which is a larger and messier set and where recognition has to handle private label and long-tail items; (2) cost structure suitable for a distributor rather than a global manufacturer, which points at on-device inference and a per-representative price rather than an enterprise programme; (3) the order as the primary output, since a distributor's representative is taking an order while a manufacturer's is checking compliance — the photograph should suggest the order rather than only score the shelf, which is a different and more directly valuable framing; (4) out-of-stock and low-stock detection tied to the distributor's own delivery schedule, so the observation becomes an order line rather than a report; and (5) competitive observation as a first-class structured output, since that is what the distributor's principals actually want from the field and what is currently lost in free text.

## Target Customer
Distributors and wholesalers with field sales teams, manufacturer representative organisations, and the retail execution vendors who could reach a much larger market with a repackaged offering.

## Impact If Solved
Shelf recognition turning into a suggested order is the specific adaptation that makes this pay for a distributor rather than for a brand, and it converts an observation into a transaction in the same interaction. The capability is deployed and proven one tier up, which makes this a distribution and packaging problem rather than a technical one.
