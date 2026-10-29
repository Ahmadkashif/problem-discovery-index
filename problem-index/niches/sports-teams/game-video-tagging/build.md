# Tags That Learn the Staff's Own Playbook

**Niche:** [[niches/sports-teams/game-video-tagging/profile|Game Video Tagging & Opponent Breakdown]]
**Industry:** [[industries/sports-teams|Sports Teams & Clubs]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Auto-tagging tools label plays in a generic vocabulary, and the video coordinator spends the night translating them into the coaches' terms.
**Tags:** #transformers #cnns #transfer-learning #evaluation-metrics #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to turn every game's film into a breakdown tagged in the coaching staff's own terms, and whoever's clubs need the fewest video-staff hours per game to reach a coach-ready breakdown takes the account.

## The Problem
A staff calls a set "Horns Flare" or "21 Personnel Mesh". The league feed says "pick-and-roll" or "pass, short middle". The coordinator retags most plays by hand to make the library searchable in the staff's language.

## Why Nobody Has Built This
Vendors sell one model to many clubs and keep a common taxonomy. Learning each staff's vocabulary needs per-club training on its own history, and clubs guard their playbooks.

## What to Build
A per-club layer on top of a pretrained play-segmentation model. It is fine-tuned on the club's historical tags, proposes staff-vocabulary labels with confidence, and routes only uncertain plays to the coordinator. Every correction is learned. Natural-language clip retrieval ("every late-clock possession against switching defences") works over the library. It runs inside the club's environment so playbooks never leave it, and demos use consented or synthetic footage.

## Target Customer
Directors of video at NBA, NHL and NFL clubs and Power Four football and basketball programmes.

## Impact If Built
Cutting a game's breakdown from ~6 to ~2 video-staff hours (estimate) returns ~330 hours a season on an 82-game schedule, before opponent breakdowns are counted.
