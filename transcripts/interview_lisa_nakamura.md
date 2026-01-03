# Interview: Lisa Nakamura - AI/ML Platform VP Sales

## Metadata

**Date:** December 15, 2024
**Duration:** 32 minutes
**Interviewer:** Marcus Chen, Sales Enablement Manager, Salesloft
**Interviewee:** Lisa Nakamura, VP Sales, CloudMind AI/ML Platform
**Company:** CloudMind (Series C, $60M ARR)
**Industry:** AI/ML Infrastructure & DevOps
**Company Stage:** Scaling from growth phase, entering enterprise segment

---

## Interview Transcript

[SALESLOFT REP] Lisa, thanks so much for taking the time. We've been following CloudMind's trajectory—the growth is impressive. Today, I want to focus on something I know is keeping you up at night: how you're managing sales cycles in an emerging category. We've heard from a lot of VPs in AI/ML that traditional playbooks don't work anymore.

[LISA] *laughs* Keeping me up at night is an understatement. Marcus, we're in this weird position where we have paying customers, we have proof points, but we don't have established buying patterns. Every single deal feels like we're pioneering. Our sales team closes deals, but it takes forever, and we can't figure out why some cycles are 2 months and others are 8.

[SALESLOFT REP] That's exactly what we're seeing across our AI/ML software clients. Let me start with something foundational. When you're talking to a prospect, how are you educating them about the problem you solve without automatically extending the cycle?

[LISA] Oh man, this is the core issue. So we solve a real problem—AI/ML teams are drowning in infrastructure complexity. But here's the catch: most prospects don't even know that's a problem yet. They think their pain is something else. It's slow model training, or data quality issues, or team productivity. What we actually solve is infrastructure orchestration.

[SALESLOFT REP] So the problem reframing is built in.

[LISA] Exactly. Last quarter, we had a deal with a Series B ML company in the Bay Area. The champion, an ML engineer, was convinced their problem was GPU allocation inefficiency. He called me directly. But when our architect did a 30-minute discovery, we realized the real issue was their entire CI/CD pipeline for ML models was custom-built and unmaintainable. The moment that champion understood that, the deal accelerated. But getting to that moment? Took three conversations.

[SALESLOFT REP] Do you have a content strategy for that? Like, are you sending triggers before the conversation?

[LISA] We've tried. We have these long-form guides on infrastructure patterns, blog posts about MLOps best practices. But they're too generic. What works is when we can grab a prospect who's at a specific moment—they're hiring their second ML engineer, or they're about to migrate infrastructure, or they've just had a failed model deployment. We need signals for that inflection point.

[SALESLOFT REP] How do you currently qualify for those signals?

[LISA] Poorly, honestly. Our SDR team asks basic questions: "How many data scientists do you have? When's your next infra project?" But that doesn't tell us whether they're ready. We had a prospect who checked all the boxes—50-person data team, struggling with infra, budget approved. But they weren't ready because they hadn't standardized their ML processes yet. We spent eight weeks in their deal before we realized we needed them to be further along.

[SALESLOFT REP] So readiness qualification—that's different from problem qualification.

[LISA] Totally different. A prospect can have the problem and not be ready to solve it. We need customers who have:
- Multiple active ML projects
- Already tried DIY solutions or open-source tools
- Some budget allocated to infra improvements
- And this is critical—an executive sponsor, not just the engineer champion

We don't have a repeatable way to identify those signals early. We discover them at week four of the sales cycle.

[SALESLOFT REP] What about timing? You mentioned some deals are 2 months and others are 8.

[LISA] The 2-month deals happen when we catch someone at a hard deadline. A company is migrating cloud providers, or they've hit a scaling ceiling with their current setup, or a major project just failed. Sudden urgency. The 8-month deals? Those are the prospects who think it's a nice-to-have. "We should probably fix our infra" is not the same as "We need to fix it by Q1."

[SALESLOFT REP] How are you thinking about compressing those cycles?

[LISA] We've been experimenting with creating artificial urgency—like, "Here are the infrastructure costs you're likely wasting," or "At your scale, you'll hit this scaling problem in 6 months." But my head of sales pushed back. He said we're overcomplicating it. What if we just focused on the segments where natural urgency exists? So we're starting to focus on companies that are actively fundraising—they always need to show efficiency metrics—or companies that are obviously growing fast.

