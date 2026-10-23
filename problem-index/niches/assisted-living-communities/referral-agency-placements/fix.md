# The Fee Paid Twice for One Family

**Niche:** [[niches/assisted-living-communities/referral-agency-placements/profile|Referral Agency Placements & Fee Disputes]]
**Industry:** [[industries/assisted-living-communities|Assisted Living Communities]]
**Type:** Fix (Pain Point)
**One-liner:** Two agencies give the same family the same community's name, both invoice, and the business office finds out when the second invoice arrives.
**Tags:** #large-language-models #feature-engineering #data-integration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to decide which move-ins a referral agency is owed a fee for, and whoever holds the timestamped first-contact record that both the community and the agency accept takes the account.

## The Problem
Families talk to several agencies and placement agents. Each sends the community a lead with slightly different names and numbers. The CRM creates two records, and after move-in both agencies claim a fee.

## Why It's Still Broken
Lead notifications arrive by email and portal in different formats, and nobody matches them to existing households in real time. Business offices pay invoices from accounts-payable queues, not the CRM.

## What a Fix Looks Like
Every incoming agency notification is parsed and matched to existing households on arrival. The counselor sees "already referred by Agency A on 3 March" at once and records the source at the first call. Invoices are matched against the record before payment, with the evidence attached to any dispute.

## Who Feels the Pain
Business office managers, sales directors defending their numbers, and agencies paid late because of disputes.

## Impact If Fixed
Avoiding one double-paid fee every year or two per community (estimate) saves ~$3,000–6,000 a year per community at ~$6,000 a fee, or ~$90,000–180,000 a year at a 30-community chain, the same order as the first-contact ledger in the build note.
