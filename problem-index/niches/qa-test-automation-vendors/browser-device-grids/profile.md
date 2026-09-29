# Browser & Device Grids

**Parent Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor here is fighting to offer the combinations that actually matter, on environments that behave like real ones, at a price per parallel session that beats running a lab — and whoever does that takes the grid account, because the alternative is self-hosting.

## Profile
**Market Size:** ~$820M US browser and device grid services
**Share of Parent Industry:** ~21% of category revenue
**Digital Adoption:** Very High — self-hosted labs are largely gone
**Target Buyer:** Quality and device operations functions
**Automation Potential:** High — matrix selection is an optimisation and is currently a guess

## What Makes This a Distinct Niche
A grid is an infrastructure business. The customer has decided not to maintain a room of devices and browsers, and is choosing on the breadth of the matrix, the number of parallel sessions their budget buys, how quickly a session starts, and how closely the environment behaves like a real device. It is competitive and largely commoditised, which pushes the differentiation to exactly the questions nobody answers: which of the thousands of offered combinations are worth running, whether an emulated environment is a sufficient substitute for a physical one, and what the customer is actually getting for the difference in price between providers. The customers most affected are those running large matrices, which is where the spend concentrates.

## Current Tools & Gaps
Commercial grids with large matrices, real device clouds alongside emulators, parallelisation, and session recording. The gaps: nobody can tell a customer which combinations are earning their cost, so the matrix is chosen by caution and grows monotonically; the difference between emulated and real device behaviour is real, consequential and unquantified; session start latency is a large share of elapsed time on short tests and is not reported; the matrix is selected from market share statistics rather than from the customer's own analytics, which are available; and defects found per combination is the obvious metric and is computed nowhere.

## Problems
- [[niches/qa-test-automation-vendors/browser-device-grids/build|🔨 Build: Thousands of Combinations, None of Them Evaluated]]
- [[niches/qa-test-automation-vendors/browser-device-grids/buy|🛒 Buy: Combinatorial Test Design, Forty Years Old]]
- [[niches/qa-test-automation-vendors/browser-device-grids/fix|🔧 Fix: The Emulator That Is Not the Device]]
