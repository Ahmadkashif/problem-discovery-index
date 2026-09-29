# Buy: Documentation Practice From Engineering

**Niche:** Policy & Document Management
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Engineering learned to keep documentation close to the thing it describes, version it together and test it, and policy management kept the document library model that engineering abandoned.
**Tags:** #bert #large-language-models #word-embeddings #evaluation-metrics #workflow-orchestration #automation #data-integration
**Contested on:** Whether the policy set describes how the organisation actually operates, or is a document library maintained because an auditor will ask for it.

## The Problem

Engineering spent twenty years discovering that documentation separated from the system it describes goes stale immediately and invisibly. The response was a set of practices now standard: keep documentation in the repository next to the code, version it with the thing it documents, review changes to both together, generate what can be generated from the source of truth, and test the examples so that documentation which no longer works fails a build.

Policy management uses the model engineering discarded. Documents live in a separate library, versioned on their own schedule, reviewed annually by date rather than by change, written by hand from templates, and never tested against anything.

The consequences are the ones engineering learned to expect: documents that describe a previous state of the world, confidently, with no indication that they have drifted.

## What Already Exists

Engineering documentation practice: docs-as-code with documentation in version control, review through the same pull request process as the code, static site generation, and documentation tests that fail when the described behaviour changes.

Policy as code: Open Policy Agent, Rego, Conftest and the policy engines that express rules as executable code enforced in pipelines — which is policy that cannot drift from practice because it is the practice.

Infrastructure as code: Terraform and its peers, where the declared configuration is the system, and documentation generated from it is accurate by construction.

Compliance as code: the emerging practice of expressing controls as executable checks, with OSCAL providing a machine-readable representation of control implementation.

Policy management: the document library modules in every GRC platform, plus the HR and legal document systems they resemble.

## The Customization Gap

**Policies must remain human-readable and legally meaningful.** Engineering documentation can be terse and technical. A policy is a governance artefact read by auditors, regulators and staff, and may have legal weight. It cannot simply become code, which is why the direct transfer fails and why the useful adaptation is binding rather than replacement.

**A two-layer model is what is actually needed.** The executable expression of a rule, enforced in the pipeline, and the human-readable policy statement that describes it — versioned together, reviewed together, and generated from a common source where possible. Policy as code and policy documents exist in different worlds and are maintained by different people with no connection.

**Review should be change-triggered.** Engineering reviews documentation when the code changes. Policy review is annual by date, which guarantees that a policy is wrong for up to a year after practice changes and that the annual review is mostly a formality.

**Generation from source of truth is possible and unattempted.** Where a control is implemented as configuration, the policy statement describing it could be generated and would then be accurate by construction — the same insight that made infrastructure documentation reliable.

**Testing has a direct analogue nobody uses.** A documentation test fails when the described behaviour changes. A policy assertion checked against control state is exactly that, and would fail in the same useful way.

**Ownership differs.** Engineering documentation is owned by the people who own the system. Policies are owned by compliance and describe systems they do not run, which is the structural reason the two drift.

## Target Customer

The compliance platforms, who should adopt the two-layer model — executable rules bound to human-readable statements — rather than continuing to run a document library beside a control monitor.

Policy-as-code vendors are the interesting adapters from the other direction: they have the executable half and no governance-artefact layer, and a product spanning both would serve a buyer neither currently reaches.

Compliance and engineering leadership jointly, since the fix requires the two functions to share ownership of the same artefacts, which is the organisational change underneath the technical one.

## Impact If Solved

The lesson engineering paid for over two decades — documentation separated from its subject goes stale silently — reaches a domain where the stale document is a governance commitment rather than a wrong code example.

Change-triggered review instead of annual review would keep policies accurate continuously, and it is a scheduling change rather than a technological one.

And generating policy text from actual configuration, where possible, produces documents that are accurate by construction, which is a far stronger position than any amount of review discipline can achieve.
