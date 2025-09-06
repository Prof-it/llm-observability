# Appendix C: Interview Transcript of Participant C

**Interview Location:** Zoom  
**Mode:** Online  
**Date:** 13/05/2025  
**Participant Role:** Lead Engineer at the case fintech

---

**Interviewer:** Okay, cool, you seem to be very involved in AI in the company, and I'm trying to gauge your role in our AI transformation. Yeah.

**Participant E:** So, I mean, I think for me it has mostly been a tool to boost or improve my productivity within my role. For example, I actually just had to put together a demo for a call with a merchant. And I was able to use Winsurf, which is an AI-assisted IDE, to build, to recreate the merchant's website in a few hours. This work normally would have taken a very long time. So that's one way that I think it's helping: we can now spin up demos to explain API concepts or help a merchant integrate much, much quicker than we could before. We plan to see how we can use it for the documentation, so, you know, have an AI chatbot on the docs that you can ask questions. It has context of all the information. And yeah, also trying to see how we can use it for content generation, right? So we want to create a bunch of tutorials that talk about how to use The Company API, stuff that will help with developer onboarding, basically. And so we recognize that we can use an LLM to help us generate content if we can come up with good topics. You know, we set like a template for what a tutorial should look like, because tutorials are pretty much templated, right? It's a series of instructions. So we can use AI to help us generate tutorials at a much faster rate than if we were just writing them ourselves.

**Interviewer:** So, are any of these things live yet, or are they just things in the works? Um...

**Participant E:** So the demos, I mean, I've already done—I've now done two demos, I've created two demos using Winsurf. So they're not live, I guess they're live in the sense that we use them for calls already, but they're not things that we've like, put on GitHub for those merchants. Um, the content generation is in the works. A member of my team is working on that. We're hoping by June we'll start publishing items. And then our docs, there's a bunch of other work that we have queued up, so it's on our roadmap, but it's far down on the roadmap at the moment.

**Interviewer:** All those projects, are they like Developer Relations projects, or is there like a The Company platform where, you know, you do these things, or is this just you and your team doing your thing?

**Participant E:** Yeah, so far it's just kind of been me and my team doing our thing. You know, I think The Company had not really established its AI stance. I guess made it clear that they're trying to, I guess, that we'll not be able to integrate some of our efforts with the platforms that The Company is providing.

**Participant E:** Okay. So, yeah, I was saying for a while it was just kind of our own thing. We were just making use of our own tools because The Company was not really clear on how we should be using AI. We knew that we shouldn't be using it for sensitive data. It was only like open-source initiatives and stuff that we would use it for, or things where we know like, you know, yeah, we're not exposing any data from The Company. But now that The Company, you know, has kind of said more formally that they want to encourage people to leverage AI tools, I think that now opens up the door for us to do some more interesting things. We can actually work with, you know, our, say, internal proprietary code. So things like the documentation that we can connect to external...

**Participant E:** ...third-party LLMs without it being a risk issue. So definitely expect that we will be exploring more exciting applications in the months to come.

**Interviewer:** But like, do you—I just wonder, right? I know like there's the whole AI thing going on, but like, do you have a clear—so is this like um, um, because I heard that there's like a sandbox AI environment somewhere that's still very coded. Do you plan to utilize these kind of platforms, or is this just um, um, Dev Rel-ish? Like, I'm just trying to understand like maybe those of you at the top see some cohesiveness that we don't see, because like everything feels all over the place right now.

**Participant E:** I think it—no, it definitely is all over the place right now. And I think maybe that's the hope is that like through this AI month group or whatever, um, we can start to build some cohesion across The Company in how we approach it. But yeah, it's definitely been very disjointed. You know, engineering has been doing their own thing. My team has been doing their own thing. People aren't really sharing how they're using AI very widely at the moment. Um, but yeah, I hope that this pilot helps. I'm actually not in it. I just don't have the time at the moment to not do any other work on my Fridays. Um, but I think there are enough people working in it, um, that something good can come out of it and maybe we'll start to see more applications of AI that are cohesive across The Company.

**Interviewer:** Okay, so, so time keeps coming up, and I think I'm approaching this interview now from like an individual explorer. You seem to have been doing a lot. I see your name on lots of Slack channels like, and...

**Participant E:** Now you're breaking up. Oh.

**Interviewer:** Oh, can you hear me now? Sorry, okay.

Speaker 3: Yeah, I can hear you. Yeah.

**Interviewer:** So, I said I think I'm approaching this like from an individual expert. So what do you think like, um, you've said time and that's what I've heard a lot. DevRel has big plans, but do you feel like you have the skills and like you have everything to just make it work right now because...

