# Reference Intervals Set by Convention for a Species With Two Hundred Breeds

**Niche:** [[niches/veterinary-practices/veterinary-reference-laboratories/profile|Veterinary Diagnostic Reference Laboratories]]
**Industry:** [[industries/veterinary-practices|Veterinary Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** One normal range per analyte per species, applied to a greyhound and a chihuahua, established from small reference populations decades ago.
**Tags:** #bayesian-inference #gaussian-processes #evaluation-metrics #confidence-intervals #hypothesis-testing

## The Problem
Every result is interpreted against a reference interval — the range considered normal. That interval is the single most consequential piece of content the laboratory publishes, because it determines whether a veterinarian sees a flag and acts.

Intervals are conventionally established from a modest reference population of clinically healthy animals, per analyte, per species, sometimes per instrument. In dogs, that single range is applied across a species with more morphological and physiological variation than any other mammal. Sighthound haematology and chemistry differ markedly from the species norm and this is well known; many other breed differences are documented in the literature and reach no reference interval anywhere.

Age is handled crudely or not at all. Instrument and method differences between an in-practice analyser and a reference laboratory shift values in ways that partition-specific intervals are supposed to handle and often do not.

The result is systematic misclassification in both directions: healthy animals of atypical breeds flagged abnormal, and genuinely abnormal results in other breeds falling inside a range too wide to catch them. Practitioners know this and correct for it informally, which is exactly the kind of tacit adjustment this index keeps finding.

## What Already Exists
The statistical machinery is entirely standard and long established. Guidelines for reference interval determination are published and widely followed. Covariate-adjusted and continuous reference intervals — where the range varies smoothly with age and other factors — are a mature methodology in human laboratory medicine, and indirect methods for estimating intervals from routine laboratory data rather than from a recruited healthy cohort are well developed and increasingly accepted.

None of it has been applied at the scale this corpus permits. Indirect estimation exists precisely for situations where a large routine dataset is available and recruiting a healthy population is impractical, which describes this case exactly — and veterinary reference intervals remain overwhelmingly direct, small-sample and unpartitioned.

## The Customization Gap
**Breed is the partition that matters and there are hundreds of them.** A per-breed interval is impossible for rare breeds and unnecessary for most; the right structure is a hierarchical model that pools across breeds and shrinks toward the species mean where data is thin. That is a modelling decision specific to this domain's structure.

**Health status must be inferred, not assumed.** Routine data is mixed sick and healthy. Indirect methods separate the healthy distribution statistically, and doing that credibly at breed level, adjusting for the reason the sample was taken, is the core technical work.

**Age should be continuous.** A puppy, an adult and a geriatric are different physiological populations, and a three-bucket partition wastes the resolution the data supports.

**Instrument and method must be a modelled covariate.** The same analyte on a practice analyser and a reference platform is not the same measurement, and the laboratory knows which instrument produced every result.

**The output has to be deployable.** Intervals ship into laboratory information systems, practice software, and printed reports. A continuous, covariate-adjusted interval has to be expressible in that pipeline and explicable to a veterinarian, which is a product problem as much as a statistical one.

**Changing an interval changes clinical behaviour.** Any revision reclassifies results and must be validated, versioned and communicated — closer to a regulated content release than to a model update.

## Target Customer
Chief Scientific Officer or Director of Clinical Pathology at a veterinary diagnostics company.

## Impact If Solved
Reference intervals are the interpretive layer under every diagnostic result in companion animal medicine, and they are demonstrably wrong for a substantial part of the population they are applied to. Breed- and age-adjusted intervals estimated from the laboratory's own national data would improve the accuracy of routine diagnosis across the whole field, using methodology that already exists and a dataset only these companies hold.
