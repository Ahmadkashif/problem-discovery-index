# The AP Clerk Chasing an Answer

**Industry:** [[ap-automation-vendors|AP Automation Vendors]]
**Type:** Worker Life Changing
**One-liner:** The clerk's job is not processing invoices, it is sending emails to people who do not reply, about invoices that cannot move until they do.
**Tags:** #large-language-models #bert #k-nearest-neighbors #gradient-boosting #evaluation-metrics #workflow-orchestration #worker-facing #automation

## The Problem
The exception queue is the clerk's day. Each item is blocked on information somebody else holds: the requisitioner who knows whether the partial delivery was agreed, the receiving team who knows whether the goods arrived, the vendor who knows what the extra line item is, the manager who has not approved.

So the clerk writes emails. Then follow-ups. Then escalations. The replies arrive over days, out of order, sometimes answering a different question. Meanwhile the vendor calls to ask about payment, and the clerk explains that it is being reviewed.

Some of the queue is genuinely urgent — a vendor threatening to stop shipping, a discount expiring, a payment run tomorrow — and the queue does not distinguish. Prioritisation is by whoever complained most recently.

Month end compresses everything. Accruals require knowing what is outstanding, which requires the queue to be current, which it is not, so the clerk works through it under time pressure while the volume of new invoices continues.

And the same exceptions recur. The same vendor, the same buyer, the same category, the same problem, every month, resolved the same way, with the same emails written again.

## Why It Matters to the Worker
The work is blocked rather than difficult, which is a specific kind of frustrating. A clerk can resolve very little on their own authority; their throughput is determined by other people's responsiveness and they are measured on it anyway.

They are the recipient of everyone's dissatisfaction. Vendors chasing payment, internal stakeholders annoyed at being asked, managers asking why the close is late. The role sits at the confluence of three groups' irritation and has no leverage over any of them.

It is repetitive without being routine. Each exception looks different enough to require reading, and resolves the same way as the last twenty.

And the career trajectory is poor. AP is where accounting careers start and frequently where they stall, because the work demonstrates persistence rather than judgement, and the judgement it does require — recognising which vendor claims are legitimate, which internal claims are not — is invisible to anyone assessing the person.

## What a Solution Looks Like
Draft the chase. The email to the requisitioner is a formulaic function of the exception type, the invoice, the purchase order and the person; generating it, sending it, tracking the reply and interpreting the answer is the largest single time saving in the role.

Interpret the reply. Answers arrive as prose — "yes we only got half of that, the rest is coming next week" — and turning that into a receipt adjustment and a released invoice is exactly the step a clerk performs manually a hundred times a month.

Prioritise by consequence. Discount expiry, payment run timing, vendor relationship criticality and supply risk are all computable, and the queue should be ordered by them rather than by complaint volume.

Resolve the repeats automatically. An exception matching a pattern resolved the same way twenty times for the same vendor does not need a fresh investigation; it needs a rule the system proposes and the clerk confirms once.

Make the recurring causes visible. A clerk who can show that a third of their queue traces to one buyer's purchase order habits has an argument they currently cannot make, and it changes the conversation from their throughput to the process.

Answer the vendor without involving the clerk. Most vendor calls ask where an invoice is, which is a status lookup the vendor could perform themselves.

## Impact If Solved
This role is a person waiting for replies, measured on how fast things move. Drafting and interpreting the correspondence, prioritising by real consequence and auto-resolving the repeats removes the waiting from a job that is otherwise almost entirely waiting, and surfaces the process problems that no one in AP is currently able to evidence.
