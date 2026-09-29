# The Requester

**Parent Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Category:** Underserved Audience
**Contested on:** Whether the person who bought ten thousand labels can tell what they actually got.

## Profile
**Market Size:** ~$210M — 7% of the US microtask and research-participant market
**Share of Parent Industry:** ~7%
**Digital Adoption:** Low — a results file and an agreement statistic
**Target Buyer:** Researchers, ML teams and market research buyers
**Automation Potential:** High — the interpretation is a modelling problem over data the requester receives

## What Makes This a Distinct Niche

A researcher or engineer receives ten thousand labels, an agreement statistic and no way to know whether the disagreements are noise, ambiguity or their own unclear instructions.

The requester is usually not a crowdsourcing specialist. They are a psychology researcher, an ML engineer, a linguist, a product team — running one or a few batches, with no background in annotation methodology, and no colleague who has done it before. They write the instructions, choose the pay, set the qualifications and interpret the results, and are given essentially no support at any step.

The niche is distinct because the requester's failures are the source of most of the harm on the other side. A requester who cannot tell ambiguity from carelessness will reject careful workers; one who cannot estimate task duration will underpay; one whose instructions are unclear will produce bad data and blame the crowd.

## Current Tools & Gaps

A posting interface, a results download, agreement statistics of varying sophistication, and documentation. Some platforms provide templates and guidance; the academic-focused ones provide more, including pay guidance and participant quality controls.

The gaps are interpretation and method. The results file is labels with no uncertainty and no indication of which items were contested. Agreement statistics are reported without the guidance to interpret them or the decomposition to act on them. And a requester with a poor batch has no diagnosis — was it the instructions, the item set, the pay level, the qualification, or the crowd.

## Problems
- [[niches/crowdsourcing-platforms/the-requester/build|🔨 Build: Interpretable Results and a Batch Diagnosis]]
- [[niches/crowdsourcing-platforms/the-requester/buy|🛒 Buy: Research Methodology Tooling Adapted to Non-Specialists]]
- [[niches/crowdsourcing-platforms/the-requester/fix|🔧 Fix: Ten Thousand Labels and a Single Kappa]]
