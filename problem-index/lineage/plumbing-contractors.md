# Lineage: Plumbing Contractors

**Industry:** [[industries/plumbing-contractors|Plumbing Contractors]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the fixture unit and Hunter's curve — a weighted load value per plumbing fixture, converted to peak design flow by a probability curve, published in NBS report BMS 65 (1940) and still the basis of pipe-sizing tables in US plumbing codes
**Builder:** National Bureau of Standards
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A plumber sizing a building's water pipe has to answer a question nobody can observe: how much water will be flowing at the worst moment?

Add up every fixture's full flow and the answer is absurd, because a hundred taps are never all open at once. Guess too low and the top floor gets a trickle when two showers run. So pipe sizes were set by local custom and by local codes, and the codes disagreed with one another with no data behind any of them.

The cost was real money. When Herbert Hoover's Commerce Department looked at housing in the 1920s, NIST's own history records the diagnosis: very little was known about how occupants used water, and **"unnecessarily restrictive code requirements were expensive to implement."** Pipe that is a size too big, repeated through every house in a country, is a large bill.

## What Got Built

A unit of load, and a curve to turn it into flow.

Each fixture type is assigned a number of **fixture units** — a weight combining how much water it draws, for how long, and how often it is used. A flush-valve toilet weighs more than a lavatory. The plumber adds up the fixture units on a branch.

**Hunter's curve** then converts that total into an expected peak flow in gallons per minute, using the probability that any given fixture is in use at the same moment as the others. Pipe size follows from the flow. The whole calculation reduces to counting fixtures and reading a table, which is how plumbing codes still present it.

Codes use a parallel drainage fixture unit to size waste and vent pipes from the fixtures that discharge into them.

## Who Built It, And Why Them

A federal laboratory, because no one else had both the motive and the test rig.

In **1921** Hoover created a building and housing division within the **National Bureau of Standards** to attack poor designs, high costs and "antiquated and obstructive building codes." His Building Code Committee found that minimum plumbing requirements could not be derived from existing codes, and NBS ran experiments on the hydraulics of house drainage. The result was *Recommended Minimum Requirements for Plumbing* — the **Hoover Code**, BH 13, revised 30 August 1928 — with **Roy B. Hunter** among its authors.

Hunter then published **BMS 65, *Methods of Estimating Loads in Plumbing Systems*, in 1940**, drawing on research reaching back to 1921 and on then-current work on plumbing for low-cost housing.

**Why NBS:** a manufacturer would have sized for its own fixtures; a plumbers' union or city code board had no laboratory and a stake in the existing rules. A neutral government lab, funded to cut the cost of housing, was the one party that gained from a smaller, defensible pipe size.

## What It Cost

**Hunter chose safety over accuracy, and said so.** His own caveat: the only complaint he had heard was that the method "tends to give larger estimates than have been found necessary for satisfactory service."

That margin compounded as fixtures got more efficient. Toilets and showerheads now use a fraction of 1940 flows, but the fixture units and the curve stayed. One critic's summary is that the curve "assumes that every home operates like a sports stadium at half-time." The result is oversized pipe: more copper, more heat lost from hot-water lines, and slow-moving water that raises water-quality concerns.

The successor is dated. **IAPMO released its Water Demand Calculator in 2017**, now in Appendix M of the Uniform Plumbing Code, which predicts peak demand for dwellings without fixture units.

## What You Still Touch

When a plumber sizes a supply line from a table in the code book, that table is Hunter's 1940 probability curve.

- [[problems/plumbing-contractors/worker-life-1|🟢 Pipe Sizing and Code Calculation Assistant]] — the direct descendant: still fixture units and code tables
- [[problems/plumbing-contractors/low-impact-2|🟡 Permit Requirement Identification by Job Type and Jurisdiction]]
- [[niches/plumbing-contractors/building-code-publishers-crossref/profile|Plumbing Code Development & Publication]]
- [[niches/plumbing-contractors/plumbing-fixture-manufacturer-rd/profile|Plumbing Fixture & Fitting Manufacturer R&D]]

**Sources:** NIST publication record, Roy B. Hunter, *Methods of Estimating Loads in Plumbing Systems*, NBS BMS 65 (1940), doi:10.6028/NBS.BMS.65; NIST Engineering Laboratory, "History of Plumbing Research at NIST" (1921 division, quoted phrases, 1928 Hoover Code, Hunter's curves and fixture-unit definition); GovInfo and NIST records for *Recommended Minimum Requirements for Plumbing*, BH 13, revised 30 August 1928, with R. B. Hunter as an author; *Official* magazine (IAPMO), "Getting Ahead of the (Hunter's) Curve" (research back to 1921, low-cost housing, Hunter's own caveat, the "stadium at half-time" quote); IAPMO press material and uniformcodes.org on the 2017 Water Demand Calculator and UPC Appendix M. ⚠️ **Not established:** the date Hunter first introduced the fixture-unit concept for drainage (some accounts place it in the 1920s Hoover work; I did not confirm it) and the first code edition to adopt BMS 65's tables. The "why NBS" comparison with other parties is my inference.
