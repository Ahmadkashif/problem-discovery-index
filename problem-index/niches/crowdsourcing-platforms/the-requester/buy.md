# Buy: Research Methodology Tooling Adapted to Non-Specialists

**Niche:** [[niches/crowdsourcing-platforms/the-requester/profile|The Requester]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The statistical methods for crowd aggregation are well developed in the literature and available as libraries; the person who needs them has never heard of them.
**Tags:** #bayesian-inference #expectation-maximization #maximum-likelihood-estimation #evaluation-metrics #confidence-intervals #hypothesis-testing #automation #descriptive-statistics
**Contested on:** Whether well-developed methods can reach a population that will not read a methods paper.

## The Problem

The methodology exists. Latent-variable aggregation models for crowd labels, item response theory, agreement statistics with known properties, and a substantial literature on crowdsourcing quality have been developed over two decades and several are available as open-source implementations.

The person who needs them is a psychology PhD student, an ML engineer with a deadline or a product manager, running one batch, who will use majority vote because it is what the platform provides and because they do not know there is an alternative. The gap is not capability — it is distribution to a non-specialist audience that will not go looking.

## What Already Exists

Open-source implementations of Dawid-Skene and its successors. IRT libraries. Agreement statistic implementations across statistical packages. The crowdsourcing methodology literature. Annotation platform aggregation features, generally limited to majority vote and simple consensus. Statistical consulting inside universities, which the ML and industry requesters do not have.

## The Customization Gap

**Delivery has to be default, not optional.** A method available as a library will not be used by this population. It has to be what the platform runs by default on the results, with the majority vote available as a comparison rather than as the primary output.

**The output must be interpretable without the method.** A posterior probability per item is only useful if the requester knows what to do with it. The delivery has to be a confidence they can filter on and a plain-language explanation, not a parameter estimate.

**The task types are heterogeneous and the models assume categorical labels.** Much of the literature assumes discrete categories. Real batches include free text, bounding boxes, rankings and continuous ratings, each needing a different aggregation treatment, and the library ecosystem is thinnest exactly where the volume is growing.

**Sample sizes per item are small.** Academic treatments frequently assume many annotations per item. Real batches often have three, which makes the joint estimation thin and the shrinkage and prior choices consequential — and defaults that work at three are what the platform must ship.

**The diagnosis is the product, not the estimate.** The literature produces better labels; the requester also needs to be told why their batch went wrong and what to change. That diagnostic layer has no equivalent in the methods literature and is what converts the statistics into a usable product.

## Target Customer

Crowdsourcing and annotation platforms, who can make good methods the default for a population that will never adopt them individually. Also the academic infrastructure providers and the statistics community, for whom this is an unusually direct route from a well-developed literature to a large practical impact.

## Impact If Solved

The aggregation models, IRT machinery and agreement statistics get used by default, and the non-specialist delivery, interpretable outputs, heterogeneous task type support, small-sample defaults and diagnostic layer get built. Concretely: twenty years of methodology reaches the people running the batches, without any of them reading a paper.
