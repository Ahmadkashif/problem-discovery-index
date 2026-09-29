# Licence Compliance From Open Source Governance

**Niche:** [[niches/game-asset-marketplaces/licensing-administration/profile|Licensing & Rights Administration]]
**Industry:** [[industries/game-asset-marketplaces|Game Asset Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software built a whole discipline for tracking third-party licences in a shipped artifact, and game assets are tracked in purchase emails.
**Tags:** #compliance #data-integration #automation #workflow-orchestration #evaluation-metrics #sets-and-logic #graph-theory #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to let a studio know what it is actually permitted to do with the several hundred assets in its project, and whoever tracks that takes the account.

## The Problem
Open source licence compliance is a mature discipline with a vendor category. Software composition analysis scans a build, identifies every third-party component, resolves its licence, checks obligations against policy, generates attribution files and produces a bill of materials that satisfies auditors and acquirers. It exists because shipping software with unknown third-party licences became an unacceptable risk. Game assets are third-party components in a shipped artifact and none of this applies to them.

## What Already Exists
Software composition analysis; licence identification and obligation mapping; policy checking against approved licence sets; automatic attribution generation; and bill-of-materials export.

## The Customization Gap
The adaptation is to binary art assets that carry no declared identity. It requires: (1) identifying components that have no package manifest or version string, so identification must be by content matching rather than by declaration — this is the substantive difference and links it directly to similarity detection; (2) licence terms that vary per marketplace and per listing rather than drawing from a small set of standard licences; (3) obligations concerning seat counts and revenue thresholds rather than source disclosure; (4) a shipped artifact that is a compiled game rather than a dependency tree, making presence detection harder; and (5) a studio with no compliance function, so the tool must be the process.

## Target Customer
Game studios, publishers conducting diligence, asset marketplaces, and software composition analysis vendors.

## Impact If Solved
Open source compliance became a discipline because unknown third-party licences in a shipped artifact were unacceptable. Components with no manifest force identification by content matching, which is what the game asset version has to solve.
