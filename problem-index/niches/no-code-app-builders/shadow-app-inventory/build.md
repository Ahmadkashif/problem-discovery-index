# The Apps in Tenants Nobody Knows About

**Niche:** [[niches/no-code-app-builders/shadow-app-inventory/profile|Shadow App Inventory]]
**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every platform's admin console lists the apps in its tenant, which is useless when the applications that matter were built on accounts the company does not know exist.
**Tags:** #graph-theory #k-means-clustering #logistic-regression #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #data-integration
**Contested on:** Every serious competitor here is fighting to produce a complete list of the applications a company's employees have built, including the ones built on accounts IT does not know exist — and whoever can produce that list takes the security and compliance account, because nobody can produce it today.

## The Problem
A compliance review asks which applications process customer personal data. IT produces a list from the systems it provisions. It does not include the customer intake app an account manager built on a free tier with a personal email, which holds nine thousand records and shares a public form link, or the two apps in a departmental tenant expensed monthly as a subscription nobody mapped to a platform. Nobody is hiding anything: the people who built these things were solving a problem the way the category told them to. The company simply cannot enumerate its own applications, and every governance conversation begins from a list known to be incomplete.

## Why Nobody Has Built This
Platform vendors can only see their own tenants, and a vendor has no commercial reason to help a customer find usage on accounts the customer is not paying for. Discovery from outside requires correlating several data sources that belong to different teams — network, finance, identity, endpoint — and nobody owns the correlation. Shadow IT discovery tooling stops at the application level, telling a company it uses a no-code platform without saying what has been built there, because going deeper requires cooperation from the platform. And the problem is only acute at audit time, which is periodic and always urgent, so it gets solved by survey rather than by system.

## What to Build
Discovery from the outside, corroborated. Correlate the available signals: network and proxy logs showing platform domains, expense and card transactions matching platform billing, identity provider sign-ins including the personal-account pattern where a corporate device authenticates to a consumer account, browser extension telemetry where deployed, and inbound connections from platform IP ranges to the company's own systems — which is the strongest and least-used signal, since an app that integrates with the company's data must reach it. Resolve those into accounts and tenants, then to people, with confidence attached. Where a tenant can be claimed, claim it through the vendor's domain verification and get the app-level inventory properly. Where it cannot, enumerate what is inferable — the platform, the user, the activity level, and the systems it connects to. Then assess rather than just list: what data it likely touches, how many people use it, whether it exposes anything externally. And handle discovery as an amnesty rather than an enforcement action, because the alternative drives the next one onto a personal device and makes the inventory permanently worse.

## Target Customer
IT, security and compliance leadership; SaaS management and cloud access security vendors for whom this is the depth their current products lack; and the no-code vendors themselves, for whom tenant claiming is a route to enterprise revenue.

## Impact If Built
The most consequential applications are structurally outside every console, which makes this a discovery problem rather than a reporting one. The inbound-connection signal is the strongest evidence available and nobody uses it, and the amnesty framing is what determines whether the inventory improves or the behaviour hides.
