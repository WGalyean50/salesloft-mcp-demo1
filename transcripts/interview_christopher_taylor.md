# Interview: Christopher Taylor - Capital Markets Tech CRO

## Metadata
- **Date:** January 2, 2026
- **Duration:** 30 minutes
- **Interviewer:** Sarah Chen, Enterprise Solutions Director, Salesloft + Clari
- **Interviewee:** Christopher Taylor, Chief Revenue Officer, Capital Markets Tech
- **Company Size:** $200M ARR | 400+ sales team
- **Focus Areas:** Sales enablement, revenue intelligence, pipeline management

---

## Transcript

[SALESLOFT REP] Christopher, thanks so much for taking the time today. I know you're in the middle of earnings season, so I appreciate you carving out thirty minutes. Before we dive in, I want to understand the current state of Capital Markets Tech's sales organization. How's the team doing with the market headwinds we've been hearing about?

[CHRISTOPHER] Appreciate the call, Sarah. Honestly, it's been a challenging six months. We've got a $200M business with a pretty lean sales operation—400 reps across equities, fixed income, and derivatives. But the market contraction is real. Our enterprise clients, especially the buy-side—hedge funds, asset managers, trading desks—they're consolidating. We're seeing RFPs consolidate from five vendors down to two, sometimes one. The budgets are there, but they're tighter than they've been in three years.

[SALESLOFT REP] That consolidation trend—I'm hearing it from almost everyone in FinTech right now. When you say consolidation, are we talking about them reducing the number of vendors they work with, or are they actually cutting headcount and therefore need less software?

[CHRISTOPHER] Both, honestly. But it's the second one that's scarier. We're seeing fixed income trading desks cut 15-20% of their people in the last twelve months. When you cut that many traders and risk managers, your software footprint shrinks too. A trading desk that had twelve Salesforce licenses two years ago now has six. They're consolidating workflows. They want one platform that does everything—real-time data, risk management, trade execution, compliance—instead of a best-of-breed stack.

[SALESLOFT REP] So they're not just cutting spending—they're simplifying their tech stack entirely.

[CHRISTOPHER] Exactly. And for us, it means our average deal size is actually down 20% year-over-year, even though our logo retention is solid at 94%. The churn is operational. They're not leaving us; they're just... shrinking. And new logos are harder to come by because the buyer journey is longer. Procurement gets involved earlier. CFOs are asking tougher questions about ROI.

[SALESLOFT REP] That's the dynamic I wanted to dig into. When you're selling into this environment, how are you structuring your value proposition? Are you leading with cost savings, or are you trying to position something more strategic?

[CHRISTOPHER] It's changed what we're doing on the sales floor, I'll tell you that. Eighteen months ago, we led with innovation—"We have the fastest real-time data pipeline in the market." Now? We lead with efficiency. "Here's how you consolidate your compliance workflows and reduce manual work by 40%." We're showing cost-benefit analysis instead of feature comparisons.

But here's the thing—and this is where I see a real opportunity—we're not actually talking about the root problem with our prospects. The budget cuts are real, but they're coming because the trading market has compressed. Volume is down. If volume comes back, they'll need more capacity and more people. We should be positioning for that rebound and showing how Capital Markets Tech helps them capture that upside without incurring new headcount costs.

[SALESLOFT REP] That's smart. So you're trying to make the case that when the market recovers, you want them to be able to scale revenue without scaling headcount proportionally.

[CHRISTOPHER] Right. We're selling them a platform for growth in a lean environment. The problem is, my sales team doesn't have the tools to articulate that or forecast it. We have Salesforce for pipeline, but we don't have real visibility into what our deals actually depend on. Is the deal dependent on a budget recovery? Is it dependent on them hiring new traders? These aren't questions we can model easily right now.

[SALESLOFT REP] What tools are you currently using for deal health and pipeline analytics?

[CHRISTOPHER] We've got Salesforce—good implementation, but it's mostly CRM. We use Gong for call recording and coaching, which has been helpful. And we've got some home-grown Tableau dashboards that pull from our data warehouse. But there's no integration. My VP of Sales can't look at a deal and say, "Okay, what are the actual risk factors here? Is this deal really on track, or are we lying to ourselves?" It's a lot of manual effort.

[SALESLOFT REP] And when you close deals, how much of that visibility carries into execution? Are you tracking whether deals are actually delivering value?

