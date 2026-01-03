# Interview: James Richardson - Data Analytics CRO

## Metadata

**Date:** November 14, 2024
**Duration:** 32 minutes
**Interviewer:** Sarah Chen, Enterprise Sales Director, Salesloft + Clari
**Interviewee:** James Richardson, Chief Revenue Officer, Data Analytics (Acme Analytics)
**Company:** Acme Analytics
**ARR:** $280M
**Industry:** Enterprise Data Analytics & BI Platform
**Interview Format:** Exploratory discovery call - pain points in modern sales operations

---

## Interview Transcript

**[SARAH]** Hi James, thanks so much for taking the time. I know how busy things are on the revenue side, especially at your scale. We're really just trying to understand how the sales landscape has shifted for enterprise data analytics companies, and given Acme's growth trajectory, I thought you'd be a perfect person to talk to.

**[JAMES]** Absolutely, happy to be here. You know, it's been a wild few years for us. We've gone from $120M to $280M ARR in about 36 months, so we've seen basically every market dynamic play out in real time. I'm curious what angle you're coming from with Salesloft.

**[SARAH]** We're really focused on helping revenue teams navigate this period where—and I think you'll relate to this—cloud bundling is shifting everything. You've got AWS, Azure, Google Cloud all bundling in analytics capabilities. You've got open-source solutions exploding in adoption. And then the whole sales-to-CS handoff is getting messier because CS is starting to own signals that used to be purely a sales responsibility.

**[JAMES]** *laughs* Okay, so you're describing basically every board conversation I've had in the last 18 months. Let's start with cloud bundling because that's probably the existential question for us right now. We compete directly against AWS Analytics, Databricks on Snowflake, Azure Synapse—all of these are either free or deeply embedded in someone's infrastructure bill already. How do you even sell against that?

**[SARAH]** That's the hard question. Walk me through—when you're losing deals to bundled solutions, what's the message they're hearing? Is it "I get it for free," or is there something else?

**[JAMES]** It's multi-layered. First, it's definitely the free tier or the "it's already in our contract" angle. But the more insidious part is the infrastructure argument. A CTO tells us, "Look, we're paying AWS $2 million a year anyway. Why would we pay Acme $500K for something that's incrementally better when we can just lean into what we've got?" And honestly, they're not entirely wrong. Our product is better—better UX, better time to insight, better data governance—but it's not 10X better. It's maybe 2 or 3X better on specific use cases.

**[SARAH]** So differentiation is getting harder to articulate?

**[JAMES]** Much harder. Five years ago, we could say, "We're the only platform that does real-time analytics at scale with sub-second latency." Now you can get 95% of that with Snowflake and some engineering work. So we've had to shift to value quantification. Like, we're telling customers, "For every $1 you spend with us instead of vanilla Snowflake, you save $4 in BI tool spend and engineering time because your analysts are 3X more productive."

**[SARAH]** Are customers buying that, or are they asking you to prove it?

**[JAMES]** They're asking us to prove it. Which is good—it keeps us honest—but it extends the sales cycle by 30-40%. We need a lot more technical proof of concept time, we need to validate against their specific data sources and workflows. It's eating up our team's time in a big way.

**[SARAH]** Let me shift to open-source for a second, because I think that's an interesting contrast. You're dealing with both—cloud bundling from the enterprise vendors, but also open-source solutions like Presto, Apache Druid, things like that gaining traction. How's that playing out for you?

**[JAMES]** Open-source is actually a different animal. With cloud bundling, you're competing against a vendor's balance sheet. With open-source, you're competing against... basically free, but with TCO messaging as your only real weapon. We tell customers, "Yeah, you can spin up Apache Druid. You can probably get 80% of what you need in the first six months. But then you're going to spend $3 million in engineering costs, you'll have no support for critical outages, and you'll have key person risk if your one Druid expert leaves the company."

**[SARAH]** Does that land?

**[JAMES]** Sometimes. The problem is we're competing against startups who have all-in-one solutions built on Presto or DuckDB, and they're charging $50K a year for a fully managed experience. We're at $500K minimums. So we lose the mid-market to them, and we're fighting harder for the enterprise. It's a wedge play, right? They get customers on the cheap now, those customers get comfortable with the architecture, and then we can't displace them later because switching costs are higher than our incremental value.

**[SARAH]** Okay, so we've got compression on both ends—cloud bundling from above, open-source wedges from below. Let me ask about something that I think is less discussed but equally important. You've got Clari's visibility into your customer health scores. You've probably got CS reaching out to you when they see usage patterns that might indicate expansion opportunity or churn risk. How's that collaboration working in your organization?

