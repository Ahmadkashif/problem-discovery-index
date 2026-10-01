# Ten Weeks of Routine Ballots

**Niche:** [[niches/asset-managers/stewardship-and-proxy-voting/profile|Stewardship & Proxy Voting]]
**Industry:** [[industries/asset-managers|Asset Managers]]
**Type:** Fix (Pain Point)
**One-liner:** Most ballot items in proxy season are routine, but each still needs a check against policy, so the hard cases get the leftover attention.
**Tags:** #gradient-boosting #large-language-models #evaluation-metrics #worker-facing #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to show that each vote and engagement follows the firm's own stated policy rather than a proxy adviser's default — and whoever can evidence that, item by item, keeps the clients and survives the political scrutiny now aimed at stewardship from both sides.

## The Problem
Between April and June the team must clear thousands of meetings. Auditor ratifications and uncontested director elections take time because a policy exception might be hiding in any of them.

## Why It's Still Broken
Custom policies are implemented in the proxy adviser platform as rules, but exceptions and edge cases are spotted by people, and there is no confidence score telling an analyst which items are safe to pass.

## What a Fix Looks Like
A triage model trained on the firm's past votes and overrides that scores every item for review need, routes low-confidence and precedent-breaking items to humans, and drafts rationales for the rest from policy text. Measure it by recall on items seniors would have escalated.

## Who Feels the Pain
Stewardship analysts working season hours; PMs consulted late on votes that matter.

## Impact If Fixed
Analyst attention concentrates on contested and material votes, and routine items are handled consistently and documented.
