# Lineage: Penetration Testing Firms

**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** SATAN (Security Administrator Tool for Analyzing Networks) — a free, browser-driven Unix network vulnerability scanner released 5 April 1995
**Builder:** Dan Farmer & Wietse Venema
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Checking whether a networked Unix host could be broken into took an expert, by hand, one service at a time.

By the early 1990s the knowledge of how intrusions actually worked lived in two places: in the heads of intruders, and in a small number of administrators who had studied them. Everyone else could read CERT advisories, which said *that* something was a problem, not how an attacker would chain harmless-looking services — finger, NFS exports, anonymous ftp, NIS — into a shell. Farmer and Venema's own framing, posted to Usenet on 2 December 1993, was that "many sites appear to lack the resources to assess what level of host and network security is adequate."

The expensive step was not fixing holes. It was knowing which ones you had, and the only method was a person who thought like an intruder spending hours probing.

## What Got Built

A program that did the probing for you and told you what it found.

SATAN, written mostly in Perl, took a target host or subnet, remotely queried the network services it exposed, collected what they volunteered about machine types and configuration, and matched the results against known vulnerabilities. Its interface was a web browser — Netscape, Mosaic or Lynx — with forms to enter targets, tables of results, and a tutorial attached to each problem explaining why it mattered and how to close it. It was released free on **5 April 1995**, with documentation art by Neil Gaiman and a `repent` command that renamed it SANTA.

That results table is the ancestor of the modern pen-test deliverable: a list of hosts, a list of findings, an explanation per finding.

## Who Built It, And Why Them

**Dan Farmer and Wietse Venema**, two individuals, not a firm.

Farmer had already written COPS at Purdue in 1989 under Gene Spafford — a set of small local checkers for Unix misconfiguration. Venema, at Eindhoven University of Technology, had written TCP Wrapper. Their 1993 paper, *Improving the Security of Your Site by Breaking Into It*, promised "to look through the eyes of a potential intruder" and announced that while writing it "we wrote SATAN." The tool was the paper, executable.

Why them and not a vendor: the knowledge was attacker knowledge, and in 1993–95 no company wanted to be seen distributing it. That was demonstrated at release. *TIME* reported on 17 April 1995 that Silicon Graphics, Farmer's employer, told him in March to abandon publication or lose his job; he published and was let go. Only people willing to absorb that cost, and who held the knowledge personally, could ship it. Bill Cheswick's defence in the same article carried the argument: "The bad guys already have these tools."

## What It Cost

**A scanner reports what it found. It cannot report what it never looked at.**

SATAN checked a fixed list of known conditions against the hosts it was pointed at. A clean result meant those checks passed on those targets. The paper itself was explicit about the limit — it did not cover social engineering or password cracking, and said of a partially probed host, "Have you uncovered all the holes on your target system? Not by a long shot." That caveat lived in the prose; the results table carried none of it.

The shape stuck. Once assessment could be automated into a findings list, the list became the product, and the human engagement that later grew around it — the time-boxed manual test — inherited the same format: findings with severities, and silence about coverage.

## What You Still Touch

Every pen-test report that opens with a table of findings and a disclaimer is SATAN's output with a tester between the scanner and the client. The disclaimer is the 1993 caveat, still outside the table.

- [[problems/penetration-testing-firms/high-impact|🔴 A Time-Boxed Sample Reported as an Assessment]] — a findings list that cannot state coverage
- [[problems/penetration-testing-firms/worker-life-2|🟢 The Engineer Handed Eighty Findings]] — the results table, scaled up
- [[problems/penetration-testing-firms/low-impact-2|🟡 Report Production and Finding Triage]]
- [[niches/penetration-testing-firms/coverage-measurement/profile|Coverage Measurement]]
- [[niches/penetration-testing-firms/report-production/profile|Report Production]]

**Sources:** Farmer & Venema, *Improving the Security of Your Site by Breaking Into It*, Usenet comp.security.unix, 2 December 1993, text read directly via cyberwar.nl mirror (affiliations Sun Microsystems / Eindhoven University of Technology; "lack the resources to assess"; "we wrote SATAN"; exclusion of social engineering and password cracking; "Not by a long shot"); Wikipedia, *Security Administrator Tool for Analyzing Networks* (5 April 1995 release, Perl, browser interface, Gaiman art, `repent`); Wikipedia, *Dan Farmer* (COPS 1989 at Purdue under Spafford; SGI termination); *TIME*, "The Devil in the Network", 17 April 1995 (SGI ultimatum in March, Cheswick quote); TidBITS, 20 March 1995 (planned 5 April release, beta circulating). ⚠️ **Not established:** the reason SGI gave — one secondary account ties it to a Justice Department inquiry, which I did not confirm; Venema's authorship of TCP Wrapper is stated from general knowledge and the paper's appendix reference, not a dated primary source. I did not establish a documented causal line from SATAN's report format to commercial pen-test report templates; that link in "What It Cost" is inference from structure. The builder is keyed as two named individuals because no firm existed at build time.
