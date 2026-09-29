# Live Commerce Platforms

## Profile
**Category:** Digital Commerce
**Market Size:** ~$50B US live shopping gross merchandise value, dominated by TikTok Shop with Whatnot leading the collectibles and specialty end
**Tech Maturity:** Streaming solved, commerce mechanics improvised — TikTok Shop, Whatnot, Amazon Live, Talkshoplive and the platform-native offerings deliver video reliably at scale. Matching a viewer to a stream in progress, moderating live, and handling inventory that sells out in seconds are all handled with machinery borrowed from adjacent problems.
**Workforce:** Live moderators, seller and host support staff, trust and safety reviewers, discovery and recommendation engineers, payments and fraud staff, category managers

## Key Pain Themes
Discovery is the category's binding constraint and it is unusually hard: a stream exists for a couple of hours, has no history, and its value to a viewer depends on what is happening in it right now. Recommendation systems built for a persistent catalogue have nothing to work with, and a stream with no viewers has no seller next week. Below that sit two operational problems the live format creates. Moderation must happen in real time, in video and chat simultaneously, where a violation is broadcast before anyone can review it — a fundamentally different problem from moderating a post. And checkout must survive a burst: a host announces a limited item and hundreds of people attempt to buy the same unit within seconds, which is an inventory and payments problem more like ticketing than like retail. The moderators and the hosts absorb the consequences, the latter running multi-hour shows single-handed while selling, entertaining and managing a chat.

## Current Tech Landscape
Video delivery is a solved commodity through standard streaming infrastructure. Discovery is the main technical investment and is largely inherited from short-form video recommendation, which optimises for watch time rather than for purchase intent. Real-time moderation combines automated audio and visual classification with human review, and the human review is necessarily after the fact. Checkout under burst is handled with queuing and inventory reservation borrowed from ticketing. Payments and fraud face an unusual pattern of impulsive high-velocity purchasing. Seller tooling — analytics, scheduling, inventory sync — is thin relative to what hosts need.

## Problems
- [[problems/live-commerce-platforms/high-impact|🔴 High Impact: Matching Viewers to Streams in Real Time]]
- [[problems/live-commerce-platforms/low-impact-1|🟡 Low Impact: Real-Time Moderation of Live Video]]
- [[problems/live-commerce-platforms/low-impact-2|🟡 Low Impact: Checkout and Inventory Under Burst]]
- [[problems/live-commerce-platforms/worker-life-1|🟢 Worker Life: Live Moderator]]
- [[problems/live-commerce-platforms/worker-life-2|🟢 Worker Life: Host Running a Four-Hour Show Alone]]
- [[problems/live-commerce-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/live-commerce-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
Live commerce is a marketplace where supply is perishable in a way no other commerce format is: a stream is available for two hours and then gone, its inventory with it. That makes matching a real-time problem with a hard deadline, and it makes the cost of getting it wrong absolute rather than deferred — an unwatched stream is not a delayed sale, it is a seller who does not return. The platforms hold second-by-second records of what was shown, said and bought, which is the richest behavioural commerce data anywhere, and use it primarily to rank streams by engagement.
