# Mapping That Reuses What Was Learned

**Niche:** [[niches/ap-automation-vendors/erp-and-dimension-mapping/profile|ERP & Dimension Mapping]]
**Industry:** [[industries/ap-automation-vendors|AP Automation Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The consultant maps this customer's dimensions in six weeks and the thousand mappings already completed on the same ERP contribute nothing.
**Tags:** #transfer-learning #large-language-models #word-embeddings #data-integration #evaluation-metrics #confidence-intervals #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to map a customer's chart of accounts, dimensions and custom fields without six weeks of a consultant — and whoever makes the integration cover the non-standard fields wins the deals that die in implementation.

## The Problem
Every customer running the same ERP has configured it differently, and every one of those configurations has already been mapped by someone at the vendor for another customer. Departments called cost centres, projects called jobs, classes used as entities, custom fields holding approval routing. The consultant starts each engagement by asking the customer to explain their configuration, and the accumulated knowledge of a thousand prior mappings on the same platform exists only in individual consultants' memories.

## Why Nobody Has Built This
Implementation was staffed as a services function, so reuse depended on people rather than on systems — and a services business that bills for the time has no urgency to compress it. Each configuration looked unique enough to justify starting fresh. Mapping decisions were never recorded in a structured form. And implementation duration is treated as a cost of sale rather than as a product deficiency.

## What to Build
Learn the mapping problem once. Build a library of configuration patterns per ERP from completed implementations, which is the core and is derivable from mappings the vendor already owns. Propose a mapping automatically from the customer's configuration by matching against the library, since most configurations are variations on a small number of shapes. Use field names, usage patterns and data content as evidence, because a field called "Class" containing entity names is identifiable from its contents. Handle custom fields as a first-class case rather than as an exception, as they are where the six weeks actually goes. Validate the mapping against real transactions before go-live, since errors currently surface in production and are expensive. Detect ERP version and configuration differences at the start rather than in week five, which is where most slippage originates. Record every mapping decision structurally so the library compounds. Let the customer confirm rather than specify, because confirming a proposal is far faster than answering open questions. Support reconfiguration after go-live, since charts of accounts change and the mapping currently ossifies. And measure implementation days by cause, as nobody knows which parts consume the time.

## Target Customer
Implementation and product leadership, customers facing a six-week deployment, ERP integration specialists, and integration platform vendors with no domain library.

## Impact If Built
Implementation was staffed as services, so reuse lived in people and a business that bills for the time had no urgency to compress it. A pattern library derived from completed mappings turns open questions into a proposal to confirm.
