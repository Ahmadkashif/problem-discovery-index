# Network Analysis Applied to Who Unblocks Whom

**Niche:** [[niches/work-collaboration-tools/invisible-contribution-work/profile|Invisible Contribution Work]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Organisational network analysis has decades of method for identifying who connects, brokers and enables in an organisation, and it is used in occasional consulting surveys while the interaction data sits unused in the collaboration tools.
**Tags:** #graph-theory #spectral-graph-theory #graph-neural-networks #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance
**Contested on:** Every serious competitor that takes this seriously is fighting to make the work that produces no ticket — reviewing, unblocking, mentoring, responding, coordinating — visible in whatever the organisation uses to judge contribution, and whoever does it changes who gets promoted.

## The Problem
An organisation wants to know who its key connectors are — the people whose absence would slow everyone else down, who bridge between teams, who are load-bearing in ways the org chart does not show. It commissions a survey, receives a snapshot months later, and files it. Organisational network analysis has a substantial academic and consulting literature answering exactly this, and the interaction data that would support it continuously — who asks whom, who answers, who is copied, who reviews whose work — is recorded in the collaboration estate.

## What Already Exists
Organisational network analysis is a developed field with established measures — centrality, brokerage, bridging, reciprocity — and a long practitioner literature. Graph analysis libraries are free and mature. Collaboration platforms expose interaction metadata through their APIs. The methods have been validated against survey-based approaches. Everything required exists; what has limited its use is that the data is sensitive and the analysis has mostly been sold as consulting.

## The Customization Gap
The adaptation is to a continuous, consented, contribution-focused use rather than a one-off diagnostic. It requires: (1) edges that mean something specific — a question answered, a review completed, a blocker resolved — rather than generic interaction volume, since undifferentiated message counts measure sociability rather than contribution; (2) direction and outcome, because the useful asymmetry is who resolves things for whom and a symmetric interaction graph loses exactly that; (3) an explicit and narrow purpose with the analysis restricted to it, since the same graph supports contribution recognition and supports mapping who talks to whom for entirely different reasons, and an organisation that is not clear about which one it is doing will be assumed to be doing the second; (4) individual consent and access — the person should see their own position and the analysis should not be run about people who cannot see it, which is the condition that makes this acceptable; and (5) aggregation for anything reported upward, with individual-level output going to the individual rather than to management, which is the same design principle as the people analytics niche in HR technology and for the same reasons.

## Target Customer
Engineering and operations leadership, talent and organisational development functions, and the collaboration vendors who hold the interaction data and have not built on it for this purpose.

## Impact If Solved
Network analysis identifies the load-bearing people an org chart cannot show, which matters for recognition, for succession and for understanding what happens when someone leaves. The methods are mature and the constraint is entirely about consent and purpose, which means the design decisions determine whether this is a contribution-recognition tool or a surveillance one — and that choice is the product.
