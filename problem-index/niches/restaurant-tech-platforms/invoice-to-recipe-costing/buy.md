# Product Matching Methods From E-Commerce

**Niche:** [[niches/restaurant-tech-platforms/invoice-to-recipe-costing/profile|Invoice-to-Recipe Costing]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Matching messy product descriptions to a canonical catalogue is one of the most studied problems in e-commerce, with published methods, open datasets and off-the-shelf tooling, and restaurant back office solves it by asking the chef.
**Tags:** #bert #word-embeddings #contrastive-learning #k-nearest-neighbors #evaluation-metrics #confidence-intervals #transfer-learning #data-integration
**Contested on:** Every serious competitor in restaurant back office is fighting to map a distributor invoice line to the recipe ingredient it actually is, at a cost per usable unit — and whoever holds the automatic match rate highest takes the account.

## The Problem
"TOM DCD IN JUICE 6/#10" is diced tomatoes in juice, six number-ten cans. A human in the industry reads that instantly. A string comparison does not. Every back-office vendor has built some heuristic matching and every one of them falls back to the customer for a large share of lines, because abbreviation expansion, unit parsing and brand handling were treated as string problems rather than as the entity resolution problem they are.

## What Already Exists
Product matching and entity resolution are extensively developed in e-commerce: sentence embedding models fine-tuned for product text, contrastive training on matched pairs, blocking and candidate generation at scale, and public benchmarks with strong published baselines. Off-the-shelf embedding models handle abbreviated retail product text far better than any hand-built heuristic. GS1 and GTIN identifiers exist where distributors supply them. The tooling and the literature are directly transferable.

## The Customization Gap
The adaptation is to foodservice distribution's particular messiness. It requires: (1) an abbreviation and unit vocabulary specific to broadline foodservice, which is conventional within the industry and opaque outside it, and which is the single highest-leverage piece of domain input; (2) pack size and unit-of-measure parsing as a first-class task rather than an afterthought, since a correct ingredient match with a wrong unit produces a plate cost that is wrong by an order of magnitude and looks plausible; (3) training pairs harvested from the vendor's own confirmed mappings, which exist in the hundreds of thousands and have never been assembled as a dataset; (4) handling the many-to-one and one-to-many cases — several distributor items mapping to one ingredient, or a single item serving several recipes at different yields — which e-commerce matching mostly does not face; and (5) calibrated confidence, so the automatic share is set by the customer's tolerance and the match rate can be reported honestly rather than claimed.

## Target Customer
Restaurant back-office vendors, foodservice distributors who would like their invoices to flow into customers' systems cleanly, and the operators paying for a product whose value is gated on this one step.

## Impact If Solved
Match rate is the metric that determines whether this category of product delivers what it sells, and adapting a mature matching discipline is far cheaper than continuing to refine heuristics. The vendor's own confirmed mappings are a large, free, labelled dataset that has been sitting unused in every one of these companies.
