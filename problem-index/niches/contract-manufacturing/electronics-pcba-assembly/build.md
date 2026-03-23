# Cross-Process Yield Analytics for SMT Lines

**Niche:** [[niches/contract-manufacturing/electronics-pcba-assembly/profile|Electronics PCBA Assembly]]
**Industry:** [[industries/contract-manufacturing|Contract Manufacturing]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No platform correlates SPI paste volume measurements, pick-and-place accuracy data, reflow oven profiles, and AOI defect detections across the full SMT process to identify which upstream parameter combinations cause downstream defects — the holistic process optimization that experienced engineers do manually but takes hours per investigation.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #tacit-knowledge-ml #revenue-impact

## The Problem
An SMT line is a sequential process: solder paste printing (SPI measures paste volume per pad), component placement (pick-and-place records placement accuracy), reflow soldering (oven profile determines thermal exposure), and inspection (AOI detects solder joint defects). A bridging defect detected at AOI could be caused by excess paste volume (SPI step), component misalignment (placement step), or incorrect reflow profile (thermal step). Currently, when AOI detects elevated defect rates, a process engineer manually pulls data from SPI, placement, and reflow systems to investigate root cause — a 2-4 hour data gathering exercise before analysis can begin. Experienced engineers develop intuition for which upstream indicators predict downstream defects, but this knowledge is individual and informal.

## Why Nobody Has Built This
Each SMT process station uses a different vendor's system (Koh Young SPI, Panasonic pick-and-place, Heller reflow, Mirtec AOI) with different data formats, different APIs, and different data granularity. Building cross-process analytics requires integrating data from 4-6 different vendor systems at the individual pad/component level — matching a paste volume reading for pad J7 from SPI to the placement accuracy for component U3 at pick-and-place to the solder joint quality for that specific joint at AOI. This pad-level data integration is a complex engineering problem that no single vendor has incentive to solve because it requires cooperation across competitor boundaries.

## What to Build
A cross-process analytics platform that ingests data from SPI, pick-and-place, reflow profiling, and AOI systems via vendor APIs and standardized file formats (IPC-CFX is an emerging standard). At the pad/component level, it correlates upstream measurements with downstream defect outcomes. A gradient boosting model identifies which process parameter ranges (paste volume, placement offset, reflow peak temperature) predict defect-free solder joints vs. defect conditions for each component type. Process engineers receive recommendations: "For 0402 passives, paste volume between 85-95% of nominal with placement offset <25 microns yields <10 DPMO."

## Target Customer
Process engineering managers at EMS companies running 5+ SMT lines, where yield optimization across multiple products and platforms is a continuous engineering effort. Approximately 1,500-2,000 EMS companies in the US.

## Impact If Built
Reduces defect investigation time from 2-4 hours to 15-30 minutes by pre-computing cross-process correlations. Enables proactive yield optimization — identifying process drift before defect rates increase. For an EMS company running $50M in annual PCBA production at 150 DPMO, reducing to 75 DPMO saves $200,000-$500,000 in rework and scrap annually.