[SALESLOFT REP] That's smart segmentation. Now, let me ask about playbook building. You've got deals closing, but have you built a repeatable playbook?

[LISA] Not really. *laughs* We have loose frameworks. Our VP of customer success identified that most of our churning customers didn't have an implementation plan before they bought. But our AE playbook is still pretty ad-hoc. Different AEs close deals different ways. One AE always brings in the architect early. Another one doesn't. Both close deals, but the sales cycle and customer success outcomes are different.

[SALESLOFT REP] Let's talk about experimentation then. How are you thinking about building a more structured playbook?

[LISA] We're starting to track it now. Every deal that closes, we're documenting: How many discovery conversations before we brought in the architect? How many stakeholders were involved? What was the initial pain framing versus the final problem we sold against? It's manual, but we're seeing patterns.

Last quarter, I noticed our fastest-closing deals—the 6-to-8-week ones—all had something in common. We did an initial assessment call with both the technical stakeholder and a business stakeholder. The technical person cares about the architecture. The business person cares about costs or time-to-market. When we could speak to both, the cycle compressed.

[SALESLOFT REP] Have you started running experiments based on those observations?

[LISA] Yes, actually. Starting in January, we're testing a "dual-champion discovery" playbook. Every first call, we require both a technical and business stakeholder. It's a small change, but we think it'll help us understand readiness faster and build consensus earlier.

[SALESLOFT REP] And win pattern analysis?

[LISA] We're doing this manually too, with our sales leadership. Every Friday, we review closed deals. Not just wins, but losses too. We have a pattern emerging: we win when the prospect has already tried solving the problem with open-source tools. They understand the value of a commercial solution because they've felt the pain of DIY. We lose to free alternatives when the buyer is price-sensitive and the problem isn't urgent.

[SALESLOFT REP] That's a qualification signal.

[LISA] Right. So we're building that into our discovery: "Have you considered Kubernetes or Apache Airflow for this?" If they say, "Yeah, we tried," that's a green light. If they say, "We don't need those," or "We're thinking about trying them," then we know we're early.

[SALESLOFT REP] Now, let's talk about coaching iteration. How are you using win/loss data to coach your team?

[LISA] That's where we're weak. We have six AEs. I review deals with each one individually, but it's not systematic. I see what works and I tell them, "Hey, try bringing in the architect earlier." But without a structured playbook, it doesn't stick. And different AEs respond differently. One AE thrives with a consultative, discovery-heavy approach. Another one is better at solution pitching once we know the problem.

[SALESLOFT REP] Have you thought about creating role-specific playbooks instead of one universal playbook?

[LISA] That's... actually brilliant. We have different buyer types and different prospect maturity levels. Maybe we do need different playbooks.

[SALESLOFT REP] Let's shift to something specific: POC scope. I know you're doing POCs.

[LISA] Yeah. And Marcus, this is where things get really interesting because POCs are consuming like 80% of my head of SE's time. We have three SEs, and they're constantly in pilots with prospects.

[SALESLOFT REP] What does a typical POC look like?

[LISA] Varies wildly. Some are two weeks, some are two months. The problem is we don't have clear success criteria upfront. We'll agree to a pilot, and then the customer keeps asking us to prove different things. "Can it handle this workload? What about this use case? Can we integrate with this tool?"

[SALESLOFT REP] Who's defining success? The customer, you, or both?

[LISA] Theoretically, both. But in practice, the customer defines it as we go. I've realized we need to nail POC criteria upfront. Like, before we even start, we should agree on: What specific infrastructure problem are we solving? What's the metric we're measuring? How many weeks is this? What happens if it succeeds?

[SALESLOFT REP] That's critical. Do you have a POC framework?

[LISA] Not formal. But we're starting to build one. A good POC, I think, should answer a specific question: "Can this solve our infrastructure problem at scale?" That's it. Not every possible use case, not every integration, not every edge case. Just: Does it work for our core problem?

[SALESLOFT REP] How long should that take?

[LISA] Ideally? Three to four weeks. We start seeing results in week one or two. Week three, we're measuring impact. Week four, we're deciding.

