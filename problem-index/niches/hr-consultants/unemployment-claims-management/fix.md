# Hearing Reps Know What Each Referee Wants and Nobody Wrote It Down

**Niche:** [[niches/hr-consultants/unemployment-claims-management/profile|Unemployment Claims Management]]
**Industry:** [[industries/hr-consultants|HR Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** The difference between winning and losing a hearing is knowing how that particular referee runs one, and it lives entirely in the representative who has appeared before them.
**Tags:** #tacit-knowledge-ml #large-language-models #data-integration #worker-facing #automation

## The Problem
A hearing representative who has worked one state for five years knows things that decide cases. That this referee will not accept a written warning without a signature acknowledging receipt. That this office weighs the final incident heavily and treats prior history as background. That in this state, "misconduct" turns almost entirely on whether the employee was warned that the specific behaviour would result in termination. That this referee lets employer witnesses speak and this one will cut them off.

None of it is written anywhere. It shapes how the representative prepares the employer witness, which documents they lead with, and how they frame the separation — which is most of the outcome.

When that representative leaves, and turnover is significant because the work is high-volume and the pay is not, it goes with them. The next person rebuilds it hearing by hearing, losing cases along the way that the departed colleague would have won.

## Why It's Still Broken
The case file records what happened, not what was learned. Determination, appeal, outcome, and the documents filed — all captured. The representative's read on why it went that way is not, because no field exists for it and no part of the process asks.

Volume makes it worse. A representative may handle several hearings a day. Debriefing after each one is time that produces no billable output, and the operation is measured on throughput and win rate, not on knowledge captured.

There is also a status dimension. Knowing the local terrain is what makes a senior representative valuable, and nothing in the compensation structure rewards making that knowledge portable. Nobody withholds deliberately; there is simply no pull.

## What a Fix Looks Like
Capture the post-hearing read as structured, reusable knowledge.

**A two-minute structured debrief.** After each hearing: what the referee focused on, what evidence carried weight, what was rejected and why, what the representative would do differently. Constrained fields with a short free text, filled in on the way out. That is a realistic ask; a written narrative is not.

**Notes attached to the referee and the office.** This is where the value concentrates. Referee-level and office-level patterns, accumulated across representatives and years, so a rep walking into an unfamiliar office arrives with what the firm collectively knows about it. Nothing about this is improper — it is preparation, the same as reading a judge's prior rulings.

**Positions that worked, indexed by separation type and state.** How the firm successfully framed a voluntary quit with good cause in this state, with the argument and the outcome. Retrieval by the situation a rep is preparing for, not by claim number.

**Check the folklore against outcomes.** With debriefs and determinations both structured, patterns that representatives believe can be tested. Some will hold and become firm knowledge; some will turn out to be superstition, which is equally worth knowing.

**Feed it into preparation.** Before a hearing, the rep should see what the firm knows about this office, this referee, and this separation type in this state. That is the payoff, and it is what makes people fill in the debrief.

## Who Feels the Pain
New representatives, learning by losing. Senior representatives, who are the firm's capability and cannot be replicated. Operations, watching win rate vary by who is available. And employers, whose tax rate depends on which representative drew their hearing.

## Impact If Fixed
Win rate is the product, and it currently varies by tenure in a role with high turnover. Making the local knowledge collective compresses the ramp on new representatives, raises the floor across the book, and turns a capability that walks out the door into one the firm actually owns — built from a debrief that takes two minutes after work the firm is already doing.