[CHRISTOPHER] That's... that's actually a gap. We're pretty good at forecasting the quarter, but once a deal closes, it gets handed off to implementation and our customer success team. We don't have a great feedback loop back to sales about whether a customer is hitting their ROI milestones. Which means our sales team isn't building customer reference ability into their pitches.

[SALESLOFT REP] Okay, let me shift gears a bit because I think this is really important. You mentioned that your prospects are consolidating vendors and looking for integrated platforms. Are you also seeing that in the platform itself? Like, are they asking for different deployment options or different ways to access your technology?

[CHRISTOPHER] Oh, completely. This is another dynamic that's changed. We're a cloud-first business—all our infrastructure is on AWS. But when we're selling to large banks or hedge funds with significant regulatory oversight, especially around data residency and compliance, the conversation has completely shifted. They want to know if they can run Capital Markets Tech in their private cloud or on-premises. They want data to never leave their environment.

And the regulations are getting tighter. CFTC moved to more stringent reporting requirements last year. SEC has new cybersecurity rules. These buy-side clients are operating in a fishbowl. Every trade is auditable. Every position is reportable. If they can't demonstrate that their trading software is secure, compliant, and auditable, they can't use it. Period.

[SALESLOFT REP] So the cloud deployment conversation is really about control and compliance, not cost.

[CHRISTOPHER] Exactly. They don't care if cloud is cheaper—they care that they can pass a compliance audit. They care that if regulators ask, "Where is this data?" they can point to a specific data center in New York or London and say, "Here. Encrypted. Compliant."

[SALESLOFT REP] Are you building out on-premises or private cloud options?

[CHRISTOPHER] We are, yeah. We've got a containerized deployment model that can run on Kubernetes in their environment. It's... expensive for us to support. Every customer is a custom deployment. But we're finding it's becoming a gating issue for large deals.

[SALESLOFT REP] That's a huge infrastructure ask. How long are those deployments taking?

[CHRISTOPHER] Anywhere from six to eighteen months depending on their complexity. A large hedge fund with multiple offices, different trading desks, legacy systems—that's a full-year implementation. And during that year, we're not getting revenue. The deal is signed, but nothing ships.

[SALESLOFT REP] Okay, so you've got this situation where you're signing deals but not recognizing revenue for a year. That's putting pressure on cash flow and your ability to fund that implementation work.

[CHRISTOPHER] Understatement. Our customer success team has expanded 40% in the last two years, but our delivery velocity hasn't kept pace with the complexity of these implementations. We're good at product development—really good—but we're not software engineers. We're financial technology people. Managing large Kubernetes deployments and compliance in highly regulated environments? That's not our core competency.

[SALESLOFT REP] Is that creating pressure to maybe slow down your sales motion or be more selective about which deals you pursue?

[CHRISTOPHER] My board is definitely pushing me on that. There's a tension between growth targets and delivery capability. We signed a seven-figure deal last quarter with a major hedge fund, and honestly, the implementation is concerning. They're demanding sub-millisecond latency for real-time position updates. That's... that's a hard requirement in trading. If our system is slow, it's not a feature gap—it's a dealbreaker.

[SALESLOFT REP] Sub-millisecond? That's aggressive.

[CHRISTOPHER] That's the baseline in high-frequency trading environments. But even for traditional asset managers, latency matters. These traders make decisions in seconds based on market data. If our platform adds even 100 milliseconds of lag, their alpha is gone. They lose money.

[SALESLOFT REP] How are you validating that your platform actually meets those requirements before you sign deals?

[CHRISTOPHER] We do POCs. We run benchmarking against their data, their network topology, their infrastructure. But here's the problem—POCs cost us real resources. We're spinning up infrastructure, dedicating an engineer or two, running for six to eight weeks. It's a $50K to $100K investment per POC, and we typically only land maybe 60% of the deals that go to POC.

[SALESLOFT REP] That's a high cost-per-win. Are you doing POC scoping differently now, or are you still treating them the same way?

[CHRISTOPHER] We're trying to be more selective, but it's hard. Because if we don't do a POC and there's a latency issue, we lose the deal anyway. And we lose credibility. So we end up doing POCs for almost every enterprise deal. It's just table stakes now.

[SALESLOFT REP] So POCs have become a cost of doing business. Do your prospects understand that going in, or is it always a surprise when you tell them you need six weeks and significant resources?

