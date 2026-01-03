# Interview: Sarah Kim - Developer Tools VP Sales

## Metadata
- **Date:** January 2, 2026
- **Duration:** 30 minutes
- **Interviewer:** Marcus Chen, Enterprise Sales Strategist, Salesloft + Clari
- **Interviewee:** Sarah Kim, VP Sales, Developer Tools Company (45M ARR)
- **Company Overview:** B2B SaaS platform for API management and developer infrastructure; $45M ARR across 400+ enterprise customers
- **Context:** Sarah's company transitioning from PLG to sales-led motion for enterprise accounts

---

## Interview Transcript

**MARCUS:** Sarah, thanks so much for taking the time today. I've been following your company's trajectory over the last couple years, and it's impressive—$45M ARR with that kind of product-led growth foundation is rare in developer tools. I'm curious about something though that I hear from a lot of founders and VPs Sales in your space: the tension between the product's organic growth and the need to go upmarket into enterprise. How's that been playing out for you?

**SARAH:** [Laughs] Marcus, if I had a dollar for every investor who's asked us this question in the last eighteen months... Look, the PLG motion got us to where we are, and I'm grateful for that. But there's this glass ceiling. We're strong with individual teams, strong with 20, 30-person companies. Our product is genuinely great for engineers. But the second you try to sell a $500K contract to a Fortune 500 company? It's a completely different animal. The procurement, the security reviews, the multi-stakeholder buying process—our product doesn't fail, our sales process fails.

**MARCUS:** That's a really honest take. So when you think about the transition, where are you seeing the biggest friction points right now? Is it identifying which accounts are actually ready to move upmarket?

**SARAH:** Exactly. That's probably 60% of the problem. We have 400 customers, but we're not great at identifying which ones have the signals of enterprise readiness. Like, we see high usage—let's say 150 API calls per day, multiple teams onboarded, consistent activity for 6+ months. But that doesn't necessarily mean they're ready to buy a contract. A growing startup could look identical to a Fortune 500 subsidiary that's just in pilot mode.

**MARCUS:** So you're looking for signals beyond just raw usage metrics?

**SARAH:** Right. We've been experimenting with what we call "expansion signals." Is the customer integrating us into their critical path? Are they hitting limits on our free tier—like, we have a rate limit at 10K daily API calls. When someone bumps up against that consistently, that's a signal. Are they asking about SSO? About compliance certifications? These behavioral signals matter more than just monthly active users.

**MARCUS:** Have you defined your PLG-to-sales threshold formally? Like, a checklist that says "when they hit X, Y, and Z, hand them to sales"?

**SARAH:** We're getting there, but honestly, it's not perfect. Right now, we're using a combination: if a customer has 3+ teams using the product, 120+ daily API calls, and has been active for 90 days without churning, we mark them as "enterprise ready." But we've found that's still too broad. We're refining it with Clari data now. We're looking at things like: are they running integrations that suggest they're in security-sensitive industries? Are they hitting API rate limits? Do we see them downloading compliance documentation? That last one's key—if someone's downloading our SOC 2 docs, that's usually a strong signal they're heading toward a procurement conversation.

**MARCUS:** I love that approach. The compliance download is a great leading indicator. Now, you mentioned selling to enterprise is different. What's been the biggest surprise for you about selling to developers at scale—like, when you're actually trying to build a team that sells this way?

**SARAH:** [Pauses] Oh man. So here's something that surprised me: developer sales isn't just about technical credibility anymore. Your reps have to understand the developer experience deeply, but they also have to be comfortable operating in this weird hybrid mode. An engineer will reject you outright if you come at them with corporate-speak. But an enterprise engineer also expects you to understand their business problems. You have to code-switch between talking about their technical constraints and their budget constraints. Most enterprise sales reps can't do that.

**MARCUS:** How are you building that capability? Are you hiring engineers-turned-sales people, or are you training traditional enterprise sales reps on technical concepts?

**SARAH:** Both, honestly, with mixed results. The engineers-turned-sales hire gives you credibility but sometimes lacks sales discipline. They want to go deep on the technical problem but don't close. The traditional sales rep? They're efficient closers but can sound like a suit to developers, and developers hate that. What's working better is hiring sales people who are passionate about developer tools—maybe they were product managers at other DevTools companies, or they ran developer relations programs. They understand developer psychology without needing to debug code.

