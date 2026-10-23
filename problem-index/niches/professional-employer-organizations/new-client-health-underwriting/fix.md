# Health Questionnaires Rekeyed From Scans

**Niche:** [[niches/professional-employer-organizations/new-client-health-underwriting/profile|New-Client Health Underwriting]]
**Industry:** [[industries/professional-employer-organizations|Professional Employer Organizations]]
**Type:** Fix (Pain Point)
**One-liner:** Prospects' health questionnaires arrive as scanned PDFs and phone photos, and underwriters retype conditions and prescriptions one form at a time during the busiest weeks of the year.
**Tags:** #large-language-models #transformers #evaluation-metrics #compliance #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to decide, from a census, a few health questionnaires and a prescription-history score, which 25-person prospects to admit to the master plan and at what rate before the broker's quote deadline, and whoever's admitted groups run closest to their priced loss ratio in the first plan year takes the account.

## The Problem
Personal and group health questionnaires carry the signals underwriters weigh most: named conditions, current specialty drugs, pending procedures, pregnancies. For a 30-person group that can mean thirty handwritten forms. Underwriters or assistants key them into the rating file, misreading drug names and missing answers, while the broker waits for a quote.

## Why It's Still Broken
The forms differ by carrier and PEO. They contain protected health information that cannot go to a generic extraction service without a business associate agreement. And quote volume is seasonal, so the PEO staffs for average weeks and drowns in Q4.

## What a Fix Looks Like
HIPAA-covered document extraction that reads each questionnaire into structured fields, normalises drug names to a formulary with cost tiers, flags missing or inconsistent answers for the broker to resolve, and summarises the group's high-cost signals on one page for the underwriter.

## Who Feels the Pain
New-business underwriters and assistants in Q4, brokers waiting on quotes, and prospects asked to resubmit forms.

## Impact If Fixed
Hours removed from every quote at the peak of the season, fewer missed high-cost drugs, and faster quotes to brokers.
