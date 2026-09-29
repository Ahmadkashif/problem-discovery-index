# Fix: The Items Are on a Public Forum and Nobody Is Reading It

**Niche:** [[niches/talent-assessment-platforms/item-security/profile|Item Security & Content Leakage]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Candidates post the questions and the answers on public sites within days, and the vendor finds out when someone mentions it.
**Tags:** #descriptive-statistics #large-language-models #evaluation-metrics #change-point-detection #confidence-intervals #workflow-orchestration #quick-win #automation
**Contested on:** Whether anyone will read the public channels where the content already is.

## The Problem

Assessment items circulate in public. Career forums have threads for specific employers' assessments. Coaching sites sell practice sets that are, in substance, the live items. Video platforms carry walkthroughs recorded during actual administrations. Shared documents accumulate items across hiring seasons.

None of this is hidden. It is indexed, searchable and frequently the first result for an employer's name plus "assessment". Candidates find it easily, which is why it exists.

Vendors find out anecdotally. A content developer stumbles across a thread, or a client mentions that their candidates seem unusually well prepared, and someone investigates. There is no monitoring, so exposure is discovered late and unevenly, and the instrument keeps running in the meantime.

## Why It's Still Broken

Nobody owns it. Content development owns creating items, legal owns enforcement, and monitoring the channels falls between them.

There is also a fatalism about it: leakage is understood to be inevitable, which is true, and has been taken to mean that measuring it is pointless, which does not follow. Knowing which items are exposed and how fast determines the rotation schedule, and rotating blind is far more expensive than rotating on evidence.

And the discovery is unwelcome — a vendor who monitored properly would know their pool is substantially compromised and would have to tell clients or act.

## What a Fix Looks Like

Read the channels. They are public.

Search systematically for content matching the item pool — semantically rather than by exact string, since leaked items are paraphrased and transcribed. Forums, coaching sites, question banks, video transcripts and document-sharing platforms. This is a retrieval task over public content and it can run continuously.

Score exposure per item. Where it appears, how prominently, how long it has been there, how many people are likely to have seen it. An item on page one of a search for the employer's assessment is compromised; one in an obscure thread is not, and treating them identically wastes rotation budget.

Watch the statistics alongside. An item whose difficulty drops sharply is exposed whether or not you found where. The two channels together are far stronger than either.

Retire on evidence rather than on schedule. Rotation budgets are limited, and spending them on the items that are actually compromised rather than on a calendar is the difference between an affordable programme and an unaffordable one.

Tell clients what proportion of their instrument is exposed. A client deciding whether to trust a score is entitled to know, and a vendor who reports it is in a much better position than one who is found out.

And use the channels as a design signal. What candidates post about tells you which items are memorable, which are ambiguous, and which are widely considered unfair — free feedback on the instrument from the people taking it, which no vendor currently reads.

## Who Feels the Pain

Employers relying on a score whose instrument is partly compromised without knowing it. Candidates who do not find the forums and are competing against those who did — a disparity that correlates with networks and resources rather than with ability. Content teams, whose expensive work is devalued invisibly. And the vendors, whose validity claims quietly stop applying.

## Impact If Fixed

Exposure gets measured from channels that are already public, which is the cheapest possible detection. Rotation budget goes to the items that are actually compromised. Clients find out how much of their instrument still measures what it claims. And the candidate discussion becomes a free source of feedback on item quality.
