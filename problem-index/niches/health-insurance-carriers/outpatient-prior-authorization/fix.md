# The Missing Note That Restarts the Clock

**Niche:** [[niches/health-insurance-carriers/outpatient-prior-authorization/profile|Outpatient Prior Authorization & Gold-Carding]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** A large share of outpatient requests arrive without the one document the criterion needs, and the request pends while the plan and the office fax each other.
**Tags:** #large-language-models #transformers #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn an outpatient authorization request into a determination inside the 72-hour and seven-day clocks without a fax or a phone call, and whoever auto-approves the largest share of requests a nurse would have approved, with no rise in overturned denials or later-audited approvals, takes the account.

## The Problem
An MRI request arrives without the note showing six weeks of failed conservative treatment, so the nurse pends it and sends a request for information. The office replies days later with a different note, and the cycle repeats. Under the seven-day standard clock, pended requests become denials for insufficient documentation that are later overturned when the right note arrives.

## Why It's Still Broken
Offices do not know which document each plan's criterion needs, and plans tell them only after submission. Portals accept any attachment. Requests-for-information letters are generic, and nobody measures which criteria generate the most pends.

## What a Fix Looks Like
Check completeness at submission. The portal or API reads the attachments against the criterion and, before the request is accepted, tells the office in plain language which specific element is missing. Plans publish the documentation checklist per service. Pends are tracked by criterion and provider, so the worst offenders get targeted education.

## Who Feels the Pain
Office staff resubmitting; UM nurses writing requests for information; members waiting on imaging or surgery; plans issuing denials that reverse.

## Impact If Fixed
Fewer pends, fewer documentation denials and fewer appeals, with decision times measured from a complete request.
