# Agtech Platforms

## Profile
**Category:** Vertical SaaS
**Market Size:** ~$4B US agricultural software, farm management and digital agronomy
**Tech Maturity:** High instrumentation, low inference — John Deere Operations Center, Climate FieldView, Trimble, AGCO and a long tail of farm management systems collect an enormous volume of machine and field data. The industry's central question, which input actually caused which yield, remains answered by anecdote and vendor trial plots.
**Workforce:** Agronomy data specialists, machine data integration engineers, implementation and dealer support staff, sustainability and compliance analysts, customer success managers

## Key Pain Themes
Agriculture instrumented itself thoroughly and learned surprisingly little. Every pass across a field is recorded — planting population and depth, application rate and product, harvest yield at sub-metre resolution — and the causal question underneath it all is almost never answered: did that seed treatment, that fungicide timing, that nitrogen rate actually change the outcome on this farm, or did the weather. Growers make six-figure input decisions annually on the basis of a neighbour's experience and a retailer's trial plot. Below that sits a data problem that has defeated the industry for two decades: machine data from different equipment brands does not reconcile, so a farm running mixed colours cannot assemble a coherent field record. Sustainability and compliance reporting has arrived as a genuine new burden with real money attached and no infrastructure. And the two people doing the work — the agronomist writing scouting reports and the farm office manager reconciling records — spend their seasons on transcription.

## Current Tech Landscape
John Deere Operations Center is the dominant platform by installed base and is tied to Deere equipment; Climate FieldView is the largest brand-independent option; Trimble and AGCO serve mixed fleets with varying success. Farm management and recordkeeping systems (Agworld, Conservis, Granular) handle planning and compliance. Satellite and drone imagery is widely available and mostly used for visual scouting rather than measurement. Variable rate prescription writing is standard practice; prescription outcome measurement is not. Carbon and sustainability programmes have created a new class of measurement and verification requirements that the existing stack was never designed for.

## Problems
- [[problems/agtech-platforms/high-impact|🔴 High Impact: Yield Attribution and On-Farm Trial Design]]
- [[problems/agtech-platforms/low-impact-1|🟡 Low Impact: Cross-Brand Machine Data Reconciliation]]
- [[problems/agtech-platforms/low-impact-2|🟡 Low Impact: Sustainability and Compliance Reporting]]
- [[problems/agtech-platforms/worker-life-1|🟢 Worker Life: Agronomist Scouting Report Writing]]
- [[problems/agtech-platforms/worker-life-2|🟢 Worker Life: Farm Office Record Reconciliation]]
- [[problems/agtech-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/agtech-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
The platforms hold what is, in principle, the largest agricultural experiment ever run: millions of field-seasons with recorded inputs, recorded management and geo-referenced yield outcomes, across every soil type and climate in the country. The variation across growers is enormous and largely unexploited. What the industry does instead is run small replicated plot trials at research farms and extrapolate. The gap between the evidence available and the evidence used is the defining feature of the category.