**MARCUS:** That makes sense. So when you're engaging with, say, a 10,000-person enterprise where developers are the power users but the procurement team is making the decision... how does your messaging shift?

**SARAH:** This is critical. For the developer—the actual user—the message is: "We make your infrastructure more reliable and secure. We solve operational headaches." For the procurement team and the CTO? It's about risk mitigation, compliance, scalability, and total cost of ownership. For the finance person? It's about preventing expensive outages. They're all using our product, but they care about different value props. That's why our sales process has to involve multiple conversations early. We can't just pitch one angle.

**MARCUS:** How are you identifying and engaging the non-developer stakeholders? Is that still coming through the developer champion, or are you going direct?

**SARAH:** That's been our biggest learning. We used to rely entirely on the developer to advocate upward. That's a mistake. Engineers don't want to be inside salespeople, and frankly, they're not good at it. Now, as soon as we sniff enterprise intent, we're getting the developer to make an intro to their manager or architect, and then we engage both. The developer gives us the technical credibility, and the manager helps us navigate procurement. It's a two-sided motion.

**MARCUS:** Let's talk about the cold-calling question. In developer tools, there's this assumption that cold outreach is dead—it's all inbound, all community, all content marketing. But when you're going enterprise, you can't just wait for inbound. How are you approaching that?

**SARAH:** [Leans forward] This is where Clari data is changing the game for us. Pure cold outreach to a developer? Yeah, that's maybe a 3-5% response rate and usually a "no thanks." But intelligent warm outreach? Much better. Here's what we're doing: Clari helps us identify companies that fit our ICP—they're in fintech, healthcare, cybersecurity, industries where API security is critical. Then, instead of a generic cold email, our sales team reaches out with context. "I noticed your company is hiring senior engineers in our space. I also see you're scaling your API infrastructure based on your recent funding round. That's why I wanted to connect..."

**MARCUS:** So you're using data to make the cold outreach feel warm. That changes the dynamic.

**SARAH:** Completely. And we're getting much higher response rates. But here's the counterintuitive part: sometimes the warm signal still comes from product usage. If we see that someone from Acme Corp—a prospect we haven't engaged yet—downloaded our documentation three times, that's a signal to reach out. "Hey, I see you're exploring our platform. I'd love to show you what's possible at scale." It feels warm to them because they recognize their own behavior.

**MARCUS:** That's the marriage of product data and sales intelligence. Speaking of which, let's dig into the product usage integration. You mentioned Clari. How are you actually piping product data into your sales process and your revenue intelligence system?

**SARAH:** Okay, so this was complicated at first. Our product team logs everything—API calls, features used, user paths, errors, integrations attempted. But that data lived in our data warehouse, and our CRM lived somewhere else, and our revenue intelligence tool was a third place. We basically built a data pipeline: every night, we run a job that takes product usage data, calculates engagement scores, and pushes key signals into Salesforce custom fields. Then Clari reads those fields, does some ML magic, and surfaces alerts when usage patterns change.

**MARCUS:** What kind of alerts are you looking for?

**SARAH:** Expansion signals mostly. Like: sudden increase in daily API calls. New teams onboarded. Users hitting rate limits repeatedly. Increased error rates—sometimes that's actually a good signal because they're pushing us harder. Churn signals too: if a customer goes from 200 API calls a day to 10, something's wrong. Maybe they're evaluating competitors, or maybe they've solved their problem and aren't iterating anymore. We need to know which.

**MARCUS:** How are you defining your PQL—your Product Qualified Lead—definition? Is it static, or are you constantly refining it based on conversion data?

**SARAH:** It's constantly evolving, which is a bit of a pain operationally but necessary. We started with a simple definition: 90-day usage, 3+ teams, 120+ daily API calls. But we learned that wasn't predictive of enterprise conversion. So we added behavioral dimensions: Are they testing integrations with other enterprise tools? Are they in compliance-sensitive verticals? Are they downloading security/compliance content? Now we're getting more sophisticated: we look at usage patterns. Like, do they have spike usage (suggesting they're experimenting) or steady, growing usage (suggesting adoption)? Steady growth is more predictive of conversion.

