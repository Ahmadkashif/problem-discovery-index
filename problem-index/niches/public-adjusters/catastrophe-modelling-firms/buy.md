# Every Client's Exposure File Is Wrong in a Different Way

**Niche:** [[niches/public-adjusters/catastrophe-modelling-firms/profile|Catastrophe Modelling Firms]]
**Industry:** [[industries/public-adjusters|Public Adjusters]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The most sophisticated hazard science in insurance is run on address files with missing construction types, wrong geocodes and unknown building heights, cleaned by hand every time.
**Tags:** #gradient-boosting #transformers #graph-neural-networks #evaluation-metrics #data-integration

## The Problem
A catastrophe model consumes an exposure file: every insured location with its coordinates, construction type, occupancy, year built, number of storeys, square footage, roof type and insured values. Model output is only as good as this input, and the input is close to universally poor.

Carriers' exposure data comes from underwriting systems populated over decades by agents typing into forms. Construction type is unknown for large fractions of a portfolio. Year built is missing or wrong. Geocoding resolves to a street centroid or a postal centroid rather than a structure — which in a hurricane storm surge model can mean a wrong side of a coastline. Commercial schedules describe a "location" that is actually eleven buildings.

Unknown attributes are filled with defaults derived from regional distributions. Those defaults are frequently the single largest source of uncertainty in a client's result, and they are invisible in the output.

Every engagement therefore begins with exposure data quality work: profiling the file, geocoding, inferring missing attributes, flagging implausible values. It is done by analysts, with rules and reference tables, and it is redone for every client and every renewal.

## What Already Exists
Property attribute data is a mature commercial market — assessor records, permit data, aerial imagery derived attributes, and national property databases with construction, roof and structural characteristics. Address geocoding to structure level is available commercially. Data quality tooling for profiling and standardisation is abundant.

None of it is assembled into what this workflow needs. Commercial property databases are built for real estate, lending and marketing, so their attribute taxonomies do not match insurance construction classification schemes, which are the schemes the vulnerability functions are defined on. Generic data quality tools flag missing values; they do not infer a construction class in a way that carries uncertainty into a loss model.

## The Customization Gap
**Inference must target the model's own taxonomy.** Vulnerability functions are indexed by specific construction and occupancy classes. Predicting "masonry" is useless; predicting the exact class the model expects, with a probability across classes, is what the pipeline needs — and only the modelling firm knows how sensitive its own functions are to each distinction.

**Uncertainty must flow into the loss distribution.** An inferred construction type carries uncertainty, and that uncertainty belongs inside the simulation rather than being resolved to a point estimate before it starts. This is the single most valuable difference from any off-the-shelf enrichment product, and it is only implementable by whoever owns the model.

**Geocoding must be structure-level and hazard-aware.** The precision required depends on the peril: a storm surge or wildfire model needs the building, while a hurricane wind model tolerates more. A hazard-aware geocoding tier is a domain-specific requirement no general geocoder expresses.

**Schedules are hierarchical.** Commercial policies describe locations containing buildings containing coverages, with values allocated inconsistently. Parsing that structure correctly is domain work, and getting it wrong misstates concentration, which is the thing catastrophe modelling exists to measure.

**Errors must be surfaced with their loss impact.** A data quality report listing ten thousand issues is unusable. Ranked by effect on modelled loss, it becomes the deliverable — and ranking requires running the model, which only this firm can do.

**Reproducibility is mandatory.** Enrichment changes results, and results go into rate filings and rating agency submissions. Every inference must be versioned, dated and reproducible, which rules out an opaque third-party enrichment service.

## Target Customer
VP of Data Products or Head of Exposure Data at a catastrophe modelling firm.

## Impact If Solved
Exposure data quality is widely acknowledged as a larger driver of result error than the hazard science, and it is addressed with per-client manual cleanup. Automated attribute inference with uncertainty propagated into the loss distribution improves every client's answer, removes the largest recurring labour cost in delivery, and turns a chronic complaint into a product.
