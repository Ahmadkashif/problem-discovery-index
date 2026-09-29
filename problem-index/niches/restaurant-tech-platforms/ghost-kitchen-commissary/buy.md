# Manufacturing Cost Allocation Applied to Shared Kitchens

**Niche:** [[niches/restaurant-tech-platforms/ghost-kitchen-commissary/profile|Commissary & Ghost Kitchen Operations]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Activity-based costing and shared-resource allocation are settled disciplines with mature software in manufacturing, and shared kitchens allocate cost by floor hours because that is what the booking calendar records.
**Tags:** #linear-regression #optimization-fundamentals #descriptive-statistics #confidence-intervals #evaluation-metrics #hypothesis-testing #revenue-impact #compliance
**Contested on:** Every serious competitor in shared kitchen software is fighting to allocate capacity, labour and cost across brands sharing one kitchen in a way the tenants will accept as fair — and whoever makes the allocation defensible takes the facility.

## The Problem
A multi-brand kitchen's shared costs — rent, utilities, a shared prep cook, dishwashing, packaging, delivery staging — are allocated to brands by revenue share, because revenue share is the only number available. A brand with high revenue and simple preparation subsidises one with low revenue and complex preparation, and the operator, looking at allocated profitability, concludes the wrong thing about which brands to keep. Decisions about the composition of the portfolio are made on an allocation method chosen for convenience.

## What Already Exists
Activity-based costing is a mature accounting discipline with decades of practice and literature, implemented in every serious manufacturing ERP and available in standalone tooling. Shared-resource allocation, cost driver identification and overhead absorption are standard. Equipment monitoring through simple current sensors or smart plugs is inexpensive. Labour tracking by task is available in every workforce product. All the components are commodity and none originates in restaurant technology.

## The Customization Gap
The adaptation is to a kitchen's drivers and to a facility that will not tolerate heavy process. It requires: (1) identifying the cost drivers that actually differ between brands and tenants — equipment time, cold storage footprint, labour minutes by task, packaging, wash load — rather than importing a manufacturing driver set; (2) measuring drivers cheaply, since a shared kitchen will not run a manufacturing execution system and the measurement must come from sensors, point of sale and light task logging rather than from disciplined reporting; (3) recipe-derived estimation for the drivers that cannot be measured directly, so a brand's labour minutes can be estimated from its item mix and preparation steps rather than observed; (4) transparency of method to tenants, because the allocation will be contested and a method that cannot be explained will be rejected regardless of its accuracy; and (5) sensitivity reporting, showing which allocation choices actually change the conclusions, which is the honest way to present a method with judgement in it.

## Target Customer
Multi-brand ghost kitchen operators, commissary facilities with cost-plus or membership models, and the food business incubators whose tenants ask exactly this question.

## Impact If Solved
Correct allocation changes portfolio decisions, and in a segment where operators have closed brands based on misallocated cost, that is the difference between a viable business and a series of expensive mistakes. The method is bought rather than invented; the work is in cheap driver measurement and in explaining the result to people who will argue with it.
