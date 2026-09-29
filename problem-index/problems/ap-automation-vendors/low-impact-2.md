# ERP Connector Depth and Coding

**Industry:** [[ap-automation-vendors|AP Automation Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The integration demo covers the standard fields and the customer's actual chart of accounts, dimensions and custom fields are mapped by a consultant over six weeks.
**Tags:** #bert #large-language-models #k-nearest-neighbors #word-embeddings #transfer-learning #evaluation-metrics #data-integration #workflow-orchestration

## The Problem
Posting an invoice to an ERP requires more than an amount and a vendor. It needs an account, a department or cost centre, often a project, class, location or grant, tax codes that vary by jurisdiction, and sometimes fields the customer invented for their own reporting.

Every ERP models this differently, and every customer configures their ERP differently. NetSuite's segments, Intacct's dimensions, SAP's cost objects and Dynamics' financial dimensions are not the same shape, and the mapping between the AP platform's model and the customer's configuration is bespoke work.

Coding an invoice to those dimensions is the recurring version of the same problem. Rules handle vendors that always map the same way. Everything else — a vendor supplying several departments, a service invoice spanning projects, a line that should be capitalised — is decided by a person.

Multi-entity customers multiply it: intercompany allocations, different charts per entity, consolidation rules, and currency.

Implementation is therefore long and consultant-led, and a meaningful fraction of deals stall in it. For the vendor it is the main constraint on how many customers can be onboarded per quarter.

## What Already Exists
Every platform ships connectors for the major ERPs with field mapping interfaces. Integration platforms provide underlying connectivity. Larger vendors employ implementation teams and partner networks. Some platforms learn coding from corrections.

## The Customisation Gap
Historical posting data is the obvious training set and is routinely ignored. A customer's ERP contains years of correctly coded AP transactions, which is a directly supervised dataset for that customer's conventions, available on day one of implementation and used by almost nobody.

Cross-customer transfer is unexploited for the same reason as in adjacent categories: charts of accounts differ in vocabulary far more than in meaning, and aligning them semantically would let a new customer start with a model informed by every similar customer already on the platform.

Mapping discovery is manual. Which of a customer's custom fields corresponds to a concept the platform models can be inferred from field names, value distributions and usage patterns, and is instead elicited in workshops.

Nothing validates a mapping against reality. A mapping that silently misposts a dimension is discovered in a month-end variance investigation, when it could be caught by replaying historical transactions through the new configuration and comparing to what the ERP actually recorded.

## Impact If Solved
Implementation length is the binding constraint on growth in this category and coding accuracy is the recurring cost of running it, and both are solved by the same asset — the customer's own posting history, sitting available and unused at the start of every project.
