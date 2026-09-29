# Lineage: Membership & Community Platforms

**Industry:** [[industries/membership-community-platforms|Membership & Community Platforms]]
**Wave:** [[series/eras/wave-10-creator-platform|10 — The Creator Platform]]
**The tool:** Discourse trust levels — the five-rung ladder (TL0 New, TL1 Basic, TL2 Member, TL3 Regular, TL4 Leader) that promotes a forum member automatically on measured reading and participation, and hands moderation powers to the higher rungs
**Builder:** Civilized Discourse Construction Kit
**Builder in vault:** [[industries/membership-community-platforms|Membership & Community Platforms]]
**Verification:** partial — see Sources

## The Problem That Came First

A community small enough to feel like one cannot afford to police itself professionally.

Classic forum software gave you two kinds of person: members and moderators. Moderators were appointed by hand, usually unpaid, and every new account arrived with the same powers as a ten-year regular — enough to spam, derail or harass on day one. The defences were more volunteers or a closed door.

On **5 February 2013** Jeff Atwood, announcing Discourse on his blog, put the state of the art bluntly: "all your software options for online community are, quite frankly, *terrible*", and asked whether forum software had "advanced at all in the last *ten years?*", setting 2000 and 2012 screenshots of the same forum side by side.

## What Got Built

A ladder that members climb by behaving like members.

Atwood's own description, *Understanding Discourse Trust Levels* (25 June 2018), gives the thresholds:

| Level | Name | How you reach it |
|---|---|---|
| TL0 | New | on sign-up |
| TL1 | Basic | 5 topics entered, 30 posts read, 10 minutes reading |
| TL2 | Member | 15 days visited, 1 like given and received, 3 replies, 20 topics, 100 posts read, 60 minutes reading |
| TL3 | Regular | over the last 100 days: half the days visited, replies in 10+ topics, a quarter of topics and posts read, 20 likes received, 30 given, no more than 5 flags |
| TL4 | Leader | manual promotion by staff only |

The purposes are stated in two lines: **sandbox new users** "so that they cannot accidentally hurt themselves, or other users while they are learning", and **grant experienced users more rights over time** "so that they can help everyone maintain and moderate the community". TL3 users can recategorise and rename topics, and a TL3 spam flag on a TL0 user's post hides it immediately.

Most of the measurement is *reading*: time spent and posts read.

## Who Built It, And Why Them

**Civilized Discourse Construction Kit, Inc.**, founded by Jeff Atwood, Robin Ward and Sam Saffron, and funded in 2013 by First Round, Greylock and SV Angel.

Atwood had co-founded Stack Exchange, and in the launch post he says what he learned there: if your goal is an excellent signal-to-noise ratio, "you *must* suppress discussion". Discourse was built to reverse that — to host discussion rather than inhibit it. That created the design problem trust levels answer: an open, discussion-first forum still needs moderation, and the people running such forums are the ones who cannot pay for it.

The business model sharpened it further. Discourse was released as "100% open source" under the GPL, with revenue planned from hosting on the WordPress pattern; by 2022 more than 3,000 instances used CDCK's official hosting. A product given away to be self-hosted by strangers cannot ship with a moderation staff. It has to ship with a moderation *mechanism* — one that works for a forum of fifty on a volunteer's server.

## What It Cost

**It rewards presence, not belonging.** The ladder measures visits, reads and likes; it cannot see whether a newcomer's first post was answered. A lurker who reads daily climbs; a newcomer ignored in week one never reaches the rung where anyone notices.

**It concentrates labour on the regulars.** The TL3 bar requires sustained activity over 100 days, so moderation power flows to the few who are already doing the most — the same people the vault identifies as burning out.

**The top rung stays manual.** TL4 is staff-only. The mechanism automates the middle of the community, not its governance.

## What You Still Touch

The ladder solved "who can we trust?" by counting activity, and left "who feels they belong?" to be measured by the same counters.

- [[problems/membership-community-platforms/low-impact-2|🟡 Moderation Tooling for Communities That Cannot Fund It]]
- [[problems/membership-community-platforms/high-impact|🔴 Retention Depends on Belonging and the Platform Counts Posts]] — activity counters, a decade on
- [[problems/membership-community-platforms/worker-life-2|🟢 The Volunteer Moderator Absorbing the Worst of It]]
- [[niches/membership-community-platforms/moderation-economics/profile|Moderation Economics]]
- [[niches/membership-community-platforms/first-fortnight-onboarding/profile|First-Fortnight Onboarding]]

**Sources:** Jeff Atwood, "Civilized Discourse Construction Kit", *Coding Horror*, 5 February 2013 (quotations, Stack Exchange lesson, open-source and hosting model, investors); Jeff Atwood, "Understanding Discourse Trust Levels", blog.discourse.org, 25 June 2018, updated December 2025 (thresholds and powers as currently documented — they may differ from the 2013 originals); Wikipedia, *Discourse (software)* (founders, CDCK, GPL, 1.0 release 26 August 2014, 2022 hosting figure). WebSearch was unavailable this session (budget exhausted); research was by WebFetch on known URLs; stackoverflow.com could not be fetched. ⚠️ **Not established:** when trust levels first shipped in Discourse, and whether they were modelled explicitly on Stack Exchange's reputation-gated privileges — the trust-levels post does not mention Stack Exchange, so the connection is drawn here only through Atwood's biography, not asserted as design lineage.