**Participant E:** Yeah, yeah. I think time is the real thing, is that I think these things are exploration. It's an amount of time, right? Because you may not necessarily—like you may have a plan, but there's so many different ways that you can approach the problem. There's so many things that you may not have even thought of. And so I think to make the most of it, you actually have to give yourself time to really explore, which is, I think, why the idea is, you know, take your whole Friday off, like you have a full day every week for these types of explorations. I very much would have liked to take part. For me, it was two things: it was one, yes, I don't feel like I have the time right now because I'm just very, very busy, um, at the moment, um, because like, you know, a teammate of mine is on sabbatical and I'm covering for their team and everything. So it's just a very, very busy time. Um, but a member of my team is actually doing it, so, you know, I'm hoping that he will be able to bring it to bear for the team. And then the second thing for me is that I actually do a lot of exploration already in my free time. I'm not necessarily missing out too much because I've already spent a lot of time learning about AI tools and I'm already using them fairly regularly in my work and personal life.

**Interviewer:** Okay. Okay. That makes sense. Okay. So now, to my project. I don't know if you've had time to like, go through the brief, and since you have been exploring with AI, it would be good to like, get your perspective, right? So do you think that like, if you have looked through it, the idea is, you know, how observability is evolving and maybe observability at The Company needs to like, evolve along, right? It's not more just about collecting telemetry data now. A lot of people are bringing security into observability. They're bringing business into observability. So did it make sense to you? And maybe from your role at The Company, right, from your perspective at The Company, does the whole idea of the project make sense to you and do you think it's feasible?

**Participant E:** Yes. I actually wish I could remember the name of the tool, but there was actually some tool for like LLM-assisted observability that I saw once. And I thought it was really cool. I think it's really, really cool. I think that there's definitely a lot that we can gain from it. And so I guess I'll talk about like my experience with our observability tools first, and I'll use that to

Right now, I've honestly never had a bunch of time to spend, or I just haven't made the time, I should say, looking through a bunch of Datadog's documentation. So most of what I know is from fumbling around and just trying to do things in the UI. LLM-assisted observability allows me to just ask questions. It changes how I can interact with a tool like Datadog because I can just ask my questions rather than having to know the exact string that I need to enter for my search or understanding all the charts and everything that we've set up to monitor the health of a particular integration.

Beyond that, I think that other applications of it are around the insight it can give you into the performance of your system. So I know engineering has tried in the past to quantify the cost of different services that we're running within The Company and even to be able to say how much we're spending on Kenya in terms of infrastructure costs versus how much we're spending on Nigeria, and to be able to include that in the different P&Ls or whatever they call them for the different countries. And I think that's really, really interesting. It would be very interesting to know how much our services are costing us, and it feels like that's something an LLM can help you do and figure out and analyze in a way that would be much easier than if you were just trying to do it on your own. So I definitely think that there are really, really cool applications. 

And then, even from a Developer Relations perspective, one thing I'm always curious about is having more insight into where developers are getting stuck on the API. So I can technically do this right now where I can go and see which endpoints are we seeing the highest number of 400 errors on, for example. But again, an LLM-powered observability tool can tell me even more. It can generate reports for me on a weekly or monthly basis to say, "Yeah, this seems to be where most developers are getting stuck." And it can just do a deeper level of analysis than I would be able to do. So yeah, I think we should definitely be trying to do more with LLMs and observability.

**Interviewer:** Yeah, that makes sense. And to be fair, I think Datadog already plans, I think they still have one in beta, to add some LLM capabilities and all of that, which would make a lot of sense. But since we are even talking observability, let me ask: how frequently do you interact with observability tools right now?

**Participant E:** Um, so on Mondays, I do support. I'm like the on-call for the support team, so if on a Monday somebody from the support team has to escalate a technical issue, there's a chance I'll have to use Datadog to do some troubleshooting or some debugging, I should say. So, yeah, and then I guess, yeah, if I'm debugging an issue with one of our third-party integrations, so let's say at least once every couple of weeks.

**Interviewer:** Okay, and how much do you think that it supports those your debugging scenarios?

**Participant E:** Oh, I mean, it's very helpful. Yeah, it's very, very helpful, particularly for viewing logs. Oftentimes, if I'm trying to figure out what's, you know, a merchant has made some complaints that what they're getting from the API doesn't match up with what they're sending to the API, going to look at the logs is the number one thing to do. So it's a useful tool for sure. In fact, I wish I could figure out how to give access to Datadog to our BPO agents so that they can also leverage it and unblock themselves quicker.

