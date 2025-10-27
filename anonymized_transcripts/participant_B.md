# Appendix B: Interview Transcript of Participant B

**Interview Location:** Lagos, Nigeria  
**Mode:** In-person  
**Date:** 14/05/2025  
**Participant Role:** Lead Engineer at the case fintech

---
**Q: Okay, so you know the background of the project. Observability is evolving from just monitoring servers to getting telemetry, to getting implications of what these metrics actually mean to the business. My first question to you is, with the current state of the company's observability, how much do you think our observability data influences business decisions?**

A: The metrics and the data from the observability platforms help us know and understand how our systems behave. The observability data and platforms help engineers from an uptime perspective. We're talking about knowing how our business is able to serve our customers, and the business cares deeply about being able to serve our customers. From a business perspective, as the company has grown and expanded to multiple markets, one of the key things that partners, merchants, and big customers ask for is our uptime. Usually they try to emphasize a couple of nines. I think the company is currently doing four nines, three nines, so 99.98. Based on the observability data we're able to gather, we are able to send merchants SLAs and sign contracts using those SLAs. So I think the observability data is the heartbeat of what we do in engineering right now, to be honest. For the business as a whole, engineering itself has a bi-weekly principal call, and on that principal call, it is literally observability data that we're reviewing to measure the performance of our platform.

**Q: Okay, so I hear you: uptime, availability. So, you track these metrics, you talk about it. But can you, for instance, easily tell, "Okay, APM uptime went up for this period, and this is what it did to like PIV," or, "We got increasing customer tickets?" How quickly is it to make that correlation?**

A: How quickly? I wouldn't say it's as quick, but do we have the data to be able to make those inferences? I think the answer is yes. Now, depending on, we probably need more instrumentation because, if you take note, the things you asked now, they are not directly tied together. The output of one probably influences the input of the other, and there are systems that are codependent. So now we need a little bit more instrumentation to be able to tie those things directly. So, for me, we are able to make those inferences, but are we able to make them as efficiently as we possibly could? I think the answer is no, but we are able to make those inferences.

**Q: Yeah, you've looked through the project brief, and it positions LLM as a possible additional tool that can help to tie things together, perhaps more efficiently. So, do you agree, based on the conceptual design which I hope you have gone through?**

A: In an ideal world, yes, but the challenge is always going to be, "What does tying these things together mean?" because this is an AI project. In the world of AI, yes, LLMs help you with a certain amount of reasoning. The LLMs help you with a certain amount of inference, and I think ultimately they help with a lot of translation, meaning taking natural language and converting it into structured text in one way, shape, or form. The answer is yes, LLMs will help, but what is the instrumentation that we would need to help the LLMs to help us? All the different data elements have their own different formats and have their own different structures. The LLMs need to know that this is how X is related to Y, and there is work that needs to be done to tie them together. The LLM needs to know that these are the parameters it needs to look at when considering traces, and these are parameters that it needs to look at when considering the applications, and these are the parameters to consider when considering merchants that might be affected by this. But you understand, the whole tying together needs some instrumentation. So absolutely, LLMs can do it, but we can't just throw data at the LLMs and ask them to solve the company's problems. The company has to solve its problems by leveraging LLMs, and I believe that's what your research is going to help us do. Your research is basically giving us the theoretical approach or the theory behind how we can tie those segments of data as it relates to observability to solve our problems.

**Q: It already said we're going to use agentic RAG and LangChain because, I mean, when I first started this research, my first idea was to pull data together in one location. But I've quickly seen how complex that can be, and based on my talk with some people, so, here we're saying, "Okay, we don't pull, just we can fetch those data in real time when we need it through agentic RAG or via the API." So, does that instrumentation make sense to you? Because I feel like it reduces the complexity of the work. And then the Observability Lead gave me an idea with MCP servers; I haven't explored it a lot, though.**

A: My answer is that it depends. When designing AI systems, there are some of them that would require... If I were to build a proper AI solution for, and yes, I've been doing a lot of research on AI, I've been playing around, I've actually even built a tiny framework, but if we were to design an AI system to help with the problems that we're mentioning, there isn't a one solution. No one can tell me, and I don't agree that RAG is going to fix the problem. I don't agree that just agents will fix the problem because there's a world where agents are way more complicated, and you don't need agents; you just need simple workflows. So all those things need to be brought to bear. Take a step back and consider what you desire, what the purpose is, what we're trying to achieve, what the data elements are, what the data sources are, and what approach might work best for the different functions or for the different procedures that we want, or different goals that we want to achieve. Because not every goal will have the same level of implementation, right? Some would literally just be reading from documents and giving you back. Some will be performing actual function calls. Some would be the LLM using its computational abilities to run those computations. Some would be literally comparing things from the embeddings that are stored, which is the documents or different type of... There are multiple implementations, and I believe a good AI system or a good LLM-powered system, especially for a company like ours, will consider all of them and would have all of them somehow working together to give you the solutions that you desire.

