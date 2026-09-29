# Fix: The Cluster Is Not the Group

**Niche:** Attribution & Expert Testimony
**Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Establishing that this activity forms a coherent cluster and establishing that the cluster is a named actor are two claims of very different strength, presented as one.
**Tags:** #evaluation-metrics #confidence-intervals #graph-theory #hypothesis-testing #compliance #worker-facing
**Contested on:** Whether an attribution claim carries a confidence anyone has calibrated.

## The Problem

Attribution involves two steps and the second is much weaker than the first.

The first is clustering: this intrusion shares infrastructure, tooling and tradecraft with a set of other intrusions, and they are plausibly the same operator. Evidence for this can be strong, and it is technical work the responder has done directly.

The second is naming: this cluster corresponds to the group publicly known as X. That rests on matching the observed characteristics against a threat intelligence vendor's published description of a group — a description assembled by a third party, from their own clustering decisions, with their own boundary judgements, using a name that may map inconsistently onto other vendors' names for overlapping activity.

The report says: the intrusion is attributed with high confidence to X. One sentence, containing both claims, with the confidence of the first attached to the combination.

The consequences follow the name rather than the cluster. Insurance exclusions reference state actors. Sanctions lists reference named entities. Public statements name groups. So the weaker claim is the one doing the consequential work, and it is presented as though it carried the strength of the stronger one.

## Why It's Still Broken

**The name is what the audience wants.** A cluster designation means nothing to a board or an insurer. A recognisable group name is actionable, which creates steady pressure to supply it.

**Vendor taxonomies are treated as ground truth.** Group definitions come from threat intelligence vendors and are adopted as though they were settled facts rather than that vendor's clustering judgement.

**Names overlap inconsistently across vendors.** The same activity is named differently by different vendors, and the relationship between those names is partial and disputed — which is well known in the field and invisible outside it.

**Separating the claims looks like hedging.** Stating the cluster confidently and the naming tentatively reads as equivocation to a reader who wanted an answer.

**The distinction is technical and the audience is not.** Explaining why the cluster is solid and the name is less so requires explaining how attribution works, which is difficult under crisis conditions.

**Nobody downstream asks.** Insurers and counsel accept the name because they have no basis to interrogate it, so the conflation is never challenged.

## What a Fix Looks Like

**Make them two sentences with two confidences.** The activity forms a coherent cluster, assessed at this confidence, on this basis. The cluster corresponds to the group known as X, assessed at this confidence, on this basis. Two sentences, and the reader can now see which claim is doing the work.

**State which vendor's taxonomy the name comes from.** Group names are vendor-specific. Naming the source makes explicit that the name is an external clustering judgement rather than a fact about the world.

**Answer the consequential question directly.** Where the decision turns on state association or sanctions exposure, address that directly with its own evidence and confidence, rather than leaving the reader to infer it from a group name. This is what insurers and counsel actually need and it is a different claim from the naming.

**Note where the naming is disputed.** Where vendors disagree about whether this activity belongs to X, say so. Disagreement between vendors is common, informative and never surfaced to the client.

**Record the naming inference separately.** What specifically matched the published group description, so that if the naming is later contradicted the specific basis is identifiable — which is how the reasoning improves.

**Educate the downstream consumers.** Insurers and breach coaches who understand that the name is a weaker claim than the clustering will ask better questions, which is what would eventually discipline the practice.

## Who Feels the Pain

The client, whose insurance coverage or sanctions position may rest on a naming claim considerably weaker than the confidence attached to it.

The responder, who understands the distinction perfectly and has no format in which to express it without appearing to equivocate.

The insurer, applying an exclusion on the strength of a group name whose evidential basis they cannot assess.

And the field's credibility, since attribution disputes between firms are frequently disputes about the naming step that neither has stated separately.

## Impact If Fixed

Splitting one sentence into two, with separate confidences, costs nothing and makes visible which of the two claims the downstream decision actually rests on.

Answering the consequential question directly — state association, sanctions exposure — gives insurers and counsel the finding they need instead of a name they must interpret.

And naming the taxonomy source would make clear that a group name is one vendor's clustering judgement rather than an established fact, which is understood inside the field and nowhere outside it.
