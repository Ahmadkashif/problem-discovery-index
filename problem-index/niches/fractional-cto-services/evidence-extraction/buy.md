# Buy: Repository Mining for the Outsider

**Niche:** Evidence Extraction
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Behavioural code analysis products compute exactly the right signals and assume a team analysing its own estate over time, which is the opposite of an advisor with one export and ten days.
**Tags:** #graph-neural-networks #gradient-boosting #k-means-clustering #evaluation-metrics #data-integration #automation #workflow-orchestration
**Contested on:** Whether a stranger can derive a truthful picture of a system from the artefacts the organisation already produces, fast enough to matter inside an eight-week engagement.

## The Problem

The derivation techniques an advisory instrument needs are not hypothetical — they are shipping. Hotspot analysis from change frequency and complexity, temporal coupling from co-change, knowledge maps from authorship, defect localisation from fix commits: all of it exists in commercial products with real customers and published validation.

The advisor cannot use any of it. The products are sold as team subscriptions, installed against an organisation's own accounts, priced per contributor per month, and designed for a team watching its own trends. An advisor wants to point the same analysis at a different company every eight weeks, from an export, under a practice account, with the results leaving when the engagement does.

So the technique that would most improve technical assessment sits one packaging decision away from the profession that needs it most, and the profession reads code instead.

## What Already Exists

CodeScene is the reference implementation of behavioural code analysis and the closest existing product to an assessment instrument — hotspots, temporal coupling, knowledge distribution, and a body of validation research behind the techniques. Code Climate, SonarQube and Codacy cover structural quality. LinearB, Swarmia, Jellyfish and DX cover flow and investment allocation. GitHub, GitLab and Atlassian expose parts of all of it natively.

On the open side, the repository-mining ecosystem is rich: PyDriller and similar libraries make commit history tractable, `git-of-theseus` and `code-maat` implement pieces of the behavioural analysis directly, and two decades of empirical software engineering research documents which signals predict what, with effect sizes.

## The Customization Gap

**Packaging, first and largest.** Per-contributor monthly pricing against an org integration is incompatible with a per-engagement, per-estate, disposable use. An advisory edition is a pricing and tenancy change over an existing engine — many client estates under one practice account, each isolated and each deletable — and it is the change that unlocks everything else.

**Cold start versus accumulated baseline.** The products are strongest when they have watched an estate for a year. The advisory case is a single retrospective read of history already recorded, which the engines can technically do and do not present, because trend dashboards are the product.

**Dirty history.** This is the real technical gap, and it is where a commercial product would earn its price over the open-source pieces. Mass reformats, monorepo migrations, vendored directories, tracker abandonment and tooling changes silently corrupt change-frequency analysis, and no product detects them and adjusts. On a team's own estate someone notices the nonsense result; on an unfamiliar estate nobody does, which is exactly when it matters.

**Tracker semantics.** Cycle time requires knowing what each team's workflow states mean. Products solve this with configuration, which assumes an administrator with knowledge of the estate. An advisor has neither, so the states must be inferred from transition topology.

**Confidence and provenance.** Team-facing products present numbers as fact because the team can sanity-check them. An advisor citing a number to an investment committee needs the evidence, the window and the caveat attached, and needs the product to decline to answer when the data cannot support it.

**Exhibit output.** The deliverable is a report section, not a dashboard. Findings need to export as artefacts with their evidence — a format nothing in the category produces.

## Target Customer

CodeScene is the obvious candidate: the technique is already right, the engine already exists, and an advisory edition opens a channel that places the product inside a new company every eight weeks with a practitioner presenting its output as their own analysis. The engineering-analytics vendors are the second tier, further from the technique but better capitalised.

Buyers are advisory boutiques, independent fractional CTOs and diligence practitioners, who price by engagement and compare the cost against a week of senior time rather than against a SaaS seat.

## Impact If Solved

Twenty years of validated repository-mining research reaches the profession that would act on it. An advisor gets coupling structure, effort concentration and knowledge risk from an afternoon's exports, and spends the recovered week on judgement.

For the vendor, the advisory channel is the best demonstration mechanism the category has: every engagement shows a company its own engineering data at the exact moment it is receptive to a conclusion about that data, with a trusted third party narrating.

And the history-repair work, once built for the advisory edition, silently improves the core product for every existing customer whose estate has a migration in it — which is most of them.
