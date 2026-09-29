# Entitlement Rules as a Model Instead of a Spreadsheet

**Niche:** [[niches/it-managed-services/software-licensing-audit-defence/profile|Software Licensing & Audit Defence Practices]]
**Industry:** [[industries/it-managed-services|IT Managed Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Publisher licensing metrics are formal rules over a formal inventory, and the industry computes them by hand in workbooks.
**Tags:** #graph-ml #large-language-models #ocr #named-entity-recognition #compliance

## The Problem
An effective licence position is arithmetic over rules: given this deployment topology and these agreements, how many units of what metric are required. The rules are elaborate — processor and core factors, virtualization and partitioning policies, named user versus concurrent definitions, indirect and digital access, sub-capacity eligibility conditional on running a specific inventory agent — and they differ by publisher, by product, by contract vintage, and by amendment.

The work is done in spreadsheets. A consultant reads the agreements, extracts the entitlements and the applicable rule set, pulls a deployment inventory, and builds a model. It takes weeks, it is only as good as that consultant's grasp of the publisher's rules, and it is rebuilt from scratch for the next client with substantially the same estate.

The exposure is asymmetric and large. Getting a virtualization rule wrong on a database estate is an eight-figure difference, and the client finds out when the publisher's finding lands.

## Why Nobody Has Built This
The rules look unformalizable because they are written adversarially — publisher policy documents are deliberately imprecise in places, and the operative meaning comes from how the publisher has actually enforced them. Practitioners reasonably concluded that judgment cannot be codified.

Most of it can. A processor factor table is a lookup. A partitioning policy is a set of conditions over a topology. Named user counting is a rule over an identity inventory. The genuinely contested points are a small fraction of the surface, and they are exactly the points a system should route to a human — which is impossible while everything is in a workbook.

The other reason is the business model. Engagements are priced on consultant time, and a firm whose model does in an hour what took three weeks has to think about how it charges. That is a pricing question dressed up as a technical objection.

## What to Build
A rules engine over a formal representation of entitlements and deployments.

**Model entitlements as structured objects** extracted from agreements: product, metric, quantity, territory, term, and the rule set incorporated by the contract vintage. Agreement extraction is a document problem the current generation of language models handles well.

**Encode publisher metrics as executable rules**, versioned by publisher policy edition, so a position can be recomputed under the rules that applied when the contract was signed and under the ones the publisher is asserting now. Being able to show both is often the whole negotiation.

**Compute over the deployment graph.** Hosts, clusters, partitions, virtualization layers, users, and access paths — most licensing exposure is a topology question, and the exposure lives in the paths nobody drew.

**Route the contested points explicitly.** Where the rule is genuinely ambiguous or the publisher's enforcement position differs from the written policy, the system should surface it as a decision with the firm's precedent attached, not silently pick a side.

**Simulate remediation.** The client's question is always what to change to reduce exposure — reconfigure a cluster, restrict a partition, retire a product. That is scenario evaluation over the same model and it is currently manual.

## Target Customer
Practice leader or managing director at a licensing advisory practice. The commercial logic is capacity: qualified licensing consultants are scarce, audit demand is driven by publisher revenue pressure rather than by client demand, and the practice turns work away.

## Impact If Built
Audit findings are quantified in the millions and are frequently wrong in the publisher's favour because the client cannot model their own position fast enough to argue. A firm that can produce a defensible position in days rather than weeks changes the outcome of the negotiation, and can do it for mid-market clients who currently cannot afford the engagement at all.
