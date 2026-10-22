# The Sales Assistant and the Revision Storm

**Industry:** [[media-rep-firms|Media Representative Firms]]
**Type:** Worker Life Changing
**One-liner:** A rep sales assistant spends most of the day re-keying the same order into different station systems every time a buyer moves a week, swaps a spot length or changes a demo, and the work peaks exactly when political orders arrive.
**Tags:** #large-language-models #transformers #seq2seq #feature-engineering #worker-facing #automation #workflow-orchestration

## The Problem
Behind every national AE at a rep firm sits a sales assistant, sometimes one assistant to two AEs (estimate). Once a buy is placed, the assistant's day is revisions. The buyer cuts a week because the client's sale moved, adds a :15 version, shifts weight from early news to late news, or changes the demo after a creative test. Each change has to be reflected in the order in each station's traffic system, confirmed back to the buyer, and checked again when the station's traffic department reports what it could and could not clear. A single national buy can be revised many times over its flight (estimate), across every station in the buy, and where electronic order exchange is not set up for that agency–station pair, each revision is typed by hand.

The volume comes in waves. The end of each quarter compresses buyers' remaining budgets into a few weeks. In even years political orders land on top: candidate and issue spots with their own paperwork, priority over regular business and frequent late changes. Then the preemptions start, and the same assistant is finding makegood offers for the displaced regular advertisers.

## Why It Matters to the Worker
The job is typing, carried out under the pressure of someone else's money. A missed revision means a spot airs in a week the client cancelled. The station bills it, the agency refuses to pay, and the assistant spends days unwinding it with the station's traffic manager. Errors are visible, and blame flows downhill from the AE.

It is also a dead end the assistant can see. The assistant knows the stations, the buyers and the inventory better than anyone, which is the knowledge an AE needs, but there is no time left in the day to learn pricing or sit in on negotiations. Assistants burn out or leave the industry before they move up, and the rep loses the people it would otherwise have grown into sellers.

## What a Solution Looks Like
Revisions arrive as structured changes rather than emails. A model reads the buyer's revision email or the revised order from the buying system and produces a precise change list: which lines, which weeks, which stations. It applies the list to each station's order through whatever integration exists, or produces a ready-to-paste change set where none does. It tracks confirmation from each station's traffic department and shows the assistant one view of every open revision and its status across the buy, with the exceptions that need a human (an unclearable week, a conflict with a political order) at the top.

## Impact If Solved
Taking the re-keying out of revisions gives each assistant back hours a day in peak weeks (estimate), cuts the missed-revision disputes that eat the following month, and leaves time to learn the pricing and negotiation work that is the route to becoming an AE.
