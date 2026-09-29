# The Same Twenty Questions

**Niche:** [[niches/payment-processors/the-integration-engineer/profile|The Integration Engineer]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Fix (Pain Point)
**One-liner:** Twenty recurring issues account for most of the support volume, every engineer knows them by heart, and the product that causes them has not changed.
**Tags:** #descriptive-statistics #workflow-orchestration #evaluation-metrics #automation #quick-win #worker-facing #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to stop the same twenty questions arriving forever — and whoever fixes the product so they are not asked changes what a support function is for.

## The Problem
Ask any payments support engineer and they will list the recurring issues without hesitation: the reused idempotency key, the unacknowledged webhook, the currency minor units, the test credential in production, the authentication flow implemented halfway, the timezone in the settlement report. These account for most of the volume. Every engineer answers them repeatedly, the documentation covers them, and merchants keep making them because the product permits the mistake and the failure mode is unclear. The support function is a permanent institution built around a fixed set of avoidable defects.

## Why It's Still Broken
Support volume is treated as a staffing question rather than as a product signal, so the response to more tickets is more engineers — the cost is absorbed in the function that receives it rather than surfacing where the cause is. The issues are documented, which makes them look like the merchant's failure to read. Fixing them requires product changes that have no obvious revenue attached. And nobody categorises tickets in a way that makes the concentration visible to product teams.

## What a Fix Looks Like
Categorise the volume and treat the top causes as defects. Classify every ticket to a specific cause and report the distribution to product, which is the fix, is a day's work to set up, and makes a concentration everybody knows anecdotally into a prioritised backlog. Make each mistake impossible or loud rather than documented — reject a reused idempotency key with a clear error, fail loudly on a test credential in production, validate the currency unit at the call — since documentation has demonstrably not worked and the product can enforce what prose cannot. Detect the misconfiguration in traffic and tell the merchant before it costs them, which catches the ones that cannot be made impossible. Improve the error messages themselves, since a clear error resolves what an unclear one escalates and this is the cheapest change available. Provide the diagnosis in the merchant's own dashboard, which deflects the ticket entirely. Measure ticket volume per cause over time, so a fix can be shown to have worked and the next one justified. Publish the top causes to merchants as a checklist, which is the low-effort version and works for some of them. Give product teams the support volume attributable to their surface, which creates the accountability that is currently missing. Track deflection rather than resolution time, since resolving efficiently is a worse outcome than not being asked. And measure tickets per merchant as the function's real metric, because a support organisation whose volume scales with customers is a product problem wearing a staffing costume.

## Who Feels the Pain
Engineers answering the same questions for years; merchants losing revenue to mistakes the product allowed; and processors growing a support function in proportion to their success.

## Impact If Fixed
Support volume is treated as staffing rather than as a product signal, so the cost is absorbed where it lands and never surfaces where the cause is. Classifying tickets by cause makes an anecdotally known concentration into a prioritised backlog, and enforcement in the product does what documentation demonstrably has not.
