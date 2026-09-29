# Product Classification and Entity Resolution Off the Shelf

**Niche:** [[niches/procurement-spend-platforms/spend-classification-supplier-master/profile|Spend Classification & Supplier Master]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Classifying product descriptions into a taxonomy and resolving company records into entities are two of the most developed applied problems in e-commerce and data management, and procurement solves both with rules and manual merges.
**Tags:** #bert #contrastive-learning #k-nearest-neighbors #graph-theory #word-embeddings #evaluation-metrics #confidence-intervals #transfer-learning
**Contested on:** Every serious competitor in spend analytics is fighting to classify at the line item rather than the supplier and to resolve the supplier master into real entities — and whoever gets those two layers right takes every analysis built on them.

## The Problem
"NITRILE GLV PWDR FREE LG 100/BX" is a product description that any e-commerce catalogue system would classify correctly in milliseconds. "ACME INDUSTRIAL SUPPLY CO", "Acme Industrial Supply Company Inc" and "ACME IND SUPP - MIDWEST" are three records that any entity resolution system would recognise as related. Procurement systems handle the first with a keyword rule and the second with a name comparison and a manual merge queue.

## What Already Exists
Product classification into taxonomies is a mature e-commerce problem with strong pre-trained models, public benchmarks and commercial services. UNSPSC and the standard procurement taxonomies are published. Entity resolution and corporate linkage are mature disciplines with commercial data — Dun & Bradstreet's linkage in particular — and open tooling. Supplier enrichment providers already deliver firmographics into these systems. Every component is available and much of it is already licensed.

## The Customization Gap
The adaptation is to procurement's own taxonomy and to a supplier graph that is a buying relationship rather than a legal structure. It requires: (1) mapping into the procurement taxonomy the organisation actually manages categories against, which is usually a customised derivative of a standard and is what makes an off-the-shelf classifier's output unusable without translation; (2) services and indirect spend handled as first-class, since e-commerce classification is built for physical goods and a large share of enterprise spend is consulting, software, logistics and facilities where the description is a project name; (3) a supplier graph that models the buying relationship — which legal entity is contracted, which is invoiced, which is the negotiating counterparty — since these frequently differ and the negotiation position depends on the third; (4) pooled learning across the platform's customers, since the same suppliers and items recur and a shared corpus is the one advantage a platform has over an enterprise doing this alone; and (5) confidence-gated human review with the corrections feeding back, because procurement taxonomies are organisation-specific and a general model will always need local adaptation.

## Target Customer
Procurement platform vendors, spend analytics providers, and the enterprises whose classification is currently a rules table maintained by an analyst.

## Impact If Solved
The classification and resolution technology is bought rather than built, and the adaptation is to the taxonomy and the services spend. Pooled learning across customers is the element that makes a platform's classification structurally better than an enterprise's own, which is the argument for buying the capability rather than building it internally.
