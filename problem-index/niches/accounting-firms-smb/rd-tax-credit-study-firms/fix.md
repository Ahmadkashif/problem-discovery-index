# Audit Outcome Feedback Never Reaches the Study Writers

**Niche:** [[niches/accounting-firms-smb/rd-tax-credit-study-firms/profile|R&D Tax Credit Study Firms]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Studies are examined two to four years after they are written, by a different team, and the outcome is almost never routed back to the people who wrote them — so the same weak framings get reused indefinitely.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #evaluation-metrics #cross-validation #data-integration #compliance #worker-facing

## The Problem
An R&D credit study written this year may be examined three years from now. By then the specialist who wrote it may have moved teams or left, the engagement is closed in the practice management system, and examination defense is handled by a separate controversy group. The information that matters most to the firm — which narrative framings drew scrutiny, which cost allocation methods were adjusted, which industries attract examination — is generated in the controversy group and dies there. Study writers therefore operate without a feedback signal on the only quality metric that counts. A framing that has been challenged four times keeps getting used because nobody who uses it has been told.

## Why It's Still Broken
The break is structural rather than technical. Study production and examination defense sit in different parts of the org with different systems, different economics, and a multi-year lag between them. Practice management systems close an engagement when the study is delivered and the fee is collected; there is no open record for the outcome to attach to years later. The controversy group documents its work in matter files organized around the examination, not around the study that triggered it, so even when a firm wants to connect the two, the join does not exist — reconstructing it means matching client, tax year, and credit position by hand across two systems that share no key.

## What a Fix Looks Like
A closed-loop layer that gives every study a durable identity persisting past engagement close, and that captures examination outcomes against it at whatever granularity the controversy group can supply: which projects were challenged, on which of the four elements, what the adjustment was, how it resolved. That record then becomes the training signal for two things the firm currently cannot do. First, retrospective analysis — which framings, industries, and allocation methods correlate with adjustment, surfaced as guidance rather than folklore. Second, prospective scoring — a new study receives a risk assessment before delivery, flagging positions that resemble ones the firm has seen challenged, so review effort concentrates where the exposure actually is. The system does not make the technical call; it makes the firm's own examination history visible to the person making it.

## Who Feels the Pain
Study writers who cannot improve because they never learn how their work performed; the controversy group that defends the same weak positions repeatedly and cannot get the message upstream; and the national technical director accountable for firm-wide quality with no data beyond anecdote.

## Impact If Fixed
Converts examination history from a cost center into the firm's most valuable proprietary dataset. Study quality becomes measurable against the outcome that matters rather than against internal review checklists. Over a few examination cycles the firm develops a defensible, evidence-backed view of its own risk profile — which is directly sellable to clients weighing an aggressive position, and which no competitor can assemble without the same closed loop.
