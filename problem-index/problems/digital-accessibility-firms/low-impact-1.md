# Automated Scanning Coverage and False Positives

**Industry:** [[digital-accessibility-firms|Digital Accessibility Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Scanners reliably catch the subset of accessibility failures that are decidable from markup, and the remainder — most of the real barriers — requires a person to look.
**Tags:** #transformers #cnns #bert #large-language-models #gradient-boosting #evaluation-metrics #compliance #semantic-segmentation

## The Problem
Automated accessibility testing detects failures that can be determined from the document — a missing alternative text attribute, insufficient colour contrast, a form control without a programmatic label, an invalid ARIA relationship. It does this reliably and at scale, and it covers a minority of the criteria that actually matter.

The rest requires judgement. Whether alternative text is meaningful rather than merely present. Whether heading structure reflects the content's actual organisation. Whether a custom widget behaves the way its ARIA role promises. Whether error messages are understandable. Whether the reading order makes sense. A scanner cannot evaluate any of these and reports the ones it can, which produces a report that is precise about a subset and silent about the substance.

False positives are the other half. Scanners flag patterns that are technically suspect and contextually fine, and every finding must be triaged by someone. A large site produces thousands of findings of which a meaningful proportion require dismissal, and the triage cost is a recurring tax that makes teams stop running the scans.

## What Already Exists
Deque's axe is the de facto engine, embedded across many products and in browser tooling, with a deliberately conservative design that minimises false positives at the cost of coverage. Level Access, Siteimprove, Evinced, Pa11y and Lighthouse all provide scanning. Linters and CI integrations catch issues at commit time. Some vendors have begun applying vision and language models to judgement-requiring criteria such as alternative text quality and heading structure.

## The Customisation Gap
The judgement criteria are exactly the ones current multimodal models can attempt, and the attempt has to be made carefully. Whether an image's alternative text conveys what the image contributes in context is a question a model can assess given the image and the surrounding content; whether a heading structure reflects the content's organisation is assessable from the rendered page. These are not certainties and should not be reported as violations — they should be reported as candidates for human review, ranked, which is a completely different product from a pass-fail scanner.

The confidence handling is what determines whether this helps or harms. An automated judgement asserted as a violation creates a false remediation task; asserted as a pass creates a false assurance, which is worse and is precisely the criticism directed at overlay products. Anything in this space must report uncertainty and must not permit a conformance claim to rest on a model's opinion.

The second gap is per-site calibration. A design system's components produce the same findings repeatedly across thousands of pages, and dismissals of a known false positive on one instance should suppress it everywhere that component appears — which requires recognising the component rather than the page. That alone removes a large share of triage volume.

## Impact If Solved
Coverage of judgement-requiring criteria is where the real barriers live, and extending automated assistance into it — as ranked human-review candidates rather than as verdicts — meaningfully expands what can be checked continuously rather than in an annual audit. Component-level dismissal removes the triage tax that causes teams to abandon scanning. Both help only if the uncertainty is carried honestly, which is the line separating a useful tool from the automated-conformance claim this industry has already seen go badly.
