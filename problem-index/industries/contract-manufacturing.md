# Contract Manufacturing

**Category:** Manufacturing & Industrial
**Tags:** #tabular-ml #time-series-forecasting #anomaly-detection #computer-vision #nlp #automation #compliance

## Industry Overview

The US contract manufacturing industry generates approximately $400 billion annually across electronics, medical devices, consumer goods, aerospace, and industrial components. Contract manufacturers (CMs) produce finished goods or subassemblies to OEM specifications — the OEM designs the product, the CM owns the production process, equipment, and workforce. The market ranges from small job shops ($5-50M revenue) to global CMOs like Foxconn, Jabil, Flex, and Benchmark Electronics.

The defining economic structure: CMs bid on programs where they will produce a known part or assembly at scale. Margin pressure is intense — OEMs use competitive bidding, and CMs compete primarily on price, quality record, and lead time reliability. The typical EBITDA margin for a CM is 5-12%. Cost overruns on a program (yield losses, rework, material waste) are absorbed by the CM, not the OEM.

## Dominant Platforms

- **Epicor / Infor / SAP** — ERP platforms dominant in mid-to-large contract manufacturers for production scheduling, BOM management, and costing
- **Plex Systems / QAD** — Manufacturing-specific cloud ERP with production floor integration, quality management, and traceability
- **Arena / Windchill PLM** — Product lifecycle management for BOM and engineering change order management
- **MES systems (Rockwell FactoryTalk, Siemens Opcenter)** — Manufacturing execution systems for production floor tracking, SPC, and quality data capture
- **Arena / Greenlight Guru** — Quality management systems for medical device CMs under 21 CFR Part 820

## Workforce and Knowledge Structure

Contract manufacturing operations depend on the tacit knowledge of experienced process engineers, quality technicians, and machine operators. A process engineer with 10 years on a specific product line knows which machine combinations produce the best yield on a given material lot, how to interpret SPC chart patterns before they generate an out-of-control alarm, and how incoming material lot variation affects process windows. This knowledge is not in any procedure document.

Quality inspection relies on trained inspectors who recognize acceptable vs. rejectable cosmetic and dimensional conditions from reference standards — a judgment call that varies by inspector, shift, and experience level. Incoming material inspection for electronic components requires knowledge of counterfeit indicators specific to each component category.

Medical device and aerospace CMs operate under mandatory process qualification requirements: every process change requires documented validation (IQ/OQ/PQ), and production records must be traceable to device history records (DHR) for the full useful life of the device.

## Key Economic Pressures

- Yield and scrap cost — yield loss on a high-value program is directly absorbed by the CM; 1% yield improvement on a $10M program is $100,000 in recovered margin
- Rework labor cost — rework on production line failures is unplanned labor that destroys program profitability; rework cost visibility and root cause attribution is often poor
- Engineering change order (ECO) management — OEM-driven design changes mid-program require coordinated BOM updates, process re-qualification, and inventory obsolescence management
- Quality escapes — a quality escape (non-conforming product shipped to OEM or end customer) triggers corrective action process, potential recall costs, and contractual penalties
- Capacity planning — quoting a new program requires accurate capacity analysis against existing programs; over-commitment leads to delivery failure, under-commitment leaves margin on the table

## Adjacencies

[[problems/contract-manufacturing/high-impact|High Impact]] · [[problems/contract-manufacturing/low-impact-1|Low Impact 1]] · [[problems/contract-manufacturing/low-impact-2|Low Impact 2]] · [[problems/contract-manufacturing/worker-life-1|Worker Life 1]] · [[problems/contract-manufacturing/worker-life-2|Worker Life 2]] · [[problems/contract-manufacturing/ml-opportunity|ML Opportunities]] · [[problems/contract-manufacturing/ai-agents-platforms|AI Agents & Platforms]]
