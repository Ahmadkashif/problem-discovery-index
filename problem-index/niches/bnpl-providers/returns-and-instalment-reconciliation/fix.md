# Still Being Charged for What You Sent Back

**Niche:** [[niches/bnpl-providers/returns-and-instalment-reconciliation/profile|Returns & Instalment Reconciliation]]
**Industry:** [[industries/bnpl-providers|BNPL Providers]]
**Type:** Fix (Pain Point)
**One-liner:** The consumer returned the item three weeks ago, the merchant confirmed the refund, and the instalment payments are still being taken.
**Tags:** #workflow-orchestration #automation #compliance #evaluation-metrics #quick-win #revenue-impact #data-integration #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to reconcile a merchant's return policy with a consumer's instalment schedule — and whoever does that removes the most common and most infuriating failure in the product.

## The Problem
The item went back. The merchant processed the return and told the consumer a refund was issued. The provider did not receive the notification, or received it without enough detail to match it to the plan, or received it after the next payment had already been taken. The consumer is charged again, contacts the provider, is told to contact the merchant, contacts the merchant, is told the refund was issued, and goes round again. It is the single most common complaint in the product, it makes both the merchant and the provider look incompetent, and it originates in a notification that did not arrive in a usable form.

## Why It's Still Broken
The refund notification is a message from the merchant's system that may be late, incomplete or absent, and the provider's schedule continues on its own timetable regardless — the two processes run independently and nothing holds the payment while the reconciliation resolves. Merchants integrate refunds with varying completeness. The provider cannot verify a return directly. And the consumer is passed between two parties each of whom is technically correct.

## What a Fix Looks Like
Stop the payment while it is unresolved. Pause the next instalment when a return is reported by the consumer, pending confirmation, which is the fix, is a policy change rather than an engineering one, and removes the most damaging version of the failure at the cost of a short delay in a small number of cases. Accept the consumer's report of a return as a trigger, since they are the party with the earliest knowledge and are currently the only one who cannot act on it. Require line-level refund notification at merchant integration, which is where the completeness problem starts and is negotiable at onboarding rather than afterwards. Reconcile proactively against the merchant's order status where the integration permits, rather than waiting for a notification. Resolve the complaint in one contact by holding the relationship with the merchant on the consumer's behalf, since the passing between parties is the experience that does the damage. Refund promptly when a payment was taken in error, without requiring the consumer to establish who was at fault. Alert the merchant when their refund notifications are incomplete, since most do not know. Report the return-related complaint rate per merchant, which identifies the integrations causing it. Track the time from return to schedule adjustment as an operating metric. And measure the churn following this experience, because it is the failure most likely to end a consumer relationship and is entirely preventable.

## Who Feels the Pain
Consumers paying for items they returned; merchants blamed for a provider's reconciliation; and providers losing customers to a notification that arrived late.

## Impact If Fixed
The two processes run independently and nothing holds the payment while the reconciliation resolves, so the consumer is charged and then passed between two parties who are each technically correct. Pausing the next instalment on a consumer-reported return is a policy change that removes the damaging version at small cost.
