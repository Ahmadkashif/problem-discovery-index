# We Were Unable to Verify Your Identity

**Niche:** [[niches/identity-verification-vendors/failed-applicant-remediation/profile|Failed-Applicant Remediation]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The message says nothing, offers nothing, and is the end of the person's relationship with the institution.
**Tags:** #worker-facing #quick-win #compliance #automation #evaluation-metrics #workflow-orchestration #descriptive-statistics #large-language-models
**Contested on:** Every serious competitor in this niche is fighting to give a person who could not be verified a documented route to prove who they are — and whoever builds that route stops the category's silent failure from being permanent.

## The Problem
The applicant did everything asked. The screen says their identity could not be verified. It does not say which check failed, whether trying a different document would help, whether a person could look at it, or who to contact. Most people conclude they have been accused of something, feel humiliated, and never return. The institution records an abandoned application. The vendor records a failed verification. Nobody records that a real person was wrongly turned away.

## Why It's Still Broken
The message was written to avoid giving information to an impostor, so it gives information to nobody — a single message serving both a genuine applicant and a fraudster is optimised for the fraudster. Nobody owns the applicant experience, since the vendor serves the institution and the institution outsourced the step. Abandonment is not attributed to the message. And no one has tested it with real people.

## What a Fix Looks Like
Say something useful and offer a next step. Indicate the failure category in terms the person can act on — the document could not be read, the photo did not match, the details could not be confirmed — which is the fix and is safe to disclose at that level. Offer a concrete next action: retry with better capture, try a different document, contact support, or provide other evidence. Provide a contact route that reaches someone who can actually decide, since the absence of one is the core grievance. Avoid language implying wrongdoing, because the accusation is what makes people leave permanently. Preserve the application so a retry is not a restart. Test the message and the flow with real users, as this is a communication problem nobody has treated as one. Report abandonment at the failure screen, which is directly observable and currently unreported. Distinguish a hard decline from an incomplete verification, since they are very different and look identical. Let the institution customise the message, because they hold the relationship and know their applicants. And measure how many people who saw this message returned, as that number is the cost of the current wording.

## Who Feels the Pain
People wrongly turned away and left feeling accused; institutions losing customers they wanted; support teams contacted by people with nowhere else to go; and the populations most likely to fail automated checks, disproportionately.

## Impact If Fixed
A single message serving both a genuine applicant and a fraudster is optimised for the fraudster, so it tells honest people nothing. Naming the failure category and offering a next step is copy and routing, and it is the difference between a retry and a permanent exclusion.
