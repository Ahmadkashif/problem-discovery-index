# Coding That Transfers Between Customers

**Niche:** [[niches/spend-management-platforms/gl-coding-and-erp/profile|GL Coding & ERP Integration]]
**Industry:** [[industries/spend-management-platforms|Spend Management Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The same merchant is coded correctly at four thousand customers and the model is rebuilt from nothing at the four thousand and first.
**Tags:** #transfer-learning #large-language-models #word-embeddings #evaluation-metrics #gradient-boosting #confidence-intervals #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to code transactions correctly into a chart of accounts unique to every customer without rebuilding the model from scratch each time — and whoever transfers learning across customers makes implementation weeks instead of months.

## The Problem
A cloud hosting charge is a software or infrastructure expense at essentially every company. A flight is travel. A restaurant is meals, unless it is client entertainment, which depends on who was present. The economics are near-universal; only the account names and the local conventions differ. Yet each implementation starts by asking the customer's controller how they code things and building rules, and the extensive knowledge the platform has accumulated across thousands of charts of accounts plays no part.

## Why Nobody Has Built This
Every chart of accounts looked unique, so the problem was framed as per-customer configuration rather than as mapping between representations of the same thing — and that framing made transfer look impossible rather than merely unbuilt. Implementation revenue and headcount are structured around the manual work. Controller corrections are treated as data entry rather than as labels. And nobody measured coding accuracy, so the cost of getting it wrong is invisible.

## What to Build
Model the semantics once and map per customer. Build a canonical expense taxonomy from the cross-customer data, which is the core and is the representation everything else hangs from. Map each customer's chart of accounts onto it semantically rather than by rules, since account names are natural language and the mapping is a language problem the category has treated as a configuration one. Use every controller correction as a training label, because corrections are made constantly and are the highest-quality signal available. Transfer the merchant-level knowledge immediately, so a new customer starts with thousands of merchants already understood. Learn the customer's idiosyncrasies on top of the shared base, as the last ten percent is genuinely company-specific and is where the rules belong. Predict department, class and project as well as account, since those are where most corrections happen and are usually inferable from the cardholder and context. Attach confidence and route only the uncertain to a human, which is what shrinks the controller's month. Detect chart of accounts changes, because they happen silently and break coding. Measure coding accuracy and correction rate per customer, which does not currently exist and is the metric the whole function needs. And shorten implementation using the transferred model, since that is where the commercial value lands.

## Target Customer
Implementation and product leadership, controllers correcting codes every month, ERP integration specialists, and accounting automation vendors treating each customer as a fresh problem.

## Impact If Built
Framing each chart of accounts as unique made transfer look impossible rather than merely unbuilt. The economics are near-universal, the account names are natural language, and thousands of existing mappings are training data.
