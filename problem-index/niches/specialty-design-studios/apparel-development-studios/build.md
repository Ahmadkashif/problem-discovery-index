# A Round Convergence Record Across Every Client

**Niche:** [[niches/specialty-design-studios/apparel-development-studios/profile|Apparel Design & Development Studios]]
**Industry:** [[industries/specialty-design-studios|Specialty Design Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A studio sells fewer sampling rounds and has never measured how many rounds its styles take, by category, fabric or factory, or which of its corrections actually converged.
**Tags:** #survival-analysis #gradient-boosting #feature-engineering #evaluation-metrics #tacit-knowledge-ml #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to get a brand's styles to an approved production sample in the fewest sampling rounds before line review, and whoever converges fastest at a predictable fee takes the account.

## The Problem
A development studio running a few hundred styles a season across a dozen clients knows anecdotally which garments are hard — tailored jackets, bias-cut dresses, stretch denim — and which factories are slow. It cannot say how many rounds a knit top takes on average, which corrections its technical designers issue that fail to converge, or which factory turns comments around in a week versus three. So it prices fixed fees on instinct and loses money on the styles that run to round five.

## Why Nobody Has Built This
The record is split across clients' PLMs, email and chat, and most of it belongs to the client. PLM vendors measure a brand's own development calendar, not a studio's performance across brands, and studios are too small to build their own analytics.

## What to Build
A studio-side ledger that records, for every style and round, the category, fabric, block, factory, the corrections issued and whether the next round passed — capturing only metadata and the studio's own corrections, so client-owned designs stay in client systems. On top: time-to-approval survival curves by category and factory, a model that predicts rounds for a new style before it is quoted, and a correction scorecard per technical designer that shows which fixes converge.

## Target Customer
Principals of apparel development studios with 5–50 staff who quote fixed fees per style and want to price on evidence.

## Impact If Built
A studio that can predict rounds per style prices profitably, routes hard styles to its senior technical designers, and can show a prospective client its convergence record — a sales asset no portfolio of sketches provides.
