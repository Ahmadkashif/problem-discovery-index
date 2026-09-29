# Fix: No Evidence of Access Is Not Evidence of No Access

**Niche:** Scope Determination
**Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The phrase every incident report uses means one thing to the responder who wrote it and something considerably stronger to everyone who reads it afterwards.
**Tags:** #evaluation-metrics #confidence-intervals #compliance #worker-facing #hypothesis-testing #revenue-impact
**Contested on:** Whether "what did the attacker access" is answered with calibrated bounds from the evidence that exists, or with a narrative.

## The Problem

"No evidence of data exfiltration was identified."

The responder means: we looked at the evidence that exists, and it does not show exfiltration. They also know that file access auditing was disabled, that netflow retention covered only the last five days of an eleven-day intrusion, and that the attacker had the access and the time to take whatever they wanted. The sentence is precisely true and carries very little.

The client's counsel reads it as a finding that nothing was taken. The executive team hears it as reassurance. It goes into a board paper as "the forensic investigation found no evidence of data theft". It informs a notification decision. It may appear in a public statement. And at each step the qualification the responder understood is stripped further, until the sentence is doing work it cannot support.

Everyone in the chain is acting reasonably. The responder wrote an accurate sentence. Counsel relied on the expert. The board relied on counsel. And the conclusion that emerges at the end is far stronger than the evidence that entered at the beginning.

If it later turns out data was taken — through a leak site, a regulator, or a subsequent claim — the sentence is read back in a very different light.

## Why It's Still Broken

**The phrase is standard and its ambiguity is convenient.** It is accurate, it is what clients want to hear, and it allows a conclusion without a commitment. Nobody has an incentive to replace it.

**The qualification lives in the conversation, not the document.** Responders explain the limitation verbally on the bridge call. Bridge calls are not minuted and do not travel with the report.

**The client wants the stronger reading.** A narrow scope means a smaller notification, lower cost and less exposure. A client hearing an ambiguous sentence will take the favourable interpretation, and asking them not to is asking against their interest.

**Stating the limitation forces expensive conservatism.** A responder who says plainly that exfiltration cannot be ruled out has, in effect, told the client to notify broadly, which is a very costly recommendation to deliver.

**Time pressure compresses everything.** A statutory clock leaves no room for a careful discussion of evidential weight.

**No convention exists for saying it better.** An individual firm writing more carefully than its competitors delivers a less useful-sounding report, which is the classic first-mover problem.

## What a Fix Looks Like

**State what the evidence could have shown.** Alongside every negative finding, name the evidence that would have established the positive and whether it existed. "No evidence of exfiltration was identified. File access auditing was not enabled and netflow covered five of the eleven days." Two sentences, and the reader now knows what the first one is worth.

**Separate the three categories explicitly in the report structure.** Established, bounded, unaddressable. A reader extracting a sentence for a board paper will extract it from a section labelled for what it is.

**Write the sentence that will be quoted.** The report will be reduced to one line by someone downstream. The responder should write that line deliberately, with the qualification inside it, rather than leaving the reduction to someone with no forensic training.

**Give counsel the bounds directly.** Maximum defensible scope, minimum established scope, and the basis for each. Counsel is making a notification decision and needs exactly this, and currently has to derive it from narrative.

**Minute the bridge call qualifications.** The caveats are already being said. Writing them down is free and is the difference between a qualification that travels and one that does not.

**Push for a reporting convention.** A standard structure requiring an evidence-limitations statement for every negative finding removes the competitive penalty for the firm that would otherwise go first — and the insurers who fund this work are well placed to require it.

## Who Feels the Pain

The organisation, which decided not to notify on the strength of a sentence that did not support the decision, and finds out eighteen months later.

The individuals whose data was taken and who were not told, because the investigation could not establish what it could not establish.

The responder, whose accurate sentence is quoted back in a very different context, and who explained the limitation to people who did not write it down.

And the firm, whose professional exposure rests on a phrase whose ambiguity everybody has been relying on.

## Impact If Fixed

Naming the evidence that would have shown the positive, alongside every negative finding, costs two sentences and transforms what a reader can do with the conclusion.

Writing the quotable line deliberately is the single most effective change available, because the reduction to one sentence will happen regardless and is currently performed by whoever is assembling the board pack.

And an evidence-limitations convention, required by the insurers who fund most of this work, would fix it across the industry at once and remove the penalty for any individual firm choosing to be clearer.
