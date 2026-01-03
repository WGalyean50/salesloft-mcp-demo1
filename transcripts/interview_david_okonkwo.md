# Interview: David Okonkwo - Cybersecurity CRO

## Metadata

**Date:** January 2, 2026
**Duration:** 30 minutes
**Interviewer:** James Chen, Senior Solutions Engineer - Salesloft + Clari Partnership
**Interviewee:** David Okonkwo, Chief Revenue Officer - Cybersecurity Platform (Fortune 500 adjacent)
**Company Profile:** $200M ARR cybersecurity platform, 450+ enterprise customers, 18-month contract terms, 40% of revenue from procurement-heavy verticals
**Context:** Discovery call exploring sales cycle challenges and Clari/Salesloft integration opportunities

---

## Conversation Transcript

**[JAMES]** David, thanks for making the time. I know you're busy, so I want to jump right into what we've been hearing from CROs in your space. We've talked to about fifteen security software companies in the last six months, and there's this consistent pattern around deal cycles getting longer. It's interesting because your ACV should push deals faster—you're at what, $500K-$1M per deal?

**[DAVID]** Actually, closer to $750K average now, which is up about 18% year-over-year. And you're right—cycle times are the problem. We're sitting at 8.5 months from first meeting to signature. That's up from 7 months two years ago. Revenue ops blames the market. Sales says it's always been this way. But when you model it out, we're leaving deals on the table just because of elongation.

**[JAMES]** 8.5 months is brutal. Walk me through where that time is actually going. Is it early-stage discovery, or is it bottlenecking at procurement?

**[DAVID]** Honestly, it's bimodal. You've got your Fortune 500 deals where procurement is an absolute bear—I'm talking 2-3 month procurement cycles after legal signs off. We're processing security questionnaires that are 200+ questions deep. Vendor risk assessments. SOC 2 audits, third-party risk evaluations. One deal we closed last quarter, the procurement questionnaire alone was a 36-item comprehensive survey covering everything from incident response playbooks to our board composition.

**[JAMES]** Are you seeing the same security questionnaire across deals, or is every buyer creating their own?

**[DAVID]** That's the maddening part—it's inconsistent. You get Dun & Bradstreet, then AuditBoard, then their own custom questionnaire from procurement. And the questions sometimes contradict each other. We've got one Fortune 500 tech company that requires separate legal review of our data residency clause because they have internal policies that supersede standard contracts. That's not in our template. So legal gets looped in, external counsel might get involved, and suddenly you're three weeks into a review.

**[JAMES]** And that's after you've already sold the deal—after the business case is approved.

**[DAVID]** Exactly. The technical buyer is sold. The economic buyer is sold. But there's this entire infrastructure of compliance and risk that operates independently. Our sales team calls it "the black box." You send docs in, and they disappear for six weeks. Then you get feedback on three questions and you're back to legal. It's sequential, not parallel.

**[JAMES]** What percentage of your pipeline is hitting that procurement wall?

**[DAVID]** About 65-70% of our seven-figure deals. Below $400K, it's maybe 35-40%. But here's the thing—our highest velocity deals, the ones that close in 3-4 months, aren't cheaper. They're actually often larger. The difference is we've got relationships already in place. We know the personas. We've mapped the buying committee early. So when procurement comes in, we're prepared.

**[JAMES]** Which brings us to something I want to dig into. You mentioned mapping the buying committee early. How are you currently doing that? What does your SDR qualification process look like?

**[DAVID]** This is where I'm actually pretty proud of our process, but it's also where we're scaling into a bottleneck. Our SDR team is really good at identifying the technical buyer. They're running MEDDIC frameworks pretty rigorously. But the problem is visibility into the procurement stakeholders. Your technical champion can't always tell you who's going to hold up legal review. And the economic buyer often isn't the one who understands the vendor risk process.

**[JAMES]** So you're identifying 70% of your buying committee and then discovering the last 30% during the sales cycle.

**[DAVID]** More like we're discovering them reactively when the deal stalls. Deal review meetings in month five or six, and a salesperson says, "Wait, we haven't had anyone from legal." And then someone finally tells you legal has been waiting on a compliance questionnaire response they asked for three weeks ago that the sales team didn't know about.

**[JAMES]** That's a communication and visibility problem. Are your AE's using any structured approach to track stakeholder engagement?

