# Source Reconciliation Adapted to Conflicting Unverifiable Claims

**Niche:** [[niches/commercial-real-estate/cre-property-data-research/profile|Commercial Property Data & Research Platforms]]
**Industry:** [[industries/commercial-real-estate|Commercial Real Estate]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data quality platforms resolve conflicts by picking the more trustworthy source; here the broker and the landlord give different rents, both are interested parties, and neither can be checked.
**Tags:** #bayesian-inference #probability-distributions #confidence-intervals #random-forests #evaluation-metrics #hypothesis-testing #graph-neural-networks #feature-engineering #data-integration #automation

## The Problem
Researchers assemble each fact from sources with reasons to shade it. A broker quotes an asking rent that flatters the building; a landlord confirms a face rent while omitting concessions that make the effective rent much lower; a tenant's representative reports the deal from their side. In most states nothing is publicly recorded that would settle it. The researcher reconciles by judgment — who usually tells the truth, what the submarket supports, what the same landlord said last time — and records a single value. That judgment is the company's core skill and it is neither documented nor consistent, and the recorded value carries no indication of how contested it was.

## What Already Exists
Data quality and master data platforms handle multi-source conflict resolution as a standard feature. Survivorship rules, source trust hierarchies, and stewardship workflows are mature in Informatica, Reltio, and the rest, and the modern data quality tools add anomaly detection and lineage. For picking a winner among conflicting values, the tooling is complete.

## The Customization Gap
Every one of those resolves conflict by ranking sources on reliability, which assumes a source is reliable or not. Here reliability is directional and situational: a broker is reliable on square footage and systematically optimistic on rent, a landlord is reliable on term and silent on concessions, and both shade in predictable directions that depend on market conditions. Nothing off the shelf can express a source that is trustworthy on one field and biased on another in a known direction. The adaptation is a source model with per-field, per-role bias estimated empirically from the cases where truth eventually emerged — a sale that reveals income, a public filing, a subsequent tenant confirmation — and reconciliation as inference under that bias model rather than as selection among candidates. The output is a value with a distribution rather than a point, which is what lets the record express that a rent is well established or barely evidenced. Corroboration structure matters too: three sources that all heard it from the same broker are one source, and a graph-aware model can tell the difference where a rules engine cannot.

## Target Customer
Heads of research methodology and data operations at property data platforms, and the senior researchers whose reconciliation judgment is the company's most valuable undocumented skill.

## Impact If Solved
Makes the company's core analytical act consistent and inspectable rather than personal, which is both a quality gain and a training accelerator for a workforce with meaningful turnover. Empirically estimated source bias also produces something directly saleable — an honest confidence attached to every contested field, which is what a subscriber underwriting a transaction most wants and nobody currently provides.