We also overlay CRM data now. If someone at the company is already a customer at their previous job and requested to use us here? That's a super strong signal. So is LinkedIn data—are they a VP of Engineering? A Principal Architect? Those folks have more budget authority.

**MARCUS:** This is sophisticated. How much of this is automated versus manual?

**SARAH:** Maybe 70% automated, 30% manual at this point. The scoring happens automatically. The alerts go to sales in Slack. But the judgment call—whether someone is actually enterprise-ready—still requires human review. We'll never automate that completely because there's always context: maybe someone looks PQL, but they're at a startup that just raised funding and there's going to be a layoff next month, and we'd know that if we paid attention to news. So our reps still need to do a sniff test.

**MARCUS:** Let's shift to SDRs for a second. You're basically asking your SDR team to do something that's not traditional enterprise sales and not community engagement. How are you structuring the SDR function? And what's your cold-call cadence actually look like?

**SARAH:** So we've actually moved away from pure cold calling, which was hard for me to do as a former enterprise sales rep. I came up in an era where cold calling was sacred. But our SDRs are doing more intelligent outreach. The cold calling that does happen is much more targeted. We might cold call 5-10 really specific accounts per SDR per week—accounts where we've seen some signal. Like, they visited our pricing page. They attended one of our conferences. We have a mutual connection.

But the bulk of the SDR motion is warm. They're reaching out to inbound leads, nurturing hand-raised leads, and engaging with people who've shown product engagement. The cold outreach is maybe 20% of the motion.

**MARCUS:** And response rates? What are you seeing?

**SARAH:** On warm outreach to people with product engagement? 25-30%. On targeted cold with a data signal? 10-15%. On pure cold? 3-5%. Our SDR productivity is actually up because they're spending less time on dead leads and more time on warm conversations.

**MARCUS:** But doesn't that create a burden on product marketing and content to generate those warm signals? Like, if your SDRs aren't cold calling, they're dependent on inbound and product signals. What if one of those taps turns off?

**SARAH:** [Nods] Great question, and honestly, it's a vulnerability. If our inbound volume drops, or if product usage signals dry up, we'd have to revert to more aggressive cold outreach. But we've invested heavily in community—we sponsor developer conferences, we run webinars, we have a robust content program. We also now have a product-led growth program that drives free trial signups, which feeds the warm pipeline. It's less efficient than pure cold calling but less exhausting on reps and more respectful to prospects.

**MARCUS:** Speaking of respect—and this is a bit of a cultural thing—how are your SDRs actually perceived by engineers? Is there any pushback to the sales outreach at all, even when it's warm?

**SARAH:** [Laughs] Oh yes. Engineers hate being sold to, period. But they hate it less when they asked you to reach out implicitly. If an engineer signed up for a trial, they're expecting to hear from us. If they downloaded compliance docs, they know we're going to reach out. The key is not being creepy about it. "I noticed you downloaded our SOC 2 documentation" works. "I noticed you're VP of Engineering at a company with 500+ engineers" can feel stalker-ish. So our team is trained to reference product behavior and intent signals, not just demographic signals.

**MARCUS:** That's a really important distinction. Now, let's move to the later-stage conversation. You close a customer. Let's say it's a $300K ACV deal. What does the transition from sales to customer success look like? And how are you thinking about expansion revenue?

**SARAH:** This is an area we're still maturing. Historically, we'd sell the contract, hand off to CS, and then ignore the customer until renewal. That's classic but dumb, especially at this price point. Now we're building what I call an "account team" approach for enterprise accounts. From day one of the sale, we have the AE assigned, but we're also bringing in a customer success manager, and increasingly, we're thinking about technical account managers too.

The handoff is critical. We do a 30-minute overlap meeting where the AE, CSM, and the customer align on success metrics. What does the customer need to achieve in year one? Are they implementing one service or multi-service? Are they hitting performance targets? And frankly, we're transparent about our expansion thesis. If they're using 10% of the product surface today, we know the growth vector is helping them move from single-team adoption to multi-team.

**MARCUS:** So you're explicit about expansion from day one?