[SALESLOFT REP] And what metric are you measuring?

[LISA] That depends on the customer. Some care about infrastructure deployment time. Some care about cost. Some care about team productivity—how long it takes to spin up a new ML environment. For one customer, we measured the time to deploy a model update: reduced it from 6 hours to 45 minutes. That was the POC win.

[SALESLOFT REP] Was that customer willing to pay after the POC?

[LISA] Yes, but here's the thing: they expected a massive discount because we'd proven ROI. We ended up at a lower price than we wanted, but a deal is a deal, and we have a customer.

[SALESLOFT REP] Have you thought about paid POCs?

[LISA] Our CEO has been pushing this. His argument is: if the customer isn't willing to invest in proving value, they're not serious. I see the logic, but we're early enough in the category that I worry it'll kill deals. Only two of our recent customers came from paid pilots.

[SALESLOFT REP] What's your commitment model for free POCs?

[LISA] That's what we're missing. We say, "Do a free pilot," and customers treat it like an extended trial. They don't commit resources, they deprioritize it, and the timeline stretches. For paid POCs, customers are obviously more committed.

[SALESLOFT REP] What if you added a commitment layer without charging?

[LISA] Like what?

[SALESLOFT REP] A POC agreement. They agree upfront to dedicate a resource, to meet weekly, to provide data, to make a go/no-go decision by week four. If they don't hit those milestones, you pause or end the POC. It's not money, but it signals commitment.

[LISA] That's smart. That would probably solve a lot of our SE time issues. If we had a true commitment, we could actually control the scope and timeline.

[SALESLOFT REP] Let me ask about paid versus unpaid. What's your theory?

[LISA] Honestly? For a category we're establishing, free POCs are part of our strategy. We're buying proof points. But we need to be smarter about which deals we do free POCs for. If someone has limited budget and they're genuinely a good fit, fine. If someone is just kicking tires? Paid POC, or a shorter engagement.

[SALESLOFT REP] Okay, let's talk about something that might be even tougher: forecasting in a new category. How are you forecasting deals when you don't have historical data?

[LISA] *sighs* This is a nightmare. Our CEO wants standard pipeline metrics—conversion rates by stage, average sales cycle. But none of that applies when you're creating a category. Last year, we had sales cycles that ranged from 4 weeks to 12 weeks. This year, they're all over the place. We don't know what's normal yet.

[SALESLOFT REP] How are you currently forecasting?

[LISA] We use traditional stage gates: Discovery, Technical Evaluation, POC, Negotiation, Closed. But the time in each stage is completely unpredictable. Some deals spend three weeks in Discovery, some spend three days. Some POCs are two weeks, some are two months. There's no pattern yet.

[SALESLOFT REP] What proxy metrics are you using instead of historical data?

[LISA] We're experimenting. We look at:
- Stakeholder count: More stakeholders usually means a longer cycle.
- Competitive situations: If they're comparing us to open-source or a competitor, longer cycle.
- Budget status: If budget is already approved, much shorter cycle.
- Implementation timeline: If they need to solve this by a specific date, we know it's real.

But these are hunches. We don't have enough data to be confident.

[SALESLOFT REP] Are you tracking whether these proxy metrics actually predict outcomes?

[LISA] We should be. We're not, systematically. But I'm convinced it's worth doing. If we could say, "When we have these four signals, the deal closes 70% of the time and takes 8 weeks," that would be huge.

[SALESLOFT REP] What about your stage definitions? Do they make sense for your category?

[LISA] Not really, to be honest. Discovery works. Technical Evaluation works. But then things get weird. In a traditional software sale, POC is clear. You're testing the product. For us, a POC is half product evaluation and half education. We're teaching them how to think about infrastructure architecture. That's not a typical product POC.

[SALESLOFT REP] Have you considered redefining your stages?

[LISA] I've thought about it. Maybe something like:
- Problem Understanding: Do they get why their infra is a problem?
- Solution Fit: Will our approach work for them?
- Implementation Planning: Can we actually do this together?
- Budget & Approval: Is it approved?
- Deal Closure

That might make more sense than the traditional pipeline.

[SALESLOFT REP] That's a founder-friendly pipeline. I like it. Now, let's talk about budget discovery. This is always tricky in enterprise, but especially in emerging categories.

