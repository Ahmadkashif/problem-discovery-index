# Lineage: Security Awareness Training

**Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** PhishGuru — the embedded-training email system: a simulated phishing message whose link, when clicked, opens a short training intervention instead of a fake login page
**Builder:** Carnegie Mellon University
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Classroom security training did not survive contact with an inbox.

The cleanest demonstration came from the US Military Academy. Every semester West Point cadets received four hours of classroom instruction in information assurance. In 2004 Aaron J. Ferguson ran an exercise called the Carronade: 512 cadets, chosen at random, were sent an email from a fictional colonel in the Office of the Commandant saying their grade report had a problem and asking them to click a link. **About 80% clicked; among freshmen, about 90%.**

The finding was not that people were careless. It was that instruction delivered at a time the learner chose was not recalled at the moment the attacker chose. Training and threat happened in different places, and only one of them was the inbox.

## What Got Built

An email that teaches at the moment of failure.

PhishGuru, developed at Carnegie Mellon, sends a simulated phishing message in the ordinary course of someone's day. If the recipient clicks, the link does not lead to a credential form; it opens a brief training intervention explaining what the message was, which cues gave it away, and what to do next time. Kumaraguru, Rhee, Acquisti, Cranor, Hong and Nunge presented the design and evaluation at CHI 2007 as *Protecting People from Phishing: The Design and Evaluation of an Embedded Training Email System*.

The follow-up, *School of Phish* (SOUPS 2009), ran it in the wild with 515 participants. Trained users still did better after 28 days; a second training message improved results further; and training did not make people less willing to click links in legitimate email.

**The mechanic is the industry's product to this day:** send a lure, count who clicks, teach the clicker on the spot.

## Who Built It, And Why Them

Carnegie Mellon University — specifically its usable-privacy-and-security research group around Lorrie Faith Cranor, Jason Hong and Ponnurangam Kumaraguru.

The reason is disciplinary. An enterprise security team could send a fake phish, as West Point did; what it could not easily do was **run the controlled experiment** — randomised conditions, retention measured weeks later, false-positive effects on legitimate mail. That is a human-computer-interaction lab's native method, and it is what turned a stunt into a design with evidence behind it.

The commercial step followed directly. In June 2008 three CMU faculty — Norman Sadeh, Lorrie Cranor and Jason Hong — founded Wombat Security Technologies in Pittsburgh to sell the research. Proofpoint acquired Wombat in March 2018 for roughly $225 million. The university built the artefact; a spin-out sold it; an email-security vendor absorbed it.

## What It Cost

**The metric came bundled with the method.** A simulation that teaches on click also measures clicks, and click rate became the number programmes report upward. But the sender chooses the lure, so the sender controls the difficulty — a programme can make its trend line look however it likes by choosing easier or harder templates.

The second cost is to the employee. Embedded training works by catching people out; at scale that means repeat clickers, remedial lists and a workforce that experiences the security team as the source of the phishing.

## What You Still Touch

The "you clicked a simulated phish" landing page is PhishGuru's intervention, commercialised. So is the quarterly click-rate chart.

- [[problems/security-awareness-training/high-impact|🔴 Measuring Click Rate on a Test You Set the Difficulty Of]] — the metric that shipped with the mechanic
- [[problems/security-awareness-training/worker-life-2|🟢 The Employee on the Remedial List]]
- [[niches/security-awareness-training/phishing-simulation/profile|Phishing Simulation]]
- [[niches/security-awareness-training/difficulty-calibration/profile|Difficulty Calibration]]
- [[niches/security-awareness-training/the-employee-who-clicked/profile|The Employee Who Clicked]]

**Sources:** Ferguson, "Fostering E-Mail Security Awareness: The West Point Carronade," *EDUCAUSE Quarterly* 2005 (ERIC EJ846559), with Network World's account (512 cadets, 80% / 90% click rates, four hours of classroom instruction); Kumaraguru et al., *Protecting People from Phishing*, CHI 2007; Kumaraguru et al., *School of Phish*, SOUPS 2009 (515 participants, 28-day retention; via ACM DL, Semantic Scholar and CybSafe research-library summaries); Wombat Security founding (June 2008, Sadeh / Cranor / Hong) and Proofpoint acquisition (March 2018, ~$225m) from company-profile and press summaries. ⚠️ **Not established:** the exact date PhishGuru was first built or deployed before the CHI 2007 paper; the precise Proofpoint deal date and price from a primary filing; and the founding details of PhishMe, the other early commercial simulated-phishing vendor — searched only in passing, so it is not dated or credited here, and CMU's priority over it as a *commercial* offering is not claimed.
