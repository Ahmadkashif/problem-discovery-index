# Weld Inspection & Documentation

**Parent Industry:** [[industries/metal-fabrication|Metal Fabrication]]
**Category:** Highly Automatable

## Profile
**Market Size:** $8-12B (embedded)
**Share of Parent Industry:** ~2-3% (embedded cost across all fab shops performing code or specification welding)
**Digital Adoption:** Medium — weld parameter logging is increasingly digital (Lincoln WeldCloud, Miller WeldSmart) but inspection documentation and code compliance records remain paper-based
**Target Buyer:** CWI (Certified Welding Inspector) or quality manager at fabrication shops performing AWS, ASME, or customer specification welding
**Automation Potential:** High — weld inspection accept/reject determination, inspection log documentation, and code compliance record assembly follow defined criteria from welding codes and are highly amenable to computer vision and automation

## What Makes This a Distinct Niche
Weld inspection and documentation is a horizontal function across structural steel fabrication, pressure vessels, pipeline, and specialty welding — any application where welding must meet a code (AWS D1.1, ASME IX) or customer specification. The inspection workflow is standardized: visual examination of each weld against acceptance criteria, dimensional measurement (weld size, reinforcement height, undercut depth), documentation of accept/reject disposition, and archival in the job quality record. CWIs are expensive ($75,000-$120,000/year), in short supply, and spend 20-30% of their time on documentation rather than inspection. The visual assessment task — reading weld surface appearance for defect signatures — is the highest-value application of computer vision with tacit knowledge ML in the fabrication industry.

## Current Tools & Gaps
Lincoln Electric CheckPoint and WeldCloud track welding parameters (current, voltage, wire feed speed, travel speed) per weld. Weld inspection logs are maintained on paper or in basic spreadsheets. Weld quality photos are taken with phone cameras and stored in unorganized folders. No platform connects weld parameter data to inspection results, enabling analysis of which parameter combinations produce acceptable vs. rejectable welds — the feedback loop that would allow welders to improve their technique based on inspection outcomes.

## Problems
- [[niches/metal-fabrication/weld-inspection-and-documentation/build|🔨 Build: AI-Assisted Weld Visual Inspection System]]
- [[niches/metal-fabrication/weld-inspection-and-documentation/buy|🛒 Buy: Digital Weld Inspection Log with Code Compliance]]
- [[niches/metal-fabrication/weld-inspection-and-documentation/fix|🔧 Fix: CWI Time Consumed by Documentation Rather Than Inspection]]
