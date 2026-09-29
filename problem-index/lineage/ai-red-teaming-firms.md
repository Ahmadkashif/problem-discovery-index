# Lineage: AI Red Teaming Firms

**Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Wave:** [[series/eras/wave-12-transformers|12 — Transformers]]
**The tool:** MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems) — an ATT&CK-style matrix of tactics and techniques for attacking machine-learning systems, published as versioned YAML with case studies and mitigations; first released as the Adversarial ML Threat Matrix
**Builder:** MITRE
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Attacks on machine-learning models had a literature and no vocabulary a defender could use.

By 2020 the academic record held years of papers on evasion, data poisoning, model inversion and model theft. None of it was organised the way a security team works: by what an adversary is trying to achieve at each stage, and which concrete technique achieves it. A penetration tester could say "we tested initial access and lateral movement" and a client would know what that meant. Nobody could say the equivalent about a model.

Microsoft put a number on the gap. In the announcement of the matrix on **22 October 2020**, it reported surveying 28 businesses, of which "twenty-five out of the 28" said they did not have the right tools in place to secure their ML systems.

## What Got Built

A grid. The Adversarial ML Threat Matrix copied the layout of MITRE ATT&CK — columns of adversary *tactics* (reconnaissance, initial access, model access, exfiltration, impact), each filled with *techniques* — and attached real-world case studies of attacks on ML systems. Microsoft's post says the structure was chosen deliberately because security analysts already knew how to read ATT&CK.

The matrix's GitHub repository now announces its "newly branded" successor: ATLAS. The ATLAS data changelog records **v1.0.0 on 17 February 2021**, "initial data definition". Transformer-era attacks arrived later: **v4.5.0, dated 25 October 2023**, added LLM Prompt Injection (AML.T0051), LLM Jailbreak (AML.T0054), LLM Meta Prompt Extraction and LLM Data Leakage. The September 2026 release lists 16 tactics, 120 techniques, 88 sub-techniques, 40 mitigations and 73 case studies.

## Who Built It, And Why Them

MITRE, with Microsoft as co-originator of the first version. The October 2020 announcement was co-written by Ram Shankar Siva Kumar of Microsoft's AI Red Team and Ann Johnson, and says Microsoft collaborated with MITRE and 11 other organisations, among them IBM, NVIDIA and Bosch. The repository lists further contributors including Airbus, PwC, Carnegie Mellon and the University of Toronto.

The reason it was MITRE comes down to one asset. MITRE already owned ATT&CK, the matrix enterprise security teams used to describe attacks, plan tests and report them. An ML threat model in the same shape would slot into the tools, training and reporting habits those teams already had; one in a new shape would have to win adoption from scratch. Microsoft had the operational attacks and the survey; MITRE had the format that makes a taxonomy usable, and it has held the artefact since — the data repository is copyright MITRE from 2021. Keyed to MITRE as the standard's owner, in line with this sweep's precedent.

## What It Cost

ATLAS catalogues what can be done; it does not measure how much of it was tried. A red-team report can mark every cell as "tested" and still have covered a sliver of the prompt space behind each one, because a technique like prompt injection is a whole family of inputs, not a single check.

The ATT&CK inheritance brings a second cost. The grid invites heat-map reporting — coloured cells as evidence of thoroughness — which turns a list of known techniques into something that looks like a coverage metric without being one.

## What You Still Touch

AI red-team engagements, vendor questionnaires and probing tools commonly map findings to technique IDs like AML.T0051. The unit a client reads is the cell. How much of the risk behind each cell was actually examined is the part still missing.

- [[problems/ai-red-teaming-firms/high-impact|🔴 Coverage Is Unmeasurable]] — the gap a technique grid makes visible without closing
- [[problems/ai-red-teaming-firms/low-impact-1|🟡 Domain-Specific Harm Taxonomies]]
- [[niches/ai-red-teaming-firms/coverage-measurement/profile|Coverage Measurement]]
- [[niches/ai-red-teaming-firms/domain-harm-taxonomies/profile|Domain Harm Taxonomies]]
- [[niches/ai-red-teaming-firms/automated-probing-platforms/profile|Automated Probing Platforms]]

**Sources:** Microsoft Security Blog, "Cyberattacks against machine learning systems are more common than you think" (22 October 2020; Ram Shankar Siva Kumar and Ann Johnson); GitHub `mitre/advmlthreatmatrix` (contributor list, ATLAS rebrand notice); GitHub `mitre-atlas/atlas-data` README and CHANGELOG (v1.0.0 2021-02-17; v4.5.0 2023-10-25 LLM techniques; current counts; ©2021–2026 MITRE). The MITRE threat-intelligence note in this vault uses the same `MITRE` key. WebSearch was not used; research was by WebFetch on these known URLs. atlas.mitre.org returned only its header, so I could not read MITRE's own launch statement. ⚠️ **Not established:** which individuals at MITRE designed the matrix and how design work split between MITRE and Microsoft — the sources say "collaborated", no more. The claim that engagements "commonly" map findings to ATLAS IDs is my characterisation; I found no survey of it.
