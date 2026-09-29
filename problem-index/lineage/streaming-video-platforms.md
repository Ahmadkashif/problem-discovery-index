# Lineage: Streaming Video Platforms

**Industry:** [[industries/streaming-video-platforms|Streaming Video Platforms]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** HTTP Live Streaming (HLS) — a video cut into short files listed in an .m3u8 playlist, with a master playlist of the same content at several bitrates for the player to switch between; Internet-Draft of 1 May 2009
**Builder:** Apple
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Streaming video used to need a streaming server.

The established way to send live or on-demand video was a dedicated media protocol, talking to specialised server software, often over UDP. It worked on a controlled network. On the open internet it met firewalls and proxies that let through web traffic and little else, and it needed server capacity that general web infrastructure did not provide. Worst of all, a stream was encoded at one quality: if the viewer's connection dropped below that bitrate, the picture stopped.

That last constraint was about to meet the phone. A handset on a cellular network sees its bandwidth change as the user walks down a street. A single-bitrate stream on that link is a spinner.

## What Got Built

On 1 May 2009, Roger Pantos of Apple submitted *draft-pantos-http-live-streaming-00* to the IETF: "a protocol for transmitting unbounded streams of multimedia data over HTTP." It shipped the following month with iPhone OS 3.0 and the iPhone 3GS.

The mechanism is almost aggressively plain:

- The encoder cuts video into **short segment files**, each an ordinary HTTP download.
- An **.m3u8 playlist** — an extended M3U playlist — lists the segments in order, with tags such as EXT-X-TARGETDURATION and EXT-X-MEDIA-SEQUENCE; a live stream is just a playlist that keeps growing.
- A **master playlist** lists the same content at several bitrates using EXT-X-STREAM-INF, and the player chooses, segment by segment, the highest one its connection can sustain.

Because everything is a plain HTTP file, it passes any firewall that passes the web, and any web cache or CDN can serve it without knowing it is video.

## Who Built It, And Why Them

Apple, because it had shipped a phone that had to play video over cellular data and owned the entire playback path on it — hardware, operating system, player and store.

Apple did not invent adaptive HTTP streaming. Per Wikipedia, Move Networks developed it between 2004 and 2006, and Microsoft demonstrated Smooth Streaming in 2008 and released it in 2009. Both were tied to their own servers or plug-ins. Apple's contribution was to make the smallest possible version and **publish it as an open Internet-Draft**, so that any encoder vendor, CDN or broadcaster could produce streams its devices would play. Owning the most desirable screen in the market, it could set the format by shipping it; publishing it cost nothing and recruited the supply side.

The standards bodies followed rather than led: Adobe released HDS in 2010, MPEG published DASH in April 2012, and HLS itself became RFC 8216 only in August 2017.

## What It Cost

**It traded latency for reach.** A player that waits for whole segments before switching sits several segments behind live — acceptable for a series, painful for sport, and the reason "low-latency" variants were later bolted on.

It also made quality a player-side guess. The server no longer knows what the viewer sees; each client picks its own bitrate from its own measurements, so a premiere night is millions of independent decisions hitting the same caches at once — and a failure shows up as every viewer's own buffering.

## What You Still Touch

Almost every streaming app on a phone or TV still asks for a playlist, then a short file, then another.

- [[problems/streaming-video-platforms/worker-life-2|🟢 The Reliability Engineer on Premiere Night]] — millions of players each choosing a bitrate at once
- [[problems/streaming-video-platforms/low-impact-2|🟡 Ad Tier Inventory and Frequency]] — ads spliced into the same segment list
- [[niches/streaming-video-platforms/streaming-reliability/profile|Streaming Reliability]]
- [[niches/streaming-video-platforms/ad-supported-tier-operations/profile|Ad-Supported Tier Operations]]

**Sources:** IETF Datatracker, *draft-pantos-http-live-streaming-00* (1 May 2009, R. Pantos, Apple Inc.; abstract quoted; EXT-X tags including EXT-X-STREAM-INF variant streams); Wikipedia, *HTTP Live Streaming* (released 2009; segment-and-playlist design; firewall traversal; RFC 8216, August 2017); Wikipedia, *Adaptive bitrate streaming* (Move Networks 2004–2006 and US patent 7,818,444; Smooth Streaming 2008 prototype and 2009 release; HLS June 2009 with iOS 3.0 and iPhone 3GS; HDS June 2010; DASH April 2012). ⚠️ **Not established:** a frequently repeated App Store rule requiring HLS, with a 64 kbit/s fallback, for video over cellular longer than ten minutes — not found in the current App Review Guidelines, and I could not reach the historical text; any Apple statement of why it published HLS openly (the "Why Them" argument is inference); how far Flash's absence on iPhone drove the design. The claim that ads are spliced into the same segment list is general industry practice, not sourced here. WebSearch was unavailable this session (session budget exhausted); research used WebFetch on known URLs only.
