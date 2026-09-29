# Court Rules & Deadline Calculation Coverage

**Industry:** [[legal-practice-software|Legal Practice Software]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Rules-based deadline calculators exist and work; keeping them accurate across thousands of courts, divisions and standing orders that change without notice is a permanent content cost nobody has automated.
**Tags:** #large-language-models #bert #transformers #word-embeddings #transfer-learning #change-point-detection #compliance

## The Problem
Missing a deadline is the most common source of legal malpractice claims. Practice management platforms answer this with rules-based calendaring: enter a trigger event, and the system generates the chain of dependent deadlines under that jurisdiction's rules.

The engine is straightforward. The content is not. Deadlines derive from federal rules, state rules, local rules of court, division-specific standing orders and individual judges' preferences, layered on top of each other, with court holiday calendars and counting conventions that differ between them. There are thousands of these bodies. They change through rule amendments, emergency orders and quiet updates to a judge's web page.

Vendors either license a content subscription or staff a team to maintain it. Either way the coverage is deepest where the customers are and thin everywhere else, and a firm in a jurisdiction the vendor does not cover well gets a calendar it cannot trust — which means it keeps the paper docket alongside.

## What Already Exists
Court rules content providers (American LegalNet, CalendarRules, Deadlines.com) license maintained rule sets for major jurisdictions and integrate with the main platforms. Federal rules are stable and well covered. E-filing systems publish some deadline information. Document AI extracts structure from rule text competently.

## The Customisation Gap
Coverage is the entire gap and it is economic rather than technical. Maintaining the top forty jurisdictions is fundable; maintaining the long tail of county courts and individual standing orders is not, at any per-seat price the market supports.

That makes it a monitoring problem rather than an authoring one. Court websites, rule amendment notices and standing orders are published — inconsistently, in scattered formats, with no change notification. Watching them continuously for changes, and drafting the rule update for a human to verify, converts an unfundable authoring burden into a reviewable queue.

The vendor's own data offers a second, underused signal. Across thousands of firms filing in the same courts, the platform observes actual filing behaviour — what was filed, when, relative to what trigger. A systematic divergence between the calculated deadline and what practitioners in that court actually do is evidence that the rule is stale or that a local practice overrides it, and it is exactly the kind of error that never surfaces until it hurts someone.

## Impact If Solved
Calendar trust is binary. A firm either relies on the system or maintains a parallel manual docket, and the second means the software failed at the thing it was bought for. Extending reliable coverage into the long tail is the difference between a product a firm uses and a product a firm double-checks.