**[JAMES]** *pauses* This is where it gets interesting because—and I'll be honest, this is a frustration of mine—CS has all this data, but the data sharing and alert systems aren't where they need to be. We have a business review cadence where CS tells us, "Hey, customer X is showing strong usage on our advanced analytics module," but that's happening quarterly. By the time we find out, the customer has either already decided to go deeper or they've started using a competing tool.

**[SARAH]** What would ideal look like for you?

**[JAMES]** Real-time signals. We need an alert system where if a customer in a specific segment is hitting certain usage thresholds—like they're doing more than 50 queries a day on our predictive analytics module—we get notified immediately. Our sales team should be able to have a proactive conversation about expansion before the customer even has to ask. And not just usage signals—we need to see product feedback, feature requests, support ticket patterns. That's expansion gold.

**[SARAH]** Are you building that right now?

**[JAMES]** We're trying to. We've got some Salesforce automation that's... okay. But it's fragile. It requires a lot of manual updating from CS. What we really need is a native integration between Clari, our product analytics backend, and Salesforce that just automatically pipes signals to our sales team. Frankly, that's a problem Salesloft probably understands better than we do.

**[SARAH]** We do. And I think that's a massive opportunity because you're hitting something that every single enterprise is struggling with—the sales-CS collaboration layer. But let me drill into expansion specifically, because I want to ask about something I've heard from other data analytics leaders. Expansion revenue as a percentage of total growth has declined year-over-year for a lot of players in your space. Is that showing up in your numbers?

**[JAMES]** *grimaces* Yeah. Last year, expansion was 32% of our net new ARR. This year we're running at 18%, and the trend is getting worse. It's the perfect storm. One, you've got product usage patterns that have plateaued. Customers aren't ramping on features the way they used to. Two, competitive pressure is insane. Customers are getting contacted by five different vendors with "cheaper" solutions. And three—and this is the biggest—our pricing model hasn't kept pace with the changing competitive landscape.

**[SARAH]** Explain that last part.

**[JAMES]** So we tier pricing on data volume. You pay based on how many GB of data you're storing and querying per month. That made sense when we were a premium product for enterprises processing petabytes. But now Snowflake is cheaper per GB, and customers are getting smarter about managing their data footprint to reduce costs. So they're not expanding—they're optimizing their usage downward to stay within their budget tier. That sounds counterintuitive to what you'd think should happen, but it's real.

**[SARAH]** Have you thought about a different pricing model?

**[JAMES]** All the time. We've experimented with seat-based pricing, consumption-based, even value-based models. But here's the catch-22: if you move to consumption-based and the market doesn't follow, you're leaving money on the table from your existing customers who are locked into volume-based. And if you change pricing for new customers only, you get angry renewal conversations with your installed base. So we're kind of stuck in a matrix where our pricing was right for the market five years ago, and now it's a handicap.

**[SARAH]** That's a hard spot. Which brings me to discounting, because I imagine if expansion is contracting and competition is up, your sales team is probably getting a lot of pressure to negotiate.

**[JAMES]** *laughs bitterly* Yeah, and that's where things get messy internally. We've had to completely rethink our discount approval workflows. Three years ago, anything under 20% discount was fine. Now we're seeing ASP compression of 35-40% in competitive deals. So we created new approval workflows—everything over 15% has to go through our VP of Sales, everything over 25% goes to me. But here's the problem: you create friction in the process, and your reps feel like you don't trust them. They start to work around the system. I've found deals where reps are bundling in free services to avoid the discount policy. That's worse because now we've got no visibility into true ASP.

**[SARAH]** What's your guidance to the team on when to discount?

**[JAMES]** We've been trying to implement value selling training, but that's been harder than I expected. It's not because our team isn't capable—it's that customers are increasingly commoditizing the conversation. They come in with five quotes from different vendors, they're comparing features on a spreadsheet, and they want to know the price. You can run the best value selling workshop in the world, but if the customer is coming in with a predetermined budget and three alternative options, you're negotiating. You're not selling.

**[SARAH]** Have you found any discount guidelines that actually work?

**[JAMES]** The ones that work are specific to customer segment and contract size. For enterprise deals above $500K, we allow more flexibility because the lifetime value is there. For SMB and mid-market, we're more rigid because volume and churn is a bigger factor. We also tie discounts to expansion commitments—like, "We'll give you 20% off year one if you commit to expanding module usage in year two." That's been somewhat effective, but again, it requires your sales team to actually have conviction in the value, and when you're facing five competitors in a bake-off, conviction is hard to maintain.

**[SARAH]** Let me back up and ask about the big picture. When you look at all these pressures—the cloud bundling, the open-source wedges, the expansion challenges, the discounting pressure—how are you thinking about your go-to-market strategy evolving?

