# Perishable Markdown Methods From Large-Format Grocery

**Niche:** [[niches/retail-pos-platforms/independent-grocery-convenience/profile|Independent Grocery & Convenience]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Large grocery chains optimise perishable markdown against spoilage with established methods and dedicated systems, and an independent grocer marks down by looking at the date code and guessing.
**Tags:** #survival-analysis #time-series-forecasting #gradient-boosting #optimization-fundamentals #confidence-intervals #evaluation-metrics #revenue-impact #automation
**Contested on:** Every serious competitor in independent grocery software is fighting to reconcile direct-store-delivery invoices against what the vendor actually left on the shelf — and whoever catches the variance takes the account.

## The Problem
A department manager walks the case each morning and decides what to mark down. The decision trades margin against spoilage on a clock that varies by item, by remaining shelf life, by day of week and by how much is on hand. Marked down too early, margin is given away on product that would have sold; too late, it is thrown out at full cost. Shrink in fresh categories is one of the largest controllable costs in grocery, and at independents the decision is made entirely by feel, several times a day, by whoever is on shift.

## What Already Exists
Perishable markdown optimisation is established practice in large-format grocery, with commercial systems, published methods and a substantial literature on dynamic pricing for perishable goods. Electronic shelf labels have fallen in price to the point where independents can deploy them. Date code capture at receiving is straightforward. Demand forecasting for fast-moving grocery items is well understood. Every component is available and the methods are not secret.

## The Customization Gap
The adaptation is to a single store with no analyst and no dedicated fresh system. It requires: (1) remaining-life demand modelling per item using the platform's cross-store data, since one store's history on one item is thin and the sell-down curve for a given perishable is broadly transferable; (2) markdown recommendations at the granularity a store can act on — a batch with a shared date code on a shelf, not an individual unit — and at the times of day when staff are actually walking the case; (3) waste capture as an input, which most independents do not record at all and which has to be made a ten-second act rather than a log; (4) electronic shelf label integration where present and printed tags where not, since the execution cost of a markdown is what determines whether recommendations are followed; and (5) reporting the outcome in the only two terms the owner cares about, margin and shrink, against what the previous practice produced.

## Target Customer
Independent grocers and small grocery chains, specialty food retailers with fresh departments, and the grocery POS vendors serving them.

## Impact If Solved
Fresh shrink is a large and controllable cost on very thin margins, and the methods to manage it have existed in the chains for years. The cross-store demand curves are the adaptation that makes it work at one-store scale, and they are available only to a platform serving many stores.
