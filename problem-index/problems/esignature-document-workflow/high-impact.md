# Why Envelopes Stall

**Industry:** [[esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** High Impact
**One-liner:** A large share of agreements sent for signature never complete, the reasons are ordinary and addressable, and the platform reports only that the envelope is outstanding.
**Tags:** #survival-analysis #gradient-boosting #logistic-regression #bert #time-series-forecasting #confidence-intervals #feature-engineering #evaluation-metrics #revenue-impact

## The Problem
An agreement is sent for signature. Some meaningful proportion never comes back. In sales contexts that is revenue that was negotiated, agreed and then lost to friction after the commercial work was finished, which is the most expensive possible place to lose a deal.

The reasons are mundane. It went to the person who negotiated rather than the person authorised to sign. The signer is on holiday and nobody knows. It arrived with no context and looks like a phishing email. It was routed through four approvers in sequence and stalled at the second. A term in it needed legal review that nobody anticipated. It requires a countersignature from someone internal who is not watching. The recipient opened it, hit a clause they objected to, and simply stopped rather than replying.

The platform sees all of this happening and reports status. Sent. Viewed. Outstanding. It knows the envelope was opened four times and never signed, which is a very specific and diagnostic behaviour, and it treats that identically to an envelope nobody opened at all.

The sender's remedy is to send a reminder. Reminders are the category's answer to every stall, they are undifferentiated, and after the second one they actively annoy the recipient.

## Why It's Unsolved
The business model counted envelopes. Revenue came from transaction volume and seats, so the product optimised for making sending easy, and what happened after sending was the customer's problem. Completion rate is reported as a customer metric rather than treated as a vendor responsibility.

Diagnosis genuinely requires context the platform has historically not had. Knowing that an envelope stalled because it went to the wrong signer requires knowing who should have signed, which lives in the customer's CRM or their signature authority matrix, not in the envelope.

Recipient behaviour is also only partially observable. The platform knows an envelope was opened and how long each page was viewed; it does not know the recipient forwarded it to their legal team and is waiting. Much of the stall is happening outside the system.

And the strategic move to agreement platforms is recent. For most of the category's history, understanding the content of the document was out of scope — the product moved a PDF and collected a signature, deliberately indifferent to what the PDF said.

## What a Solution Looks Like
Stall prediction at send time, from the envelope's own characteristics: routing depth, whether the signer has signed before, agreement type and value, page count, time of week, and whether the document contains terms that historically trigger review. A sender who is told this envelope has a poor completion outlook and why can fix it before sending, which is worth far more than a reminder afterwards.

Diagnosis from behaviour. Opened repeatedly and unsigned, opened and abandoned at a specific page, forwarded, never opened — each has a different remedy, and the platform can distinguish them. Page-level dwell before abandonment is an unusually direct signal about which clause is the obstacle.

Signer identification is the highest-value single fix. Whether this person has authority to sign this kind of agreement at this value is knowable from the customer's own history and from prior envelopes, and sending to the wrong person is one of the most common causes of stall.

And escalation that is a real action rather than a reminder — routing to an alternate signer, alerting the internal owner, or flagging the specific clause that appears to be the obstacle.

## Impact If Solved
Completion rate is the metric that matters to every customer of these platforms and the one the category has never taken responsibility for. Agreements that stall after the commercial negotiation is complete are the cheapest possible revenue to recover, and every diagnostic signal needed is already flowing through the platform.
