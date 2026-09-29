# Lineage: Player Research Firms

**Industry:** [[industries/player-research-firms|Player Research Firms]]
**Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**The tool:** TRUE — Tracking Real-Time User Experience, Microsoft Game Studios' instrumentation system that logs gameplay events from a playtest build and analyses them together with the players' attitudinal, demographic and contextual data
**Builder:** Microsoft
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A playtest could tell you *what* happened or *why*, but not both at once.

The classic games usability session is a player behind a one-way mirror, a researcher taking notes, and a questionnaire afterwards. It captures reasons — "I didn't see the grenades" — from one player at a time, and it depends on the researcher happening to be watching the right moment.

Instrumentation — having the game itself log what the player does — captures the opposite. It scales to hundreds of players and records every death, but a log line says a player died at a coordinate, not that she was frustrated, or bored, or never noticed the item that would have saved her.

The TRUE paper states the gap in one sentence: when behaviour is collected "without attitudinal, demographic, and contextual data," researchers "have no way to answer the 'why' behind the 'what'."

## What Got Built

TRUE, a system Microsoft Game Studios researchers described at CHI in April 2008. It **combined the collection and analysis of behavioural instrumentation with other HCI methods**: the game build logs what the player does, and that log is analysed together with what the player reports and with the context of the session. The practical effect is that a spike in deaths can be read next to the recording of those deaths and next to what players said about that section — the 'what' and the 'why' side by side.

The paper's claim is that it had "evolved instrumentation methodology and analysis to extensively improve the design of video games," demonstrated through two case studies, and it asked the wider HCI community to adopt and adapt it.

The public face of the method arrived a year earlier. In August 2007 *Wired* described Randy Pagulayan — later a TRUE co-author — running Bungie's lab for *Halo 3*: cameras on the player's face and controller, every moment of on-screen action recorded, and more than **3,000 hours of play from some 600 ordinary players**, tracked down to where, "down to the square foot," players most often died.

## Who Built It, And Why Them

Microsoft, because it was a platform holder that published games at volume.

*Wired* made the point explicitly: most studios "just pay people to report any bugs they find," but "because it is owned by Microsoft, which launches dozens of Xbox and PC games every year, Bungie has access to one of the most advanced game-testing facilities ever built."

**That is the business case.** A lab with recording rooms, recruiting pipelines and an instrumentation system is a fixed cost. An independent studio shipping one game every three years cannot amortise it. A first-party publisher running a portfolio across a console it also owns can, and it has a direct interest in each title's reception, because a flop hurts the platform as well as the game. The six TRUE authors — Jun Kim, Daniel Gunn, Eric Schuh, Bruce Phillips, Randy Pagulayan and Dennis Wixon — all gave Microsoft Game Studios, Redmond, as their affiliation.

## What It Cost

**TRUE lived inside the publisher.** It required instrumentation built into the game, which a first-party team could demand and an outside research firm usually cannot. The method spread through publication; the hooks into the build did not come with it.

And its loop ended at the ship date. TRUE measured a pre-release build to change design before launch. It said nothing about whether the change worked once real players arrived.

## What You Still Touch

A research firm's readout that pairs a heatmap of deaths with a clip of a player swearing at that corner is TRUE's format, usually rebuilt by hand.

- [[problems/player-research-firms/high-impact|🔴 Findings Delivered, Outcomes Never Returned]] — the loop TRUE closed only up to launch
- [[problems/player-research-firms/low-impact-2|🟡 Session Analysis at the Speed of a Deadline]] — synchronised streams, without the build hooks
- [[niches/player-research-firms/study-instrumentation/profile|Study Instrumentation]]
- [[niches/player-research-firms/outcome-telemetry-linkage/profile|Outcome Telemetry Linkage]]

**Sources:** WebSearch was unavailable this session (session cap reached); research was by direct fetch and bibliographic APIs. Jun H. Kim, Daniel V. Gunn, Eric Schuh, Bruce Phillips, Randy J. Pagulayan and Dennis Wixon, "Tracking Real-Time User Experience (TRUE): A Comprehensive Instrumentation Solution for Complex Systems," *Proceedings of CHI 2008*, pp. 443–452, doi 10.1145/1357054.1357126 — metadata from Crossref (date 6 April 2008), abstract and author affiliations from OpenAlex; full text not accessible (ACM 403, no open copy). Clive Thompson, "Halo 3: How Microsoft Labs Invented a New Science of Play," *Wired* 15.09, August 2007, page 1 read via the Wayback Machine (Pagulayan, 3,000 hours, 600 players, square-foot deaths, the Microsoft-ownership quotation). ⚠️ **Not established:** which games the paper's two case studies used, and when TRUE was first used in production — neither could be read without the full text. The description of in-play attitudinal prompts and video synchronisation follows the abstract's "attitudinal, demographic, and contextual data" and the *Wired* lab account; its exact mechanics are not confirmed from the paper. That the *Halo 3* lab used TRUE by that name is not stated on the page read.
