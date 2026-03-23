# Candidate-to-Requisition Matching & Ranking

**Parent Industry:** [[industries/staffing-agencies|Staffing Agencies]]
**Category:** Highly Automatable

## Profile
**Market Size:** $15-20B (embedded cost across all staffing firms)
**Share of Parent Industry:** Embedded function — represents 40-60% of recruiter time across the industry
**Digital Adoption:** Medium — ATS platforms offer keyword search, but semantic matching and learned ranking are not yet standard
**Target Buyer:** VP of recruiting technology or CTO at a mid-size staffing firm looking to scale recruiter productivity
**Automation Potential:** High — the core matching problem is a well-defined ML task with abundant historical training data in placement records

## What Makes This a Distinct Niche
Candidate-to-requisition matching is the central operational challenge of every staffing agency. Recruiters spend 40-60% of their working day searching ATS databases for candidates who might fit open job orders, using keyword searches that miss 70-80% of viable matches due to vocabulary mismatches between job order language and resume language. The matching problem in staffing is distinct from corporate recruiting: staffing agencies must match one candidate to many possible job orders across multiple clients and industries, support real-time matching for urgent fill requests, and incorporate hard constraints (location, shift, credentials, availability) alongside soft skill matching. This is the single highest-leverage automation opportunity in the staffing industry.

## Current Tools & Gaps
Bullhorn's native search is keyword-based with Boolean operators. Sense and Herefish provide candidate engagement automation but do not improve matching. Eightfold AI and hireEZ offer talent intelligence from the employer side but do not address the staffing agency's multi-client, multi-industry matching problem. The gap is a semantic matching layer that sits on top of the existing ATS, encodes job orders and candidates into a shared embedding space, and returns ranked shortlists based on learned relevance from historical placement outcomes.

## Problems
- [[niches/staffing-agencies/candidate-matching-ranking/build|🔨 Build: Semantic Matching Engine with Staffing-Specific Ranking]]
- [[niches/staffing-agencies/candidate-matching-ranking/buy|🛒 Buy: Resume Parsing and Skill Normalization Layer]]
- [[niches/staffing-agencies/candidate-matching-ranking/fix|🔧 Fix: Stale Candidate Database and Reactivation Prioritization]]
