# Assignment and Market Design From Operations Research

**Niche:** [[niches/game-hosting-providers/matchmaking/profile|Matchmaking]]
**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Operations research and market design solved matching under waiting cost and quality trade-offs, and matchmakers use hand-tuned weights.
**Tags:** #optimization-fundamentals #markov-decision-processes #convex-optimization #confidence-intervals #evaluation-metrics #causal-inference #hypothesis-testing #dynamic-programming
**Contested on:** Every serious competitor in this niche is fighting to trade match quality against wait time against latency without knowing what any of the three costs in whether the player comes back — and whoever establishes that currency takes the account.

## The Problem
Dynamic matching under waiting cost is a well-developed field. Ride-hailing dispatch, organ allocation, kidney exchange, ad auctions and labour market clearinghouses all solve versions of it, with formal treatment of the batching trade-off — wait longer for a thicker market and a better match, or clear now — and with objectives derived from measured outcomes rather than set by hand. The theory is public and the practitioners are numerous. Matchmaking is the same problem with better data and hand-tuned weights.

## What Already Exists
Dynamic matching and batching policies; market thickness and clearing interval analysis; assignment optimisation under multiple objectives; waiting cost modelling; and deferred acceptance mechanisms.

## The Customization Gap
The adaptation is to sub-second decisions over a population that is also the customer. It requires: (1) decisions made in seconds at enormous volume, ruling out the computational approaches most market design assumes — this is the substantive difference and forces heuristic policies with proven bounds rather than exact solutions; (2) an objective that must be estimated from behaviour rather than stated, since players cannot report their own utility; (3) a geographic latency constraint with no analogue in most matching markets; (4) participants who churn permanently if the matching is poor, making the objective long-horizon rather than per-transaction; and (5) skill ratings that are themselves estimates with uncertainty, so match quality is measured with error.

## Target Customer
Multiplayer platform vendors, studios operating multiplayer titles, matchmaking service providers, and operations research consultancies.

## Impact If Solved
Market design solved dynamic matching under waiting cost and the theory is public. Sub-second decisions at volume, against an objective that must be estimated from behaviour, is what has to be rebuilt.