[LISA] Budget is the weirdest part. Some customers have dedicated infrastructure budgets. Some are trying to carve it out of engineering budgets. Some are using customer success or DevOps budgets. There's no standard.

[SALESLOFT REP] How are you discovering budget?

[LISA] We ask directly: "Is there budget for this?" But the answers are vague. "We'll find it if this is a priority," or "It'll probably come out of Q1 planning," or "We're still figuring it out." Those don't tell me if we actually have a deal.

[SALESLOFT REP] What are your budget signals?

[LISA] Good question. A strong signal is when they've already spent money on infrastructure solutions. If they bought a Kubernetes platform or invested in DataOps tools, we know they value infrastructure. That's where money exists. A weak signal is "We're thinking about it in budget planning." That might mean nothing.

[SALESLOFT REP] What about stakeholder mapping? Who's holding the budget?

[LISA] That's the challenge. Typically, it's the VP of Engineering or CTO. But for some customers, it's the VP of Data, VP of ML, or even the CFO if they're looking at cost optimization. We're not always finding the right person.

[SALESLOFT REP] How are you mapping that?

[LISA] On discovery calls, we ask who owns the infrastructure budget. Sometimes the technical champion doesn't even know. Then we have to do research, make assumptions. It's inefficient.

[SALESLOFT REP] Do you have a stakeholder mapping framework?

[LISA] No. But I think we need one. Something like: Identify the technical champion, ask them who owns the budget, confirm with that person directly. Then identify the economic buyer—who ultimately approves spending? For us, it's often the CFO or head of finance looking at cost impact. We're not always talking to them early enough.

[SALESLOFT REP] Budget discovery in emerging categories is hard because there's no established budget allocation. Have you noticed patterns in which customers have money readily available?

[LISA] Yes, actually. Companies that are:
- Hypergrowth: They're hiring engineers fast, they need infrastructure to scale. They have money.
- Recently funded: Series B, C, D companies with fresh capital. They're investing in infrastructure.
- Large enterprises moving to cloud: They have dedicated budgets for infrastructure transformation.

The hard cases are mature companies trying to optimize. They have limited budgets, and infrastructure feels like an operational expense, not an investment.

[SALESLOFT REP] So you're naturally segmenting toward growth companies.

[LISA] We are. That's not a bad thing—that's where our product works best, and those customers have clearer budgets. But we're missing the enterprise segment because we don't know how to navigate their budget cycles.

[SALESLOFT REP] Let me ask: in your deals, when does budget get discovered?

[LISA] Too late. Usually, we're in technical evaluation or POC before we seriously discuss budget. Then we find out there isn't budget, and we're stuck.

[SALESLOFT REP] What if you moved budget discovery earlier?

[LISA] How early?

[SALESLOFT REP] Second discovery call. Once you've confirmed they have the problem and they care about solving it, ask directly: "How would you fund this if we can prove it works?" Not "Do you have budget?"—that's easy to say no to. But "How would this be funded?" forces them to think about the mechanism.

[LISA] That's different. We could probably get better answers that way. And if they say, "We don't know," we know we need to do stakeholder discovery.

[SALESLOFT REP] Exactly. One more thing on budget: Are you experiencing any category creation challenges specific to budget?

[LISA] Oh, 100%. Enterprise companies don't have a "MLOps infrastructure" line item. It's hidden in various budgets. So we might solve a problem that saves the company $2M per year in infrastructure costs, but that money isn't allocated to one budget that we can tap. It's distributed across five different teams' budgets. That makes budget discovery much harder.

[SALESLOFT REP] That's a structural problem of being in a new category.

[LISA] Right. And I don't know how to solve that except to keep educating customers that infrastructure investment is important and should be centralized.

[SALESLOFT REP] Okay, last thing. Let's go back to category creation challenges more broadly. What's the hardest part?

[LISA] The hardest part is that everything takes longer because you're not only selling the product, you're teaching the market what the category is and why it matters. We're not just competing with other vendors. We're competing with the option to do nothing, or to stick with DIY solutions.

Second hardest is that our team doesn't have a playbook yet. Every deal feels unique. We're learning as we go, which is exciting but also stressful. How do you coach a team on a playbook that doesn't exist yet?