**Interviewer:** Yeah, then not have to wait for you guys. Would you say this is the same experience with your team, right?

Speaker 4: Yeah, so.

**Interviewer:** So on a scale of one to five, how easy is it to use Datadog currently, maybe?

**Participant E:** I'd put it somewhere in the middle. Again, I think that the tool is probably easy. It is easy to use. I'm just limited by my own understanding. The things that I know how to do, I know how to do them; they're very easy to do. There's a lot of stuff that I was able to figure out kind of intuitively. And yeah, I imagine that all the other stuff, if I read the documentation, it would be very easy for me to figure it out. So actually, I would say it's probably very... it's... if five is like very, very, very easy, I would say maybe it's four. Okay.

**Interviewer:** Cool. So like, I think that's fair enough. But a lot of times, do you think like the data is enough? Because I've been on incident calls where you have all the data, but you need to call an experienced engineer to explain. But do you really run into those kinds of scenarios?

**Participant E:** I mean, I've had them for some specific instances. I remember some issues I was having with a merchant at one point. And yeah, you know, I'm looking at the logs, but I still couldn't make enough sense of them to understand the issue. But I don't know if that was... it wasn't a fault of the tool, I guess, as much as it was our own understanding of the process, if that makes sense. So the issue that the merchant was having, it's like, again, you know, like you said, you'll have to call the person that built the API so they can help you decipher the thing. But the tool itself, like Datadog, is doing what you expect it to do. It's giving you the information that you need to debug. Somebody probably just didn't set up the right things to be passed to Datadog.

**Interviewer:** Yeah, and I think that's the place where we're getting to. So a lot of observability has been like, you know, you need telemetry, you need logs, and when you look at it also, you see that sometimes the context to resolve some incidents is actually not generated by systems. Yeah, some of those contexts are like in the heads of people in product documentations, and that's why we are trying to say, "Okay, can we have like operational knowledge in a vector database or something that people can easily just pull against their, you know, their normal observability data?" And there are platforms that actually do it. I know Elastic has an option for you to bring in your RAG source and just attach it to your database, and that's somehow where this project is supposed to be geared, right?

**Participant E:** I see.

**Interviewer:** It's not just operational data, it's like business data. So latency is high, what does that mean for PIV, like those kinds of correlations?

Participant L: Oh yeah, I like that. Yeah, yeah.

**Interviewer:** So, based on that, do you think that this is a reasonable project? I mean, and I'm saying reasonable based on The Company's context.

**Participant E:** A hundred percent. I think that, you know, we can definitely be more data-driven. And I think the more data points that we can share, the larger picture we're able to create about how the business is doing. You know, like, yeah, being able to say, being able to attribute a number and be able to say like, you know, a 2% increase in latency equals an X percent loss in your PIV or whatever is pretty cool. Like, that would be very, very interesting. It just, yeah, it grounds everything that everybody is doing in some reality, I guess. Everything can be tied to proper metrics. So, yeah, I think it definitely benefits us.

**Interviewer:** Okay. How much do you know about the technologies that I put in the brief? So I know I put a RAG framework. Some people have said, "Oh, I think you use MCP servers." And then some people have said, "Do you have any recommendations on like my conceptual idea based on all your plenty personal research?"

**Participant E:** I would need to go through it again, I think, to make a suggestion, but yeah, I am familiar with those tools, and so can definitely advise.

**Interviewer:** Let me share. Yeah.

**Participant E:** Yes, I remember this now. Okay, it's a RAG agent telemetry business metrics. Yeah. And so you said what people were suggesting?

**Interviewer:** So someone had said to use MCP. Okay, so somebody says, "Oh, our AI maturity at The Company is just somehow, just take everything to Bedrock," which I think they have support for a lot of these things. Somebody has said, "Oh, you don't need to use Bedrock. You can switch this up and use MCP servers instead of different telemetry agents." Do you have any ideas of anything that needs to switch up? But I think we should... What do you think about hosting? I mean, generally, if I wanted to host this solution, would you recommend like, let's just use the vendor, or let's try and do this in-house, or let's do some parts here and there like based on what you know, constraints knowledge yeah 




***********
**Participant E:** Based on our constraints, it would need to be in-house, considering the data sources that we want to use here, right? But I think, yeah, and I think we have access to Bedrock, which I believe we should use for the models because, again, that will keep it in-house within our AWS infrastructure, if I'm not mistaken. So that would be ideal to use. The question of using an MCP server or RAG, I think, is separate from using something like Bedrock, because you can still use an MCP server, if I'm not mistaken, and connect to a model via Bedrock.

