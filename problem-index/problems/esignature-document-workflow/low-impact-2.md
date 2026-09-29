# Identity Assurance for High-Value Signing

**Industry:** [[esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Identity verification options exist across the full range from an emailed link to a government ID check, and companies apply one setting to every agreement because nothing tells them which transactions warrant more.
**Tags:** #gradient-boosting #logistic-regression #graph-neural-networks #confidence-intervals #feature-engineering #evaluation-metrics #compliance

## The Problem
An electronic signature's legal weight depends partly on the assurance that the person signing was who they claimed to be. The default in most deployments is an emailed link — the signer proves control of an email address and nothing more.

For a policy acknowledgement that is entirely appropriate. For a property transaction, a large commercial agreement, a loan document or anything a fraudster would find worth attacking, it is thin. Business email compromise is a well-established attack pattern precisely because email control is easy to obtain, and an attacker who controls an email account can sign an agreement.

Stronger options exist: knowledge-based authentication, one-time passcodes to a verified phone, government ID document verification with liveness checks, and qualified certificates. They cost more, they add friction, and every one of them reduces completion rate.

So companies pick one level and apply it universally. Almost always the weak one, because completion rate is the metric everyone watches, which means the high-value transactions carry the same assurance as the routine ones.

## What Already Exists
Identity verification is a mature market. Document verification with liveness detection is reliable and widely available. Knowledge-based authentication is offered by the major platforms. Phone-based authentication is standard. Remote online notarisation is legal in most US states and integrated by several vendors. Qualified electronic signatures under eIDAS provide a high-assurance path in Europe.

## The Customisation Gap
Risk-based selection is entirely absent. Whether a given envelope warrants stronger verification depends on its value, its type, whether the signer is known, whether the routing looks unusual, whether the email domain is newly seen, and whether the pattern resembles known compromise attempts. That is a scoring problem and no platform performs it, so the choice is a global setting.

The signals for it are present. A platform sees an organisation's normal signing patterns across years, so an unusual counterparty, an unusual routing, a change of email domain for a known signer, or a request timed to arrive during a holiday period are all detectable deviations.

Cross-customer signal is the platform's unique advantage: an attack pattern seen against one customer is directly relevant to the next, and no individual company can see it.

Step-up is the third gap. Verification is decided when the envelope is sent, and it should be possible to require more at the moment the signature is attempted, when the risk signals are actually observable.

## Impact If Solved
Signature fraud on high-value agreements is a real and growing attack surface defended by a global setting chosen to protect completion rate. Applying assurance proportionate to risk protects the transactions that matter without imposing friction on the ninety-five per cent that do not.