[CHRISTOPHER] It's built into our sales cycle now. Enterprise deals are basically: initial conversation, POC scoping, six to eight week POC, evaluation and signoff, contracting. That's a nine-month sales cycle minimum. Sometimes twelve months.

[SALESLOFT REP] That's a long runway. How are you maintaining deal momentum over that kind of timeline?

[CHRISTOPHER] Gong helps. Being able to go back and listen to calls, identify where we're losing momentum, coach the team on objection handling—that's valuable. But honestly, the issue isn't coaching. The issue is that our prospects are managing multiple competing priorities. They're under budget pressure. They're dealing with regulatory changes. The trading desk manager who's championing our solution might get fired or relocated. The deal momentum just... dies.

[SALESLOFT REP] Do you see deals that never make it out of POC?

[CHRISTOPHER] Yeah, probably 30-40% of POCs result in "we need to revisit this next year" or "we're going to build this in-house instead." And the ones that do convert often take longer than we forecast.

[SALESLOFT REP] What's your current forecast accuracy on these long-cycle deals?

[CHRISTOPHER] Honestly? Fifty-fifty. We're probably off by 60-90 days on average for any deal over $500K. The Salesforce pipeline looks solid, but the deals slip.

[SALESLOFT REP] Where do the slips happen? Is it on the prospect side or your side?

[CHRISTOPHER] Mostly prospect side. Their budgets shift. Regulatory issues come up. Leadership changes. But there's also stuff on us—we underestimate implementation scope, or there's a technical issue with latency that we didn't catch in the POC. Then we're re-scoping the implementation and re-negotiating terms.

[SALESLOFT REP] When that happens, are you losing the deal entirely or just compressing margin?

[CHRISTOPHER] Both, sometimes. If we re-scope downward—"Okay, we'll implement the trading module but not the compliance module"—we're taking lower ACV. If there's a technical issue, we might offer implementation support as part of the deal, which costs us but keeps the deal intact. It's not great for unit economics.

[SALESLOFT REP] Let me ask you this differently. When you're looking at a prospect, how do you decide whether to pursue them? What's your criteria for a viable deal?

[CHRISTOPHER] Good question. We look at: One, do they have the right technology infrastructure? If they're on ancient legacy systems and can't support cloud or Kubernetes, we know it's going to be a nightmare. Two, budget—are they actually willing to spend? In this environment, that's tougher to verify. Three, technical viability—can we actually meet their performance requirements?

But here's where I want to be honest with you: we're not great at this upfront. We do a lot of exploratory POCs to figure out if something is actually viable. Which costs us. Ideally, we'd pre-qualify much harder before we invest in a POC.

[SALESLOFT REP] What would help you pre-qualify better?

[CHRISTOPHER] I don't know. This is where I think a tool like Clari could help, but I'm not fully sure how. We need better technical diligence before we commit resources. We need a way to model what the implementation is actually going to look like before we're six months in and discovering surprises.

We also need better signals on whether a deal is actually progressing. In Salesforce, a deal is open until it's closed. But some of those open deals are dead. The prospect isn't responding. There's been no engagement in six weeks. We're just... pretending it's still alive.

[SALESLOFT REP] How are you currently identifying those dead deals?

[CHRISTOPHER] Our managers do it manually. They look at their forecast, see a deal that seems off, ask the rep about it. The rep says, "Oh yeah, they're just in budget review," and maybe it's true, maybe it's not. There's a lot of gut feel.

[SALESLOFT REP] So there's no systematic way to identify stalled deals?

[CHRISTOPHER] Not really. And that's a problem because we're carrying a lot of dead weight in our pipeline. If I could flush out the dead deals and be realistic about what's actually going to close, I could make much better decisions about where to invest my team's time.

[SALESLOFT REP] That's interesting because that would affect how you're thinking about POC investments. If you had better visibility into actual deal momentum, you could probably be more selective about which deals you take to POC.

[CHRISTOPHER] Exactly. Right now, it's like, "Do they need what we build? Take them to POC." But we should be asking, "Is this deal actually viable? Is there real budget? Is there real champion? Is their technical environment compatible?" and only then invest in a POC.

[SALESLOFT REP] Let me ask about the other side—when deals do close and you're in implementation, how much are you tracking whether the customer is hitting their expected ROI?

[CHRISTOPHER] Very little, to be honest. We have SLAs around implementation timelines and feature delivery. We don't have SLAs around business outcomes. A customer could go live and not be using 60% of the platform, and we wouldn't know it until renewal.

