# Deployment Discovery Across Estates Nobody Documented

**Niche:** [[niches/it-managed-services/software-licensing-audit-defence/profile|Software Licensing & Audit Defence Practices]]
**Industry:** [[industries/it-managed-services|IT Managed Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Answering what is installed where is a solved problem for IT operations and an unsolved one for licensing, because licensing needs different facts.
**Tags:** #data-integration #graph-ml #anomaly-detection #ocr #automation

## The Problem
Before any licence position can be computed, the estate has to be inventoried: what is installed, on what hardware, in which virtualization topology, accessed by whom, in which environments. Clients rarely know. Estates accumulate through acquisitions, cloud migrations, and a decade of undocumented change, and the answer has to be assembled from whatever tools happen to exist.

That assembly is the slowest part of an engagement and the least defensible. An audit is an adversarial process, and a deployment figure a consultant cannot substantiate is one the publisher will substitute their own number for.

## What Already Exists
IT asset management and discovery is a mature category — ServiceNow, Flexera, Snow, Tanium, Lansweeper, and the cloud providers' own inventory services all discover installed software and hardware competently and at scale.

## The Customization Gap
Discovery tools answer the operations question. Licensing asks a different one.

**The unit is the licensable topology, not the machine.** Whether a database instance is licensable at cluster level or partition level depends on the virtualization technology, its configuration, and the publisher's sub-capacity policy — including whether a specific inventory agent was running, which is itself a condition of eligibility. Generic discovery reports installations; licensing needs the topology and the evidence about it.

**Editions and features drive the metric.** Two identical-looking installations can differ by an order of magnitude in cost because one has an enterprise feature enabled. Detecting feature usage rather than product presence is a different capability, and it is where the exposure is.

**Users and access paths count.** Named user and indirect access metrics require identity and access inventory, including systems that reach the licensed product through an intermediary application — the indirect access exposure that has produced the largest findings in this field, and the one no discovery tool models.

**Point-in-time evidence with a chain of custody.** An audit asks what was deployed during a period, and the answer must be evidenced and reproducible months later. Generic tooling maintains current state and overwrites history.

**Discovery under adversarial conditions.** Some engagements run with limited access, on estates where the client cannot deploy agents, using log extracts and partial data. Estimating a defensible position from incomplete evidence — and stating its uncertainty — is a licensing-specific requirement no operations tool has.

## Target Customer
Head of licensing practice or director of technical delivery, where discovery is the schedule risk on every engagement and the weakest point in every negotiation.

## Impact If Solved
Discovery is where audit defence engagements slip and where positions become indefensible. Producing a licensing-shaped inventory with evidence attached shortens the engagement and, more importantly, changes what the firm can assert when the publisher disputes it — which is the entire value of the work.
