# The One Endpoint Whose Authorisation Differs

**Niche:** [[niches/api-infrastructure-providers/api-security-shadow-endpoints/profile|API Security & Shadow Endpoints]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Authorisation is implemented per endpoint by whoever wrote it, so among two hundred similar endpoints one checks ownership differently, and nothing compares them.
**Tags:** #descriptive-statistics #k-means-clustering #graph-theory #logistic-regression #evaluation-metrics #confidence-intervals #compliance #quick-win
**Contested on:** Every serious competitor here is fighting to produce a complete inventory of an organisation's exposed endpoints and what each one does with sensitive data — and whoever does that takes the security account, because nobody can currently produce the list.

## The Problem
Two hundred endpoints follow the same pattern: accept an identifier, verify the caller is entitled to that resource, return it. One hundred and ninety-nine verify entitlement against the authenticated principal. One verifies that the identifier is well-formed and returns the resource. It was written in a hurry, reviewed by someone who checked the business logic, and has been in production for three years. This is the most commonly reported API vulnerability class, it is a deviation from the organisation's own prevailing pattern, and nothing anywhere compares an endpoint against its neighbours.

## Why It's Still Broken
Authorisation is implemented in application code, endpoint by endpoint, and review looks at the change rather than at the population. Scanners test for known vulnerability signatures rather than for inconsistency with local convention, which is a different question and the one that would find this. The gateway enforces authentication and generally does not know what authorisation each endpoint should apply. And the deviation is invisible by construction: the endpoint works, its tests pass, and nothing is obviously wrong with it in isolation.

## What a Fix Looks Like
Compare endpoints against each other, which nothing currently does. Group endpoints by their shape — parameters, resource type, operation, response structure — into families that should behave alike, which is ordinary clustering over the specification and the observed traffic. Within each family, compare authorisation behaviour: which credentials are required, whether a tenant boundary is enforced, what happens with an identifier belonging to somebody else — and report the outliers, which is a short list and is where the vulnerabilities are. Test the boundary actively rather than inferring it, by issuing requests with a credential from one tenant against another's resource in a controlled environment, which is the definitive check and is cheap. Compare against the prevailing pattern rather than against an abstract standard, since the organisation's own convention is the right baseline and the finding is deviation from it. Apply the same comparison to rate limiting, input validation and error verbosity, each of which varies inconsistently for the same reason. And run it continuously, because every new endpoint is another chance for the deviation.

## Who Feels the Pain
Security teams whose scanners find known signatures and miss local inconsistency; engineers who implemented authorisation correctly nineteen times and once did not; and organisations whose breach, when it comes, will be through an endpoint that differed from its neighbours.

## Impact If Fixed
Comparing endpoints within a family is straightforward clustering plus a controlled test, and it targets the vulnerability class that dominates reported API incidents. Using the organisation's own prevailing pattern as the baseline is what makes the findings precise rather than generic.
