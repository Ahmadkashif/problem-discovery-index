# Market Appetite That Lives in Relationships

**Niche:** [[niches/insurtech-platforms/excess-surplus-specialty-lines/profile|Excess, Surplus & Specialty Lines]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Which E&S markets write which risks is knowledge held in individual brokers' heads, so placements go to more markets than necessary, underwriters drown in submissions they will decline, and a broker who leaves takes the map with them.
**Tags:** #descriptive-statistics #k-nearest-neighbors #evaluation-metrics #confidence-intervals #hypothesis-testing #workflow-orchestration #tacit-knowledge-ml #automation
**Contested on:** Every serious competitor in E&S technology is fighting to make manuscript coverage comparable across markets so a broker can tell a client what they are actually buying — and whoever makes coverage comparison reliable takes the account.

## The Problem
A broker with a difficult risk decides where to send it. They know from experience that three particular underwriters have written similar business, that one market has pulled back from the class this year, and that another will look at it if the loss history is clean. A newer broker at the same firm does not know any of this and sends to twelve markets, most of which decline. The firm's placement efficiency, and the underwriters' submission load, both depend on knowledge that exists only as individual experience and that the firm's own records could reconstruct — every submission it has sent, to whom, and what came back.

## Why It's Still Broken
Appetite is treated as relationship knowledge and relationships are how this market works, so codifying appetite feels like it devalues the thing brokers are paid for. It is also genuinely dynamic — markets enter and exit classes continuously, so a static appetite guide is wrong within months, which is the reason the published versions are not used. And nobody has made the connection that the broker's own submission history is a continuously updating record of exactly what each market actually writes, as opposed to what its appetite guide says.

## What a Fix Looks Like
Build the appetite map from the firm's own placement history. Every submission sent, the risk's characteristics, the market it went to, and the outcome — declined, quoted, bound, and at what terms — is already recorded in the firm's system. Aggregated, that is a live map of what each market actually writes, which classes it has quietly stopped writing, which underwriter within a market handles what, and what its quote-to-bind behaviour looks like. Recommend a placement list per risk from that history, with the evidence, so a newer broker starts where an experienced one would. Detect appetite shifts as they happen, since a market that has declined six submissions in a class it used to write has changed something and the broker should know before sending a seventh. The firm's knowledge stops being a property of who is employed this year, which matters in a market with high broker mobility.

## Who Feels the Pain
Newer brokers guessing where to place and burning credibility with markets; underwriters receiving submissions they were never going to write; and firms whose placement capability walks out with a departing broker.

## Impact If Fixed
Targeted placement raises the broker's hit rate and cuts the submission load on underwriters at the same time, which is one of the few genuinely mutual improvements available in this market. The appetite map is built from records the firm already keeps and is the clearest case in the vault of institutional knowledge that exists as data and is treated as personality.