**[JAMES]** Honestly, we're in a transition year. We've realized that trying to compete on feature parity with cloud giants is a losing game. So we're doubling down on three areas: one, vertical specialization. We're going to own specific verticals like financial services and healthcare where our governance and compliance story is way stronger. Two, we're building a partner ecosystem because we can't do everything ourselves, and partners can help us land higher in the organization. And three—and this is the biggest shift—we're investing heavily in product-led growth. We're launching a free tier, which is terrifying for our enterprise sales team, but we're learning that the market has fundamentally shifted. Enterprise deals don't start with enterprise buyers anymore. They start with a data analyst downloading our free version.

**[SARAH]** How's that landing with your sales organization?

**[JAMES]** Mixed bag. Some of my sales leaders get it. Others are worried about cannibalization and channel conflict. But I think they're missing the forest for the trees. Yes, you might lose some deals to the free tier. But you're also getting a 10,000-person pipeline of people who are already familiar with your product, who are already buying in on the value, and who just need someone to help them navigate the enterprise procurement process. That's actually a way better sales motion than cold calling a CTO and trying to convince them to run a proof of concept.

**[SARAH]** Speaking of cold calling and demand generation, how's that working for you right now?

**[JAMES]** Demand gen has been our biggest challenge. You can spend $10K on a campaign and get 50 MQLs and maybe 3 of those turn into real opportunities. The conversion rates are down 40% from two years ago. There are a few reasons: one, the market is saturated. Everyone's doing the same campaigns. Two, your target buyers are more informed and more skeptical. Three, and I think this is underrated, your competitors are out-marketing you. Databricks is spending like crazy, Snowflake has massive brand awareness, and we're fighting for mind share against more well-funded companies.

**[SARAH]** What's working for demand gen?

**[JAMES]** Community and content. We launched a really strong thought leadership program where we're getting our engineers on podcasts talking about real problems in data engineering. That's generating genuine pipeline. We're also investing in events—not the big tradeshows, but smaller, vertical-specific workshops where we can have deeper conversations. And we're doubling down on partner and customer referrals because those have the highest quality pipeline.

**[SARAH]** Okay, let me ask a specific question about Salesloft and Clari and how you're using revenue intelligence. How deep are you into your revenue stack?

**[JAMES]** We use both. Clari for forecasting and health scoring, Salesloft for activity management and engagement. Honestly, they're not as integrated as they should be. I want a system where I can see a customer's health score and immediately know what actions my sales team has taken in the last 30 days, what emails have been sent, what calls have been logged. Right now I'm clicking between tools.

**[SARAH]** What would change if that integration was tighter?

**[JAMES]** We'd spend less time in status updates and forecasting meetings. We'd have way more visibility into what's actually happening with customers. And we'd be able to train our team better because we could see patterns. Like, "Hey, this rep's emails get 45% open rates when they do X, but 20% when they do Y." That's real coaching material.

**[SARAH]** Have you thought about what it would take to move the needle on expansion revenue?

**[JAMES]** *leans back* Yeah, a lot actually. I think it takes four things. One, better data about what customers are doing inside our product and how that maps to expansion opportunity. Two, a disciplined cross-sell motion—right now we're reactive. A customer asks about a module, we sell it. We should be proactive. Three, pricing flexibility or at least more options. And four, and this is the hardest—a real commitment from our product team to build features that actually drive expansion. We have a lot of features that are nice-to-have but don't unlock new use cases. We need to be more ruthless about what we build.

**[SARAH]** On the pricing flexibility front, have you considered moving to an annual plan model with quarterly business reviews?

**[JAMES]** We do quarterly business reviews now, but they're more report-out than upsell engine. The issue is we haven't fully separated pricing discussions from expansion discussions. When you bring up pricing, customers immediately think you're trying to raise their rates. We need a model where expansion is a conversation about value and usage and new capabilities, and pricing is a separate conversation about what that's going to cost.

**[SARAH]** That makes sense. Last question for you, and then I'll let you go: if you had a magic wand and could change one thing about how sales and go-to-market works in your organization, what would it be?

**[JAMES]** *thinks for a moment* Honestly? I'd solve the data and insights problem. Right now, every decision I'm making is one step behind reality. By the time I see a trend in Clari, the problem has been happening for two months. By the time my team reports on what's happening in deals, there's been a week of delay. I want to live in a world where my entire revenue team has real-time visibility into what's happening with customers—not just in CRM, but in product, in support, in the customer's bill. Give me that, and I think we can make dramatically smarter decisions about how we sell, who we focus on, what we prioritize. That's where I think Salesloft and the broader revenue intelligence space can actually move the needle.

**[SARAH]** That's a really clear articulation. I think we can help with that. What I'm hearing is that you need better integration between your sales, CS, and product data, more real-time signals, and a way to operationalize those signals so your team can actually act on them.