**[DAVID]** We use Salesforce pretty heavily. But Salesforce is what people put in when they want to keep their pipeline number. Real intelligence about who's bought in, who's neutral, who's actively blocking—that's in our AE's heads and maybe in a Slack thread. We've tried Gong for call recording and analysis, and we get good data, but it's after the fact. We're not using it prospectively to say, "You need to talk to this persona before you go into procurement."

**[JAMES]** Let me ask you something different. You mentioned deals that close in 3-4 months. Let's say you've got a $2M deal that closes in four months versus an $1.8M deal that takes 11 months. What's the key variable?

**[DAVID]** Buyer maturity and competitive situation, honestly. If the buyer is already sold on needing your category—they've had a breach, they're post-incident—that deal moves fast because there's urgency. They're going to fix the problem whether it's you, us, or Cloudflare. But if it's a proactive renewal or an expansion deal where the buyer is less certain about urgency, you're basically competing on features and price, and that's a slower process.

**[JAMES]** And when they're less certain about urgency, you're spending more time on discovery and proof. That's where the SE availability becomes critical, right?

**[DAVID]** Oh my God, yes. We're at about a 3.5:1 AE-to-SE ratio, which sounds fine until you dig into utilization. Our SEs are splitting time between three or four deals in active evaluation simultaneously. Proposal turnaround for a customized proof of concept is 10-14 days. But if the SE is booked on three other POCs, you're looking at 21-28 days. Meanwhile, you've got a competing proof of concept happening in real-time, and the buyer is comparing your speed to execute with your competitor's speed.

**[JAMES]** Has your sales team flagged that as a constraint? Like, "We lost this deal because our POC took too long"?

**[DAVID]** Rarely explicitly. But when you do post-mortems on stalled deals, it comes up. We lost a deal to [competitor] last quarter, $1.2M, and when we did the post-mortem, the buying committee said, "Your team couldn't get a POC environment stood up for 18 days. [Competitor] had one running in four days." Now, our POC is more complex. We're doing a more thorough integration proof. But the buyer doesn't distinguish between thoroughness and slowness.

**[JAMES]** So you're actually more thorough, but you're losing deals on delivery speed.

**[DAVID]** That's the tension, right? We could stand up a shallow POC in four days, but then we're not proving the real integration value. The buyer runs the shallow test, sees limitations, and says, "Actually, we're not sure this works for us." And then we're back to square one trying to expand scope. It's this weird paradox where being slow and thorough is better than being fast and shallow—but only if the buyer has patience.

**[JAMES]** How are you managing POC scope today?

**[DAVID]** We have a scope template. It's got four tiers based on deal size. But once a POC starts, scope creep is inevitable. The technical team starts asking questions that require us to test against their production environment, not a sandbox. The buyer wants to validate not just the main use case but edge cases. And honestly, sometimes it's a game-playing mechanism. The buyer knows scope creep extends the evaluation period, which gives them negotiating leverage.

**[JAMES]** Negotiating leverage for what?

**[DAVID]** Budget cycles, competitive evaluations, approval processes. If you're deep in a POC for six months, that POC becomes the default option. Moving to a competitor now means starting a POC from scratch. So there's switching costs. But also, if your deal is tied to a fiscal year budget and we're in month eight of a nine-month evaluation, the buyer can either push the contract signature into next fiscal year or accelerate it to this fiscal year. That's a leverage point for pricing discussions.

**[JAMES]** So scope creep is partly procurement strategy.

**[DAVID]** Absolutely. And we're not naive to it, but we don't have a good way to manage it without damaging the relationship. If an AE says no to a scope expansion request from a technical buyer, you're assuming risk on the deal. What if the buyer does need that data point to get internal approval?

**[JAMES]** This brings me to something that came up in a lot of conversations: "no decision" deals. Deals that move into the "stalled" category after months of evaluation. What does that look like in your world?

**[DAVID]** We track it, and it's actually a leading indicator of trouble. If a deal's been in "evaluation" or "proof of concept" for more than five months and we haven't had any forward movement in the last month, we'll call it at risk. But how many convert to "no decision"? I'd say 15-18% of our six-figure deals in evaluation get stuck. Some of those resolve eventually—we'll close them in month 12 or 13. But some just... languish. Buyer says they're still evaluating but there's no activity.

