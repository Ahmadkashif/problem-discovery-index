# A Programme Budget That Recalculates Itself

**Niche:** [[niches/tour-operators/faculty-led-university-programs/profile|Faculty-Led University Programmes]]
**Industry:** [[industries/tour-operators|Tour Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A faculty-led programme's per-student price depends on enrolment, currency and supplier quotes that all move after the fee is published, and nobody models the range.
**Tags:** #monte-carlo-methods #probability-distributions #logistic-regression #optimization-fundamentals #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to get a faculty-led programme through the university's risk, academic and procurement review and deliver it at the per-student price students were quoted, and whoever clears approval fastest with a price that holds to departure takes the account.

## The Problem
The provider builds a budget for a target enrolment, perhaps twenty students. Many costs are fixed per programme: guides, a coach, a lecture venue, faculty travel. Others are paid in local currency months later. If twelve students enrol, the per-student cost jumps, and someone, whether provider, department or students, absorbs it. Budgets are reworked by hand each time.

## Why Nobody Has Built This
Programmes are bespoke, so providers treat each budget as a one-off document. The universities' systems manage applications and risk, not provider economics. The provider holds the history of past enrolments against targets, but it sits in spreadsheets.

## What to Build
A budget engine that tags every cost line as fixed, per-student or per-room, and by currency and payment date. It predicts the enrolment distribution from the faculty member's past programmes, the destination and the application deadline. From these it simulates the per-student price range. It proposes a fee and a minimum-enrolment clause both sides can accept, and recalculates instantly as applications arrive.

## Target Customer
University-programme leads at educational operators and custom-programme providers, and the education-abroad offices that approve fees.

## Impact If Built
Fees that hold to departure, fewer mid-cycle price changes or cancellations, and faster agreement on budgets with education-abroad offices (estimate).
