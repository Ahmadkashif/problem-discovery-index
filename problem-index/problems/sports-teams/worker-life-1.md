# The Video Coordinator's Overnight Breakdown

**Industry:** [[sports-teams|Sports Teams & Clubs]]
**Type:** Worker Life Changing
**One-liner:** After every game and before every opponent, a video coordinator cuts and tags hundreds of plays by hand, often overnight, and gets back the hours that should go to learning the game they want to coach.
**Tags:** #cnns #transformers #object-detection #evaluation-metrics #worker-facing #automation #workflow-orchestration

## The Problem
In the NBA and NHL, and in college football and basketball, the video coordinator is the first person in the building after a game and the last to leave before the next one. After a game they cut every possession or shift and tag it: play type, coverage, pick-and-roll defence, zone entry, the players on the floor, the result. Before the next opponent they do the same to the opponent's last several games, then build the clip packages each coach asked for. A basketball game has ~200 possessions and a hockey game hundreds of zone entries and faceoffs. On a back-to-back, the work runs through the night on the plane.

Tools such as Hudl Sportscode, Catapult Pro Video and Synergy speed up cutting and offer some automatic tagging from tracking data. But coaches use their own play names and tag definitions, and those differ from the league's event feed. So the coordinator still checks and retags most of what the tool proposes, and builds the coach's packages by hand.

## Why It Matters to the Worker
Video coordinator is the classic entry point to a coaching career, and the job's hours crowd out the part that makes it one. Coordinators in season work ~80–100-hour weeks (estimate), often for modest pay, and the work that fills them is mechanical: scrubbing to a timestamp, typing a tag, exporting a clip. The value they could add, seeing a pattern in the opponent's late-clock sets and telling the assistant coach about it, needs the hours that tagging takes.

Mistakes are visible. A mis-tagged play in a scouting package becomes the wrong clip in a pregame meeting, in front of the head coach.

## What a Solution Looks Like
Automatic tagging that learns the staff's own vocabulary. The club's video and tracking data feed a model trained on the coordinator's past tags. It proposes a tag for every play, with confidence, and asks the coordinator to check only the uncertain ones. Coaches' clip requests are written in plain language ("every high pick-and-roll they ran against a drop coverage in the fourth quarter") and assembled automatically. Corrections feed back, so the tags drift toward the staff's own definitions over a season. Any demo outside the club's own licensed game film runs on consented or synthetic footage.

## Impact If Solved
If auto-tagging removes ~4–6 hours of manual work per game and per opponent breakdown (estimate), a coordinator on an 82-game schedule gets back several hundred hours a season. Those hours go to the analysis and coaching apprenticeship the job is supposed to provide, and the error rate in pregame packages falls.
