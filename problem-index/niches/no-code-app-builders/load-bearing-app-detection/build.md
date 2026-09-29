# The Day It Stopped Being a Convenience

**Niche:** [[niches/no-code-app-builders/load-bearing-app-detection/profile|Load-Bearing App Detection]]
**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every no-code app that succeeds crosses from convenience into dependency, the crossing is invisible, and the company finds out when the person who built it hands in their notice.
**Tags:** #gradient-boosting #survival-analysis #graph-theory #change-point-detection #evaluation-metrics #confidence-intervals #automation #compliance
**Contested on:** Every serious competitor here is fighting to detect the moment an app crosses from a personal convenience into a business process the company cannot lose — before the person who built it leaves — and whoever does that takes the platform governance account, because that crossing is the category's only genuine crisis.

## The Problem
An operations analyst builds a tracker for warranty claims because the spreadsheet was unmanageable. It is good. Their team adopts it. The service desk starts entering claims directly. Finance builds a report on its output. A supplier is given a form that writes into it. Eighteen months later it processes several hundred claims a week, has an automation that emails customers, and is the only record of claim status. The analyst takes a job elsewhere. In the handover meeting somebody asks who else can change the app and the answer is nobody, and the second question — whether the company could operate without it for a week — is answered by silence.

## Why Nobody Has Built This
The category's entire value proposition is that building is easy and requires no permission, and a product that monitors what people build sits uncomfortably against that positioning. Vendors measure apps created and active users, which are adoption metrics, and criticality has never been a metric anyone asked for. Detection also needs signals the platform holds but has never combined — usage breadth, dependency edges, process integration, external exposure — and combining them requires deciding what load-bearing means, which nobody has defined. And the crisis, when it comes, is attributed to the departing person rather than to a missing capability.

## What to Build
Criticality as an observed property, scored continuously. Combine the signals the platform already has: number and breadth of users relative to the builder's own team, growth trajectory, dependency from other apps and systems, scheduled or deadline-bound execution, data volume and irreplaceability, external party access, and whether an automation takes an action in the world such as sending a customer email or writing to a system of record. Score every app on that basis and detect the crossing with change-point methods, since what matters is the transition rather than the level. Then respond proportionately at the moment it happens, which is the entire point: prompt the builder to document while they still remember, require a second owner, enable backup and export, and add the app to the continuity inventory — all of which are cheap at the crossing and expensive after the resignation. Join to the directory so a builder's departure notice produces the list of their apps ranked by criticality, with a handover plan, weeks before their last day rather than during it. And report the estate's criticality distribution to IT, which is the inventory conversation this category has never been able to have.

## Target Customer
IT and platform governance leadership at organisations with meaningful no-code adoption, operations leaders whose processes are running on these apps, and the platform vendors, for whom this is the maturity story enterprise buyers keep asking for.

## Impact If Built
The crossing happens to every successful app, is fully observable, and is measured by nobody. Detecting it converts the category's recurring crisis into a routine prompt at the moment when documentation and a second owner cost almost nothing.
