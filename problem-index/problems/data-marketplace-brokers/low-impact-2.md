# Licence Term Expression and Enforcement

**Industry:** [[data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every dataset arrives with permitted-use terms written in contract prose, and nothing in the delivery path knows what they say — so compliance depends on whoever read the agreement remembering it two years later.
**Tags:** #large-language-models #bert #transformers #word-embeddings #transfer-learning #evaluation-metrics #compliance

## The Problem
Data licences are specific and restrictive. Internal analytics but not resale. Modelling but not model training. Use in a product but not display to end users. Retention for the term and deletion afterwards. Territory restrictions. Sublicensing prohibited. Attribution required.

These terms live in a signed agreement. The data lands in a warehouse. Between the two there is no connection at all.

Two years later an engineer who never saw the contract joins a table into a training pipeline. A product team builds a feature that displays derived values to customers. An analyst shares an extract with a partner. Each may breach a term nobody in the room knew existed.

The exposure has grown sharply. Data used to train models is now a live litigation and regulatory question, and licences increasingly address it explicitly — which means the distinction between permitted analytics and prohibited training is now the most consequential term in many agreements and the one least likely to reach the engineer.

The marketplaces deliver the data and the contract separately, and consider the terms the buyer's problem.

## What Already Exists
Contract lifecycle management systems store agreements and extract metadata. Data catalogues (Collibra, Alation, Atlan, Unity Catalog) support tagging and policy attachment. Access control in modern warehouses is granular and capable. Data lineage tracking has matured considerably. Some marketplaces publish standardised licence templates. Creative Commons demonstrated machine-readable licence expression decades ago.

## The Customisation Gap
Licence terms are never converted into a machine-readable form, so the capable policy engines in the warehouse have nothing to enforce. The catalogue can hold a tag and nobody generates the tag from the contract.

Extracting permitted use, prohibited use, retention period, territory and attribution requirements from a data licence is a well-shaped document task on a document class that is fairly standardised in structure. Once extracted, most of the terms map onto access controls and lineage checks that the warehouse can already enforce.

Downstream lineage is where the real enforcement lives. Whether a restricted dataset has flowed into a training pipeline, a customer-facing feature or an external share is answerable from lineage graphs that most modern platforms already maintain, and nothing checks it against licence terms.

Retention and deletion obligations are the quietly universal failure. Almost every licence requires deletion at termination, almost nobody deletes, and this is directly enforceable from an expiry date and a lineage graph.

## Impact If Solved
Licence breach exposure has grown from a contractual footnote to a material risk as model training became a contested use, and compliance currently depends on institutional memory. Extracting terms into enforceable policy uses infrastructure buyers already own and converts an unmanaged risk into an automated control.