**[JAMES]** When you do a post-mortem on a "no decision," what are you usually finding?

**[DAVID]** The most common reason is consensus failure among the buying committee. The technical team loved us. The procurement team had concerns about vendor stability—we're a smaller company than some competitors—and legal couldn't agree on data handling clauses. Rather than negotiate those items, the buyer just delayed. Sometimes indefinitely.

**[JAMES]** So the buying committee isn't aligned and instead of escalating or negotiating, they just delay.

**[DAVID]** Right. And here's the thing that's really frustrating: we often don't know about the procurement or legal issues until we push. We assume deal delay is just normal evaluation timing. We're not getting visibility into the actual blockers until we do an explicit stakeholder check-in. By then, three months have passed and the consensus gap is even wider.

**[JAMES]** Are you doing stakeholder mapping exercises during the sales cycle?

**[DAVID]** Not systematically. It's dependent on how proactive the AE is and how good their relationship is with the technical buyer. If the AE has a strong relationship, they might explicitly ask, "Who else needs to sign off?" If not, it's a surprise when procurement shows up.

**[JAMES]** Let's talk about that. Multi-threading into accounts. You mentioned the best deals have relationships already in place. How are you currently building and tracking those relationships?

**[DAVID]** We've got a few account executives who are phenomenal at this. They'll have meetings with three or four different personas in the account before the deal is even in Salesforce. They're having coffee with the head of IT security, lunch with the procurement director, back-channel conversations with the CFO's office. That intelligence informs the deal strategy. But this is an art, not a science. It's driven by individual relationship-building skill and territory history.

**[JAMES]** And you can't scale an art across a sales org.

**[DAVID]** No. And what happens is your top 10% of AEs are landing 40% of the revenue because they have these deep relationships. Your bottom 50% is doing transactional deals or working markets where they don't have as much history. It's not evenly distributed.

**[JAMES]** When you look at your multi-threaded deals versus your single-threaded deals, what's the win rate difference?

**[DAVID]** Significant. Four-or-more-contact relationships close at about 72% win rate. Two-contact relationships are around 48%. Single-contact deals are maybe 28%. So there's a direct correlation between contact breadth and close rate. But here's the challenge: a four-contact relationship takes time to build and maintain. If your AE is managing 20-25 accounts, finding time to meet with four personas per account in each account is challenging.

**[JAMES]** What's your contact coverage target?

**[DAVID]** Officially, three to four per account. In reality, we're averaging 1.8 to 2.1 contacts per account that are actively engaged. So we're undershooting our own target by about 50%.

**[JAMES]** That's a gap. Why?

**[DAVID]** A few things. One: AE bandwidth. Our AEs are spending 60% of their time in Salesforce, email, and admin work. That's not customer-facing. Two: relationship gatekeeping. The technical buyer doesn't always want you talking to procurement because it raises questions. They'll say, "Let me socialize this internally before we involve legal." Three: we don't have a good system for tracking who we should be talking to. We're not using relationship intelligence to say, "For this account, you're missing conversations with the head of audit or the facilities manager." It's guesswork.

**[JAMES]** So you've got a 1.8 contact average when your data shows you need 4 to win. And the main blockers are AE time, stakeholder access, and visibility into the org chart. Have you looked at using business development reps or account executives specifically for stakeholder mapping?

**[DAVID]** We've talked about it. But we haven't pulled the trigger. There's a philosophy question there—do you hire additional headcount to solve for a process problem, or do you fix the process first and then hire? We've historically been a "fix the process first" company. But I'm increasingly wondering if that's limiting our velocity.

**[JAMES]** Let me put a pin in that and come back to it. You mentioned technical cycles and scope creep. Tell me about a deal where the technical cycle really extended and how that impacted the deal outcome.

**[DAVID]** We have a great example. A Fortune 100 insurance company, $2.8M opportunity. We got a POC kicked off in month three of evaluation. The scope was pretty contained: integration with three of their key systems, performance testing at their data scale. Straightforward. But about week three of the POC, they asked if we could test against their actual production architecture, not our simulated test environment. Now we're in a different conversation. We need to deploy in their environment, we need security clearance, we need infrastructure coordination with their ops team.

