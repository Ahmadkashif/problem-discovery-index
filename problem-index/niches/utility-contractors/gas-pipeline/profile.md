# Gas Pipeline

**Parent Industry:** [[industries/utility-contractors|Utility Contractors]]
**Category:** High Market Share

## Profile
**Market Size:** $25-30B
**Share of Parent Industry:** ~18%
**Digital Adoption:** Medium — SCADA monitors pipeline pressure and flow. GIS tracks pipeline assets. But leak detection, integrity assessment, and PHMSA compliance documentation are heavily manual. Pipeline replacement prioritization relies on age-based rules rather than condition-based prediction.
**Target Buyer:** Gas utility contractor owner, safety director, or integrity management engineer
**Automation Potential:** High — leak probability prediction is a tabular ML problem with rich feature sets (age, material, soil, pressure, break history), and compliance documentation is a structured automation opportunity

## What Makes This a Distinct Niche
Gas pipeline contracting is the most safety-critical segment of utility construction. A gas main failure can cause explosions, fires, and fatalities — the 2018 Merrimack Valley gas explosions in Massachusetts (caused by over-pressurization during pipe replacement) killed one person, injured dozens, and damaged 131 structures. Pipeline contractors install, maintain, and replace gas mains (high-pressure transmission and medium-pressure distribution) and service lines (low-pressure connections to buildings). The aging infrastructure crisis is acute: 45% of US gas distribution mains are older than 40 years, including cast iron mains installed in the early 1900s that leak at 100x the rate of modern polyethylene pipe. Utilities are under regulatory pressure (PHMSA Pipeline Safety regulations) to replace aging pipe, creating a $10B+ annual replacement market. The replacement prioritization decision — which pipe segments to replace first — is currently based on material and age rather than actual leak probability, leading to suboptimal capital allocation.

## Current Tools & Gaps
SCADA monitors pipeline pressure and flow, detecting major leaks through pressure drops. GIS maps pipeline assets with material, diameter, installation date, and operating pressure. Leak survey crews walk or drive routes with gas detection equipment to identify leaks. PHMSA compliance requires detailed documentation of every pipeline segment's material, installation date, maximum allowable operating pressure, leak history, and integrity assessment. No tool predicts which pipe segments are most likely to leak based on the full feature set (material, age, soil conditions, proximity to trees, pressure, temperature cycling, previous break history, cathodic protection status).

## Problems
- [[niches/utility-contractors/gas-pipeline/build|🔨 Build: Pipeline Leak Probability Predictor]]
- [[niches/utility-contractors/gas-pipeline/buy|🛒 Buy: GIS Platform with Integrity Prediction]]
- [[niches/utility-contractors/gas-pipeline/fix|🔧 Fix: PHMSA Compliance Documentation]]
