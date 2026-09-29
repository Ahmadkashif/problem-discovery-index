# The Developer With Tickets

**Parent Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Category:** Underserved Audience
**Contested on:** Every serious competitor that takes this seriously is fighting to give a developer a finding they can act on — what it means, whether it matters here, and exactly how to fix it — and whoever does that takes the remediation rate, because the current output is a ticket about code they did not write.

## Profile
**Market Size:** ~$190M US attributable to developer-facing remediation experience
**Share of Parent Industry:** ~6% of category revenue
**Digital Adoption:** None — the finding arrives as a ticket with a severity and a link
**Target Buyer:** Security leadership buys it; developers must act for anything to change
**Automation Potential:** Very High — the fix is frequently determinable and is not determined

## What Makes This a Distinct Niche
A developer receives tickets about vulnerabilities in transitive dependencies they never chose, with no context on whether it matters and no clear way to fix it. The experience is specific: the ticket names a component several levels down a dependency tree, cites a severity assigned by a stranger, links to an advisory written for security researchers, and asks for remediation by a date. The developer does not know whether their code reaches the vulnerable path, cannot upgrade the transitive dependency directly because their direct dependency pins it, and has no indication of what upgrading would break. They mark it in progress, ask in a channel, or let it age. The relationship between the security function and engineering is substantially determined by this interaction, and it is designed by nobody.

## Current Tools & Gaps
Ticket creation from findings, automated dependency update pull requests, and advisory links. The gaps: the ticket explains the vulnerability rather than the action, which is the wrong content for the recipient; transitive dependencies cannot be upgraded directly and the ticket does not say what the actual remediation path is; the upgrade's risk — what breaks — is unstated, which is the developer's real question; automated update pull requests exist and are frequently not connected to the security finding, so the developer receives both separately; and nothing measures whether findings are actually remediated or merely aged out.

## Problems
- [[niches/software-supply-chain-security/the-developer-with-tickets/build|🔨 Build: A Ticket About Code They Did Not Write]]
- [[niches/software-supply-chain-security/the-developer-with-tickets/buy|🛒 Buy: Automated Remediation That Already Works]]
- [[niches/software-supply-chain-security/the-developer-with-tickets/fix|🔧 Fix: The Transitive Dependency You Cannot Upgrade]]
