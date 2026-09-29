# Buy: Continuous Auditing From Internal Audit

**Niche:** Audit Testing & Evidence
**Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Internal audit adopted continuous auditing and full-population analytics two decades ago, and external attestation still samples twenty-five.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #compliance #data-integration #automation
**Contested on:** Whether a control's operation is established from its full population or from twenty-five items because that is the convention.

## The Problem

Testing an entire population rather than a sample is not a new idea in audit. Internal audit moved substantially in this direction two decades ago and the tooling is mature.

Continuous auditing runs control tests automatically against full transaction populations on an ongoing basis. Data analytics in audit — extracting a complete population and testing every item against defined rules — is standard practice in internal audit functions and is taught as core method. Exception-based auditing focuses effort on the items that fail rather than on a sample of everything. And the tooling for it is commercially mature.

External attestation, performed by the same profession under a different standard for a different reader, largely still samples. Some of the large firms use analytics in their assurance work, and in the specialist SOC 2 market it is the exception rather than the method.

The reason is not capability. It is that internal audit's client wants the exceptions found, and external attestation's client does not.

## What Already Exists

Audit analytics: ACL, IDEA and the analytics modules in audit platforms, designed specifically for extracting and testing full populations.

Continuous auditing: methodology and tooling for ongoing automated control testing, well established in internal audit practice and documented by the professional bodies.

Internal audit practice: full-population testing as normal method, with professional guidance and training behind it.

Assurance analytics at the large firms: data analytics applied in financial statement audit, developed substantially and applied unevenly in attestation work.

Compliance platforms: the continuous control evidence described in [[industries/grc-compliance-platforms|GRC & Compliance Platforms]], which is the population source.

## The Customization Gap

**Internal audit's incentive is inverted.** Internal audit works for the organisation's board and is rewarded for finding problems. External attestation works for the company being audited and is rewarded for not finding them, which is the whole reason the methods diverged.

**The report format does not accommodate the result.** Internal audit reports findings and rates. An attestation report is an opinion, and there is nowhere in it to say that a control operated on ninety-six per cent of four thousand items.

**Data extraction is harder from outside.** Internal audit has standing access to the organisation's systems. An external auditor requests evidence, which is why the compliance platform integration matters so much.

**Sampling standards are defensible and permit less.** Attestation standards specify sampling adequacy and do not require more, so the profession's own rules have no pressure toward the better method.

**Continuous auditing assumes a continuous relationship.** Internal audit is ongoing; attestation is periodic, which changes what continuous means and suggests a different engagement model.

**The skills exist in the same firms.** Many audit firms have analytics capability in their financial assurance practice and do not apply it in attestation, which makes this a transfer inside an organisation rather than an acquisition.

## Target Customer

Specialist attestation firms, for whom audit analytics is a capability available off the shelf and a differentiator in a market competing on price.

The large accounting firms, who already have the analytics capability in their financial assurance practices and have not moved it across.

Standards bodies, who could revise guidance to encourage or require full-population testing where the data supports it — which is the change that would make the method the default.

## Impact If Solved

A method that internal audit adopted two decades ago is available, tooled and taught, and external attestation has not moved because its incentives point the other way.

Exception-based testing — examining everything and focusing effort on what fails — is more efficient than sampling once the extraction exists, which removes the cost argument that justified the original compromise.

And the analytics capability sits inside many of the same firms, applied to financial assurance and not to attestation, which makes this a transfer rather than a build.
