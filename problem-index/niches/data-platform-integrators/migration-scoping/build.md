# Migrating What Is Used

**Niche:** [[niches/data-platform-integrators/migration-scoping/profile|Migration Scoping]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The migration carries everything because establishing what matters is harder than translating it.
**Tags:** #data-integration #graph-theory #evaluation-metrics #descriptive-statistics #optimization-fundamentals #revenue-impact #confidence-intervals #automation
**Contested on:** Every serious competitor in this niche is fighting to establish which of a decade's warehouse logic and four thousand reports actually needs to move — and whoever scopes that honestly takes the account.

## The Problem
A platform migration begins with an inventory: thousands of tables, transformations and reports accumulated over a decade. The scoping question is which of them the organisation still needs. Nobody can answer it, because usage has never been measured and dependencies are partly undocumented, so the default is to carry all of it. The programme is then priced, staffed and scheduled against an estate that is mostly inventory, and the inventory arrives on the new platform intact.

## Why Nobody Has Built This
Usage data exists in the source platform and nobody has run the analysis. Scoping down reduces the programme's size, which reduces its fee. Clients fear missing something. And translating everything is a defensible decision nobody is blamed for.

## What to Build
Scope from usage and dependency rather than from the inventory. Analyse the source platform's query history to classify the estate into used, occasionally used and dormant, which is the core and is the input the scoping decision has never had. Trace dependencies so a used asset carries what it needs and nothing more, since naive usage filtering breaks things and is why nobody trusts it. Identify the assets worth rebuilding rather than translating, as a decade-old transformation frequently encodes a workaround for a limitation that no longer exists. Quantify the cost of carrying the dormant portion onto a consumption-priced platform, which is the argument that changes the client's mind. Keep the source available read-only rather than deleting, which removes the fear that drives carry-everything. Stage the migration by usage so the valuable assets move first and the programme delivers early. Monitor the source after cutover to catch anything that was needed and not carried, which is cheap insurance. Report what was carried and never used afterwards, which is the evidence for the next client. Price the programme on the scoped estate honestly, which is a commercial choice and the harder half. And offer the scoping analysis as a standalone engagement, since it is valuable whether or not the migration proceeds.

## Target Customer
Data platform integrators, client programme and data leadership, platform vendors funding migrations, and migration tooling providers.

## Impact If Built
The default is to carry everything because establishing what matters is harder than translating it, and the inventory arrives intact on the new platform. Usage-and-dependency scoping is the input the decision has never had.
