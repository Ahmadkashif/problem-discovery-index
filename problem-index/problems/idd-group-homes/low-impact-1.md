# Shift Notes That Prove the Daily Residential Rate

**Industry:** [[idd-group-homes|IDD Group Homes]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every billed day of residential habilitation must be backed by notes showing the supports in the person's individual service plan were delivered, and generic note tools and AI scribes do not know what an IDD auditor looks for.
**Tags:** #large-language-models #transformers #bert #evaluation-metrics #compliance #revenue-impact #automation

## The Problem
Medicaid pays a group home a daily residential habilitation rate for each resident, tiered by assessed support needs. The rate is earned only if the day's documentation shows that the resident was present and that staff delivered the habilitation supports written into the person-centred individual service plan (ISP). That means progress on the person's own outcomes, such as cooking a simple meal, using the bus, or managing money, in the state's required format. State reviewers and Medicaid Fraud Control Units audit samples of days. A note that says "Jamie had a good day, ate lunch, watched TV" supports nothing, and the day can be recouped, with extrapolation across the sample in some states (estimate).

So DSPs spend the last part of every shift writing notes against outcomes they may not know well, often in a second language, after a double shift. House managers then chase missing notes before billing closes. Kibu says its customers have cut weekly documentation time from about 200 hours to about 20, a vendor claim (Hartford Business Journal via search summary). Whatever the true number, the burden is large.

## What Already Exists
IDD record systems (Therap, MediSked, SETWorks, iCareManager, Kibu, Netsmart myEvolv) provide note templates linked to ISP goals, attendance tracking and claim generation. General-purpose AI scribes, built for clinicians, turn a conversation into a SOAP note. Revenue-cycle claim scrubbers check codes and units against payer edits.

## The Customisation Gap
What an IDD auditor checks is not what a clinical scribe produces. The note must name the specific ISP outcome and the support strategy used, describe the person's response in observable terms, and reflect the person's own preferences in person-centred language. It must also match the attendance record, including the state's rule for counting a day when the resident spends a night at the family home or in hospital (rules vary by state, estimate). The vocabulary is state-specific (habilitation, community integration, supports versus services) and so are the formats: Pennsylvania, New York and Ohio each define their own documentation standard. A useful tool would draft the note from the DSP's spoken account mapped to the ISP outcomes. It would flag days whose notes would fail the state's standard before the claim goes out, and show the house manager which outcomes have gone undocumented for a month. Claim scrubbers miss all of this because the claim itself is valid; it is the note behind it that fails.

## Impact If Solved
A 40-home agency billing ~200 resident-days a night (~73,000 a year, estimate) that cut audit-failed days by even half a percentage point would protect hundreds of billed days a year from recoupment (estimate). Each DSP would get back twenty to thirty minutes at the end of every shift (estimate), and the person's plan would be read daily rather than once a year.
