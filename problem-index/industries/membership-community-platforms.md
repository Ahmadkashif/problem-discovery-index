# Membership & Community Platforms

## Profile
**Category:** Digital Media & Creator Economy
**Market Size:** ~$6B US in paid community and membership subscriptions plus the software layer beneath them; the platform tier takes roughly $700M-1B in fees and subscriptions
**Tech Maturity:** Competent forums, no instrumentation of the thing being sold. Circle, Mighty Networks, Skool, Discourse, Bettermode and Discord provide posting, spaces, events, courses and payments. What every one of these businesses actually sells is belonging, and the analytics report daily active users and post counts — activity metrics that correlate weakly with whether anyone felt connected.
**Workforce:** Community managers, volunteer and paid moderators, membership and creator operators, platform engineers, trust and safety staff at the larger platforms

## Key Pain Themes
Paid communities live on recurring revenue, and churn in them is almost entirely silent. A member stops opening the app in week three, stays subscribed out of inertia, and cancels at renewal four months later. By the time the cancellation arrives the disengagement is a quarter old and unrecoverable. The signal that predicts it — whether the member's first post got a reply, whether anyone learned their name, whether they found a subgroup — is present in the data and reported nowhere.

The structural pathology is well known and unaddressed by tooling. A small minority of members produce most of the content; newcomers post once into a room that does not answer and never return; a handful of loud voices set a tone that quietly excludes; and the founder's own participation is the load-bearing element, which does not scale and cannot go on holiday.

The third theme is moderation economics. Communities small enough to be intimate are too small to fund trust and safety, so the work falls on the founder or on volunteers — people doing unpaid emotional labour with no tooling, no policy support and no escalation path, who burn out on a predictable cycle.

## Current Tech Landscape
Circle and Mighty Networks lead the paid creator-community tier; Skool grew fast on a simplified gamified model; Discourse remains the open-source standard for forums; Discord dominates free real-time community and is used commercially despite not being built for it. Patreon and Substack provide membership monetisation with lighter community layers. Bettermode and Khoros serve brand and enterprise communities. Moderation tooling is native and basic at the creator tier; enterprise-grade trust and safety vendors exist and are priced far above what a thousand-member community can pay.

## Problems
- [[problems/membership-community-platforms/high-impact|🔴 High Impact: Retention Depends on Belonging and the Platform Counts Posts]]
- [[problems/membership-community-platforms/low-impact-1|🟡 Low Impact: Onboarding and Member Matching]]
- [[problems/membership-community-platforms/low-impact-2|🟡 Low Impact: Moderation Tooling for Communities That Cannot Fund It]]
- [[problems/membership-community-platforms/worker-life-1|🟢 Worker Life: The Community Manager Who Is Also the Community]]
- [[problems/membership-community-platforms/worker-life-2|🟢 Worker Life: The Volunteer Moderator Absorbing the Worst of It]]
- [[problems/membership-community-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/membership-community-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
A community platform holds the complete interaction graph of a group of people who paid to be there: who replied to whom, who was ignored, who found a subgroup and who never did, and — on the other side — who renewed. That is an unusually clean dataset for a question these businesses cannot currently answer, which is what causes someone to stay. The structural failures are legible in the graph: a newcomer whose first post received no reply, a community whose reply structure is centralised on one person, a subgroup that has closed to outsiders. None of it is surfaced, because the category inherited its analytics from social media, where the objective was engagement volume rather than whether any individual person felt included.
