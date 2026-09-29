# One Assurance Setting for Every Transaction

**Niche:** [[niches/esignature-document-workflow/risk-based-identity-assurance/profile|Risk-Based Identity Assurance]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Verification level is chosen once during implementation and applied to every agreement thereafter, so small transactions carry friction they do not need and large ones carry risk nobody priced.
**Tags:** #gradient-boosting #logistic-regression #bayesian-inference #confidence-intervals #evaluation-metrics #hypothesis-testing #compliance #revenue-impact
**Contested on:** Every serious competitor in signing assurance is fighting to set the verification level per transaction from its actual risk rather than per account from a default — and whoever does that gives customers both lower fraud and less friction, which are currently traded against each other.

## The Problem
A company sets identity verification to an emailed access code, because anything stronger reduced completion in a pilot. That setting applies to a routine service order and to an asset transfer worth six figures. When a signature is later disputed, the audit trail shows that someone with access to an email account clicked a link — which is what the company chose, for every transaction, without ever being shown that the choice was different for different transactions. The alternative company sets government identity verification for everything, pays for every check, and watches completion fall on the ninety percent of agreements that never needed it.

## Why Nobody Has Built This
Assurance is configured during implementation by a solutions consultant and revisited approximately never. The information that would justify a graduated approach — how often signatures are disputed, at what value, under which verification method — is not collected by anyone: disputes surface in legal and are never reported back to the platform, so the loss side of the trade-off has no data at all. Vendors also have mixed incentives, since stronger verification is often a paid add-on and a recommendation engine that says most transactions do not need it reduces attach revenue. And per-transaction assurance requires the risk to be assessed at send time, which nothing does.

## What to Build
Assurance recommended per transaction. A risk score at send time from what is observable — transaction value, document type, whether the counterparty has signed with this sender before, the recipient domain and its history, geography, the irreversibility of what is being agreed, and the sender's own configured risk appetite. That score maps to a rung on the ladder, with the reasoning shown, because a legal or fraud owner will not accept an unexplained assurance decision. Where signals during signing are inconsistent with the expected pattern, step up mid-flow rather than failing, which is standard in payments and absent here. Feed back the outcomes that exist — declined verifications, abandoned signings, and, where the customer will report them, disputes and repudiations — since the loss side is currently unmeasured and even sparse data is better than the nothing available today. And report the counterfactual plainly: what this policy would have cost in verification fees and completion against the flat setting, which is the number that decides whether anyone adopts it.

## Target Customer
Fraud and trust functions at high-value transaction senders, legal risk owners, and the signature platforms for whom this converts an unused feature ladder into a reason to buy the higher rungs.

## Impact If Built
The flat setting guarantees a wrong answer on both ends of the distribution, and the correction needs no new data collection to begin. The disputed-signature feedback loop is the missing measurement in the whole category, and even a partial one would put a number on a risk that is currently argued about without one.
