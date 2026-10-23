# Client Instructions Written as Prose

**Industry:** [[answering-services|Telephone Answering Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every new client's after-hours rules arrive as an email, a phone conversation and a marked-up PDF, and a setup specialist hand-translates them into a branching script that nobody tests against the cases the client actually cares about.
**Tags:** #large-language-models #transformers #seq2seq #evaluation-metrics #workflow-orchestration #automation #quick-win

## The Problem
Onboarding a medical group, an HVAC contractor or a property portfolio means turning the client's intentions into an account the operator can follow. The client describes them loosely: which calls are emergencies, who is on call, what to say about the ER, which callers get patched, which vendor to call for elevators, what to do if nobody answers a page. An account setup specialist turns that description into script screens in Startel or Amtelco: questions, branches by call type and time of day, the on-call lookup and the delivery method. The build is commonly a day or more of back-and-forth for a complex account (estimate), and then the instructions keep changing. A new physician joins, the property adds a building, the contractor stops doing weekend service, and each change arrives by phone or email and is edited into the live script by whoever takes it.

The result is drift. Rules contradict each other ("page for all post-op calls" in one place, "hold post-op calls after midnight unless bleeding" in another). Edge cases nobody discussed get resolved by the operator on the night. Nobody can say which version of the instructions governed a disputed call six months ago.

## What Already Exists
The TAS platforms provide capable scripting engines (Amtelco's Intelligent Series scripts branch by call type, time of day and day of week; Startel offers equivalent script and dispatch builders), and general workflow and IVR builders exist across the contact-centre market. Some services keep a standard template per client type. Version history exists in the platforms at the level of the screen edit.

## The Customisation Gap
What answering services need on top is industry logic: a structured intake that asks a new client the questions that matter for its vertical, such as the clinical red flags a pediatric group escalates, the outdoor-temperature rule for no-heat calls, or the release-status questions a funeral home needs on a first call. They also need a compiler that turns the client's answers and prose into a decision table the platform can run. Conflict detection should flag rules that contradict or leave gaps. Before go-live, a test suite of synthetic calls should run through the script and come back to the client for sign-off as "here is what we will do with each of these twenty calls". Every change needs dating and attribution so the governing version of any past call can be produced. Language models can draft the decision table and the test calls; the client's sign-off makes them binding.

## Impact If Solved
Setup time for a complex account falls from days to hours, and the client confirms behaviour on concrete test calls rather than trusting that its email was understood. When a call is disputed, the service can show which signed-off rule it followed, which is the evidence that decides both client disputes and negligence claims.