**Q: So what do you think should be in place? I mean, there is a clear use case. We're trying to correlate operational, telemetry, and business data. So when I say operational data, product documentations, incident reports, all of these things can sit in a vector database instead of in people's heads. And then, yes, so the use case is clear.**

A: What about storage for those? What about storing the vector database? We now introduce new problems such as uptime of the vector database, right? All those things need to be factored in.

**Q: They will get, of course, they'll get factored in. So, so these are your, thank you, so these are your, so if I hear you, you're saying, "Okay, I think this is a feasible project." But yeah, I think this is what should be considered, right?**

A: Absolutely. Everything needs to be considered.

**Q: So you've mentioned costs, you've mentioned data. You've been particular about data. Is there anything else you want to flag?**

A: I'm saying data. And when I say, and I always repeat data again, data is not just any type of data. There is dirty data and there is clean data. Data has to be cleaned. Data has to be structured in a certain way. What are the inputs that we're giving the LLM? What are the outputs that we're getting from the LLM? The hardest part of building AI applications, from what I gather from my own experience, a little experience that I have, is interpreting what the LLM decides to spit out. Because the honest truth is if you are expecting structured data and the LLM spits something that is non-structured, then how are you going to resolve that? How are you going to factor that? It might be a correct response, but if your programmatic interface to the LLM's output does not match what the LLM's output is, then you understand that you have a failure. It might actually be the correct, and it could be as simple as the LLM saying or giving two sentences instead of one. So how you handle and parse those responses usually tend to be very, very tricky for LLM-based applications. And I think that's where a lot of effort would go. Have I answered your question? What was the question again?

**Q: Considerations**

A: Yeah, exactly. So those are things. So the data is one: cleaning up the data, what are the inputs, what are the outputs, which LLM are we using? Because, no, sorry, what model are we using? Because now there are multiple models. What is the budget? What are the context windows? How many parameters? Because sometimes you probably don't need something with 70 billion parameters; you probably need something with 3 billion, and it works. You should

**Q: So what structures do you think the company currently has in place to support the project? As the Head of Infrastructure, I've shown you my solution, and you've mentioned all these considerations. With the current setup, what does the company have to support my use case?**

A: None. And here's why: the company is still in its infancy when leveraging LLMs. I don't mean that negatively; I mean right now we're exploring the different ways we could use LLMs within our systems. There are people in the company thinking about how LLMs can solve their own problems. Some are easier to solve, some are very difficult, some require a little work, and some just require plugging in.

For instance, a simple use case: an audit-based solution is very different from a fraud-based solution within the same world of LLMs. One simply involves embeddings, while the other requires a lot of tooling, function calling, or back-end tooling—not the LLM making calls, but you building custom logic and implementing the LLMs to call the functions. So you have to define those functions properly. You see how different those two implementations are.

At this point in time, we are exploring what the possibilities can be. There are a few people in the company trying to make investments for people to explore a lot more. But once we get a few use cases that we think are feasible with limited bandwidth—and we are still a payment company—once we get a few use cases we can implement, I know the company is willing to put resources down, implement those solutions, and test them out quickly. I think that is something the company is currently exploring and willing to do.

**Q: So it's safe to say that there's no clear roadmap here; it's still a lot of exploring.**

A: There isn't a clear roadmap, but the intentionality the company is taking is something I admire. The company is taking the month of May as "AI Awareness Month" and giving people the opportunity to explore. I think it's going to turn up some pretty interesting things in the future.

**Q: The sense I get is that the data team is not very "big data" focused. So I think we still see observability data as observability data, and transaction data as transaction data. Teams just sit and analyze their data, but there's a trend now where people think that big data—just bringing data together and analyzing it together—has a lot of value. On a scale of one to five, how would you rate the big data strategy at the company?**

A: We don't have a big data strategy at the company. Let me put it this way: when you talk about big data in terms of everything together, we don't. I think our data is still going to be siloed or segmented for a while. The reason why is that data engineering at the company is currently making data available for business decisions. Data engineering is trying as much as possible to support the business needs from an analyst perspective, like data analysis and everything, so that the business can make more decisions. Now, once we get a good handle of what that looks like, or what that should look like, or the evolution of that, we can start thinking, "Oh wait, should we actually bring all the data elements together?"