I think when an MCP server comes in is, yeah, and the question of do we need RAG if we have an MCP server, because with an MCP server you can just fetch the data at the time that you need it.

**Interviewer:** See, like that's where we have the API calls, and somebody has told me, "Oh, it's not a database that you should have; you should have Redshift." Okay, um, like the vector database is supposed to hold the static documents, like product manuals. Yeah, that's kind of...

**Participant E:** Stuff. Yeah, exactly. So, yeah, a knowledge-based agent is the one that's pulling from things like Notion, right? Yeah.

**Participant E:** Um, yeah, that makes sense, storing that in a vector database. Um, yeah, I guess business metrics, if you can get directly from Redshift, that's better than going through the database API. And then what telemetry agent? Yeah, so, and again, you know, you've said Datadog is working on some stuff. I won't be surprised if they have an MCP server soon that easily lets you execute queries. Yeah. So I think it's a combination of these things. I think definitely hosting internally and using Bedrock.

**Interviewer:** But yeah, I think everybody has said it's feasible, right? I've just heard things like, "Because of the resource strength, where are you going to keep your observability work when you're doing this?" You know, and all of that.

But yeah, really about that, what do you think The Company has to do for people to have more room to like, take experimentation to the next phase?

**Participant E:** Yeah, maybe because they're mandated to just do more of this type of thing. I think it just needs to be clear from the highest levels that experimentation is welcome. So when you have the CEO coming out and saying, "We're going to spend this month tinkering with AI stuff," it lets people know that it's encouraged, and I think it just creates a mindset shift. The Company was like that much earlier in our history, I think because things were a bit less serious; we had not been acquired. You know, and it was just a small startup, so people had more, I guess, leverage or were given more bandwidth to explore different things. But now it's like everything's so mission-critical; we're all focused on reliability, maintaining the system, etc. But yeah, I think that if company leadership fosters an attitude of positivity towards exploration, it creates a mindset shift in the company where people now begin to work on these types of things more often.

**Interviewer:** Okay, but there's that part, and you know, the feedback I've heard is, and it's even feedback you've given, like, "You've created AI month, but I can't really use AI month because I have other things." So is there a world where we're thinking of actually bringing people to focus on AI, like maybe a separate team?

**Participant E:** I think we'd have to have a—we will need a win first. We'll need to deploy something that is game-changing. You know, if as part of this AI month, one of the projects that comes out cuts support—maybe it cuts the number of support tickets that we get by 50%, and so therefore we're able to hire half the number of BPOs that we have right now—you know, that's clear monetary gain that we get from that. And I think at that point, there would be more sentiment for, "You know, we should take this thing more seriously and actually start..."

**Participant E:** ...building more and more tools. So until that initial win, I feel like it will still just be a thing where people are like, "Hey, we should explore it, but your other work is more important." We just need a big win for AI.

**Interviewer:** Okay, I wish I could be confident enough to tell you, "Oh, this will be a win," but I don't know that. No.

**Participant E:** Hey, back yourself up. We'll see, though. Let's work; you know, you never know where we'll go.

**Interviewer:** Yeah, I mean, but yeah, I...

**Participant E:** Actually agree.

**Interviewer:** ...with you. Like there needs to be something to sustain momentum, but it does seem like, like you said, leadership encouraging it is a good first step.

**Interviewer:** Yeah, so you've helped me a lot with my change management part of my work, my questions.

**Interviewer:** There's nothing else I want to ask you. Um, but yeah, like even if there's something I've not asked you, do you have any general thoughts? I'm still trying to look for one question.

**Participant E:** Um, no, honestly, I think in the course of your questions, I've shared most of my thoughts on AI. I'm very bullish about its capabilities. I think it is a real game-changer, and I think that everybody needs to be exploring it a lot more. There's so much work that we do that's just kind of like, you know, low-level grunt work that I think AI can really help us with.

**Interviewer:** But then what does that do to the workforce? Like, are you... are you anticipating...

**Participant E:** I...

**Interviewer:** ...fear? Because there are legitimate people who are scared of losing their jobs to AI.

**Participant E:** It unlocks us. I think that this isn't the first time something like this has happened, and yeah, there are definitely some jobs that will no longer exist because they're more efficient to do with AI. But there are not a finite number of jobs to be had, if that makes sense. Your job did not exist 60 years ago; your job didn't exist even 20 years ago, right?

