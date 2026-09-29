# Legacy Codebase Comprehension

**Parent Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Category:** Low Digitized
**Contested on:** Every serious competitor here is fighting to let an engineer understand and safely change a system written decades ago by people who have left — and whoever does that takes the enterprise, because these estates run the business and nobody dares touch them.

## Profile
**Market Size:** ~$1.2B US attributable to legacy comprehension, documentation and modernisation tooling
**Share of Parent Industry:** ~9% of category revenue
**Digital Adoption:** Very Low — modern tooling largely does not reach these estates
**Target Buyer:** Enterprises in banking, insurance, government and industrial sectors
**Automation Potential:** High — the code is complete and static and the analysis is mechanical

## What Makes This a Distinct Niche
Enormous quantities of code that run banks, insurers, utilities and governments were written between twenty and fifty years ago, in languages and styles the current tooling ecosystem has largely ignored, by people who have retired. The organisations maintaining them are in a specific and well-known bind: the systems work, nobody fully understands them, the people who did are gone, changes are made by the smallest possible increment with the largest possible caution, and every modernisation proposal founders on the fact that nobody can specify what the system currently does. This is a comprehension problem before it is a modernisation problem, and it is distinct from ordinary code navigation because the difficulty is not finding a definition but reconstructing intent from code that encodes decades of accumulated business rules with no accompanying explanation.

## Current Tools & Gaps
Vendor-specific tooling from the mainframe platform providers; modernisation and transpilation services from consultancies; static analysis for some of these languages; and documentation that is out of date where it exists at all. The gaps: navigation and cross-reference tooling is primitive compared to modern ecosystems and is where most of the daily friction is; business rules are embedded in code with no separation, so nobody can enumerate what the system actually decides; dead code is a large fraction of these estates and nobody knows which fraction; the dependency structure between programs, jobs and data is undocumented; and modernisation projects consume enormous budgets and fail at a well-documented rate, largely because they begin without understanding the system being replaced.

## Problems
- [[niches/developer-tools-vendors/legacy-codebase-comprehension/build|🔨 Build: The System Nobody Can Specify]]
- [[niches/developer-tools-vendors/legacy-codebase-comprehension/buy|🛒 Buy: Program Analysis That Predates the Problem]]
- [[niches/developer-tools-vendors/legacy-codebase-comprehension/fix|🔧 Fix: Nobody Knows Which Half Is Dead]]
