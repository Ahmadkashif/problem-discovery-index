# Documentation Drift From the Software It Describes

**Industry:** [[technical-content-agencies|Technical Content Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The code ships weekly and the prose does not, so examples stop compiling, parameters are renamed and screenshots show an interface that no longer exists.
**Tags:** #bert #transformers #large-language-models #change-point-detection #gradient-boosting #evaluation-metrics #automation #workflow-orchestration

## The Problem
Documentation describes a moving target. A method gains a parameter, a default changes, an endpoint is versioned, a configuration key is renamed, a UI is redesigned. Reference documentation generated from code tracks some of this automatically; the prose that explains how to actually use the thing — guides, tutorials, conceptual explanations, troubleshooting — does not.

The failure is corrosive out of proportion to its size. A reader who follows a tutorial and hits an error at step four because the example uses a renamed parameter does not conclude that one page is stale; they conclude the documentation cannot be trusted, and they stop using it. Trust in a documentation corpus is a single shared quantity and every stale page spends it.

Detection is by reader complaint. Someone files an issue, or posts in a forum, or opens a support ticket, and the page is fixed. Pages describing less-used features drift indefinitely because nobody reads them enough to complain, which means the documentation is least reliable exactly where a reader has the least ability to work around it.

## What Already Exists
Reference documentation generated from OpenAPI specifications, code annotations or protobuf stays current automatically and is the part of this problem that is solved. Executable documentation — testing code samples in CI — exists in mature projects and is the single most effective intervention where it is adopted. Link checkers catch broken references. Vale and similar tools enforce style but not accuracy. Some platforms surface page age and last-reviewed dates, which readers largely ignore.

## The Customisation Gap
The unsolved part is prose that references code without being generated from it. A tutorial mentioning a parameter name, a configuration key, an endpoint path or a version constraint has a semantic dependency on the codebase that no tooling tracks, and extracting those references and checking them against the current code is a tractable analysis nobody performs.

The second gap is change-triggered review routing. When a pull request renames a configuration key, the set of documentation pages referencing it is computable, and surfacing that at review time is the intervention that prevents drift rather than detecting it. This requires the documentation and the code to be analysed together, which docs-as-code makes possible and almost nobody does.

Screenshots and interface descriptions are the hardest case and the most visibly stale. Detecting that a UI has changed in a way that invalidates a screenshot is now approachable with vision models comparing a current capture against the documented one, and flagging it for review is far better than the current mechanism, which is a reader noticing.

And staleness risk should be ranked rather than uniform. A page's drift risk is a function of how fast the underlying component changes and how much traffic and task-criticality the page carries, and directing scarce review capacity by that ranking is what makes maintenance affordable for a small team.

## Impact If Solved
Drift is the most common reason readers stop trusting documentation, and trust is corpus-wide rather than page-specific. Semantic dependency extraction with change-triggered routing moves the fix to the moment of the code change, where it costs minutes; vision-based screenshot validation addresses the most visible category; and risk-ranked review lets a small team maintain a large corpus, which is the actual constraint in every documentation programme.