**Participant E:** So, but what happened? New technology brought forth new applications of technology, which brought forth new jobs around that technology. The same happened in the industrial revolution way back when machines started taking jobs that human beings usually used to do in factories. It took away those jobs, but it also created a bunch of new jobs because people now have to maintain those machines. People have to build new machines that are more efficient than those old machines. People have time to explore other things and go to other jobs that already exist, because that's another thing: people also assume that there are not deficiencies in other types of jobs already. You know, it's like, yeah, AI may take away a copy marketer's job, but maybe we also need more teachers, and so that person can be a teacher instead. Or by AI doing the content marketing, it frees that person up to focus on being more strategic about their work, and so they're now planning marketing campaigns rather than just writing copy. So, um...

I think that, yeah, you definitely want to acknowledge that it will change the face of work, and there will be some jobs that it will replace, but I see no reason why we cannot be optimistic and look forward to it enabling us to do other, more fulfilling work.

**Interviewer:** But what if, um, you know, but what if I'm legitimately scared by the process of doing more fulfilling work? I'm the one that has to upskill or be let go.

**Participant E:** I mean, but isn't that what we should all want as human beings? You know, the...

**Interviewer:** The question is, is there the right support? Like, I mean, look at this, if we had to do something AI-related, there needs to be some intentionality about upskilling, don't you think?

**Participant E:** A hundred percent. Yeah. And I think that we are moving in that direction. For example, I know there's—I got an invite for a "how to use Claude, Grok, and ChatGPT at work" call tomorrow. So people are being invited to learn how to become natives of this new technology so that they don't get left behind. And I think that, yeah, if you are a forward-thinking person who wishes to improve, you'll take advantage of those opportunities.People are being invited to learn how to become natives of this new technology so that they don't get left behind. And I think that, yeah, if you have like. If you are a forward thinking person who wishes to improve, you know, you'll take advantage of those opportunities. The people that don't, for lack of a better word, are just lazy, I guess.  

**Interviewer:** Okay, so you think the employees have responsibilities too?

**Participant E:** Absolutely, absolutely.

**Interviewer:** But then again, let's look at the dark side of AI. How do you think we can mitigate it? I mean, for instance, if we consider my specific solution, there's finance data. There's giving AI the power to tell things, and we know there are hallucinations, there is bias. What would you recommend? Is that a deterrent, or how should we manage that?

**Participant E:** It definitely shouldn't be a deterrent. It's just another problem to solve, another thing to consider; it's acknowledging that. Because if you think about it, every tool that you already use is like that in some way. You know, we're trusting that Datadog's service will work. We're trusting that the frameworks we use to build The Company API will work. We're placing some sort of faith in the thing, but we're also putting checks and balances in place so that we're not left, you know, flat on our faces if one of our services starts to fail us. So in the same way, I think you approach AI with caution. You plan appropriately. You recognize that it's prone to hallucinations, so you verify the responses it gives you. You just be smart about the way you use it. I think the dark sides of AI that worry me more exist outside of, I guess, the corporate applications of AI. I see it there as more of a productivity booster. I think the dark side is in stuff like deep fakes and misinformation.

**Interviewer:** And stuff.

**Participant E:** Like that.

**Interviewer:** Okay, yeah, that makes sense. And...

**Participant E:** Environmental damage too, actually, because apparently, it costs a lot of energy.


**Interviewer:** Do you have any recommendations around how we should handle data to support more AI use cases?

**Participant E:** Yeah, I think that we should maybe consider replicating real data. So if you want to—I feel like, ideally, we should give people the opportunity to test very rapidly, right? And we want people to create applications that use The Company data. But the process of reviewing and granting access to that data is long, right? Because the governance committee has to review the tool that you want to use. They have to review the access that the tool will have, and so you might even be limited by their bandwidth or their ability to understand the use case.

 I think that one way to accelerate people's upskilling and also the exploration of ideas around using AI for The Company would be to, again, so the sandbox environment, basically, extend it to sandbox data. Take a bunch of data. So if it's like merchant data that I want to use, right? Take a bunch of merchant data, randomize it somehow, and create a sandbox that contains this data and mirrors The Company environment in such a way that I can build my application and test it and not have to worry about exposing The Company data. But as I'm building it, I know that the format of the data I'm using and everything matches The Company already, right? 


**Interviewer:** So I hear you. Sounds like you're saying that we need some experimentation with data, like some play data, right?

**Participant E:** Exactly, yeah, dummy data that we can use to play with.


**Interviewer:** I really, really, really appreciate your time, honestly.

**Participant E:** No problem at all, very happy to be of assistance.



---

*All company and participant identifiers have been anonymized in accordance with the project’s data ethics and confidentiality commitments.*
