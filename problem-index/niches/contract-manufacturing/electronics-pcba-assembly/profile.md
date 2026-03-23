# Electronics PCBA Assembly

**Parent Industry:** [[industries/contract-manufacturing|Contract Manufacturing]]
**Category:** High Market Share

## Profile
**Market Size:** $80-100B
**Share of Parent Industry:** ~20-25%
**Digital Adoption:** High — SMT lines are heavily instrumented with AOI, SPI, and reflow profiling, but data integration across these systems is poor
**Target Buyer:** Engineering Manager or Operations Director at EMS (Electronics Manufacturing Services) companies
**Automation Potential:** High — defect classification, solder paste inspection optimization, and component counterfeit detection are data-rich automation targets

## What Makes This a Distinct Niche
Electronics PCBA (Printed Circuit Board Assembly) contract manufacturers operate high-speed SMT (Surface Mount Technology) lines that place and solder components onto PCBs at rates of 20,000-80,000 components per hour. The process generates massive data volumes from automated optical inspection (AOI), solder paste inspection (SPI), reflow oven profiling, and functional testing — but this data lives in siloed systems from different vendors (Koh Young SPI, Mirtec AOI, Heller reflow ovens) and is rarely analyzed holistically. Defect rates at best-in-class EMS companies are 50-200 DPMO (defects per million opportunities), but achieving and maintaining this level requires continuous process optimization that depends on experienced process engineers who understand the interaction between stencil design, paste volume, component placement accuracy, and reflow profile.

## Current Tools & Gaps
Koh Young and CyberOptics provide SPI systems. Mirtec, Viscom, and Koh Young provide AOI systems. Aegis FactoryLogix and Valor MSS provide MES for electronics assembly. These tools capture data within their functional domain but don't provide cross-process analytics — correlating SPI paste volume readings with downstream AOI defect detections to identify optimal paste windows, or linking reflow profile data to specific solder joint defect types. Process engineers manually perform these correlations when investigating yield problems.

## Problems
- [[niches/contract-manufacturing/electronics-pcba-assembly/build|🔨 Build: Cross-Process Yield Analytics for SMT Lines]]
- [[niches/contract-manufacturing/electronics-pcba-assembly/buy|🛒 Buy: AOI Defect Classification Tuned for Electronics Assembly]]
- [[niches/contract-manufacturing/electronics-pcba-assembly/fix|🔧 Fix: Siloed Inspection Data Across SPI, AOI, and Functional Test]]