**[JAMES]** And all of that wasn't scoped.

**[DAVID]** Exactly. The original scope was "test integration capability." The expanded scope was "validate with our actual systems under actual conditions." That's a different engagement. It took us an additional four weeks to get infrastructure access and another three weeks to run the test because their ops team is supporting multiple workstreams. So we went from a four-week POC to a twelve-week POC.

**[JAMES]** And the buyer needed this production environment proof?

**[DAVID]** The technical team needed it. They were concerned about performance degradation. But—and this is important—the economic buyer and the project sponsor didn't necessarily need that level of proof. It was the technical team's risk aversion. They wanted to de-risk the deployment before committing to the license agreement. Which I understand. But it extended the deal cycle significantly.

**[JAMES]** Did you have a conversation with the economic buyer and sponsor about the value of moving faster with less perfect proof, or did you just accommodate the scope expansion?

**[DAVID]** We accommodated it. And here's why: we didn't want to jeopardize the relationship. If we pushed back and said, "You don't need production environment proof," we're either undermining the technical team's judgment or we're creating risk for ourselves if something does break in production. So we just accepted the scope expansion, executed it, and the deal closed.

**[JAMES]** Did it close at the original price?

**[DAVID]** No. They pushed for a 12% discount on the basis that they needed extra time to evaluate and they wanted a lock-in price in case fiscal year budgets moved. So we gave up margin and extended timeline simultaneously.

**[JAMES]** So the scope creep cost you time and money.

**[DAVID]** Yep. And this is happening on multiple deals. We're not systematic about scope management, so we end up in this position constantly. The buyer knows that pushing for more evaluation will eventually result in concessions because we want the deal to close and we've already spent the resources.

**[JAMES]** Going back to something you mentioned earlier: the competitive dynamic. How much of the cycle extension is driven by competitive pressure? Like, the buyer is evaluating you simultaneously with a competitor?

**[DAVID]** Significant. I'd estimate 60-65% of our six-figure deals are in competitive evaluations. And what that means is the buying process is anchored to the competitor's timeline and maturity, not ours. If we move fast on our POC and they move slow, the buyer delays our close to match their timeline. If they move fast and we move slow, we lose.

**[JAMES]** How are you tracking competitive dynamics during the sales cycle?

**[DAVID]** Our AEs are getting feedback from the technical buyer on whether we're competing and against whom. But that's dependent on the buyer being willing to share. Sometimes we find out we're in a competitive bake-off only when we reach the proposal stage. We're not using any competitive intelligence tools. We're basically relying on sales team intel.

**[JAMES]** And you're not mapping competitive timelines against your own timelines.

**[DAVID]** Not formally. That's something I've thought about but haven't implemented. It would be useful to know, "Competitor is 4 weeks ahead in their POC" or "Competitor is in procurement while we're still in evaluation." That visibility would help us adjust our strategy.

**[JAMES]** Let's talk about budget cycles because I think this is an underappreciated variable in extended sales cycles. How much of your deal timeline is driven by the buyer's fiscal year or budget processes?

**[DAVID]** Probably 25-30% of our cycle timing. If a deal gets kicked off in October and the buyer's fiscal year ends in December, you're in a race to close by end of year. Miss that window and you might wait until next fiscal year budget is approved. But if you kick off in January and you're still evaluating by end of July, you're waiting for next fiscal year budget allocation. And we've had deals stall for six months because the buyer's next fiscal year allocation process wasn't complete.

**[JAMES]** And when those budget cycles align poorly with your sales cycle, what do you do?

**[DAVID]** You wait, mostly. Or you negotiate an early commitment if the buyer is willing to reserve budget from current year for next year. But that's a conversation we're often not having early enough. We should be asking about budget allocation and fiscal year processes in discovery, but we're not. We're assuming discovery is about problem statements and use cases, not about procurement and budget processes.

**[JAMES]** That's a discovery design problem. Are you teaching your SDRs and AEs to ask about procurement and budget timing in initial qualification?

**[DAVID]** Not really. The qualification framework is MEDDIC, which touches on decision criteria and timeline, but not explicitly on procurement process, legal approval, or budget cycle specifics. That would be a good process change. We'd learn earlier whether a deal is going to be a four-month deal or a twelve-month deal based on the buyer's process.