**SARAH:** Yes, but carefully. We're not that sleazy. [Laughs] We're saying, "We know you're starting with API monitoring. Based on what we see with similar companies in your industry, the natural next steps are usually API versioning, then API governance, then developer portal. We'll flag those as expansion opportunities down the road." We're mapping the customer's growth to product adoption growth. It's not pushiness; it's product roadmap alignment.

**MARCUS:** What are your expansion triggers? Like, concretely, when does an AE step in and say, "This account is ready to expand"?

**SARAH:** We have a few:

**Usage threshold**: If a customer is using 70%+ of our product (measuring by feature adoption), they're probably ready for something bigger. Maybe they need a premium tier with dedicated infrastructure, or they need our enterprise support SLA.

**Budget signals**: If they're hiring in the space, they have money. We track hiring via LinkedIn data and news. If a company doubles their engineering headcount, they're probably going to hit the limits of what they're doing today.

**Time-based**: Around month 4-5, we're ready to have an expansion conversation. They've integrated us into their workflow, they're getting value, and we can be specific about the next tier.

**Churn risk**: Counterintuitive, but sometimes a customer is at risk of switching because we don't have a feature they need. The expansion motion can be: "Let's talk about our roadmap and what's coming in Q2."

**MARCUS:** And when you engage the expansion conversation, who's involved? Is it the same AE?

**SARAH:** Same AE leads it, but the CSM is heavily involved. The CSM's got the relationship with the customer's operations team. The CSM knows that the customer is frustrated with incident response time—that's a real pain point we've picked up in check-ins. The AE can then come in and say, "We have a premium support tier that includes dedicated incident response. Let me show you how that works." It feels less sales-y because it's coming from a relationship, not a cold pitch.

**MARCUS:** This is textbook account-based selling, but I want to make sure I understand the mechanics. Are you reserving this kind of account team structure for accounts above a certain size, or are you doing it for all enterprise deals?

**SARAH:** All enterprise deals. Once we cross $100K ACV, it gets the account team. It's resource-intensive—we have 12 AEs, 8 CSMs, and 2 TAMs. But at that price point, it's worth it. Below $100K, the AE owns the relationship but hands off to a CSM who manages a broader book.

**MARCUS:** Let's talk renewals. At $300K-500K deals, renewal rates matter enormously. What's your net revenue retention looking like, and how is the sales org involved in the renewal process?

**SARAH:** [Takes a breath] Honestly, this is where we've had the biggest miss as we've scaled. For the first two years, we had 110% NRR, which was amazing. But as we've gone bigger, we've dropped to about 102-105%. The issue is expansion wasn't baked into the sales process early enough. We were selling standard contracts, not thinking about what the expansion path looked like 12 months in.

Now renewals are a shared motion. About 6 weeks before renewal, the CSM does a business review. They're looking at: What did you implement? Are you at 100% adoption? Are there adjacent services you're not using? That conversation happens before the AE touches the account. If there are expansion opportunities, the AE comes in 4 weeks before renewal and has a conversation around, "Your license expires in 4 weeks. Based on your usage, here's what we're seeing other similar companies do..."

**MARCUS:** And that upsell conversation—is it a separate contract, or do you try to expand the existing deal?

**SARAH:** Both approaches work. Sometimes it's easier to do a separate expansion contract. Like, they had a $300K monitoring contract; now they add a $150K governance contract. Other times, we consolidate into a single larger contract. Operationally, fewer contracts is cleaner, so we push toward that. But it depends on procurement preferences.

**MARCUS:** What percentage of your renewal cohort is expanding?

**SARAH:** About 65% expand by some amount—even if it's small. 30% are flat renewals. 5% are churn. We're trying to push that 65% higher by being more proactive about expansion, and honestly, by having better conversations earlier.

**MARCUS:** Speaking of churn, what's your churn analysis look like? What do you see as the common reasons companies don't renew, especially in developer tools?

**SARAH:** A few patterns. One: they built it themselves. Developers will say, "We can build our own API monitoring in-house." Sometimes they can, sometimes they're overestimating their capacity. By the time we realize they're serious about it, it's too late to course-correct.

