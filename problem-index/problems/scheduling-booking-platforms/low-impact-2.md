# Reminder and Confirmation Sequences

**Industry:** [[scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Reminders are a shipped, configurable, universally deployed feature that no vendor has ever tested, so an entire industry sends a message twenty-four hours before because that is what everyone else does.
**Tags:** #causal-inference #hypothesis-testing #logistic-regression #gradient-boosting #confidence-intervals #evaluation-metrics #revenue-impact

## The Problem
Every scheduling platform sends confirmations and reminders. Every business configures them once at onboarding, usually accepting the default, and never revisits them.

The defaults are conventions. Twenty-four hours before, by email, with an SMS option. Some platforms add a second reminder an hour ahead. The wording is generic and template-driven.

None of it has been evaluated. There is no published evidence, and as far as one can tell no vendor-internal evidence, on whether the twenty-four hour timing is better than forty-eight or two, whether SMS outperforms email by enough to justify the cost, whether a second reminder helps or annoys, whether requiring a confirmation tap changes behaviour, or whether any of it differs by sector, appointment type or customer.

These are trivially testable questions on platforms handling tens of millions of appointments. The randomisation is easy, the outcome is unambiguous, and the answer would be immediately valuable to every customer.

Instead the industry has a folk practice that has not changed since SMS reminders were introduced.

## What Already Exists
Reminder configuration with timing, channel and template editing is standard. SMS delivery is integrated at every vendor. Confirmation and cancellation links are universal. Calendar invitations with native reminders are standard. Some platforms offer basic delivery reporting — sent, delivered, opened.

## The Customisation Gap
Measurement is entirely absent. Delivery is reported; effect is not. Nobody can say what a reminder is worth, which means nobody can say whether a second one is worth its annoyance or whether SMS is worth its cost.

Per-segment optimisation follows from measurement and does not exist. A first-time customer booking six weeks ahead and a weekly regular booking yesterday are different situations, and both receive the same sequence.

Channel selection should follow evidence about the individual — which channel this person has actually responded to before — and instead follows a global setting.

Confirmation requirements are the most interesting untested variable, because requiring an active response both increases salience and provides a signal the business can act on. Whether it reduces attendance among people who simply do not check messages is exactly the sort of thing that needs testing rather than assuming.

And the platform's scale is what makes it tractable: a single business cannot run this experiment, and a vendor with millions of appointments can answer it definitively in a quarter.

## Impact If Solved
Reminders are the industry's only lever against its largest loss, and they are configured by convention and never measured. Running the experiments would produce evidence the entire sector lacks, and per-segment optimisation would apply it, using infrastructure every vendor already operates.
