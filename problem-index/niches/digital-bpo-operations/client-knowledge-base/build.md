# Build: Contact-Derived Knowledge Gap Detection

**Niche:** [[niches/digital-bpo-operations/client-knowledge-base/profile|Client Knowledge Base Quality]]
**Industry:** [[industries/digital-bpo-operations|Digital BPO Operations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Derive what the knowledge base is missing and getting wrong from the contacts themselves, ranked by volume and by the contact time it costs.
**Tags:** #large-language-models #word-embeddings #k-means-clustering #evaluation-metrics #confidence-intervals #transformers #automation #data-integration
**Contested on:** Whether knowledge gaps can be identified from the contacts they cause rather than from content review.

## The Problem

Knowledge base maintenance is driven by product releases and by whoever remembers. The evidence that would direct it — which questions customers actually ask, which of those the content answers well, which it answers wrongly, and which it does not answer at all — is generated continuously in the contacts and never reaches the content owner.

The result is a knowledge base that is comprehensive about what the product team thought to document and thin on what customers actually ask about. Agents work around it, learn the answers informally, and the article stays as it is for years.

With assist retrieving from that content and presenting it confidently, the cost of each defect has multiplied.

## Why Nobody Has Built This

The content sits with the client and the contacts sit with the BPO, and nobody owns the join. The BPO's quality function is measured on agent performance; the client's knowledge team is measured on publication volume and review cadence.

The analysis also requires reading contacts at scale and clustering them by question, which until recently was expensive enough that nobody attempted it beyond crude category tagging.

And the finding is a criticism of the client's own team, which makes an account manager cautious about presenting it — though framed as an operational improvement with a ranked list attached, it is welcomed far more often than feared.

## What to Build

A gap and defect detection pipeline over the contact corpus.

**Cluster the questions, not the contacts.** Extract the customer's actual question from each contact and cluster semantically. Existing contact categorisation is built around routing and billing codes and is far too coarse; a clean question taxonomy derived from the contacts themselves is the foundation and is immediately useful on its own.

**Match each cluster to the knowledge base.** Does an article address this question, does it address it correctly, and is it findable by the words customers and agents actually use. Three separate failures with three different fixes — missing, wrong, and unfindable — and conflating them is why content projects underdeliver.

**Rank by cost, not by volume.** A gap's cost is its contact volume times the extra handle time it causes times the repeat contact rate it produces. That ranking is far more useful than volume alone and it is computable from data the operation holds. It also converts the finding into a business case the client's content owner can take to their own leadership.

**Detect staleness against reality.** Articles whose content contradicts what agents actually say in successful contacts, or which are frequently corrected in the assist loop, or which predate a product change. The first is the interesting one: where agents consistently deviate from the documented answer and the contact resolves, the article is wrong and the agents are right.

**Draft the fix.** For a detected gap, a draft article generated from the contacts where agents resolved the issue successfully, for the client's content team to review. This is what turns a report into something a small, overstretched team can act on, and it is the difference between a finding and an improvement.

**Report to the client as a product.** A monthly knowledge quality report with ranked gaps, defects, estimated cost and drafted fixes. This is genuinely valuable to a client with no other view of their content's accuracy, and it reframes the BPO from a vendor being measured to a partner supplying evidence.

## Target Customer

BPO account and operations leadership, for whom this is both a quality improvement and an unusually strong client-relationship asset. Also clients' support content owners directly, who want exactly this and have no way to generate it.

## Impact If Built

Knowledge base maintenance gets directed by what customers actually ask rather than by what shipped. Gaps get ranked by what they cost. Drafts arrive with the findings, which is what makes a two-person content team able to act. And the ceiling on the BPO's quality — set by someone else's content — starts rising.
