# Entry Summary Completion Checklist and Missing Data Detection

**Industry:** [[customs-brokers|Customs Brokers]]
**Type:** Worker Life Changing
**One-liner:** Customs entry preparers who submit entries to ACE with incomplete or inconsistent data — triggering CBP holds and rejection notices that delay cargo release — get a pre-submission completeness check that catches missing fields and data inconsistencies before the entry is filed.
**Tags:** #llm #compliance #automation #worker-facing

## The Problem

CBP entry rejections from incomplete or inconsistent data are among the most common and preventable delays in customs clearance. Common causes: missing country-of-origin certificate, invoice value not matching the entry value, HTS quantity-unit-of-measure mismatch, missing FDA prior notice for food imports, incomplete party data. Each rejection delays cargo release by 24-48 hours, generating additional demurrage and detention charges for the importer.

An experienced customs entry preparer does a mental completeness check before filing — knowing from experience which data combinations trigger rejections for specific commodity types. Junior preparers miss the less obvious requirements (FDA prior notice requirement for entries with HTS codes in Chapters 2-21, for example).

## Why It Matters to the Worker

A CBP rejection is immediately stressful — the broker must notify the importer of the delay, diagnose the missing data, obtain it from the shipper, and refile. This takes 2-4 hours on a good day and can extend to multiple days if the missing documentation requires the foreign exporter's involvement. Catching the deficiency before filing costs 5 minutes; catching it after filing costs 2-4+ hours.

## What a Solution Looks Like

A pre-submission checklist in the broker's ACE workflow: when the entry preparer marks the entry ready to file, the system runs a completeness check based on the entry's commodity type, country of origin, and import party configuration. It flags: missing required documents (FDA prior notice for Chapter 2-21 HTS, fish and wildlife certificate for regulated species, USDA phytosanitary certificate for plants), data inconsistencies (invoice value vs. entry value discrepancy > 5%), and commodity-specific requirements (ADD/CVD (antidumping/countervailing duty) case numbers if the HTS/country combination is subject to an order).

## Impact If Solved

Reduces entry rejection rate. Each avoided rejection saves 2-4 hours of remediation time and avoids $200-$500 in demurrage per day of delay. A broker filing 1,000 entries per month with a 2% rejection rate that's reduced to 0.5% saves 15 hours and $3,000-$7,500 per month.
