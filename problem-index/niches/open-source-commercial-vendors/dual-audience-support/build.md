# The Same Answer, Written Twice

**Niche:** [[niches/open-source-commercial-vendors/dual-audience-support/profile|Dual-Audience Support]]
**Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Support engineers at open-source companies answer the same question in a contracted ticket and in a public issue, and must maintain a distinction that is commercially necessary and feels indefensible to hold.
**Tags:** #bert #word-embeddings #k-means-clustering #large-language-models #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to let one answer serve both a paying customer and a public community without the support engineer holding the boundary personally — and whoever does that takes the support organisation, because that boundary is the job's defining discomfort.

## The Problem
A support engineer resolves a contracted ticket about a configuration interaction, writing a detailed explanation. The same afternoon an almost identical question appears in the public issue tracker from somebody who is not a customer. They know the answer; it is on their screen. Posting it publicly serves the community and blurs a boundary their commercial organisation depends on; not posting it feels wrong, since the answer costs nothing to copy. They post a short version and feel bad about both halves. Neither knowledge base has the full answer, and the same investigation will be conducted again in three months in whichever corpus it did not land in.

## Why Nobody Has Built This
The two support channels were built as separate systems for separate audiences, and nothing was designed to span them. The boundary was articulated commercially — paid support gets response commitments — and not operationally, so what is actually withheld is left to individual judgement, which is why it feels indefensible: nobody has said what it is. The knowledge divergence is a consequence nobody owns. And the support engineer's discomfort is a cultural observation rather than a metric.

## What to Build
Separate what is genuinely entitlement from what is merely knowledge. Articulate the boundary explicitly as response commitment, escalation, dedicated attention, private context and advisory time — rather than as access to answers, which is the framing that makes the current position defensible and is almost never stated. Then make the knowledge flow both ways: a resolution written in a contracted ticket becomes a public article by default unless it contains customer-specific context, and a detailed public resolution enters the support knowledge base automatically. Match incoming questions across both corpora, so an engineer answering either sees whether it has been answered in the other, which eliminates the duplicated investigation. Deflect the repeated community questions with the answering layer the maintainer niche describes, since a large share of the public volume is questions that have been answered and the community has no support organisation to route them. Measure the duplication, since the proportion of questions answered twice is a number nobody has and is the case for the whole change. And read the community corpus commercially, because it contains product signal, adoption evidence and the questions that precede purchase, and the support organisation is currently the only part of the company that sees it.

## Target Customer
Support leadership at open-source companies, the engineers holding the boundary, and the community whose answers currently depend on somebody's personal willingness.

## Impact If Built
The boundary is commercially necessary and is currently defined by what is withheld rather than by what is provided, which is why it feels indefensible to the people holding it. Bidirectional knowledge flow removes the duplicated investigation, and articulating entitlement as service rather than as access resolves the discomfort honestly.
