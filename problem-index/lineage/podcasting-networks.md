# Lineage: Podcasting Networks

**Industry:** [[industries/podcasting-networks|Podcasting Networks]]
**Wave:** [[series/eras/wave-10-creator-platform|10 — The Creator Platform]]
**The tool:** the RSS `<enclosure>` element — one tag per feed item carrying a media file's URL, its length in bytes and its MIME type, introduced in RSS 0.92 (December 2000) and demonstrated on 11 January 2001 with a Grateful Dead song
**Builder:** UserLand Software
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Audio on the web was something you went and got.

By 2000 a weblog could syndicate text: RSS let a reader's software check a site on a schedule and pull new items without anyone visiting. A sound file had no equivalent. It sat at a URL. The listener had to know it existed, click, wait for the download and then move it somewhere they could play it. A recurring show — the thing radio had always been — could not recur on the web, because nothing delivered the next episode.

The format that did the delivering already existed. It simply had no place in it for a file.

## What Got Built

One element, three attributes.

In October 2000 Tristan Louis proposed, in a draft, that media files be attached to feeds. Dave Winer implemented the idea: RSS 0.92, published in December 2000, added `<enclosure>`, which "permitted audio files to be carried in RSS feeds." In the RSS 2.0 form it takes a `url`, a `length` in bytes and a `type`, and the specification recommends **only one enclosure per item**. On 11 January 2001 Winer demonstrated it on *Scripting News* by enclosing a Grateful Dead song.

The shape is the whole mechanism. A feed reader that sees an enclosure can fetch the file in the background, so the next episode is already on the device when the listener wants it. Everything later called podcasting — the word itself came from Ben Hammersley in February 2004; Adam Curry's *Daily Source Code* started that August; Apple added podcast support to iTunes 4.9 in June 2005 — ran on that tag.

## Who Built It, And Why Them

UserLand Software, the company Winer founded in 1988 and ran as CEO until 2002, because UserLand already controlled the format.

Winer had designed an XML syndication format for his *Scripting News* weblog in December 1997, and UserLand published successive RSS versions. That meant adding a field needed no committee, no vendor negotiation and no standards body — only a new version of a spec UserLand wrote and software UserLand shipped. A broadcaster wanting to distribute audio would have built a proprietary player and a subscription service; a format owner could add one element and let every feed reader inherit it.

In July 2003 Winer and UserLand assigned the RSS 2.0 copyright to Harvard's Berkman Center and froze the format. **Freezing it froze the enclosure too.**

## What It Cost

The enclosure delivers a file and reports nothing back.

Because the reader fetches the whole file and plays it offline, the publisher learns only that a request was made for a URL. Whether anyone pressed play, how far they listened, or whether the device downloaded the episode automatically and never opened it — none of that travels back through the feed. The whole measurement edifice of podcast advertising, including the download rule described in [[lineage/audio-adtech-networks|Lineage: Audio Adtech Networks]], exists to squeeze an audience figure out of a server log the enclosure was never designed to produce.

The one-enclosure recommendation, and an open format anyone could host, also meant no one owned the distribution. That openness is why independent shows can exist, and why a network has no default channel to the listener it could lean on.

## What You Still Touch

Every podcast app that "downloads new episodes" is reading an enclosure tag. And the reason a network cannot see whether listeners stayed past episode one is the same reason Winer's 2001 demo worked: the file left, and nothing came back.

- [[problems/podcasting-networks/high-impact|🔴 Show Audience Retention Prediction]] — the listening data the feed never returned
- [[problems/podcasting-networks/low-impact-2|🟡 Cross-Promotion Audience Overlap Analysis]]
- [[niches/podcasting-networks/audio-audience-measurement/profile|Audio Audience Measurement & Ratings]]
- [[niches/podcasting-networks/podcast-hosting-platform-analytics/profile|Podcast Hosting Platform Analytics]]

**Sources:** Wikipedia, *RSS enclosure* (Winer's late-2000 implementation; url/length/type attributes; one-enclosure recommendation); Wikipedia, *Podcast* (Tristan Louis's October 2000 draft; Hammersley coinage February 2004; *Daily Source Code* August 2004; iTunes 4.9 June 2005); Wikipedia, *RSS* (RSS 0.91 Netscape July 1999; RSS 0.92 December 2000 with enclosure; RSS 2.0 September 2002; copyright to Berkman July 2003); Wikipedia, *Dave Winer* (UserLand founded 1988, CEO to 2002; December 1997 format; 11 January 2001 Grateful Dead demo). This vault's `lineage/audio-adtech-networks.md` is cross-linked as vault material, not corroboration. ⚠️ **WebSearch was unavailable this session (session cap reached)**; the RSS 0.92 specification at backend.userland.com refused the connection, so the spec text itself was not read. ⚠️ **Not established:** the exact day RSS 0.92 was published; whether the enclosure was written by Winer alone or with other UserLand staff; Winer's own stated reason for adding it; and when "one enclosure per item" became the recommendation. The argument that a format owner could move faster than a broadcaster is interpretation, not a sourced finding.
