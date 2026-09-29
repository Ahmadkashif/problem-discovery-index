# A Ticket About Code They Did Not Write

**Niche:** [[niches/software-supply-chain-security/the-developer-with-tickets/profile|The Developer With Tickets]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A developer receives tickets about vulnerabilities in transitive dependencies they never chose, with no context on whether it matters and no clear way to fix it.
**Tags:** #graph-theory #large-language-models #bert #gradient-boosting #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to give a developer a finding they can act on — what it means, whether it matters here, and exactly how to fix it — and whoever does that takes the remediation rate, because the current output is a ticket about code they did not write.

## The Problem
A ticket arrives: high severity vulnerability in a serialisation library, remediate within thirty days, with a link to an advisory. The developer has never heard of the library; it arrived through a framework they use. They cannot upgrade it because their framework pins a version range. They do not know whether their application calls the affected code. The advisory describes an attack requiring a configuration they may or may not have. They spend forty minutes establishing none of this conclusively, mark the ticket in progress, and it ages. Multiply by thirty tickets a quarter and the security function's entire output is an aged queue and a deteriorating relationship.

## Why Nobody Has Built This
The ticket is generated from the finding, and the finding is about the vulnerability, so the ticket describes the vulnerability — which is the right content for a security analyst and the wrong content for the person expected to act. The remediation path for a transitive dependency requires resolving the dependency graph to find which direct dependency to upgrade and to what, which is computable and is not computed. The upgrade's risk is the developer's actual question and is unaddressed by anybody. And the developer is not the buyer, so their experience has never shaped the product.

## What to Build
Send an action rather than a finding. State whether it matters here — reachable, exploitable in this configuration, exposed — using the prioritisation capability, and do not send the ones that do not, which is the largest single improvement and is a prioritisation decision rather than a presentation one. State the actual remediation path: not the vulnerable transitive package but the direct dependency to upgrade and the version that resolves it, which is a graph computation the tool can perform and the developer cannot easily. State what the upgrade would break, using the risk assessment from the remediation niche, because that is the developer's real question and its absence is why tickets age. Open the change rather than describing it, since automated dependency update tooling exists and is frequently not connected to the security finding — a ticket and an unconnected pull request is worse than one linked change. Explain the vulnerability in terms of what an attacker could do to this application, rather than linking an advisory written for researchers. Provide a route to dispute, since the developer sometimes knows the finding does not apply and currently has no mechanism except a comment. And measure remediation rather than ticket creation, since the number of tickets opened is the metric that rewards exactly the behaviour that has destroyed the relationship.

## Target Customer
Security leadership whose findings age unremediated, the developers receiving them, and the vendors whose ticket-generation feature is the category's most disliked output.

## Impact If Built
The ticket describes the vulnerability to somebody who needs an action, which is why findings age. Computing the real remediation path and stating the upgrade risk answer the developer's two actual questions, and not sending the findings that do not matter is the prerequisite for any of it being read.
