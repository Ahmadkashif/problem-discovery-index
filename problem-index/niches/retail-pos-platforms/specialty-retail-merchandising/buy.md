# Enterprise Demand Planning Repackaged for One Store

**Niche:** [[niches/retail-pos-platforms/specialty-retail-merchandising/profile|Specialty Retail Merchandising]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Retail demand planning and assortment optimisation is a mature enterprise software category with decades of method behind it, and nothing in it has ever been packaged for a merchant with one store and no analyst.
**Tags:** #time-series-forecasting #gradient-boosting #exponential-smoothing #dimensionality-reduction #confidence-intervals #evaluation-metrics #feature-engineering #hypothesis-testing
**Contested on:** Every serious competitor in specialty retail software is fighting to tell an independent retailer what to mark down, when, and by how much — and whoever moves end-of-season sell-through and margin most takes the account.

## The Problem
The methods that would help an independent retailer exist in full: seasonal demand forecasting, size and colour curve estimation, assortment planning, allocation, and markdown optimisation, all developed and refined in enterprise retail. They are sold as implementations costing more than an independent's annual revenue, configured by consultants, and operated by planning teams. The mismatch is entirely one of packaging and operating model, not of applicability — a store buying six hundred styles a season faces the same structure as a chain buying sixty thousand, with less data per style and more at stake per decision.

## What Already Exists
Demand forecasting libraries and hierarchical forecasting methods are open and mature. The retail planning literature on size curves, sell-through modelling and markdown optimisation is published and substantial. Commercial planning vendors serve the enterprise tier. Retail calendars, seasonality handling and promotional effect estimation are standard. Everything required is documented; nothing in the technical stack is a barrier.

## The Customization Gap
The adaptation is to one store's data volume and one owner's available attention. It requires: (1) hierarchical forecasting with borrowing across merchants, since a single store's history at style-colour-size level is too thin to forecast alone and pooling is the only route to a usable estimate; (2) size and colour curve estimation from the platform's aggregate rather than from the store's own sales, which is where independents most consistently mis-buy and where cross-merchant data is decisive; (3) an interface that presents three decisions a week rather than a planning workbench, because the user is the owner and they are also serving customers; (4) automatic handling of the data quality problems endemic to small merchants — items entered inconsistently, categories used loosely, receipts posted late — which enterprise systems assume away and which will otherwise dominate the output; and (5) outputs in the merchant's own vocabulary, since an independent buyer thinks in styles, seasons and vendors rather than in planning hierarchies.

## Target Customer
POS platforms serving specialty retail, the retail ERP vendors serving larger independents, and the consultancies currently selling planning services to merchants who cannot afford software.

## Impact If Solved
Adapting a mature discipline is far faster than inventing one and arrives with the seasonality, size curve and markdown problems already solved in principle. The pooling across merchants is the specific adaptation that makes it work at one-store scale, and it is available only to the platform.
