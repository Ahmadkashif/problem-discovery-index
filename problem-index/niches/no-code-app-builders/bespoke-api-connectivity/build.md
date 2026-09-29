# Connected in the Session, Not the Sprint

**Niche:** [[niches/no-code-app-builders/bespoke-api-connectivity/profile|Bespoke API Connectivity]]
**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The builder who needs the internal inventory system has an afternoon and no ability to read an API specification, and every tool available to them assumes the opposite of both.
**Tags:** #large-language-models #transformers #bert #evaluation-metrics #confidence-intervals #cross-validation #data-integration #worker-facing
**Contested on:** Every serious competitor here is fighting to get a non-engineer connected to an internal system nobody has written a connector for, in the session where they need it — and whoever does that takes the builder, because the alternative is a hand-rolled HTTP block and a lost afternoon.

## The Problem
An operations person building an app needs data from the internal fulfilment service. What they have is a wiki page with three example requests and a colleague who says the token comes from an environment variable. What the platform offers is a block with fields for method, URL, headers and body. They spend an afternoon on authentication alone, get a 401 they cannot interpret, ask a developer, and either succeed narrowly or give up and export a CSV weekly by hand — which is the outcome that quietly happens most often and never appears in any vendor's data.

## Why Nobody Has Built This
Custom connector tooling was built for developers because developers were the ones who asked, and the people who most need it do not know what to ask for. Authentication is treated as configuration rather than as a recognised pattern to be detected and handled, which is why it is the dominant failure point. Inferring an interface from partial information — a wiki page, three examples, a curl command — was not practical until recently and is now well within reach, but no vendor has reframed the problem that way. And the failure mode is silent: the builder does not file a ticket, they do it by hand forever.

## What to Build
Connection from whatever the builder has. Accept any of the available inputs — a specification file, a documentation URL, a pasted example, a curl command, an exported request — and produce a candidate connector from it, with a language model doing the reading that the builder cannot. Detect the authentication pattern rather than asking, since nearly every API uses one of a handful and recognising it removes the largest obstacle; then walk the builder through obtaining the credential in terms of what they will see, not in terms of the protocol. Probe the live system to confirm inferences before the builder relies on them — test the endpoint, verify the pagination, check the error shape — and report what was confirmed and what was assumed, honestly, since a connector that is right about four things and guessing about the fifth should say so. Expose the result as named actions with typed fields rather than as endpoints. Register it as a first-class connector in the platform so it is visible, monitorable, maintainable and reusable, which is what distinguishes this from the hand-rolled block. And where the builder is genuinely blocked, produce a precise request for the developer who can unblock them, which is far more useful than the current escalation of pasting an error into a chat.

## Target Customer
No-code and automation platform vendors, and the enterprise platform teams who currently field these requests one at a time from builders across the business.

## Impact If Built
The systems excluded from every marketplace are the ones the business actually runs on, and the current fallback either consumes an afternoon or silently becomes a manual export. Authentication detection and honest confirmation of what was inferred are the two things that determine whether a non-engineer gets connected at all.
