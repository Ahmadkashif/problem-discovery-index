# The Model Change That Broke Every Audience

**Niche:** [[niches/customer-data-platforms/warehouse-native-composable/profile|Warehouse-Native Composable]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The data team renamed a column in a refactor, eleven audiences now return nothing, and nobody connected the two events for nine days.
**Tags:** #data-integration #change-point-detection #workflow-orchestration #automation #quick-win #evaluation-metrics #graph-theory #compliance
**Contested on:** Every serious competitor in this niche is fighting to activate from a warehouse the vendor never touches, at the reliability and latency a customer-facing use case needs — and whoever does that takes the organisations that already own their data.

## The Problem
The data team refactored a customer model, renaming a column and changing a status value's encoding. Their own tests passed and their dashboards were updated. Eleven marketing audiences defined on that model now return empty or wrong results, a suppression list is no longer excluding anyone, and a triggered journey has stopped firing. The data team did not know the audiences existed; the marketing team does not read the warehouse's change log. Nine days later somebody notices a campaign performing oddly. The composable architecture's strength — using the organisation's own governed model — is also the surface through which this class of failure arrives.

## Why It's Still Broken
The warehouse's dependency graph stops at the analytics layer and does not include marketing activations, so a refactor is tested against dashboards and not against audiences — the lineage is incomplete at exactly the boundary the architecture created. The two teams have different tooling and different change processes. Audiences fail silently by returning fewer rows rather than erroring. And nobody owns the boundary.

## What a Fix Looks Like
Extend the lineage across the boundary. Register every audience and activation as a dependency of the warehouse models it reads, which is the fix and puts marketing activations into the same dependency graph the data team already uses. Break the build on a change that would break an audience, which is the standard practice one side of the boundary already follows and simply does not extend across it. Alert on membership collapse, since an audience dropping from two hundred thousand to eleven is unambiguous and needs no lineage at all to detect. Notify the data team of downstream consumers before a change ships, so the refactor can account for them. Version audience definitions against model versions, which makes the coupling explicit. Test audiences in the data team's own continuous integration, which is where the change is made and the only place it can be caught before deployment. Distinguish an empty audience from a small one, because the failure returns fewer rows and the system treats that as a valid result. Escalate suppression failures immediately, since those have consequences the others do not. Give marketing visibility of upcoming model changes in terms they understand. And measure time from model change to audience break detection, because the boundary between two competent teams is where this architecture's failures live.

## Who Feels the Pain
Marketing teams whose audiences empty without warning; data teams blamed for refactors nobody told them had consumers; and organisations whose suppression stopped silently.

## Impact If Fixed
The warehouse's lineage stops at the analytics layer, which is exactly the boundary this architecture created, so refactors are tested against dashboards and not audiences. Registering activations as dependencies extends a practice one side already follows across the boundary where the failures live.
