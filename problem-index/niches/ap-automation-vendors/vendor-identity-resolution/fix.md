# Searched, Not Found, Created Again

**Niche:** [[niches/ap-automation-vendors/vendor-identity-resolution/profile|Vendor Identity Resolution]]
**Industry:** [[industries/ap-automation-vendors|AP Automation Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The supplier is already in the system under a name the person searching would never guess, so they create a new record.
**Tags:** #quick-win #automation #data-integration #evaluation-metrics #worker-facing #word-embeddings #descriptive-statistics #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to determine which records refer to the same supplier across a decade of duplicates, abbreviations, mergers and typos — and whoever resolves most accurately using what every other buyer knows owns the record everything else depends on.

## The Problem
Someone needs to pay a supplier. They search the vendor master for the name on the invoice. The supplier is there, recorded under a parent company name, an old trading name, or with a leading article that puts it elsewhere alphabetically. The search returns nothing. They create a new record, and the master file gains its fifth version of the same company. The search box is the exact point where the duplicate problem is created, and it does exact and prefix matching.

## Why It's Still Broken
The search was built as a database lookup, so it does what a lookup does — an interface that returns what was typed is working correctly by its own definition, and nobody framed the miss as the cause of the duplicates. Creation is quicker than investigating. The consequence appears months later as an exception. And nobody instruments the search-then-create sequence.

## What a Fix Looks Like
Make the search find things and make creation harder. Implement fuzzy search across names, former names, tax identifiers and bank details, which is the fix and addresses the problem exactly where it originates. Search invoice history as well as the master file, since the supplier may be recognisable from a past invoice under another name. Check the proposed new record against likely matches at creation and show them, because that is the last moment before a duplicate exists. Require a confirmation that no match applies rather than allowing silent creation, as a single click of friction at the right moment prevents most of it. Offer cross-customer matches where the network recognises the supplier, which will catch the cases a single file cannot. Instrument how often a create follows a failed search, since that sequence is the duplicate rate's leading indicator and is not measured. Surface the record's full alias list so searchers see what a supplier is also known as. Let users add an alias in one action, which captures knowledge that currently stays in their head. Handle leading articles, punctuation and legal suffixes properly, as they are responsible for a surprising share of misses. And review new records created in the first weeks after the change, to confirm the fix worked.

## Who Feels the Pain
AP staff creating duplicates in good faith; procurement with split spend; clerks resolving the resulting exceptions; and everyone who eventually has to clean it up.

## Impact If Fixed
A search that returns what was typed is working correctly by its own definition, so nobody framed the miss as the cause of the duplicates. Fuzzy search plus a match check at creation closes the exact point where the problem is born.
