# An Error That Describes a Symptom

**Niche:** [[niches/internal-developer-platforms/the-application-developer/profile|The Application Developer]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The platform rejects a deployment with a message about a validation failure three layers down, and the actual reason is that the platform does not support what the developer asked for.
**Tags:** #bert #descriptive-statistics #k-means-clustering #evaluation-metrics #confidence-intervals #worker-facing #quick-win #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to let a developer find out what the platform supports before they build on the assumption that it does — and whoever does that takes the adoption, because discovery by failure is why developers route around.

## The Problem
A deployment fails with an error from the underlying orchestrator about an invalid field in a generated manifest. The developer did not write that manifest and does not know what the field is. The actual situation is that they requested a configuration the platform's abstraction does not express, the abstraction generated something invalid rather than rejecting the request, and the failure surfaced three layers below where the mistake was made. They spend an hour reading orchestrator documentation for a system the platform exists to hide from them, and then ask in the channel.

## Why It's Still Broken
The abstraction passes errors through from the layer below because that is what happens by default, and translating them requires anticipating them, which nobody has done systematically. The platform's validation is at the point of application rather than at the point of request, so an unsupported input is detected late and by the wrong component. Error messages are written by platform engineers for their own debugging. And the developer's hour is invisible to everyone.

## What a Fix Looks Like
Reject at the boundary, in the developer's language. Validate the request against the capability surface at the point it is made rather than at the point it is applied, which catches the unsupported input before anything is generated and is the structural fix. Never pass an underlying error through unmapped, since an error from a layer the platform exists to hide is a leak of exactly the complexity the developer was promised freedom from — map it or state plainly that the platform cannot express this. Say what is not supported and what the alternatives are, because the developer's next question is always whether there is another way and it is currently a channel message. Name the escape path if one exists, which is the provisioning niche's bounded escape. Include what to do and whom to ask, since the platform knows which team owns the capability. Collect the unmapped errors that reach developers, which is a ranked list of the leaks and is the fix backlog. And measure how often a developer's next action after an error is a message in the support channel, which is the direct measure of whether errors are self-serviceable and nobody tracks it.

## Who Feels the Pain
Developers reading documentation for a system the platform was supposed to hide; platform engineers answering the resulting questions; and organisations whose platform adoption erodes one bad error message at a time.

## Impact If Fixed
Validating at the request boundary rather than at application catches the unsupported input where the developer can understand it. Mapping every underlying error is the discipline that stops the abstraction leaking, and the error-to-support-message rate is the measure of whether it is working.