Two: competing solutions. There's a ton of competition in the API management space now. If a customer is comparing us to three other vendors at renewal time, price becomes a huge factor. We've learned to be more aggressive about competitive displacement earlier.

Three: organizational change. A VP of Engineering leaves. Budget gets reallocated. The new engineering leader has a different tool preference. This is less about us and more about internal politics.

Four: value not realized. Sometimes we sell to someone who oversells the success internally. They promised their CTO they'd reduce incident response time by 40%. We delivered 20%. By renewal, they're disappointed and want to try something else.

**MARCUS:** That last one is interesting. How do you prevent over-promising?

**SARAH:** Sales coaching and validation. We've implemented a rule that before the AE signs the contract, the CSM has to validate that the customer's success metrics are achievable. If a customer says, "We need to reduce incident response time by 40%," we're pushing back in the discovery call and saying, "Based on your infrastructure, 15-20% is realistic in year one. That's still significant. Here's why." It's uncomfortable to say no to expansion upside in the sales cycle, but it saves us at renewal.

**MARCUS:** This brings up something I want to ask about. You're going from a product-led business to a sales-led business. That means your sales team is now the bottleneck for growth in a lot of ways. Are you seeing pressure to speed up the sales cycle or compromise on qualification just to hit growth targets?

**SARAH:** [Long pause] Yeah. There's definitely tension. My board wants to see 40% YoY growth at this scale. That means we need to close more deals faster. There's pressure to lower the bar on what constitutes a qualified account. But when I lower the bar, my renewal rate suffers. When my renewal rate suffers, my CEO gets nervous. It's a balancing act.

What's helping is that we've gotten smarter about qualifying. We're saying no faster. If someone doesn't have our ICP criteria—they're not in a security-sensitive industry, they don't have 100+ engineers, they're not going to spend $100K+ on this—we're telling them we're not the right fit. That frees up our team to focus on better-qualified prospects. It also sets expectations early. If we tell someone, "I don't think we can deliver value at your current scale," they respect us more. And sometimes in a year, their situation changes and they come back ready to buy.

**MARCUS:** Let's do a final question about something I think you alluded to earlier—the messaging challenge. You're selling to developers, but increasingly, you're selling to non-developers who buy for developers. How have you differentiated your go-to-market messaging? Like, what's the core value prop you're leading with for enterprise?

**SARAH:** Great question. We've actually developed three distinct positioning angles:

**For the developer user**: "Build and deploy APIs faster with less operational overhead."

**For the engineering leader**: "Reduce the time your teams spend on infrastructure troubleshooting. Lower incident response time. Improve mean time to resolution."

**For the security and compliance buyer**: "Centralized visibility into API activity. Audit trails. Compliance-ready infrastructure. Reduce your breach risk."

All three are true. All three are us. But the emphasis is different. Sales has to be trained to pick the right angle based on who's in the room. If it's the developer and their manager, we lead with the first two. If procurement is at the table, we emphasize the third.

**MARCUS:** And in your sales materials? Your website? Your deck?

**SARAH:** Website is definitely developer-first. That's still our jam. But we have enterprise-specific collateral now. Case studies that talk about the pain points of 10,000-person companies. ROI calculators that show cost of ownership. Security datasheets. It's less "We're cool" and more "We're reliable and compliant."

**MARCUS:** Last question, and I'll let you go. What's one thing you wish you'd known two years ago when you started this transition?

**SARAH:** [Laughs] Where do I start? Probably this: the transition from PLG to sales-led is not about hiring salespeople. It's about fundamentally changing how you think about go-to-market. It's about product integration, data infrastructure, sales discipline, and honestly, some cultural change. For a company that grew up engineering-first, asking engineers to center their product decisions around sales signals feels weird at first. But it's essential.

Also, I wish I'd understood earlier that you can't run a pure cold outreach motion at scale in developer tools anymore. You have to be smarter, warmer, more data-driven. It's less about hustle and more about precision.

And finally, don't underestimate the complexity of selling to multiple personas. We spent a lot of time and money on courses and training to teach our team how to navigate that dynamic. It's not intuitive for salespeople who came up in traditional enterprise sales.

**MARCUS:** Sarah, this has been super valuable. Thank you for being candid about what's working and what's not.