I don't know that that is the conversation right now, but that conversation is crucial because it will definitely support an AI or LLM strategy or machine learning strategy at the company. Now, can we leverage AI, generative AI, or machine learning without big data? We absolutely can. But it's just, again, always: what are the considerations? What are the triggers that we're going to make? We're probably going to have to create multiple bindings for Datadog, for AWS, for MySQL, for this, for that. And then in the application layer, try to tie those elements together. So those are things that we might have to do. It's more work from a programmatic perspective. But again, it depends on the scope. Not everybody wants to tie all that data together. Not everybody wants to have systems that can speak to every single thing because it's a large project. So it makes sense to scope it in some environments. Not every environment wants to do that.

**Q: Okay. So it looks like data is clearly not ready for AI use cases.**

A: How did you say that?

**Q: That's what I said. Okay. Now I'll ask you to rate the data maturity for AI usage.**

A: I think we have data that is ready to be used today.

**Q: Okay?**

A: But I think we should start from: what do we want to achieve with the AI? What do we want the LLMs to be able to do? What applications? And I'm not talking about applications from what we want to build. I'm saying what applications of the data do we want at the company? Then we will see if the way the data is structured currently supports that application.

**Q: So how about for this specific application? This is the trend. We think observability has gone past just sending logs and telemetry. Observability is beginning to expand. Companies are bringing security into observability. Companies are trying to give you business data into observability.**

A: But we have a lot of data for observability currently.

**Q: Yes, but what about the other? For instance, where is your database of product operations, where are your product docs?**

A: Okay. If you want to build an application that does all that, we start with the data that we have. For a good POC, to be able to test the utility of these tools and the LLMs in our own context, we will need to play around with the data that we have right now. Say maybe on DataDog. How do we get the data on DataDog to be leveraged or accessed by the LLM application, first and foremost? And then let's see how the team can throw some questions and be able to get some answers from there. And what does tuning look like? Because there's a whole myriad of problems that are LLM-related. Data is not the problem; data problems can be solved, and we have a lot of answers for data problems, but there are a lot of unanswered questions when it comes to building LLM-based applications because LLMs have a mind of their own sometimes. So people are still learning; they're building frameworks, methodologies, and different things for LLMs.

So I think we can do an MVP. An MVP is basically: "Okay, observability alone. What type of questions can we answer?" And we see how the LLM gives us answers, how accurate it is, how many hallucinations it gives. We swap in one model for another model. We do all that. Then we begin to add data elements across different verticals, and that will now be another project. That would be, "Okay, fine, we've played around with observability data. Can we now add product metric data, for instance?" And then we start seeing how we can tie those systems together in the application background that will leverage LangChain. So those are some of the things. That's how I think it can work. Definitely, we don't need to wait for the data to be code-ready.

**Q: Judging from how complex you've said data problems and LLM problems are, it seems like a lot of problems. So do you think there's a point in outsourcing some of the solutions? For instance, Amazon Bedrock can allow you to even bring scattered data and multimodal data into their knowledge base. And then you have that. They have a suite of LLMs. How much of this solution do you think we don't have to do by ourselves, specifically for this project? Do you think, "Oh, this is a solution that we can just leverage Bedrock for through and through," or do you think, "Okay, I think it's worth starting with Bedrock, and then after a few years..." What would you say?**

"

A: That is a huge feat. But from a data privacy, now this is me not as an AI enthusiast, but as a lead, I do not want the company data to live on a platform. I would rather the company houses something internally, because we don't know the extent of failures as it regards, as it relates to LLMs. We don't know the extent, and what I mean by that is, we don't know, a while back, I, I, I, I think businesses have been able to solve this now, but they don't know the difference between your data and my data. Okay? Like, you can literally, it's the same model, you just ask them what, you know, ask them whatever it is, and they will answer you. That's what they are meant to do. And I think they're going to figure out how to solve that problem now.

But the truth is, the risks exist, especially for proprietary data. So it's crucial for companies to consider their IP very, very carefully. I know companies, even some of the companies that you mentioned on this call, in this interview, that deploy a version of LLMs, and they close every other thing. They don't allow any other LLM to be used, no other platform to be used. They host internally, that's it. And they have very, very stringent controls to prevent anything that is proprietary to exist outside of their own environment. And by their environment, and whether you're working remotely or not, you cannot use a USB drive to remove data. You cannot transfer data to your personal cloud. You cannot also upload data anywhere, anyhow, to platforms that are not theirs, you get? So there are companies that have very, very strong security controls preventing that. Those are the more mature companies. There's a reason why we are calling them more mature.

So there is definitely something there. They're not just overdoing, they know when they're trying to guide kids. There are companies that have invested internally, build their own teams, and allow their teams, you know, use some type of platforms as well. Say maybe an OpenAI on Azure with certain types of guarantees. Right? Of course, they don't send all their data to Azure. They use the models on Azure.

