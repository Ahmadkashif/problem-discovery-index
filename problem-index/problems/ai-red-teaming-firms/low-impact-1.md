# Domain-Specific Harm Taxonomies

**Industry:** [[ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic harm categories are well established and widely published, and what actually goes wrong in a clinical triage assistant or a lending decision system is not on any of those lists.
**Tags:** #large-language-models #bert #word-embeddings #k-means-clustering #evaluation-metrics #transfer-learning #compliance

## The Problem
Standard harm taxonomies cover the categories everyone knows: violence, illegal activity, hate speech, self-harm, privacy violation, misinformation. They are published, broadly agreed, and reasonable.

They do not describe what goes wrong in a deployed system in a specific domain. A clinical triage assistant's serious failures are under-triaging a presentation that needs urgent care, producing confident guidance outside its validated scope, and being manipulated by a patient description into a wrong disposition. A lending assistant's failures involve proxy discrimination, inconsistent treatment of comparable applicants, and explanations that do not match the actual decision basis. An enterprise assistant's failures involve leaking information across permission boundaries.

None of that appears in a generic taxonomy, and all of it is what the client actually needs tested.

So every domain engagement begins with a domain expert and a red team researcher building a taxonomy from scratch — enumerating what would count as a serious failure here, how severe each is, and how to probe for it. It takes weeks and it is rebuilt for the next client in the same sector.

## What Already Exists
Published taxonomies from NIST, MLCommons, and various research groups cover generic harms with reasonable rigour. The EU AI Act and sector regulators define risk categories that shape what must be assessed. Clinical safety frameworks, financial fairness standards and sector incident taxonomies exist independently and are mature. Bug bounty severity scales exist for traditional security. Some firms publish domain-specific guidance.

## The Customisation Gap
The domain knowledge exists in the sector, not in the AI safety literature, and nothing bridges them. Clinical risk management has decades of structured thinking about failure modes; financial regulators have detailed fairness expectations; neither has been mapped onto what an AI system can get wrong.

Nothing accumulates across engagements. The fifth healthcare client's taxonomy is built from nothing despite the firm having built four before, because taxonomies are delivered as client artefacts rather than retained as a growing asset.

Severity calibration is inconsistent and consequential. The same finding is rated critical by one team and moderate by another, which makes reports incomparable and undermines the client's ability to prioritise. Severity should be anchored on realised consequence — what actually happens if this failure occurs in this deployment — and is usually anchored on researcher intuition.

Incident data from the sector is the unexploited input. Published clinical incidents, regulatory enforcement actions and litigation describe what has actually gone wrong in the domain, and mining that for AI-relevant failure modes is a well-shaped task nobody performs.

## Impact If Solved
Domain taxonomy construction sits on the critical path of every sector engagement and determines whether the testing examines what matters. Building it from sector incident data and accumulating across clients converts weeks of expert authoring into review, and severity anchoring on real consequence makes findings comparable and actionable.
