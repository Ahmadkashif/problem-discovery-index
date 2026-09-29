# API Security & Shadow Endpoints

**Parent Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Category:** Low Digitized
**Contested on:** Every serious competitor here is fighting to produce a complete inventory of an organisation's exposed endpoints and what each one does with sensitive data — and whoever does that takes the security account, because nobody can currently produce the list.

## Profile
**Market Size:** ~$520M US API security and discovery
**Share of Parent Industry:** ~13% of category revenue
**Digital Adoption:** Low — most organisations cannot enumerate their own endpoints
**Target Buyer:** Security functions and platform engineering
**Automation Potential:** Very High — traffic observation answers the inventory question directly

## What Makes This a Distinct Niche
The premise of every API security control is knowing which APIs exist. Most organisations do not: there are endpoints behind the gateway and endpoints beside it, services exposed directly during an incident and never reverted, old versions still reachable, internal endpoints that became externally accessible through a load balancer change, and acquired companies' estates nobody has inventoried. The consequence is that the controls protect the documented subset and the incidents happen in the rest, which is the consistent pattern in publicly reported API breaches: the vulnerable endpoint was one nobody knew was there, or one whose authorisation logic differed from its neighbours. The contest is discovery and classification rather than policy enforcement, which is the part the gateways already do well for the traffic they see.

## Current Tools & Gaps
API security vendors offering discovery and runtime protection, gateway policy enforcement, web application firewalls, and specification-based scanning. The gaps: discovery is usually limited to traffic that passes the gateway, which excludes exactly the endpoints that matter; authorisation logic is per endpoint and inconsistent, and nothing compares endpoints against each other to find the odd one out; sensitive data flowing through endpoints is not classified, so nobody knows which endpoints expose personal or financial data; and the specification, where one exists, describes intent rather than what is reachable.

## Problems
- [[niches/api-infrastructure-providers/api-security-shadow-endpoints/build|🔨 Build: The Endpoint Nobody Knew Was There]]
- [[niches/api-infrastructure-providers/api-security-shadow-endpoints/buy|🛒 Buy: Attack Surface Management, One Layer Deeper]]
- [[niches/api-infrastructure-providers/api-security-shadow-endpoints/fix|🔧 Fix: The One Endpoint Whose Authorisation Differs]]
