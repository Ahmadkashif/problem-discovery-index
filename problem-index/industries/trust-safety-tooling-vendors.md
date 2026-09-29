# Trust & Safety Tooling Vendors

## Profile
**Category:** Trust, Safety & Security
**Market Size:** ~$3B US in trust and safety technology — content classification, fraud and abuse detection, child safety tooling, and the case management systems that sit around them — from Hive, ActiveFence, Cinder, Checkstep, Unitary, Thorn, Sift and a growing specialist field
**Tech Maturity:** Capable classifiers sold on numbers nobody can verify. These vendors supply the automated layer that decides what reaches a human reviewer and what is actioned outright, across text, image, video and audio, in many languages. Every vendor reports accuracy on its own test set, there is no shared benchmark, and a buyer comparing two products is comparing two self-administered exams.
**Workforce:** Machine learning engineers and researchers, policy specialists translating customer rules into classifier configuration, data annotators producing labelled training data, solutions engineers, customer-facing trust and safety advisors

## Key Pain Themes
Performance claims are unfalsifiable in practice. Vendors publish accuracy figures computed on internal test sets whose composition is not disclosed, and the failures that matter — lower-resource languages, specific communities, reclaimed speech, context-dependent meaning, novel harm types — are precisely the ones an aggregate figure conceals. Regulatory regimes now require platforms to report on their moderation accuracy, and the platforms depend on vendors whose accuracy is asserted rather than measured.

The second theme is that the operating point is where the harm is decided and it is set as a configuration. A threshold determines the balance between missing harmful content and removing legitimate speech, those costs are not commensurable, and they differ per category and per customer — and the product usually ships a single confidence score and leaves the choice to a customer with no framework for making it.

The third is that novel harms arrive faster than labelled data. New abuse patterns, coordinated campaigns and emergent slang appear and classifiers trained on historical labels miss them for weeks — which is the period in which a new harm does most of its damage.

## Current Tech Landscape
Hive and ActiveFence provide broad classification across modalities; Unitary and Checkstep focus on specific media and workflow; Cinder and similar provide the case management layer; Thorn and the hash-matching infrastructure around NCMEC handle known child sexual abuse material with a long-established and effective mechanism. Sift, Sardine and the fraud vendors cover account and transaction abuse. Large platforms build in-house and buy selectively. Multilingual models have improved and their per-language performance remains unevenly disclosed. Regulatory reporting regimes have begun to require accuracy statistics that the underlying tooling is not instrumented to produce honestly.

## Problems
- [[problems/trust-safety-tooling-vendors/high-impact|🔴 High Impact: Every Vendor Reports Accuracy on Its Own Exam]]
- [[problems/trust-safety-tooling-vendors/low-impact-1|🟡 Low Impact: The Threshold Is Where the Policy Actually Lives]]
- [[problems/trust-safety-tooling-vendors/low-impact-2|🟡 Low Impact: Harms That Arrive Before the Labels]]
- [[problems/trust-safety-tooling-vendors/worker-life-1|🟢 Worker Life: The Annotator Labelling the Training Data]]
- [[problems/trust-safety-tooling-vendors/worker-life-2|🟢 Worker Life: The Lone Trust and Safety Engineer]]
- [[problems/trust-safety-tooling-vendors/ml-opportunity|🧠 ML Opportunities]]
- [[problems/trust-safety-tooling-vendors/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
This category supplies the automated layer that determines what billions of people see and what happens to their accounts, and it competes on self-reported accuracy figures that cannot be compared. The absence of a shared benchmark is the field's defining gap — it prevents buyers from choosing on quality, prevents regulators from verifying platform claims, and allows the per-language and per-community failures that cause most documented moderation harm to remain invisible in an aggregate number. Building one is a coordination problem rather than a technical one, and it is the single change that would most improve outcomes across every platform these tools are deployed on.
