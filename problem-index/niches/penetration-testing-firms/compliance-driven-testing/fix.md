# Fix: Nobody Will Say What the Requirement Requires

**Niche:** Compliance-Driven Testing
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Frameworks require penetration testing and none of them define it, so the requirement is satisfied by whatever an individual auditor happens to accept.
**Tags:** #evaluation-metrics #compliance #confidence-intervals #hypothesis-testing #revenue-impact #workflow-orchestration
**Contested on:** Whether the engagement is scoped to find problems or to produce the artefact an auditor will accept, and whether anyone is willing to say which.

## The Problem

A framework says the organisation should perform penetration testing. It does not say by whom, at what depth, over what scope, with what methodology, or what evidence demonstrates it happened adequately. The auditor applies their own judgement, which varies between firms, between individual auditors, and between years.

This ambiguity is the root of most of the pathology in this niche. A buyer cannot tell what they need to purchase, so they purchase the cheapest thing that has the right name. A testing firm cannot tell what to offer, so it offers whatever its competitors are getting away with. An auditor cannot point to a criterion, so they accept a document that looks professional. And a customer reading a security questionnaire answer has no idea whether the annual test behind it was two weeks of expert work or an automated scan.

The whole chain runs on an unstated standard that everyone approximates and nobody writes down. The result is a market where the artefact is the product and depth is invisible, which is precisely the condition under which quality cannot be rewarded.

## Why It's Still Broken

**Framework authors deliberately avoid prescription.** Writing "penetration testing" rather than specifying depth keeps the framework applicable across organisations of wildly different sizes and risk profiles, and avoids the maintenance burden of a technical specification. The vagueness is a design choice with real justification.

**Specification would exclude.** A defined minimum depth would price some small organisations out of certification, which framework bodies are reluctant to do and which would attract genuine criticism.

**Auditors are not equipped to judge.** Assessing whether a penetration test was adequate requires technical expertise most audit teams do not have. They check that a report exists, is recent, is from a credible-looking firm and shows findings being addressed — which is what they can reasonably assess.

**Everyone in the chain benefits from the ambiguity except the organisation.** The buyer gets a cheaper artefact, the thin-service firm gets a sale, the auditor avoids a technical judgement. The only loser is the organisation's actual security, which is nobody's line item.

**No body owns the definition.** Framework authors defer to practitioners, practitioners defer to auditors, auditors defer to the framework. It is a circle with no one in it willing to write the number down.

## What a Fix Looks Like

**Publish what auditors actually accept.** Not a new standard — an empirical description, gathered across many audits, of what has satisfied which auditors for which frameworks. The compliance automation platforms see thousands of audits and could produce this immediately. It would give buyers a realistic picture and would expose the variance, which is itself the argument for fixing it.

**Adopt a service-level vocabulary.** Defined, named tiers of testing depth — automated with validation, scoped manual assessment, comprehensive assessment — that firms can sell against and buyers can specify. This does not require any framework to change; it requires the profession to agree on words, and it lets a buyer state what they want and an auditor state what they expect.

**Require a coverage statement as the evidence.** The auditor's criterion becomes not "a report exists" but "the report states its scope, its coverage and its depth". This is assessable without technical expertise, and it makes the thin engagement visible without requiring anyone to judge its adequacy — which is exactly the property an audit criterion needs.

**Separate the artefact from the assurance in questionnaires.** Customer security questionnaires should ask what depth of testing was performed and over what scope, not whether a test occurred. A yes-or-no question invites the cheapest yes.

**Accreditation bodies should publish guidance.** CREST and its peers are the natural authors of a depth vocabulary and a recommended evidence standard, and this is the kind of collective-action fix no individual firm can achieve.

**Firms should state their tier unprompted.** A firm that labels its own service level honestly, before anyone requires it, is making a bet that buyers will eventually care — and is the only kind of actor who can start this without waiting for anyone.

## Who Feels the Pain

The organisation, which believes a requirement has been met meaningfully and has bought a document, and finds out otherwise only if something happens.

The security team, whose single annual testing budget is spent on an artefact procured by a compliance function to satisfy an auditor.

The firms doing deep work, competing against a thin deliverable in a process where the difference is invisible, watching the price of expertise fall every year.

And the customers and insurers relying on questionnaire answers that treat a two-week expert assessment and an automated scan as the same yes.

## Impact If Fixed

Publishing what auditors actually accept is achievable now by parties who already have the data, and would replace an industry-wide guess with a description.

A depth vocabulary is the change with the largest structural effect: it lets buyers specify, auditors expect and firms compete on something other than price, and it requires no framework revision.

And making a coverage statement the evidence criterion would turn an unassessable requirement into an assessable one, which is the fix that makes every other improvement in this industry commercially viable.
