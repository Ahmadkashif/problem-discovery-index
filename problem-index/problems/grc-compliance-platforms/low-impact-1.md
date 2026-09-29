# Mapping Between Frameworks That Overlap

**Industry:** [[grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** An organisation pursuing four frameworks implements largely the same controls four times, and reconciles them in a spreadsheet that goes stale at the next revision.
**Tags:** #bert #transformers #word-embeddings #contrastive-learning #large-language-models #evaluation-metrics #compliance #graph-neural-networks

## The Problem
Organisations end up pursuing several frameworks at once — a SOC 2 report for enterprise customers, ISO 27001 for international ones, a sector framework, a customer's bespoke requirements, and a privacy regime. The underlying controls overlap heavily; the wording, structure and evidence expectations do not.

Reconciliation is done with crosswalks: a spreadsheet mapping each framework's requirements to a common internal control set, maintained by a compliance team. It is laborious to build, subtly wrong in places, and goes stale when any framework is revised — which happens continuously across a portfolio of five.

The staleness is the expensive part. A revision changes wording, splits a requirement, or adds an expectation, and nobody notices until an auditor does. Then evidence that satisfied the previous version is challenged and the organisation is remediating under audit pressure.

And the mapping is a judgement that carries risk. Declaring that one framework's requirement is satisfied by evidence collected for another is a defensible position that an auditor may not accept, and the reasoning behind each mapping lives in the head of whoever made it.

## What Already Exists
Platforms ship pre-built crosswalks between major frameworks and maintain them as a product feature, which is a genuine and substantial part of their value. The Secure Controls Framework and similar community efforts publish open mappings. Standards bodies occasionally publish official mappings between their own frameworks. Enterprise GRC platforms support a common control model with framework overlays. Consultancies sell mapping as a service.

## The Customisation Gap
The shipped crosswalks are generic and every organisation's internal control set is its own. The mapping that matters is from this organisation's actual controls — as implemented, in their configuration, with their exceptions — to each framework's requirements, and that is the layer platforms leave to the customer.

Revision handling is the concrete gap. When a framework is revised, the useful artefact is a diff expressed in the organisation's terms: which of our controls are affected, which evidence is no longer sufficient, what specifically changed and what we need to do. Platforms notify that a revision occurred; nobody produces the consequence.

Mapping confidence is the third piece. Some mappings are unambiguous and some are arguable, and treating them identically means an organisation cannot see where its coverage rests on an interpretation an auditor might reject. Expressing confidence, with the reasoning attached, is what makes a mapping defensible in an audit rather than asserted.

And customer-specific requirements are the unserved case. Enterprise customers impose bespoke security requirements in contracts, which overlap the frameworks substantially and are mapped by nobody — so an organisation satisfies the same requirement several times for several customers without recognising it is the same requirement.

## Impact If Solved
Multi-framework compliance is the normal state and the overlap is reconciled by hand at every organisation independently. Mapping from the organisation's own implemented controls rather than from a generic set, producing revision diffs in the organisation's terms, and expressing mapping confidence would remove a recurring manual burden and — more importantly — surface where certified coverage rests on an interpretation nobody has examined.