**[JAMES]** Okay. Let me zoom out and ask you this: if you could fix three things about your sales process to reduce deal cycles and increase win rates, what would they be?

**[DAVID]** That's a good question. Three things: One, visibility into the procurement and legal processes earlier. We're in discovery but we're not asking about vendor risk, compliance questionnaires, or legal review timelines. We're just finding the technical buyer and assuming the rest will flow.

Two, better stakeholder mapping and multi-threading. We're leaving deals on the table because we're not building relationships across the buying committee. We're single-threaded or two-threaded when we should be four-threaded.

And three, POC scope management. We need a more rigorous way to define scope, negotiate scope changes, and have conversations with economic buyers and sponsors about the cost of scope expansion in terms of timeline and deal economics.

**[JAMES]** If I could show you a tool or a process that addressed all three—visibility into procurement risk factors, stakeholder relationship intelligence, and POC scope governance—would you be interested?

**[DAVID]** Absolutely. But I'd need to see how it integrates into our existing workflow. We've bought tools before—Gong, a predictive analytics platform, Outreach. Some of them have had real impact. Others became shelf-ware because they required too much manual data entry or they didn't integrate with Salesforce. So it would depend on integration, adoption ease, and whether it actually helped us win more deals or close them faster.

**[JAMES]** What would success look like? Like, what metrics would you be tracking to determine if this was working?

**[DAVID]** Sales cycle time, obviously. I want to see that 8.5-month average come down to 7 months within a quarter. Win rates on six-figure deals increasing from the current 52% to 60%+. And contact coverage increasing from 1.8 to at least 3.5 per account in active deals. Those would be the primary metrics.

**[JAMES]** And what would a 60% win rate on six-figure deals mean for your revenue?

**[DAVID]** [Pauses] That's... significant. We've got $240M in pipeline currently. If 45% of that closes instead of our current 52% average, we're talking about $40M in additional annual revenue. Probably $8-12M in margin upside depending on deal mix. So this is worth real investment.

**[JAMES]** I appreciate the specificity. Last question: what's your biggest fear about implementing a new sales tool or process?

**[DAVID]** Adoption. My sales team has been doing things a certain way for a long time. They've built relationships and intuitions based on that way of working. Asking them to change their discovery, asking them to multi-thread differently, asking them to use a new system—that has friction. I need a vendor or partner who understands that and can help drive adoption, not just tool implementation.

**[JAMES]** That makes sense. What would help with adoption? Like, what kind of support would you want?

**[DAVID]** Training, obviously. But more than that—working with one or two of my top AEs first to prove the concept. If I can show the sales team that the tool helped Jane land a $1.5M deal or helped Mike reduce his cycle time from 10 months to 7 months, adoption becomes much easier. You need social proof within the organization.

**[JAMES]** What's the timeline you're thinking for a tool like this?

**[DAVID]** We've got a board meeting in Q1 where we're looking at operational efficiency and deal cycle reduction. This would fit that narrative. So if we could move fast in January and February, we could have a proof of concept by March. If it's working, we implement more broadly in Q2.

**[JAMES]** That's helpful. I really appreciate your time and your candor. This has been super useful context.

**[DAVID]** Happy to help. And I'm genuinely interested in what you're building. If you can make this work, if you can give us visibility into the real procurement blockers earlier and help us build better stakeholder relationships, that's transformative for how we operate. Send me something by end of month?

**[JAMES]** Absolutely. I'll put together a customized brief on how Salesloft + Clari could address your specific workflow, and we'll schedule a follow-up conversation with your team.

**[DAVID]** Perfect. Thanks, James.

**[JAMES]** Thank you, David.

---

## Key Takeaways

### Deal Cycle Challenges
- **Current State:** 8.5-month average sales cycle, up from 7 months two years ago; 65-70% of seven-figure deals hitting procurement bottlenecks
- **Primary Bottleneck:** Procurement and legal processes (2-3 month cycles) happening sequentially after business case approval, not in parallel
- **Secondary Bottleneck:** SE availability constraining POC turnaround (10-14 days becomes 21-28 days in resource contention)

