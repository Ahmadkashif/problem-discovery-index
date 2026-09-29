# Machine Learning Opportunities — Work Collaboration Tools

**Industry:** [[work-collaboration-tools|Work Collaboration Tools]]
**Derived from:** [[problems/work-collaboration-tools/high-impact|High Impact]], [[problems/work-collaboration-tools/low-impact-1|Low Impact 1]], [[problems/work-collaboration-tools/low-impact-2|Low Impact 2]], [[problems/work-collaboration-tools/worker-life-1|Worker Life 1]], [[problems/work-collaboration-tools/worker-life-2|Worker Life 2]]

---

## 1. Work State Inference from Activity
#gradient-boosting #survival-analysis #bert #large-language-models #time-series-forecasting #confidence-intervals #feature-engineering #evaluation-metrics

**Problem statement:** A task's status is what someone last typed, usually under social pressure before a status meeting. The behavioural record that would reveal true state — comment recency, linked document edits, open unreviewed pull requests, reassignment history, silent re-scoping — is captured by the same platforms and never used to compute status.

**ML task:** Classification of true work state from activity signals, plus survival modelling of time-to-completion conditional on current state
**Input data:** Task metadata and status change history; comment and activity timestamps; linked artefact activity from integrated tools (commits, reviews, document edits); assignee's activity distribution across their other work; re-scoping and reassignment events; historical completed tasks with their full activity traces.
**Target:** Whether the task was genuinely progressing at a point in time, derived retrospectively from what subsequently happened — a task that completed shortly after was progressing; one that sat for a month was not.
**Evaluation metric:** The operational metric is disagreement precision: of tasks the model flags as stalled while marked in progress, what proportion were genuinely stuck as judged by the team. Report lead time before the stall became visible through conventional means. Aggregate accuracy is uninformative because most tasks are unambiguous.
**Scope:** The ethical boundary is the design constraint and must be architectural: outputs describe work items and dependencies, never individual activity levels. This is both the only version teams will accept and the more accurate one, since most stalls are dependency problems. Cross-tool activity is essential and requires the work-item resolution layer as a prerequisite. 3 ML engineers plus a product manager with delivery experience, 6 months.
**Data availability:** Task and activity data is complete within each platform and fragmented across the estate. Retrospective labelling from outcomes is clean and requires no annotation.

---

## 2. Cross-Tool Work Item Resolution and Dependency Inference
#graph-neural-networks #bert #word-embeddings #k-nearest-neighbors #feature-engineering #evaluation-metrics #data-integration

**Problem statement:** A piece of work exists simultaneously as a task, a design, tickets, code, a document and a thread, and nothing establishes that these artefacts are the same work. Integrations are pairwise and field-level, so a company with nine tools has thirty-six brittle links and still cannot see what blocks what.

**ML task:** Entity resolution across heterogeneous systems into work items, followed by dependency inference from observed waiting patterns
**Input data:** Artefact metadata across tools — titles, participants, timestamps, explicit references, content; explicit links where they exist as labels; historical sequences of activity across artefacts; team and ownership structures.
**Target:** Canonical work item identity across artefacts; and directed dependency edges between work items.
**Evaluation metric:** For resolution, pairwise precision and recall against explicitly linked pairs held out, with precision weighted higher since a false link creates a spurious dependency that misleads a plan. For dependency inference, whether predicted blocking relationships correctly anticipate observed waiting, evaluated forward in time rather than retrospectively.
**Scope:** Explicit references (a commit message citing a ticket) provide abundant weak labels to bootstrap. Dependency inference from behaviour is the genuinely new capability — declared dependencies are always incomplete because declaring them is unpaid work — and learning that this team's work consistently waits on that team's review is an organisational finding no company currently has. 3 ML engineers, 6-8 months.
**Data availability:** Rich within any single vendor's estate and requires customer-authorised access across estates, which is the commercial obstacle rather than the technical one.

---

## 3. Template Induction from Successful Projects
#bert #word-embeddings #k-means-clustering #dbscan #large-language-models #evaluation-metrics #hypothesis-testing #transfer-learning

**Problem statement:** Template galleries are authored top-down and describe a generic process, so teams abandon them within a month and every project ends up a different shape — which is why portfolio reporting in these platforms does not work. The template that would have fitted is the team's own best previous project.

**ML task:** Clustering completed projects by structural shape, extracting recurring phase and task patterns, and associating structural choices with delivery outcomes
**Input data:** Completed projects with task structures, phases, dependencies, role assignments and durations; outcome measures (on-time completion, scope change, reopen rate); team and project type; template usage and abandonment events.
**Target:** A proposed project structure for a given team and work type; and the association between structural features and outcomes.
**Evaluation metric:** Template retention — whether a team is still using the proposed structure at project end, which is the honest measure and the one existing galleries fail. For the outcome association, effect sizes with intervals rather than significance claims, since observational structure-outcome relationships are heavily confounded by project difficulty.
**Scope:** The outcome linkage is where this becomes evidence rather than convenience, and it is also where the confounding is severe — well-run teams both use more structure and deliver on time. Cross-customer analysis makes the association estimable where a single company's project count does not. Structural drift detection, noticing that a team abandoned the structure mid-project, needs no modelling and is a strong signal the structure was wrong. 2 ML engineers, 5 months.
**Data availability:** Every platform holds a decade of completed projects. Outcome measures are weak — most platforms do not record whether a project was considered successful — so proxies like schedule adherence must carry the analysis.

---

## 4. Notification Importance Prediction
#gradient-boosting #logistic-regression #bert #time-series-forecasting #feature-engineering #cross-validation #evaluation-metrics #worker-facing

**Problem statement:** Each tool tunes notifications to maximise engagement with itself, nobody owns the aggregate, and the worker experiences an interruption load that grew without a decision. Per-tool settings force a binary between too much and missing something, and the common resolution — turning most off and checking periodically — converts interruption into anxiety.

**ML task:** Per-recipient binary classification of whether a notification warrants immediate delivery, with a batching policy over the remainder
**Input data:** Notification events with source, type, sender, subject and referenced work item; recipient's subsequent behaviour (opened, acted on, ignored, dismissed, and latency); whether the recipient is the sole actionable party; whether anything is blocked pending their response; recipient's current calendar and activity state; historical response patterns by sender and topic.
**Target:** Whether the recipient acted on the notification promptly, treating action rather than opening as the signal.
**Evaluation metric:** Recall on genuinely urgent items must be very high, since a missed blocking request is the failure that ends adoption. Report the interruption reduction achieved at fixed recall — the honest framing is how many fewer interruptions for the same responsiveness. Continuous time recovered per day is the outcome measure that matters to the user.
**Scope:** The business model conflict is the real obstacle: a vendor measured on engagement is being asked to reduce interactions with its own product. Cross-tool aggregation is where the value is and no single vendor will build it, which makes this a natural third-party or platform-level product. The organisational view — which teams and processes generate the most interruption for others — is a straightforward aggregation and a genuine management finding. 2 ML engineers, 4-5 months.
**Data availability:** Notification and response data is complete within each platform. Cross-tool aggregation requires either an operating system layer or explicit user-authorised access to multiple estates.
