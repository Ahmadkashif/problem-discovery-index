# Subrogation Found After the Money Is Gone

**Industry:** [[property-casualty-insurers|Property & Casualty Insurers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Claims systems already flag obvious subrogation, but recovery depends on state fault rules, limitation periods and inter-company arbitration deadlines that generic rules engines do not encode, so recoverable dollars are found after payment or not at all.
**Tags:** #bert #logistic-regression #feature-engineering #evaluation-metrics #workflow-orchestration #automation #revenue-impact

## The Problem
When a carrier pays a claim that someone else caused, it can recover the payment from the responsible party or that party's insurer. The opportunities are everywhere: the other driver in an auto collision, the manufacturer of a failed water heater, the contractor whose torch started a roof fire, the landlord whose pipe flooded a tenant's unit. Most are spotted by the adjuster who handles the claim, if that adjuster notices, has time, and remembers to refer it. The rest are found later by a recovery unit or vendor reviewing closed files. By then evidence has been discarded, the product has gone to a landfill and the limitation period may have run.

Industry rules of thumb put leakage at ~10–15% of recoverable dollars at a typical carrier (estimate). The losses concentrate where identification is hardest: property claims with a product or contractor cause, multi-vehicle auto claims where fault is split, and commercial claims where a lease or contract governs who bears the loss.

## What Already Exists
Core claims platforms (Guidewire ClaimCenter, Duck Creek Claims) have subrogation flags and rules. Analytics vendors and claims-fraud platforms offer subrogation-propensity scores. Recovery vendors work contingency books of closed files, and Arbitration Forums runs the inter-company arbitration most auto and property carriers have signed up to (recalled).

## The Customisation Gap
Recovery depends on rules a generic score does not know. Comparative fault differs by state: pure comparative, modified comparative with different bar points, and contributory negligence in a few jurisdictions; Florida moved from pure to modified in 2023. Limitation periods differ by state and by claim type, and Florida cut its general negligence period from four years to two. The made-whole doctrine and anti-subrogation rules vary. Commercial policies often carry waivers of subrogation in leases and construction contracts, so the contract has to be read before pursuing anyone. Arbitration agreements set their own filing windows and evidence rules. A useful tool reads the loss description, police report and photos for a third-party cause, checks the governing state's fault and limitation rules, looks for a waiver in the policy and the insured's contracts, preserves evidence at first notice, and tracks every recovery against its real deadline.

## Impact If Solved
Moving identification from after payment to first notice lets evidence be preserved and demands filed inside every deadline, recovering a larger share of the ~10–15% leakage (estimate) that flows straight to the loss ratio, with no change to underwriting or price.