[SALESLOFT REP] Do you think that's a missed opportunity?

[CHRISTOPHER] Oh, completely. If I could track, real-time, whether a customer is actually getting value—whether their trading desk is using our platform to increase alpha, whether their compliance team is meeting their reporting obligations—I could intervene early. I could ask, "Hey, you're underutilizing the platform. Let me connect you with a customer success manager." That would reduce churn and increase upsell.

[SALESLOFT REP] And in this environment where you're dealing with budget-constrained customers, showing them real value could mean the difference between them renewing at lower ACV or staying flat.

[CHRISTOPHER] Or it could mean they're willing to expand because they're seeing ROI. Right now, we're not even collecting that data.

[SALESLOFT REP] Okay, one more thing I want to dig into. You mentioned these deals are complex, they have long timelines, they need POCs. When you're selling to a CRO or a CFO—someone who's managing budget—how are you justifying the investment in a POC?

[CHRISTOPHER] That's the hard conversation. We're saying, "We're going to invest our resources and some of your resources for six to eight weeks. We'll run this against your data and your infrastructure and prove that we can meet your performance requirements." Most of them understand that. Trading firms especially—they're used to doing technical validation. They get it.

But there's cost, right? They have to dedicate their infrastructure team, their compliance people. We're asking them to slow down their evaluation to be rigorous.

[SALESLOFT REP] Do they ever push back and say, "Can't you just tell us if you can do this?"

[CHRISTOPHER] All the time. And my answer is: "Not for something this critical. If we say yes and we're wrong, you lose money. We can't take that risk."

[SALESLOFT REP] That's a smart answer. But I'm curious—when you're in a POC and you discover that you CAN'T meet their latency requirements, how do you handle that?

[CHRISTOPHER] We usually try to find creative solutions. Maybe it's about how they use the platform rather than changing the platform. "Okay, real-time position updates aren't going to work at sub-millisecond latency, but here's how you batch updates every 500 milliseconds and still get what you need."

[SALESLOFT REP] Do they buy that?

[CHRISTOPHER] Sometimes. It depends on their use case. High-frequency trading? No, they're not going to accept 500 millisecond batches. That's not going to work. But a traditional asset manager with longer investment horizons? They might be okay with slightly delayed updates if it means they get the full platform with better compliance reporting.

[SALESLOFT REP] So you're customizing the value proposition based on what you learn in the POC.

[CHRISTOPHER] We have to. Because the reality is, we're a platform, not a point solution. We do twenty things. They need maybe five of them. We're trying to package and price it in a way that makes sense for them and for us.

[SALESLOFT REP] Let's talk pricing for a second. How are you pricing these deals in a budget-constrained environment?

[CHRISTOPHER] We're moving away from per-user licensing toward value-based pricing. Instead of "X dollars per trader," we're saying "X dollars per trading desk" or "X dollars per AUM under management." It's more aligned with their value.

But it also means we need to understand their business better. We need to know not just that they use our platform, but how much value they get. Otherwise, we're just guessing.

[SALESLOFT REP] That's where the outcomes tracking you mentioned earlier becomes really important.

[CHRISTOPHER] Right. If I can show that Customer A uses our platform and their trading costs are down 8%, and that's worth $2 million, I can price accordingly. But right now, I'm pricing based on benchmarks and comparable deals, which is much less defensible.

[SALESLOFT REP] When you're thinking about expanding into new markets or new use cases—because that's something I hear from other capital markets firms—is the same calculus true?

[CHRISTOPHER] We're looking at expanding into options trading on the buy-side. Right now, we're mostly focused on equities and fixed income. Options is a different beast—higher complexity, different risk models, different regulatory requirements. But there's a huge market opportunity.

The problem is, we'd need to develop new functionality, which takes engineering time. And we'd need to prove it to prospects with POCs, which takes sales and implementation time. And in this budget environment, I'm not sure we have the resources.

[SALESLOFT REP] So the expansion is possible but risky given the current constraints.

[CHRISTOPHER] Exactly. If the market comes back and budgets open up, we'd be well-positioned to expand into options. But right now, it feels like we should be focused on deepening relationships with our current customer base and maximizing their lifetime value.

[SALESLOFT REP] That makes sense. Last question, and I'll keep it high level: if you could wave a magic wand and fix one thing about your sales process, what would it be?

