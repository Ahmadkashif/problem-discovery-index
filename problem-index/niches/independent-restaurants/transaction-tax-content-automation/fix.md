# Researchers Decide the Hard Cases and the System Stores a Flag

**Niche:** [[niches/independent-restaurants/transaction-tax-content-automation/profile|Transaction Tax Content & Determination]]
**Industry:** [[industries/independent-restaurants|Independent Restaurants]]
**Type:** Fix (Pain Point)
**One-liner:** A researcher reads three sources and a private letter ruling to decide one taxability question, and the corpus records the answer as a boolean.
**Tags:** #tacit-knowledge-ml #large-language-models #graph-ml #worker-facing #compliance

## The Problem
Most of the corpus is mechanical — this jurisdiction, this rate, this date. A meaningful minority is not. Whether a state's prepared-food rule reaches a particular configuration of product and service is often genuinely unsettled, resolved by reading statute, regulation, a department bulletin, sometimes a private letter ruling issued to somebody else, and occasionally by calling the department.

A researcher does that work and reaches a position. The corpus stores the position: taxable, or not, at this rate, in this jurisdiction, for this category. The authorities relied on, the alternative reading considered, how confident the researcher was, and the fact that the department's guidance is ambiguous — none of it is stored anywhere the next person can find.

So when the state issues clarifying guidance two years later, nobody can identify which entries depended on the reading that just changed. When a customer's auditor challenges a position, the researcher who set it may have left. And when the same ambiguity appears in the fourth state to adopt similar language, it is worked out again from scratch.

## Why It's Still Broken
The corpus is a determination engine. Its consumers are software calls that need an answer in milliseconds, so the schema holds answers, and everything that is not an answer was designed out.

Research is also organized by production. The content calendar is driven by rate change volume and jurisdiction coverage, both of which are counted, and reasoning capture is counted by nobody.

And there is a defensive instinct: a written record saying the firm considered two readings and chose one looks, to a cautious lawyer, like a document an auditor or a plaintiff would enjoy. That instinct leaves the company unable to answer its own questions internally, which is the more expensive position.

## What a Fix Looks Like
Make the determination an object with provenance, kept internal.

**Positions carry their basis.** The question, the authorities cited, the reasoning, the alternative reading, a confidence level, the researcher, and the date — attached to the corpus entries that depend on it. One position typically underpins many entries across categories and localities, and that relationship is the thing worth modelling.

**Monitored dependencies.** A position resting on an absence of guidance should flag itself when guidance appears; a position drawn by analogy to another state should surface when that state's law moves. The company already monitors those sources; nothing connects the monitoring to the positions affected.

**Reuse across jurisdictions.** States copy each other's statutory language constantly. A researcher facing a familiar ambiguity in a new state should see how the firm resolved it before, with the reasoning — the single largest efficiency available in the research function.

**An internal confidence map.** Knowing which parts of the corpus are settled and which are judgment calls is the map of where the company is exposed, and it does not exist in any form today.

**Audit outcomes fed back.** When a customer's position is challenged and upheld or overturned, that is direct evidence about a determination the company made. It currently reaches a support team and stops there.

## Who Feels the Pain
Researchers, re-deriving reasoning colleagues worked out. Content leadership, unable to say what a new bulletin affects. Customer support, defending positions with no recorded basis. And customers, who are collecting tax from consumers on the strength of a boolean.

## Impact If Fixed
The rules corpus is the company's entire moat, and the reasoning that produced its hardest entries is being discarded as it is created. Storing it makes the corpus maintainable when the law moves, defensible when it is challenged, and far cheaper to extend into the next jurisdiction that copies language someone here has already read closely.
