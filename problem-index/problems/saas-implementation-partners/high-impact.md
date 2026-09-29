# Four Hundred Implementations and No Record of Which Configurations Worked

**Industry:** [[saas-implementation-partners|SaaS Implementation Partners]]
**Type:** High Impact
**One-liner:** The firm has configured the same platform hundreds of times, the adoption data for every one of them sits in a customer tenant, and the next discovery workshop starts from a blank page.
**Tags:** #gradient-boosting #survival-analysis #causal-inference #confidence-intervals #k-nearest-neighbors #evaluation-metrics #tacit-knowledge-ml #data-integration

## The Problem
An implementation is a long sequence of configuration decisions. Which objects and fields, which validation rules, which approval chains, how many stages in the pipeline, which processes to automate and which to leave manual, how much to customise versus how much to change the customer's process. Each decision is argued in a workshop, recorded in a requirements document, built, tested and delivered.

The consequences become visible after go-live. Some fields are never populated. Some automations fire constantly and some never. A workflow that the customer insisted on is abandoned within a quarter and users route around it. Adoption either holds at ninety days or decays, and which of those happens is the actual measure of whether the implementation succeeded.

None of that reaches the partner. The engagement closes at hypercare, the usage data belongs to the customer, and the consultants move to the next project. So a firm with fifteen years of delivery history cannot say which approval chain designs survive contact with users in mid-market manufacturing, or whether the customers who insisted on heavy customisation adopted better or worse than those who did not. Those questions have answers sitting in four hundred tenants.

The practical loss shows up in two places. In delivery, every engagement rediscovers requirements that are close to identical to a dozen prior ones, because there is no evidence-backed default to start from — only an accelerator package whose contents were assembled by whoever built it and whose actual performance is unknown. In sales, the firm competes on certifications and case studies when the buyer's real question is what works for an organisation like mine, which the firm could answer better than anyone and does not.

## Why It's Unsolved
The data belongs to the customer, in a tenant the partner's access to ends with the contract. Getting usage telemetry out would require a clause nobody currently negotiates and a customer's agreement to let their vendor observe their staff's system use — which is a legitimate concern that has to be handled by aggregation and anonymisation rather than waved away.

The technical shape is awkward too. Configuration lives as platform metadata in heterogeneous forms across tenants, versions and platform releases, and comparing two implementations requires a normalised representation of configuration that nobody maintains. Adoption metrics differ by platform and are not standardised.

The commercial incentive is mixed. A partner paid by the hour benefits from rediscovery; an evidence-backed default configuration reduces billable discovery time. Firms say they want reuse and measure their people on utilisation, and the second wins.

And there is a genuine uncomfortable finding waiting. A serious analysis would likely show that a meaningful share of the customisation partners build is never used, which is an awkward result for a business model that bills for building it.

## What a Solution Looks Like
Contract for aggregate telemetry. A post-go-live measurement clause granting the partner anonymised, aggregated usage data for a defined window is a modest ask that most customers will accept, because the customer also wants to know whether adoption held. The partner offers the analysis back as part of the deal.

Normalise the configuration. A representation of what was built — objects, fields, automations, approval structures, integration patterns, customisation depth — comparable across tenants and platform versions, is the prerequisite for any of this and is a substantial but ordinary engineering project.

Join configuration to adoption and to organisation shape. With a few dozen implementations represented this way, a firm can begin answering which patterns adopt well for which kinds of organisation, with intervals. With a few hundred it becomes genuinely predictive, and it is the only dataset of its kind because no single customer has more than one implementation and the platform vendor sees configuration without the delivery context.

Feed it into discovery rather than replacing discovery. The value is starting a workshop with an evidence-backed default — organisations like yours typically adopt this pattern and abandon that one — which shortens the argument rather than removing the conversation.

## Impact If Solved
This turns a partner's delivery history from a portfolio into an asset. It shortens discovery, raises adoption, and gives the firm the only credible answer to the question buyers actually ask during selection. It would also expose how much of what the industry builds goes unused, which is uncomfortable and is the finding most likely to improve outcomes for customers — and the first firm willing to publish it has a positioning nobody else can match.
