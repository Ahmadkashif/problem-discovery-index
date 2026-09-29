# AI Agents & Platform Opportunities — Work Collaboration Tools

**Industry:** [[work-collaboration-tools|Work Collaboration Tools]]

---

## 1. Observed Status Agent
#ai-agent #gradient-boosting #survival-analysis #large-language-models #confidence-intervals #evaluation-metrics #workflow-orchestration #worker-facing

**Concept:** An agent that computes project status from what happened rather than from what was typed. It watches activity across the connected estate — task comments, document edits, code reviews, threads — infers the true state of each work item, and surfaces the disagreements: marked in progress, no activity of any kind for eleven days. It forecasts completion from the team's measured cycle time rather than from estimates given in a planning meeting, and it assembles the status report in the several shapes stakeholders want from a single underlying assembly. It describes work items and dependencies and never individual activity levels, which is both the only acceptable framing and the more accurate one.

**Inputs:** Task metadata and status history; activity timestamps across integrated tools; linked artefact state; dependency graph; historical cycle times by work type and team.

**Outputs / Actions:** A disagreement list — declared status versus inferred, with the evidence. Stall alerts framed as dependency findings. Completion forecasts from measured throughput with intervals. Status reports generated in each stakeholder shape. Recurring bottleneck analysis showing where work stalls repeatedly across projects.

**Why now:** The behavioural record has existed for a decade and the data model was never revisited, because a status field is simple and auditable. Inference is now reliable enough to show alongside the declared status, which is the form that earns trust without demanding it.

**Market:** Work management platform vendors and enterprise PMOs. Project management capacity is spent on collection and reformatting, which is a capacity argument leadership grasps immediately — though the vendor conflict is real, since fewer status interactions looks worse on engagement metrics.

---

## 2. Work Graph Platform
#ai-platform #graph-neural-networks #bert #word-embeddings #evaluation-metrics #data-integration #workflow-orchestration #automation

**Concept:** A platform that resolves work across tools into single items and infers the dependency graph between them. It recognises that a ticket, a design frame, a pull request, a document and a thread are one piece of work, using titles, participants, timing, references and content. It then learns blocking relationships from observed waiting — this team's work consistently waits on that team's review — rather than requiring anyone to declare them, since declaring dependencies is unpaid work that never gets done. From the graph it computes cascade impact: when this slips, what else moves and by how much.

**Inputs:** Artefact metadata across the tool estate; explicit links as weak labels; activity sequences; team and ownership structures; historical slip events and their downstream effects.

**Outputs / Actions:** Canonical work items spanning tools. An inferred dependency graph with confidence per edge. Cascade impact analysis on any slip. Cross-team bottleneck reporting. Alerts when a dependency's upstream work has stalled, delivered to the downstream owner who currently finds out at the deadline.

**Why now:** Pairwise field-level integration was always the wrong architecture and persisted because each vendor wanted to be the centre. Resolution across heterogeneous systems is now straightforward, and explicit references provide abundant labels to bootstrap it.

**Market:** Enterprises running heterogeneous tool estates — which is all of them — and the iPaaS vendors as an adjacent move. Cross-team dependency failure is where organisational delivery actually breaks, and no product currently makes it visible.

---

## 3. Attention Budget Agent
#ai-agent #gradient-boosting #logistic-regression #bert #evaluation-metrics #worker-facing #automation #workflow-orchestration

**Concept:** An agent that sits above every work tool and decides what actually deserves an interruption. It predicts, per notification and per recipient, whether this warrants delivering now — from who sent it, what it concerns, whether the recipient is the only one who can act, whether anything is blocked on them, and what they are currently doing. Everything else batches into a small number of delivery points. Focus protection is real rather than a status light: the held set is genuinely held, and the sender sees it, so the availability expectation adjusts rather than persisting silently.

**Inputs:** Notification streams from every connected tool; recipient response history by sender, type and topic; blocking relationships from the work graph; calendar and current activity state; team norms and working hours.

**Outputs / Actions:** Immediate delivery for a deliberately narrow urgent set. Batched delivery for everything else. Real focus protection with sender-visible state. A weekly attention report per person showing continuous time recovered. An organisational view of which teams, meetings and processes generate the most interruption for others.

**Why now:** The training signal — what people actually act on versus dismiss — has been accumulating in every platform for years, and no single vendor will build this because it means treating their own notifications as part of a budget rather than a right. That is precisely what makes it a third-party or operating-system-layer opportunity.

**Market:** Enterprises directly, as a wellbeing and productivity purchase, and operating system or workspace vendors positioned above the individual tools. The interruption load is a collective action failure, and the buyer is the organisation that has noticed its people have no continuous hour in the day.