Third is that we can't accurately forecast. We don't know if a deal in month one will close in month two or month four. That makes planning really hard.

[SALESLOFT REP] And the upside?

[LISA] The upside is that we're establishing market position. When the category matures, we'll have first-mover advantage. Our early customers are very loyal because we helped them solve a problem they didn't even know they had. And from a sales perspective, there's less competition right now. We're not fighting established players as much as we're fighting inertia.

[SALESLOFT REP] That's a good position. So, if you could focus on three things in the next 90 days, what would they be?

[LISA] One: Build a structured POC framework with clear criteria and timelines. That'll fix our SE resource issue.

Two: Create a playbook based on our win patterns. Document what works, test it consistently, and coach around it.

Three: Get better at identifying budget earlier. Stakeholder mapping, earlier budget conversations, better qualification.

[SALESLOFT REP] And how can we help?

[LISA] Honestly? Help us operationalize this. We need tools and frameworks to track deal data, run experiments, and iterate on the playbook. Salesloft could help us create a system that lets us learn from every deal without it being manual.

[SALESLOFT REP] We can definitely help with that. Let's set up a follow-up call next week. I want to bring in someone from our enablement team to look at your data and help build that system.

[LISA] Perfect. This conversation already helped—I've got some concrete things to work on.

---

## Summary of Key Takeaways

**Category Education & Qualification:**
- Lisa's team struggles with problem reframing because prospects don't yet recognize MLOps infrastructure as a distinct category. They conflate it with other problems.
- Readiness qualification is more important than problem qualification—a prospect can have the pain but not be ready to solve it.
- Early signals include: hiring ML engineers, failed DIY attempts, budget allocated to infra, and executive sponsorship (not just technical champions).

**Playbook Building:**
- CloudMind doesn't yet have a documented playbook. Wins happen through ad-hoc approaches, creating variability in sales cycles and customer outcomes.
- A pattern is emerging: deals close faster when both technical and business stakeholders are involved from discovery.
- Win/loss analysis is manual and not yet systematized into coaching.
- Suggestion: Create role-specific playbooks rather than one universal approach, since different AEs and buyer types need different strategies.

**POC Scope & Management:**
- POCs are consuming 80% of SE resources due to undefined success criteria and scope creep. Scope is determined during the POC, not before.
- Ideal POC duration: 3-4 weeks, measuring a single specific metric (not multiple outcomes).
- Free POCs lack commitment signals; prospect priorities drift. Solution: Add contractual commitment layer (dedicated resources, weekly meetings, firm go/no-go decision).
- Paid POCs (only 2 of recent customers) show higher commitment but Lisa worries about killing early deals. Hybrid approach: Free POCs for strong fits, paid for exploratory prospects.

**Forecasting Challenges:**
- Traditional pipeline stages don't work for category creation because variance is too high (cycles range 4-12 weeks, POCs range 2-8 weeks).
- Proxy metrics being tested: stakeholder count, competitive situations, budget approval status, implementation urgency.
- Stage definitions may need to be reframed around problem understanding, solution fit, implementation planning, and budget approval rather than traditional product stages.
- Category-specific challenge: Implementation POCs are half-product evaluation, half-customer education, which doesn't fit standard POC definitions.

**Budget Discovery:**
- Budget sources are fragmented across multiple teams (engineering, data, DevOps, finance) with no standard allocation.
- Weak signals: "We'll find it in budget planning," "We're thinking about it"
- Strong signals: Prior infrastructure investments, hypergrowth companies, recently funded companies
- Budget discovery happens too late (during technical evaluation or POC). Suggestion: Move it to second discovery call by asking "How would you fund this if it works?" rather than "Do you have budget?"
- Specific category challenge: Cost savings from the solution may be distributed across five budgets rather than consolidated into one funding source.

**Organizational Readiness:**
- Lisa's sales team is learning as they go, which creates coaching challenges. They need systematic ways to capture learnings from each deal.
- Stakeholder mapping isn't structured; who holds the budget often isn't clear until late in the cycle.
- Three priorities for next 90 days: structured POC framework, documented playbook from win patterns, earlier budget discovery and stakeholder mapping.

