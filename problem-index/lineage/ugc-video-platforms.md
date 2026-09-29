# Lineage: UGC Video Platforms

**Industry:** [[industries/ugc-video-platforms|UGC Video Platforms]]
**Wave:** [[series/eras/wave-10-creator-platform|10 — The Creator Platform]]
**The tool:** YouTube Content ID — a fingerprint of every upload matched against reference files supplied by rights holders, each of whom pre-selects what happens on a match: block the video, track its views, or run ads and take the revenue
**Builder:** Google
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A video site that lets anyone upload has no idea what it is hosting until someone complains.

The legal shape of the complaint was already fixed. Under the DMCA safe harbour, a host that removes material when notified is shielded, so the unit of enforcement was a notice about one clip, sent by a rights holder who had to find that clip first. That breaks when a catalogue owner must search a site growing by the hour, title by title, and the clip reappears the next day.

The complaint arrived in its largest form in **March 2007**, when **Viacom filed a US$1 billion lawsuit against Google and YouTube**, citing more than 150,000 unauthorised clips viewed about 1.5 billion times. Google had announced the purchase of YouTube on **9 October 2006** and closed it on **13 November 2006**, for US$1.65 billion in stock. It had bought the complaint along with the site.

## What Got Built

A matching system that runs before anyone complains.

Rights holders upload reference files. Every new video is fingerprinted and compared against that library. On a match, the system does not ask anyone; it applies the policy the rights holder chose in advance:

- **Block** the video
- **Track** it, keeping the viewing statistics
- **Monetise** it, running ads with the revenue going to the rights holder

YouTube began trials of automatic detection in **June 2007**, under the name **"Video Identification"**. Google's own blog carried a post titled *"Latest content ID tool for YouTube"* on **15 October 2007**; Wikipedia's article on the Viacom case dates the filtering system's implementation to early 2008. The system later took the name Content ID.

The third option is the one that made the tool. Blocking removes a liability. Monetising turns an infringing upload into licensed inventory the rights holder is paid for, without the uploader's consent.

## Who Built It, And Why Them

Google, because it was Google that stood to lose.

YouTube before the acquisition had licensed matching technology from **Audible Magic**, which says it licensed a "Content ID" technology to YouTube in 2006 and later sued when Google trademarked the name in 2014. But Audible Magic's product was audio identification sold to anyone. What was built after October 2006 answered a narrower question — how does the owner of the world's largest video site turn a billion-dollar lawsuit into a revenue share? — and only the owner had reason to build that. Wikipedia credits the system to Google. Its reported cost was **US$60 million by 2016** and **at least US$100 million by 2018**.

That cost is also why the tool took this shape. A system this expensive only pays back if the matches can be monetised, and monetisation only works if large catalogue owners sign up. So eligibility was restricted to uploaders meeting criteria that, in practice, limit direct use to large companies and the agencies that represent them.

## What It Cost

**The rights holder decides.** When an uploader disputes a claim, the dispute goes to the party claiming the copyright, which has the final decision. Only since **April 2016** have disputed videos continued to earn while the dispute runs.

**Nobody checks for fair use before the action.** Matching is automatic and applies policy without human review, which is how a white-noise video received copyright claims in January 2018.

**The claim is an asset, so it attracts fraud.** In 2021 two men were charged with using a fake company, MediaMuv, to claim about 50,000 songs, collecting US$20,776,517.31 in royalties; one received a 70-month sentence in June 2023.

## What You Still Touch

A creator's video is claimed within minutes, its revenue moves to someone else, and the appeal goes to the claimant. That is a policy the rights holder set in advance, applied by a machine, and reviewed by the party it benefits.

- [[problems/ugc-video-platforms/low-impact-1|🟡 Copyright Matching and Weaponised Claims]] — the direct descendant of pre-set match policies
- [[problems/ugc-video-platforms/high-impact|🔴 Livelihood Decisions Made by Systems That Cannot Explain Themselves]]
- [[niches/ugc-video-platforms/copyright-matching-and-claims/profile|Copyright Matching & Claims]]
- [[niches/ugc-video-platforms/appeals-and-redress/profile|Appeals & Redress]]

**Sources:** Wikipedia, *Content ID* (June 2007 trials, "Video Identification", Google as developer, block/track/monetise, dispute procedure, April 2016 change, cost and payout figures, white-noise and MediaMuv cases, Audible Magic trademark suit); Wikipedia, *Viacom International Inc. v. YouTube, Inc.* (March 2007 filing, US$1 billion, 150,000 clips, "early 2008" implementation); Wikipedia, *History of YouTube* (acquisition dates and price); Google Official Blog, "Latest content ID tool for YouTube", 15 October 2007 (title and date only — the post body did not load, so its contents are not relied on). WebSearch was unavailable this session (budget exhausted); research was by WebFetch on known URLs. ⚠️ **Not established:** the names of the Google/YouTube engineers who designed the system; whether any Audible Magic technology remained inside the 2007 system; the exact public launch date — the June 2007, October 2007 and "early 2008" dates come from different sources and are reported as such.
