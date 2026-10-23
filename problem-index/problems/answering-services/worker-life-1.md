# The Death Call, Then the Next Caller in Queue

**Industry:** [[answering-services|Telephone Answering Services]]
**Type:** Worker Life Changing
**One-liner:** An answering-service operator takes a family reporting a death, a suicidal caller or a screaming tenant, and the next call drops into her headset seconds later; routing that knew what she had just been through would give her a minute to recover and a fair share of the hardest calls.
**Tags:** #bert #transformers #large-language-models #worker-facing #workflow-orchestration #automation

## The Problem
Answering services take the calls nobody else is awake for. In one night an operator may log a hospice nurse reporting a death to a funeral home, a parent who is panicking, a patient who says they want to end their life and has reached a doctor's after-hours line, a caller who has been drinking and is abusive, and a tenant shouting about water pouring through the ceiling. The automatic call distributor treats each of these as the next unit of work. When the call ends, the operator is "available" again and the queue hands her another one, often a cheerful appointment request she must answer in the client's name a few seconds after a death call.

Nothing records which calls were distressing. The platform logs call type by account, not by what happened on the call. Supervisors can see handle time and occupancy, but not that one operator has taken four death calls and two abusive callers since midnight while the person beside her has taken none. Abusive callers are handled by whoever happens to answer, and repeat abusers ring back into the same queue.

## Why It Matters to the Worker
The job pays near the bottom of office work (the BLS median for switchboard operators, including answering service, is ~$36,750 a year) and runs through nights and holidays. What it costs operators is emotional, and the tools do not acknowledge it. People who answer crisis and death calls for a living describe the cumulative weight of them. Dispatch and crisis-line work has formal debriefing and peer support, which answering services rarely provide. An operator who is shaken has to choose between taking the next call anyway and going on unpaid break, and being berated by an abusive caller with nobody stepping in is a common reason given for quitting in the first months (estimate).

## What a Solution Looks Like
Routing that knows the emotional load. Each call is classified after it ends, from its transcript and disposition, into types such as death notification, crisis or suicidal statement, abuse or threats, and highly distressed caller. After one of these the operator gets a short protected recovery window before the next call is offered, and the system spreads the hardest call types across the shift rather than letting them pile onto one person. Calls flagged as abusive in progress can be taken over by a supervisor with one keystroke, and numbers with repeated abuse are routed straight to a senior operator. Supervisors see a shift view of who has carried what, and operators can mark a call for a debrief.

## Impact If Solved
A 2-3 minute recovery window after the ~5-10% of calls that are distressing (estimate) costs a mid-size service a fraction of an operator-hour per shift and removes the back-to-back pattern that operators find hardest. If first-90-day attrition among new operators fell by even a fifth (estimate), a service hiring dozens of operators a year would cut its recruiting and training load in proportion, and keep more of the people who stay long enough to become experienced.