[CHRISTOPHER] Visibility. Real, end-to-end visibility. From the first conversation with a prospect all the way through implementation and into the customer lifecycle. I want to know: Is this deal real or fake? Is this customer getting value or not? Are we on track to hit our number or not? Right now, I'm running a $200M business with spotty information. I'm making decisions based on gut feel and historical patterns.

If I had better tools for seeing the truth about our pipeline and our customers, I could make smarter bets. I could be more selective about which deals to pursue, which means better efficiency. I could focus on deals that are actually viable and worth the POC investment. And I could track customer value in real-time, which would help me upsell and retain better.

[SALESLOFT REP] That's the most important thing I've heard in this conversation. Because everything we've talked about—the POCs, the long cycles, the complex implementations, the budget constraints—all of that goes back to visibility and decision-making.

[CHRISTOPHER] Yeah. And I think as an industry, we're behind. Most CROs I talk to are in the same boat. We've got Salesforce and Gong and maybe some custom dashboards, but we don't have a system of record for real revenue intelligence.

[SALESLOFT REP] That's helpful to hear. I appreciate you being so candid about where you are.

[CHRISTOPHER] Happy to do it. Genuinely curious where Clari is headed on this. The sales intelligence piece is table stakes now. Everyone has call recording, everyone has pipeline visibility. The companies that win are the ones that can predict and prevent deal slippage before it happens.

[SALESLOFT REP] Totally agree. Let me follow up with some initial ideas on how Salesloft + Clari could help you with what you've described—especially around identifying dead deals early, improving POC qualification, and tracking customer outcomes. I'll send something over early next week.

[CHRISTOPHER] Perfect. And Sarah—thanks for not doing a product demo on this call. It's nice to just talk about the business.

[SALESLOFT REP] That's the whole point. If we're going to help you, we need to understand what you're actually dealing with.

---

## Summary of Key Takeaways

### Market & Budget Dynamics
- **Buy-side consolidation is operational, not just budget-cutting.** Christopher's clients are consolidating trading desks, which reduces their software footprint. Deal sizes are down 20% YoY despite strong logo retention (94%).
- **Value justification has shifted from innovation to efficiency.** Prospects want to know how Capital Markets Tech helps them do more with fewer people, not just faster or cooler.
- **Growth positioning is untested.** Christopher sees an opportunity to position the platform as enabling growth without headcount expansion, but his sales team lacks the tools to forecast or model this scenario.

### Sales Process Complexity
- **POCs are a non-negotiable requirement and a significant cost.** Enterprise deals require 6-8 week POCs with $50K-$100K investment per POC. This is driven by latency and compliance requirements that can't be assessed without real technical validation.
- **Forecast accuracy suffers on long-cycle deals.** 50-50 accuracy on deals over $500K, with average slippage of 60-90 days. Most slippage is on prospect side, but implementation scope underestimation also contributes.
- **Deal momentum visibility is largely manual.** Christopher's team lacks systematic way to identify dead deals. Many deals in the pipeline are likely stalled but labeled as "in budget review."

### Technical & Compliance Barriers
- **Cloud-native isn't solving the problem.** Regulatory requirements (CFTC, SEC) and data residency concerns are pushing customers toward on-premises/private cloud deployments. This adds 6-18 months to implementation timelines.
- **Latency is non-negotiable and a discovery risk.** Sub-millisecond latency is baseline for trading environments. POCs sometimes reveal that the customer's requirements can't be met, but this is discovered mid-way through the evaluation.
- **Implementation complexity is resource-constrained.** Christopher's team has grown 40% but delivery velocity hasn't kept pace. Kubernetes deployments and compliance requirements are outside core competency.

### Revenue Quality Issues
- **Post-sale visibility is nearly non-existent.** No tracking of whether customers are hitting ROI milestones or using the platform effectively. Churn and underutilization aren't discovered until renewal.
- **Pricing has shifted to value-based, but value isn't being measured.** Pricing is aligned to business outcomes (AUM, trading volumes) but the firm can't actually demonstrate the outcomes post-sale.

### Opportunity for Salesloft + Clari
- **Christopher is explicitly asking for revenue intelligence at the pre-sales and post-sales level.** He wants to identify dead deals before they waste time, qualify deals before POC investment, and track customer outcomes to improve renewal rates and expansion.
- **Decision velocity is the core need.** Rather than being sold features, Christopher wants to reduce uncertainty and make better bets about where to invest his team's limited resources.
