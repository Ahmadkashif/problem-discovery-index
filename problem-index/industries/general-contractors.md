# General Contractors

## Profile
**Category:** Construction & Trades
**Market Size:** ~$450B in US general contracting (commercial and residential combined); SMB GC segment (firms under $50M annual revenue) accounts for ~$200B
**Tech Maturity:** Low — Procore and Buildertrend have strong adoption for project management and scheduling; estimating software (Sage, Bluebeam, PlanSwift) exists; AI and ML are essentially absent from the GC's workflow
**Workforce:** Project managers, superintendents, estimators, foremen, carpenters, laborers, subcontractor crews — a mid-size GC running 10-15 simultaneous projects employs 50-200 people in a highly distributed, field-based operation

## Key Pain Themes
General contracting margins are notoriously thin (3-7% net on most commercial projects) and the primary levers for profitability are accurate estimating, subcontractor reliability, and change order management — all of which depend on internalized pattern recognition that experienced GC operators develop over decades. Estimating is the industry's most consequential judgment task: experienced estimators have built a mental model of cost per square foot by project type, structural system, and local market conditions that allows them to gut-check a takeoff before it's complete — a skill that takes 10+ years to develop and that junior estimators cannot replicate without significant supervision. Subcontractor reliability is the second major variable: experienced superintendents and project managers have mental models of which subs show up, do quality work, and don't inflate change orders — but this knowledge is informal, not shared across the firm, and lost when a key employee leaves. Change order management is where most GC profitability leaks occur: owners scope-creep projects without formally authorizing changes, documentation is delayed and then disputed, and GCs lose legitimate claims because they weren't documented in real time.

## Current Tech Landscape
Procore is the industry-standard project management platform for GCs doing $5M+ in annual revenue — it handles RFIs, submittals, daily reports, and change orders. Buildertrend serves the residential GC market. Estimating software (Sage Estimating, PlanSwift, STACK) handles digital takeoffs but requires experienced estimators to apply the unit costs. Subcontractor management software (Procore Subcontractors, Vet the Sub) provides some vendor management capability. Drones (DJI, Wingtra) are increasingly used for site surveys but with minimal AI interpretation. The intelligence gap — predictive cost modeling from plan images, subcontractor performance scoring, schedule delay prediction — is entirely absent.

## Problems
- [[problems/general-contractors/high-impact|🔴 High Impact: AI-Assisted Preliminary Cost Estimation from Architectural Drawings]]
- [[problems/general-contractors/low-impact-1|🟡 Low Impact: Subcontractor Performance Scoring and Bid Analysis]]
- [[problems/general-contractors/low-impact-2|🟡 Low Impact: Change Order Documentation from Field Observations]]
- [[problems/general-contractors/worker-life-1|🟢 Worker Life: Job Site Progress Reporting from Photos]]
- [[problems/general-contractors/worker-life-2|🟢 Worker Life: Schedule Delay Cascade Prediction]]
- [[problems/general-contractors/ml-opportunity|🔵 ML Opportunities]]
- [[problems/general-contractors/ai-agents-platforms|🤖 AI Agents & Platforms]]
