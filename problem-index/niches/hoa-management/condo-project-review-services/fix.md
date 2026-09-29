# The Same Project Is Reviewed From Scratch Fifty Times a Year

**Niche:** [[niches/hoa-management/condo-project-review-services/profile|Condominium Project Review Services]]
**Industry:** [[industries/hoa-management|HOA Management]]
**Type:** Fix (Pain Point)
**One-liner:** A 300-unit tower generates dozens of reviews a year, each one starting from an empty screen.
**Tags:** #data-integration #workflow-orchestration #tacit-knowledge-ml #automation #worker-facing

## The Problem
Condominium sales cluster. A large project in an active market produces mortgage applications continuously, and each one requires a project review. The same association, the same budget, the same reserve study, the same questionnaire — reviewed again, by a different reviewer, from the beginning.

The reviewer who handled it in March worked out that this association's budget lists reserve contributions under an unusual heading, that its management company sends the wrong reserve study version unless asked specifically, and that the litigation disclosure refers to a matter resolved two years ago. In June, a different reviewer rediscovers all three, and spends the same forty minutes doing it.

Nothing carries forward except the determination and its expiry. The reasoning does not, the document quirks do not, and the open questions do not.

## Why It's Still Broken
The file is the unit of work, because the file is the unit of billing and the unit of the deadline. Every incentive in the operation points at closing the file in front of you, and none points at leaving something behind for the next person.

The systems reflect that. Review platforms are case management systems keyed to loans, with the project as an attribute of the case rather than an entity in its own right. There is nowhere to write a note about a project because the schema does not have a project to attach it to.

And there is a real compliance worry underneath, which is that carrying a prior determination forward could look like not doing the review. That is a legitimate concern about conclusions and a bad reason to discard context. Knowing where the reserve contribution is printed is not a conclusion.

## What a Fix Looks Like
Make the project a first-class record and let reviewers deposit into it.

**A project file that persists**, carrying every prior determination, the documents behind them, and the changes between them. When a reviewer opens a new case, they should see this project's history and what has moved since the last review — which is also the substance of the current review, so the framing does the work.

**Reviewer notes attached to the project**, typed and dated: document quirks, contacts who respond, questions raised and how they resolved. This is the tacit knowledge Pass 1 identifies throughout HOA management — knowing which management companies produce reliable documents, which boards disclose fully — and it currently exists only as individual reviewers' memory.

**A change-driven review.** Present the delta explicitly: reserve contribution down 12%, insurance deductible doubled, new special assessment disclosed. The determination is still made fresh against the criteria, and the reviewer is looking at exactly what should drive it.

**Open items that survive.** A question a reviewer raised and could not resolve should be waiting for the next reviewer, not lost when the file closes.

None of this pre-decides anything. It gives the reviewer the context the firm already paid to acquire and currently throws away fifty times a year on the same building.

## Who Feels the Pain
Reviewers, repeating work under a closing deadline and unable to benefit from a colleague's identical effort three months earlier. Operations leaders, who see the throughput cost and cannot locate it in any single file. And lenders, who receive determinations of uneven quality on the same project depending on who happened to pick it up.

## Impact If Fixed
Repeat reviews of an established project should take a fraction of a first review, and today they take nearly the same. In an operation where reviewer hours are the cost structure and turnaround is the product, that is the single largest efficiency available — and it produces, as a by-product, the longitudinal project record that makes everything else in this niche possible.
