# Remote Configuration Safety

**Parent Industry:** [[industries/game-liveops-services|Game LiveOps Services]]
**Category:** 🟠 Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to tell someone what a configuration value actually reaches before they change it in a live game — and whoever maps the blast radius takes the account.

## Profile
**Market Size:** ~$350M US
**Share of Parent Industry:** ~12% of category revenue
**Digital Adoption:** Low — tribal knowledge
**Target Buyer:** Platform engineering leads
**Automation Potential:** High — dependency mapping and change control

## What Makes This a Distinct Niche
A live game's behaviour is controlled by thousands of remote configuration values. Any of them can be changed by anyone with access, instantly, against the whole player base. The blast radius of any given value is known by whoever wrote it, if that person is still there. Configuration is treated as data rather than as code — no review, no tests, no dependency graph, no staged rollout — despite having identical power to change the running game and a far lower barrier to doing so.

## Current Tools & Gaps
A configuration console with a search box, an audit log nobody reads, and institutional memory. The gaps: no dependency map between values and systems; no impact preview; no staged rollout; no automated validation of ranges and combinations; and no ownership recorded per value.

## Problems
- [[niches/game-liveops-services/remote-configuration-safety/build|🔨 Build: Knowing What a Value Reaches]]
- [[niches/game-liveops-services/remote-configuration-safety/buy|🛒 Buy: Change Management From Software Release Engineering]]
- [[niches/game-liveops-services/remote-configuration-safety/fix|🔧 Fix: One Number, Every Player, Immediately]]
