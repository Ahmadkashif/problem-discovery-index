# Three People Connected to the Same System Three Times

**Niche:** [[niches/no-code-app-builders/bespoke-api-connectivity/profile|Bespoke API Connectivity]]
**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Type:** Fix (Pain Point)
**One-liner:** A hand-rolled HTTP connection is invisible to everyone except the person who built it, so the same internal system gets integrated from scratch by each new builder who needs it.
**Tags:** #descriptive-statistics #k-means-clustering #graph-theory #evaluation-metrics #confidence-intervals #data-integration #quick-win #automation
**Contested on:** Every serious competitor here is fighting to get a non-engineer connected to an internal system nobody has written a connector for, in the session where they need it — and whoever does that takes the builder, because the alternative is a hand-rolled HTTP block and a lost afternoon.

## The Problem
Three people in a company have each spent an afternoon connecting an app to the internal fulfilment service. Each worked it out independently. Each stored the credential differently, one of them in a plain field in the app configuration. Each handles errors differently, and two of them do not handle errors at all. When the service's authentication changes, all three break at different times and each person debugs it alone. The platform sees three unrelated HTTP blocks and has no idea they point at the same system.

## Why It's Still Broken
Generic HTTP blocks are opaque by design: the platform stores a URL and headers and attaches no meaning, so there is no entity representing a connection to a system. Nobody within the company has visibility across builders' apps, because governance tooling reports apps rather than their integrations. And credential handling inside these blocks is genuinely poor in a way that would be a finding in any security review, which nobody runs because the apps are invisible.

## What a Fix Looks Like
Recognise connections as entities. Cluster HTTP blocks across the estate by host, path shape and authentication pattern, which identifies that three apps talk to the same system — a straightforward grouping over configuration the platform already stores. Promote a recognised cluster into a shared, named connection with a single credential held properly, which fixes the security problem and the duplication together. Surface existing connections to a builder starting a new integration, so the fourth person finds the work the first three did rather than repeating it. Flag credentials stored in plain configuration fields, which is a one-line check with a genuinely serious finding rate. Alert all dependents when a shared connection fails, rather than each builder discovering it separately over a fortnight. And report the connection inventory to IT, which is the first time anyone in most organisations would see what the no-code estate actually talks to.

## Who Feels the Pain
Builders repeating an afternoon somebody else already spent; security teams unaware that credentials sit in application configuration; and IT functions with no map of what the estate connects to.

## Impact If Fixed
Clustering configuration the platform already holds turns invisible, duplicated, insecure connections into named shared ones. The plain-credential check is a quick win with a high hit rate, and the connection inventory is information no organisation currently has at all.
