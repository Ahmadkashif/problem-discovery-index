# Engineering Change Order Management

**Parent Industry:** [[industries/contract-manufacturing|Contract Manufacturing]]
**Category:** Highly Automatable

## Profile
**Market Size:** $5-8B (embedded)
**Share of Parent Industry:** ~1-2% (embedded engineering cost across all CMs)
**Digital Adoption:** Medium — PLM systems track ECOs but impact assessment, BOM traversal, and re-qualification determination remain manual engineering tasks
**Target Buyer:** Engineering manager or PLM administrator at CMs managing 10+ concurrent programs
**Automation Potential:** High — ECO impact assessment follows a deterministic analysis pattern (BOM traversal, process impact classification, regulatory trigger detection) that is currently performed manually by experienced engineers

## What Makes This a Distinct Niche
Engineering Change Orders are the most disruptive recurring event in contract manufacturing — OEMs issue design changes that ripple through BOM structures, process documentation, tooling, test fixtures, and quality specifications. The CM must assess impact, estimate cost and timeline, negotiate the change with the OEM, and implement it across all affected systems. For a CM running 20-50 concurrent programs, ECO volume is 5-20 per week, and each ECO assessment consumes 3-10 engineering days. The ECO management process is structurally the same across all CMs regardless of industry segment — making it a horizontal automation target that benefits medical device, aerospace, electronics, and commercial CMs equally.

## Current Tools & Gaps
Arena PLM and Windchill PTC manage ECO workflow routing, version control, and approval chains. These tools track the ECO through its lifecycle but don't perform the engineering analysis — determining which BOMs are affected, which process steps change, whether regulatory re-qualification is triggered, and what the implementation cost and timeline will be. This analysis is performed manually by engineering staff who must trace through documentation that may span multiple systems.

## Problems
- [[niches/contract-manufacturing/engineering-change-order-management/build|🔨 Build: AI-Powered ECO Impact Assessment Engine]]
- [[niches/contract-manufacturing/engineering-change-order-management/buy|🛒 Buy: PLM with Manufacturing Impact Analysis]]
- [[niches/contract-manufacturing/engineering-change-order-management/fix|🔧 Fix: Manual BOM Traversal for Change Impact]]
