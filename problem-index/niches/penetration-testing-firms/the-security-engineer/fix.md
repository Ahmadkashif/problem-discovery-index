# Fix: Eighty Findings and One Person

**Niche:** The Security Engineer Receiving the Report
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The engagement ends when the report is delivered, and the hardest part of the work — getting other teams to fix things — starts there and belongs to someone who was not part of the engagement.
**Tags:** #evaluation-metrics #confidence-intervals #worker-facing #workflow-orchestration #compliance #revenue-impact
**Contested on:** Whether severity reflects what a finding means in this organisation's architecture, or a rating assigned by someone who has never seen it.

## The Problem

The report is delivered on a Thursday. The firm presents it, answers questions, and moves to the next engagement. The engagement is complete.

For the client's security engineer it has just started. Eighty findings have to be read, understood, re-prioritised against architecture the report's author never saw, converted into tickets in four teams' different formats, explained to developers who have never read a penetration test and are mid-sprint on something else, negotiated into roadmaps owned by managers who did not commission the test and have no accountability for its findings, and then chased for four months.

They have no authority over any of those teams. Their leverage is persuasion, the implied weight of a compliance deadline, and escalation they can use perhaps twice a year before it stops working. The test they commissioned to improve security produces a document and a political project.

And the difficulty is invisible to everyone. The firm delivered a good report. The security leader has evidence testing was performed. The engineering teams have a list of things somebody wants. The person in the middle turns a deliverable into an outcome by force of will, and every year the report arrives again.

## Why It's Still Broken

**The engagement is scoped to delivery.** Firms sell testing and write reports. Remediation support is occasionally offered, rarely bought, and sits outside the model — which is how the profession has always been structured.

**Severities are assigned without context and used as authority.** A development manager sees "high" and either drops everything or, more often, learns after a few cycles that the ratings do not reliably correspond to real risk in their environment and starts discounting all of them. Miscalibrated severity destroys the credibility of the whole document.

**The findings are written for the wrong reader.** A tester writes for a security audience. The person who must implement the fix is a developer who needs the specific change in their code, not a description of the attack.

**Security has responsibility without authority.** This is the structural core of it. The engineer owns the outcome and commands none of the resources, which is a position no amount of tooling fully resolves.

**Nobody measures the remediation burden.** The cost of turning a report into fixes is not tracked anywhere, so it is not resourced, so it lands on one person's discretionary effort.

**The report arrives as a batch.** Eighty findings at once is a demand shock against teams with committed sprints. The same eighty delivered progressively over the engagement would have been absorbable.

## What a Fix Looks Like

**Deliver findings progressively, not in a batch.** High-severity issues on the day they are found, the rest as they are confirmed. Teams can absorb a trickle and cannot absorb a flood, and this costs the firm nothing.

**Require the firm to state severity assumptions.** Each finding's rating with the assumptions behind it — assumed exposure, assumed data sensitivity, assumed absence of compensating controls — so the engineer can adjust with one look instead of re-deriving the whole assessment. A tester can write this in a line and almost none are asked to.

**Ask for a developer-facing remediation section.** Written for the engineer who will make the change: the specific fix, in the relevant framework, with the code-level guidance. Firms can produce this and are rarely asked, and it removes the largest translation burden on the receiving side.

**Cluster before delivery.** The firm should group the eleven instances of one class into a single systemic finding with instances listed. They see the pattern clearly and currently report it as eleven items because the template is a list.

**Buy the triage session.** A half-day with the tester and the security engineer together, after delivery, going through the findings with the client's architecture on the table. Cheap, enormously effective, and it is the one thing that transfers the tester's reasoning into the context where it will be used. Firms should sell it by default rather than on request.

**Resource the remediation work explicitly.** The organisation commissioning a test should budget the engineering time to act on it, at the same moment. Buying the finding without funding the fixing is the most common and least examined failure in this cycle.

**Give the engineer a mandate.** A pre-agreed commitment from engineering leadership that findings above an agreed threshold get scheduled, so the engineer is administering a policy rather than negotiating eighty times.

## Who Feels the Pain

The security engineer, almost entirely — holding the outcome, commanding nothing, and spending months on political work that is nobody's idea of the job.

The developers, handed security tickets written for someone else, arriving in a batch, cutting across a sprint they had already committed.

The organisation, which pays for a good test and captures a fraction of its value because the last mile is unfunded and unowned.

And the testing firm, whose careful work produces less improvement than it should, which they never learn because nothing reports back.

## Impact If Fixed

Progressive delivery and pre-delivery clustering cost the firm nothing and transform what arrives on the receiving side — a trickle of grouped systemic issues is a manageable programme where a batch of eighty items is a crisis.

A half-day triage session with the tester present is the highest-return hour in the entire cycle, and it is currently an upsell rather than a default.

And funding the remediation at the same time as the test is the single decision that determines whether a penetration test changes anything, which makes its routine omission the largest waste in this industry.