**[JAMES]** Exactly. And I need to do it without adding a bunch of operational overhead. We're not going to hire 20 new people in revenue operations. It's got to be more efficient and more automated.

**[SARAH]** Got it. I'm going to send you a proposal outlining how we could build that out, and I'd love to schedule a follow-up with you and your VP of Sales to walk through specifics. There might be some custom work required, but I think we have a path.

**[JAMES]** Sounds good. I appreciate the conversation. This has been really helpful—nice to talk to someone who actually understands the dynamics we're facing.

**[SARAH]** My last thing: I'll also connect you with two other enterprise data analytics companies we work with. Both are dealing with similar expansion challenges and cloud bundling pressure. Might be useful to hear how they're approaching it.

**[JAMES]** That would be great. Always good to know you're not alone in this.

**[SARAH]** Thanks again, James. We'll follow up with that proposal by end of week.

**[JAMES]** Perfect. Looking forward to it.

---

## Key Takeaways

### Competitive Dynamics
- **Cloud Bundling Pressure:** Customers are choosing bundled solutions from AWS, Azure, and Google Cloud despite inferior differentiation, citing infrastructure consolidation and existing contracts. Acme must shift from feature parity to value quantification (saving customers $4 for every $1 spent with Acme).
- **Open-Source Wedges:** Mid-market is being captured by cheaper all-in-one solutions built on Presto/DuckDB. Open-source requires TCO messaging around support, key person risk, and total cost of ownership, but Acme is losing wedge deals to $50K startups.
- **Demand Generation Saturation:** Market is saturated with similar campaigns. Conversion rates down 40% YoY. Community, thought leadership, vertical events, and partner referrals are the only high-ROI channels.

### Expansion Revenue Decline
- **Product Usage Plateaus:** Customers are not ramping on new features; instead, they're optimizing usage downward to stay within budget tiers.
- **Pricing Model Misalignment:** Current per-GB pricing model is disadvantageous in a competitive market where customers want to reduce costs. Pricing has not evolved with market dynamics.
- **Reactive Motion:** Cross-sell is reactive—customers ask about modules rather than sales proactively selling expansion. No disciplined expansion revenue machine.
- **Expansion ARR Impact:** Expansion revenue declined from 32% of net new ARR to 18% YoY. Trend accelerating downward.

### Sales Operations & Discounting
- **ASP Compression:** Sales team facing 35-40% discount pressure in competitive deals. Standard discounts have escalated from 20% (three years ago) to requiring approval at 15%+ to avoid devaluation.
- **Broken Discount Workflows:** Approval processes create friction; sales teams work around guardrails by bundling services. No visibility into true ASP.
- **Value Selling Challenges:** Sales team training on value selling is ineffective when customers come armed with spreadsheets comparing five vendors and predetermined budgets.
- **Segment-Based Guidelines:** Discount flexibility works better when tied to contract size (>$500K enterprise gets more flex) and expansion commitments ("20% off Year 1 if you commit to expansion in Year 2").

### Sales-CS Collaboration Gaps
- **Delayed Signals:** CS data sharing happens quarterly via business reviews, creating two-month lag before sales acts on churn/expansion signals.
- **Missing Real-Time Alerts:** No automated alert system when customers hit usage thresholds that indicate expansion opportunity. Sales team is reactive rather than proactive.
- **Integration Deficiencies:** Clari and Salesloft are not tightly integrated. Manual clicking between tools for health scores, activity logs, and email engagement metrics.

### Go-to-Market Evolution
- **Vertical Specialization:** Shifting from horizontal cloud competition to vertical specialization (financial services, healthcare) where governance and compliance value is defensible.
- **Product-Led Growth Transition:** Launching free tier to build bottom-up adoption pipeline. Enterprise sales organization initially skeptical about cannibalization, but recognizing free tier creates informed 10K-person pipeline.
- **Partner Ecosystem:** Building partnerships to extend reach and land higher in customer organizations, offsetting limitation of direct enterprise sales motion.

### Immediate Priorities for James
1. **Better data integration and real-time visibility** into customer health across product, support, and sales—single source of truth for revenue team decisions.
2. **Operationalize CS-to-sales handoff** with automated alerts and data flows.
3. **Separate pricing and expansion conversations** so expansion is about value and usage, not about raising rates.
4. **Tighten discount guardrails** while enabling segment-specific flexibility; track true ASP impact.
5. **Invest in product-led growth** and vertical specialization rather than competing on feature parity with cloud giants.

---

**Next Steps:** Salesloft to send proposal on revenue intelligence integration, schedule follow-up with VP of Sales, and provide peer connections to other enterprise data analytics companies facing similar dynamics.
