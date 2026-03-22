# VCPR Tracking Across Species and Farm Clients

**Niche:** [[niches/veterinary-practices/mixed-animal-rural/profile|Mixed Animal Rural]]
**Industry:** [[industries/veterinary-practices|Veterinary Practices]]
**Type:** Fix (Pain Point)
**One-liner:** Veterinarians can only prescribe medications when a valid Veterinary-Client-Patient Relationship (VCPR) exists — but rural vets managing hundreds of farm clients across multiple species track VCPR status manually, risking prescribing without a valid relationship and exposing themselves to regulatory action.
**Tags:** #decision-trees #feature-engineering #compliance #automation #worker-facing

## The Problem
A VCPR — the legal foundation allowing a veterinarian to prescribe, dispense, and treat — requires that the vet has recently examined the animal (or representative animals in a herd) and has sufficient knowledge of the animal to make diagnostic and treatment decisions. VCPR requirements vary by state (some require annual renewal, others require examination within the last 12 months for each species on a farm), and the definition of "sufficient knowledge" differs for individual companion animals vs. herds. A rural mixed vet may have valid VCPRs with 50 companion animal households and 80 farm operations, each with different species, different last-exam dates, and different state-specific renewal requirements. When a farmer calls at 10 PM asking the vet to prescribe antibiotics for a sick calf, the vet must determine whether they have a valid VCPR for that farm's cattle — and currently, this determination relies on memory or flipping through paper records while standing in the barn.

## Why It's Still Broken
No PMS tracks VCPR status as a discrete entity. Cornerstone tracks when a patient was last seen, but VCPR is a relationship-level concept — it applies to a client-species pair (e.g., "I have a VCPR with Smith Ranch for their cattle, but NOT for their horses because I've never examined their horses"). Building VCPR tracking requires understanding the legal definition per state, mapping it to exam records per client per species, and alerting the vet when a VCPR is expiring or when they're about to prescribe without one. This is a compliance problem that every mixed practice vet knows about and manually manages through memory and paper, but no software vendor has addressed because the companion animal market (where VCPR is simpler — one pet, one household, one annual exam) is far larger and more profitable.

## What a Fix Looks Like
A VCPR management layer (standalone or PMS-integrated) that: (1) maintains a VCPR registry showing every active client-species relationship with last examination date and calculated expiration based on state-specific rules, (2) alerts the vet before prescribing when a VCPR is expired or has never been established for the requested species, (3) generates proactive notifications when VCPRs are approaching expiration ("Your VCPR with Johnson Farm for swine expires in 30 days — schedule a herd health visit"), (4) produces an auditable VCPR compliance report for state veterinary board inspections. Decision-tree logic handles the state-specific rule variations and species-specific examination requirements.

## Who Feels the Pain
The rural mixed vet who mentally juggles VCPR status for 100+ farm clients across 3-5 species while fielding after-hours prescription requests, and who faces regulatory action if they prescribe without a valid VCPR — a risk that increases as the practice grows and the vet's memory becomes less reliable.

## Impact If Fixed
Eliminates the regulatory risk of prescribing without a valid VCPR, which can result in state board disciplinary action including license suspension. Proactive expiration alerts drive scheduling of herd health visits that generate $200-500 per visit in revenue that would otherwise lapse when the vet forgets to schedule the annual farm call. Reduces after-hours decision stress by providing instant VCPR lookup instead of relying on memory at 10 PM.