### Procurement Complexity
- **Security Questionnaires:** 200+ question assessments; inconsistent across buyers (Dun & Bradstreet, AuditBoard, custom)
- **Vendor Risk Processes:** Separate from technical evaluation; operate in black box with 6-week turnaround expectations
- **Legal Review:** Data residency and compliance clauses sometimes require external counsel, adding weeks
- **Discovery Gap:** Security questionnaire requirements not discovered until month 5-6, when deal is deep in evaluation

### Stakeholder & Multi-Threading Issues
- **Target:** 3-4 contacts per account; Current Performance: 1.8-2.1 contacts per account (50% shortfall)
- **Win Rate Impact:** 4+ contacts = 72% win rate; 2 contacts = 48%; 1 contact = 28%
- **Relationship Gatekeeping:** Technical buyers reluctant to introduce procurement/legal early; creates surprise delays
- **AE Time Constraint:** 60% of AE time in admin/Salesforce; limited capacity for stakeholder relationship building

### Technical Cycle & Scope Dynamics
- **POC Scope Creep:** Drives 4-week to 12-week extensions; often driven by technical team risk aversion, not business requirement
- **Scope Creep Economics:** Extends timeline AND results in price concessions (12% discount example); buyer knows extended POC = leverage
- **No Formal Governance:** AEs accommodate scope expansion to preserve relationships; economic buyers not engaged in scope trade-off conversations
- **Competitive Timing:** 60-65% of deals in competitive evaluations; buyer's timeline anchored to competitor maturity, not forecast

### Budget & Fiscal Year Dynamics
- **Impact on Cycle Time:** 25-30% of deal timeline variation driven by budget cycles
- **Discovery Blind Spot:** Not asking about fiscal year allocation, budget approval timelines, or procurement process timing in qualification
- **MEDDIC Limitation:** Current qualification framework addresses decision criteria but not procurement process or budget cycle specifics

### "No Decision" Dynamics
- **Current Rate:** 15-18% of six-figure deals; tracked as "stalled" after 5+ months with no forward movement
- **Root Cause:** Buying committee consensus failure (technical team sold, procurement/legal have concerns)
- **Visibility Gap:** Issues discovered reactively when deal stalls, not proactively during evaluation
- **Lack of Escalation:** Buyers delay rather than negotiate; sales team often unaware of actual blockers

### Opportunity & Urgency
- **Revenue Impact:** 60% win rate on six-figure deals vs. current 52% = $8-12M margin upside
- **Timeline:** Q1 board meeting on operational efficiency; proof of concept possible by March
- **Adoption Risk:** Sales team needs social proof; pilot with top AEs before org-wide rollout
- **Required Support:** Training + proof of concept with high-performing AEs; tool must integrate with Salesforce; adoption dependency critical

### What David Needs
1. **Earlier Visibility:** Procurement and legal risk factors discovered in discovery, not month 5
2. **Stakeholder Intelligence:** Org chart context and relationship mapping to identify missing personas
3. **POC Governance:** Scope definition, change management, economic buyer engagement in timeline/cost trade-offs
4. **Integrated Workflow:** Solution must fit existing CRM and require minimal manual data entry
5. **Adoption Support:** Not just tool implementation; training + proof of concept + internal social proof required

---

## Background Context for Follow-Up

### Account-Specific Intelligence
- **AE Performance Gap:** Top 10% of AEs generating 40% of revenue due to relationship depth; indicates process/system can unlock significant upside
- **Competitive Position:** Competing against larger vendors (Cloudflare mentioned) on execution speed; smaller company perception as vendor risk factor
- **Product Advantage:** POC more thorough than competitors but loses on delivery speed; positioning/scope management could resolve

### Organizational Readiness
- **Process Orientation:** "Fix process first, then hire" philosophy; receptive to systematic improvements
- **Tools in Place:** Salesforce, Gong, Outreach; looking for integration, not replacement
- **Executive Support:** CRO personally tracking metrics and timelines; high-level buy-in for change initiative
- **Timeline Window:** Q1 board presentation creates urgency; 60-day proof of concept window realistic

### Risk Factors
- **Sales Team Skepticism:** History of bought tools becoming shelf-ware; requires strong adoption plan
- **Process Resistance:** AEs comfortable with current approach; need internal champions to demonstrate ROI
- **Integration Complexity:** Salesforce integration critical; custom workflows may be required
- **Short Timeline:** Proof of concept expected by March limits implementation depth; MVP approach necessary

