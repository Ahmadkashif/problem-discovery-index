# Linking Patients Across Sources Without Ever Identifying One

**Niche:** [[niches/pharmacy-independents/prescription-market-intelligence/profile|Prescription Market Intelligence Providers]]
**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The longitudinal patient view is the premium product, it depends on tokens matching across sources that tokenise differently, and the match rate is an assumption.
**Tags:** #graph-neural-networks #transformers #evaluation-metrics #data-integration #compliance

## The Problem
The high-value products are longitudinal: a patient's treatment pathway across pharmacies, prescribers, payers and time. Building them requires recognising that a dispensing record at one pharmacy and a claim from a different source belong to the same person — without ever holding an identity.

The mechanism is tokenisation. Identifiers are hashed at the source under a shared scheme, and matching happens on tokens. It works, and it works imperfectly. Sources tokenise on different field combinations, with different normalisation, different completeness, and different error rates. A patient who moves, marries, or is entered with a transposed date of birth breaks into two people. Two patients collapse into one.

The consequence is a quiet bias in every longitudinal analytic. A treatment pathway analysis that undercounts continuation because the patient switched pharmacies looks exactly like a real discontinuation. Persistence and adherence — the most commercially important longitudinal outcomes — are measured on a linkage whose failure mode is to fragment exactly the patients who move around the system most.

Match quality is largely managed as an engineering property. There is rarely a per-cohort statement of what the linkage rate was and which direction its errors run.

## What Already Exists
Privacy-preserving record linkage is a real research field with mature techniques: Bloom filter encodings, secure multiparty protocols, and probabilistic linkage under encryption. Commercial tokenisation providers serve this industry and the health data market generally. Modern entity resolution over graphs is well developed.

What is missing is the vertical layer. Generic PPRL assumes a linkage problem with a definable evaluation set. Here there is no gold standard by construction — you cannot verify a match without identity, which is the entire point of the design. Commercial tokenisation gives interoperable tokens and says nothing about how well they perform on a given cohort.

## The Customization Gap
**Evaluation must work without ground truth.** Linkage quality has to be estimated from structure — duplicate-record signatures, implausible longitudinal patterns, capture-recapture across overlapping sources, comparison against known population statistics. This is the core technical problem and no off-the-shelf product addresses it.

**The graph is the discriminator.** Beyond tokens, a patient is characterised by their prescriber, pharmacy, payer, therapy and timing. That relational structure resolves ambiguity that token matching alone cannot, and it is exactly what generic linkage products do not model.

**Errors must propagate into the analytic.** A persistence curve computed on a linkage with an estimated fifteen per cent fragmentation rate should carry that as uncertainty, not present as a point estimate. Nothing off the shelf connects linkage quality to downstream output.

**The regulatory posture is a design constraint.** The de-identification determination underpinning the whole business depends on demonstrable re-identification risk limits. Any change to linkage — including improvements that raise match rates — must be assessable against that determination. This is why generic entity resolution cannot simply be turned up.

**Source heterogeneity is permanent.** Suppliers will not standardise. The system must handle differing tokenisation schemes, completeness and quality, and account for the fact that a source's match behaviour is itself informative about who its patients are.

## Target Customer
VP of Data Science or Chief Privacy Officer at a prescription data provider — this sits on the boundary between the two, which is part of why it is unowned.

## Impact If Solved
Longitudinal analytics are the premium tier of this business and the basis of real-world evidence work that increasingly reaches regulators. Measured, per-cohort linkage quality with propagated uncertainty makes those products defensible in a setting where an unmeasured bias in patient linkage silently becomes a clinical claim.
