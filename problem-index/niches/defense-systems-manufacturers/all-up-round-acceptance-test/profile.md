# All-Up-Round Assembly & Acceptance Test

**Parent Industry:** [[industries/defense-systems-manufacturers|Defense Systems Manufacturers]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this niche is fighting to get finished rounds through acceptance test the first time, and whoever raises first-pass yield at all-up-round acceptance test takes the account.

## Profile
**Market Size:** ~$400M a year of test station software, test data analytics, failure analysis and MES tooling on missile final-assembly lines (estimate)
**Share of Parent Industry:** ~0.8% of the five codes' receipts (estimate)
**Digital Adoption:** Medium — test stations log everything, but failure analysis, retest decisions and links back to build records are manual
**Target Buyer:** Director of missile final assembly and test; test engineering manager
**Automation Potential:** High for failure triage and correlation; low for disposition

## What Makes This a Distinct Niche
At the prime's own plant, sections arrive from suppliers and in-house cells and are integrated into a round, then tested: electrical continuity, guidance and seeker functional checks, built-in test and environmental screens. A round that fails is diagnosed, reworked and retested, consuming test-station hours that are themselves a rate constraint. The contest here is not sub-tier supply but yield at the last gate, and the winner is whoever turns test failures into root causes fastest and stops them recurring. The data (test results, build records, rework histories) belong to the prime, unlike the supplier data in [[niches/defense-systems-manufacturers/solid-rocket-motor-supply/profile|Solid Rocket Motor & Propellant Ingredient Supply]].

## Current Tools & Gaps
Custom automated test equipment software, MES (iBASEt Solumina, Siemens Opcenter), failure reporting, analysis and corrective action systems, and PLM. Gaps: failures analysed one round at a time; no cross-round correlation of test signatures with supplier lots, build stations or rework; "retest OK" outcomes that hide intermittent faults. The EMS-side test analytics in [[niches/electronics-contract-mfg/test-engineering-departments/profile|Test Engineering Departments]] cover boards, not rounds.

## Problems
- [[niches/defense-systems-manufacturers/all-up-round-acceptance-test/build|🔨 Build: Root-Cause Linking From Round Test Failures to Build Records]]
- [[niches/defense-systems-manufacturers/all-up-round-acceptance-test/buy|🛒 Buy: Electronics Test Analytics Adapted to Missile Acceptance]]
- [[niches/defense-systems-manufacturers/all-up-round-acceptance-test/fix|🔧 Fix: The Failure Retested Until It Passes]]