There are people that would have vector databases, but then that's the thing, right? So for them to even have a database, all they're doing is they're just getting embeddings. So they're translating, they're sending, and they get the vector embeddings. They study vector embeddings. This is extra overhead. There are some companies that don't bother. They don't want to even bother about vector embeddings. They just throw everything to you.

**Q: Yeah, so what would you prefer for a project like this?**

A: My best, my best route is, everything exists internally, but that is not feasible. That is, we would have to, I think it's a mix of many things, because if there's a use case, if the use case was brought to me, I'll have to first evaluate what the use case is.  My gut instinct is to say no to putting the data anywhere else. That's to stay inside. But it's a conversation. How essential is the...?

**Q: Well, I mean, we technically use... Where does this data currently stay? Business data is on Redshift on AWS, remember?**

A: Okay, so... So, that's the thing. So where, what do you want to do with the data? How many platforms are we going to use? I need to see, and I'm doing this, you need to give me, because I'm going to ask you, "How many hours does this take from you, even with Bedrock?" And I'm going to watch, I'm going to see, I'm going to try to calculate how many hours it takes from you over time, and we'll decide to shut it down or not. Do you understand? That's what I'm saying. There is the context of the organization that has to be put in place, unless we are saying nobody's going to do any observability thing anymore.

**Q: I hear you, that if this is going to work, we need more hands?**

A: We need hands. Even without AI, we need hands.

**Q: you've said a lot about monitoring, evaluation. So what would you say now, how, in your opinion, are we balancing speed and safety for the company?**

A: So... Are you talking about...

**Q: AI. Sorry**

A: We need to understand AI. We need to understand the space. We need to create a governance framework that would... There has to be awareness for responsible usage. Those are the things. Those are the things that we know now. And to be honest, what is responsible usage? It depends on the business. There are some businesses that don't have as many sensitive things as the company. Responsible usage will differ from business to business. But we need to let people know that data that might not actually exist in certain places, someone should not carry merchant data, for instance, and once they want to analyze, then dump it in Claude, do you get?

A: You carry Excel with 10,000 customers and their users and their phone numbers, and you want to analyze in Claude, something like that. It should not be done, right? So, yeah.

**Q: So, governance framework, awareness for responsible usage.**

A: And then once we, once people understand... Then we can start. Remember, yeah, yeah. I mean, that's all. Sorry, the kickoff, there was a lot of emphasis on some responsible usage as well.

**Q: So in all of this, what would you say is the role of leadership now in taking me from the point where we are to the point where I can present this project and successfully deploy into production without stress? And you're part of the leader...**

A: So I will have to weigh the benefits, the pros and cons. Because I'll have to weigh the pros and the cons. What do I stand to gain and what do I stand to lose if you only focus on this? I'll need to know what the timeline is. So here's the thing, right for all these applications, building the application is not the issue, like there will be things that need to change, there will be more things that need to be done, which is why  I talked about investments earlier. The company has to be able to make the investments. If we're going to be building an application or that is on Bedrock or wherever, right we can't just build it and move on, it is build once and continue,  especially when it comes to AI machine learning, there is way more maintenance than there is for other applications, because one wrong parameter, one wrong response can bring the whole system and we have to also make sure that it is consistently be responding in the right way so there is a certain level of monitoring that i think we are underestimating right which is what i talk about when i say investments. Now, if the company is not willing to do that, or doesn't have the appetite to do that, then should they be outsourcing to somebody that builds  

**Q: Well, let me ask you now, and very directly. Do you think this project is valuable to the company?**

A: Yes, it is. It's an application of the data that we have. You currently help us generate the data. I don't want to remove an element of that data generation just because we want to emphasize the application of the data that exists. Does that make sense?

**Q: On a scale of one to five, how much do you think that observability data supports company operations?**

A: 4.5.

**Q: Okay. Then how would you say that we can, on a scale of one to five, how do you rate our efficiency in linking observability data to business implications? "My latency is low because latency is low, PIV dipped."**

A: 1. Something. We do that every single time. Every single time we have a latency conversation, we always think about PIV, how it impacts PIV, what that looks like. Right now, somebody would buzz the data team. They will go and spend one day or something and get the answer and come back. It is not efficient, but we always do.

**Q: Okay, do you think people have context outside their teams? Like, I mean, when I was talking to somebody, you know, the company has calls, and then we start talking together, we start solving it together. But I remember when I joined observability, I would just see an endpoint, but I knew nothing about it. Then it took a while to... And in fact, I'm still piecing the picture. So how well would you rate that culture of transparency?

A: There's a lot of transparency. There are documents, documents that... The problem is the fact that there are just too many things going on, but is there a world where it can be better, right? Of course.

---

*All company and participant identifiers have been anonymized in accordance with the project’s data ethics and confidentiality commitments.*