**SARAH:** Thanks for the conversation. It's helpful to articulate where we're at. These are the problems I'm living with every day.

---

## Key Takeaways

### PLG-to-Sales Transition
- **Challenge**: High product usage doesn't always equal enterprise-ready status. Behavioral signals (compliance downloads, rate limit hits, SSO requests) are more predictive than raw usage metrics.
- **Solution**: Develop a formal threshold checklist combining usage metrics (3+ teams, 120+ daily API calls, 90+ day activity), behavioral signals (integration testing, compliance documentation access), and vertical/demographic data.
- **Action**: Track these signals automatically via product data pipeline; trigger sales engagement at consistent, data-driven thresholds.

### Selling to Developers at Enterprise Scale
- **Challenge**: Developer reps must code-switch between technical credibility and business problem-solving. Traditional enterprise reps sound corporate; engineer-turned-salespeople lack sales discipline.
- **Solution**: Hire sales professionals with DevTools PM or developer relations backgrounds who understand developer psychology without needing to code.
- **Action**: Build a multi-threaded engagement model where developers advocate within their organizations; reach out directly to technical leaders and managers early.

### Product Data Integration & Revenue Intelligence
- **Challenge**: Product data and CRM/revenue intelligence systems operate in silos; building a data pipeline is complex but necessary.
- **Solution**: Run nightly data jobs that calculate engagement scores from product usage logs and push key signals into Salesforce custom fields; feed this into revenue intelligence tools like Clari.
- **Action**: Define PQL criteria dynamically based on conversion data (not static); look for expansion signals (feature adoption rates, compliance downloads, usage patterns) alongside traditional engagement metrics.

### SDR Strategy: From Cold Calling to Warm Signals
- **Challenge**: Pure cold calling has low ROI (~3-5%) and exhausts reps; can't scale pure inbound. Need hybrid approach.
- **Solution**: Shift SDRs toward intelligent warm outreach using product behavior and intent signals. Cold outreach reserved for 5-10 high-signal accounts per rep per week.
- **Action**: Train SDRs to reference product behavior (downloaded docs, visited pricing page, mutual connection) to make cold feels warm. Measure response rates: warm outreach (25-30%), targeted cold with signal (10-15%), pure cold (3-5%).

### Account-Based Sales & Account Team Structure
- **Challenge**: Individual AEs can't manage the complexity of enterprise deals. Renewal rates suffer without proactive expansion. Non-sales stakeholders (CSMs, TAMs) are critical to customer success.
- **Solution**: Build account teams for $100K+ ACV deals (AE + CSM + TAM). Align on success metrics at contract signature. Map product adoption to expansion opportunities.
- **Action**: Align expansion triggers (usage thresholds, hiring signals, time-based, churn risk). Engage expansion conversations at 4-5 month mark with CSM relationship context.

### Renewal & Expansion Strategy
- **Challenge**: Flat renewals and churn. Customers often over-promise on adoption internally, leading to disappointment at renewal.
- **Solution**: Have CSMs validate success metrics during sales cycle (realistic targets > overselling). Structure renewals as business reviews at 6 weeks out. Separate expansion conversations at 4 weeks out.
- **Action**: Target 65%+ of renewal cohort for expansion. Current NRR is 102-105% (goal: higher). Track churn reasons: self-build, competitive displacement, org change, value realization gap.

### Enterprise Messaging & Positioning
- **Challenge**: Single value prop doesn't resonate across developer users, engineering leaders, and compliance buyers.
- **Solution**: Develop three distinct messaging angles: (1) Developer: Speed and operational overhead reduction. (2) Engineering Leader: Incident response time, MTTR. (3) Compliance: Visibility, audit trails, breach risk reduction.
- **Action**: Build separate collateral for each persona; train sales to tailor messaging based on room composition. Enterprise website emphasizes reliability, compliance, case studies with cost of ownership data.

### Cultural Lessons
- The transition from PLG to sales-led requires product decisions centered around sales signals—uncomfortable for engineering-first companies but essential.
- Data-driven precision outperforms aggressive cold outreach at scale in developer tools space.
- Sales effectiveness depends on multi-persona navigation skills—not intuitive for traditional enterprise salespeople.
