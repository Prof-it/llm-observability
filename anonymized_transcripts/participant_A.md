# Appendix F: Interview Transcript of Participant A

**Interview Location:** Zoom  
**Mode:** Online  
**Date:** 12/05/2025  
**Participant Role:** Lead Engineer at the case fintech

---

**Interviewer**: So if you had looked at the project brief I shared, there was a diagram, I mean, it's just a conceptual diagram, of what I think may work. Did you see that?

**Participant A**: Yes, yes, I did see it. Okay.

**Interviewer**: So, um, did that make sense to you?

**Participant A**: Um, yeah, I think it made sense to me. I didn't have any issues with that diagram.

**Interviewer**: Okay, so if I come to you and I'm like, "Um, I have this interesting..." and that's exactly what I'm doing. "Like, we have this interesting plan for observability, and I think data has to, data can help us." What would be your first reaction? What would you say is my plan?

**Participant A**: Um, I guess I would start off by saying, "Do we have the right tools to handle such large amounts of data?" Typically, our data warehouse and our reporting tools like Metabase handle not huge amounts of data that we would see in like a Datadog, for example. So those logs are absolutely huge. And from a transactional data perspective, we're looking at maybe just a few hundred million records of data. But on the log side, I know that that data can get absolutely enormous. So I think in order to start using that data to a larger extent, and especially if want to blend that data with our company data, I would first ask, "Do we have the right kind of tools and infrastructure to actually be dealing with such large amounts of data?"

**Interviewer**: Okay. And by "your infrastructure," would you, like, do you have any particular ones in mind?

**Participant A**: I don't. I know we attempted to do a project with Security, I think it was last year already, where we were going to bring in logs to Redshift, which is our data warehouse. So there was a security event, if I can call it that. And as you know, we only store the logs, I think, for two weeks in Datadog. So our expectation was that we could bring that into Redshift. But when the data engineers attempted to do that, it was not going to work due to the size of the data. So what that meant is we need to put that data elsewhere or potentially just leave that data in our data lake in S3 and then be able to have tools to access the data directly from S3 and not actually put it into a structured data warehouse. 

So, yeah, I don't know any tools off the top of my head, but that would definitely be the first step to be able to use the data to a larger degree. I think second to, "Do we have the right tools?" is, "Do we have the right understanding of that data?" So in order to build an LLM or to use an LLM of any sort on our data, that data needs to be properly cataloged and explained to the LLM. And so that's an exercise we're actually going through at the moment, looking at our transactional data in Metabase and making sure that it's properly cataloged and explained so that we can start to access that data and results via an LLM. So I would say with log data, it would also be just as important. So, have we got the right expertise on what the metadata is, what the builds mean, do we have that properly documented in a way that an LLM can read? Yeah. Okay. Yeah, those are the first things that would come to my mind.

**Interviewer**: Yeah, that makes sense. So I'll just share my screen so that... So the idea of... Because, like, I can already tell that handling a lot of data is crazy. The idea of the architecture is to use... Can you see my screen? I'm not going to show the green bar. So the idea of the architecture here is to use LangChain. And rather than having to bring a lot of data together, we can actually query this data via the API, right? So I think a lot of where my proposed architecture would need a lot of bringing of data together would be here, where we would have a vector database and we'll query that. But I think the general idea is an agent can query Datadog, an agent can query Metabase or any other business BI tools that we have. And yes, we can also query maybe our own custom vector database that has, like, maybe operational manuals, product documentations. So with that kind of architecture, does that make the data layer less complicated?

**Participant A**: I think it does. The only thing I would update is where you have the Metabase API, because there's no company data actually stored in Metabase. So the data lives in Redshift, and then we just view that data via Metabase, but there's no actual data in Metabase itself. So, yeah, we would have to pull the data from Redshift, which is the Data Warehouse.

**Interviewer**: So are there other visualization tools? If the CEO wanted to see the health of the company, where would he go? Or what do you think are the key business metrics that would typically track, coming from a business perspective, and where would I find it?

**Participant A**: So look, the key metrics you'll find in the WBR (Weekly Business Review), that gets published on a Monday. And the key metrics you'll find in there is transaction counts, transaction values, success rates, and also net revenue and the growth rates across markets, across products, including for transfers. So yeah, I would say the WBR is a good place to start with the key, key metrics. But if you want to have, you know, maybe more metrics, or you want to look at maybe metrics only for a particular merchant or only for a particular channel, then to do that, you would go into Metabase. 

We have a lot of different visualizations that we've built over the years, and they all relate to various different aspects of the business. So if you were maybe looking for PIV for a specific channel over the last 24 months, then we have the PIV dashboard where you can go to find that information. So we have a curated list of reports we've built in Metabase. I think we have about 50 different reports. So it would really depend on exactly what you want to look at. And then you would find all the detail for that in Metabase. And it can be anything from merchant reports, fraud, disputes, net revenue, finances, onboarding compliance, just about any aspect of the business that you would like to understand, we would have a report for that in Metabase.

**Interviewer**: Okay. So based on what I've shared now, okay, I just wonder, looking at the fact, so I know I've talked to somebody before and they're like, "Okay, your plan looks good, but I wouldn't know how to go about implementing it." Like people are struggling to follow the Gen AI trend or to work with LLMs. Is there a clear plan right now that the data team has? Because when you talk to people, they will always tell you that when it comes to AI, data is king. If you have bad data, it's garbage in, garbage out. So I feel like at some point, there's got to be a standardized idea of how people want to use data for their... I mean, there may be different use cases, but is there a plan right now for the data team to be able to support multiple use cases? Like for me now, it's LLM-powered observability. Someone else may have another use case, and someone else may have another use case. So I'm wondering, is there a plan for how the data team plans to support different...

**Participant A**: Yeah. Okay, so there isn't an explicit plan at the moment. We are exploring a couple of use cases in the team as part of AI month. And one of those use cases is an LLM for people to get information and metrics that they're looking for in natural language. So rather than trying to write a piece of code themselves to extract the data, can they just engage with an AI in natural language and get the information they want? So we are exploring that. We're using OpenAI to do it. And then part of the learnings that are coming out of that, we will use to put into a formal roadmap. 

One of them that we have already seen is going to be major to enabling this whole AI space at the company is our data documentation. We have some basic documentation which we thought would be enough for an LLM to use and make sense of, but we quickly learned that our documentation is not as detailed and as contextualized as we need it to be to get good quality things back from the LLM. Like you said, garbage in, garbage out kind of situation. So yeah, we're still busy going through the process of understanding where the gaps are and what we need to do to close them so that people can start using AI on our data. So over the next couple of weeks, we'll flesh out a more formal plan. But definitely one thing that we're going to have to invest a lot of time in is our data documentation.

**Interviewer**: So what do you mean data documentation? What does that mean exactly?

**Participant A**: So what that means is basically explaining all the tables and all the columns and all the calculations in the data warehouse so that an LLM will know where to go to find certain information. So maybe just a very basic example, if we have a merchant table, we need to be able to say, "Okay, in this merchant table, we have a column called country. This is the merchant's country. And we note the country using the ISO standard code." Then if someone wants to go and pull the merchant country via the LLM, the model will know, "Okay, it needs to go to the merchant table and it needs to look at the country field." So that is the kind of information that we need to catalog. Yeah, we're probably, so at the moment, we're just kind of populating that on a Google sheet. But ideally, all the documentation needs to go into a proper repo as well. So it can be reviewed, maintained. But yeah, we need every table, every column, and ideally every calculation we do in the data warehouse to be explained in detail in natural language.

**Interviewer**: So it sounds like all the data cleaning, data auditing.

**Participant A**: Yes.

**Interviewer**: So is this going to be targeted at Redshift data?

**Participant A**: Yes, this is definitely going to be targeted at Redshift data.

**Interviewer**: Okay. Yeah.

**Participant A**: I'm not sure if other teams would also be going through the same kind of exercise on their own data warehouses. I'm thinking, for example, core, we don't have any control over some database itself directly. So if there was to be an LLM that ran off the company core, then that database would also have to be properly documented. But we in the data team specifically only care about Redshift.

**Interviewer**: Okay, okay. Um, do you see, do you think this will still be the case in two years? Because there is a world where people, you know, we tend to see big data and just bringing data together from different areas and trying to get insights from it. So is there that view for the data team that one day, you know, would have that structure to just absorb data from anywhere and try to make sense out of it?

**Participant A**: Yeah. Yeah, look, I definitely think at the moment now there needs to be a big effort to standardize and document all the data that is currently in Redshift, and then going forward on an ongoing basis, it would be much less effort to just make sure that everything is properly documented and cataloged as it's coming in again. Yeah, so I guess that would probably change over time.

**Interviewer**: Okay, thank you. So if I, if I now specifically with this solution, I think I wanted to ask what data management and data governance strategy would you be particular about just to ensure that this is implemented well. But I think that I can already sense from some of your answers. But if I was going to put that to you specifically, you know, from your data perspective, what would you highlight?

**Participant A**: Yeah, so I think just in terms of the quality of our data, we obviously would have that human layer of somebody looking at results, interpreting them, and making sure that they're accurate. So I think we need to be very confident in the quality of our data so that anyone can use the data and pull the data and feel very happy about it. So one thing we'll need to do in terms of quality is standardize our data. And what I mean by that is make sure that we're using the same kind of naming conventions across our data warehouse. A small example of that is a merchant at the company can either go by merchant ID or integration ID. It is the same thing

**Participant A**: Um, it is the same thing, but an LLM is not going to know that merchant and integration are interchangeable. So we need to be very sure in the data warehouse that everything is consistent and standardized, and it's something we haven't necessarily thought about up till now. So I would say that will be one new thing for us to pick up. I also think something that we would need to think about is just making sure that users are interpreting the output of an LLM in the correct manner. Because if users are not prompting an LLM perfectly correctly and they get certain data out, they might infer the wrong insights from that data and then end up making bad decisions with the data. So I'm not sure how companies are resolving that. But yeah, that is something that's a concern for me. So when I think about people using an LLM to get data and then inferring the wrong insights from it, we would need some kind of oversight function or something to ensure that that doesn't happen.

**Interviewer**: So would this maybe be a human review, or are there strategies in place where there's an LLM review and what another LLM has said? So are you saying like, yeah?

**Participant A**: So yeah, basically something like that. I think the human aspect, especially for now, would also be an important one. And it might even be that a person using an LLM maybe has their colleague verify that they're interpreting the results in the correct manner. It could just be as easy as that. But I do think that until we have a lot of confidence in our LLMs, we would prefer a model where a human is reviewing the results as opposed to another LLM.

**Interviewer**: Okay. That makes sense. Okay. Based on your oversight, currently, how much, and it's fine if you have a very different opinion, but how well would you say that observability data currently informs business decisions? So I mean, you play with a lot of data, and you have a lot of data that I know that goes into a WBR report, right? And they primarily come from Redshift and Metabase. But in your course of all data at the company, would you say, "Oh, that's," you know, if you interact with our observability tools at all?

**Participant A**: Um, no, I don't. So I would probably say people are using it very little and probably not as much as they should be. Okay. Yeah. So for example, like our key metrics in the business, there isn't really anything in there that speaks to observability, other than maybe our success rate. But because that's such a high-level metric, and it comes at the end of a long value chain of things happening in a transaction, yeah, it can be hard to actually infer anything practical from a success rate. But I think people are generally using observability data very little in making business decisions.

**Interviewer**: If you had to put that on a scale of one to five, where would you put that?

**Participant A**: I would put it maybe as a one.

**Interviewer**: Wow.

**Participant A**: Okay. Yeah.

**Interviewer**: Okay. And you never have to interact with observability tools?

**Participant A**: No. But,

**Interviewer**: Do you see, do you have any scenario where you feel like, "Okay, I have this business metric, but maybe if I knew something like this, and maybe from the application performance part, then it will be perfect"? Like, do you have any?

**Participant A**: So, not really. We've done some work with some Engineers like a year or two ago, and I think then we could have probably used some insights from this data. But that project has since closed, and I think what I would probably find it most useful for now is fraud investigations. Because we do work a lot with the fraud team on when there's a fraudulent event, so either collection or transfer, just trying to understand where did that fraud come from, how did it happen. And I think some observability data could really help us get to the bottom of those fraudulent events.

**Interviewer**: Okay.

**Participant A**: Yeah. Especially where it's not just a random isolated event, where it's a targeted, large-scale event happening over a period of time.

**Interviewer**: And so far, what would you say have been the obstacles to really using observability data for fraud events?

**Participant A**: I would say just having the right tools to be able to access the data. Like I mentioned in the beginning, the logs are so large, so we can't really bring them into Redshift. And we don't really have another way to interact with that data.

**Interviewer**: Do you think LLMs can help here? Or do you think the solution could help the LLM or the LLM specifically?

**Participant A**: I think, yeah, I think so. I think if we can get the proper understanding of the data documented, then I definitely think LLMs can solve that kind of problem.

**Interviewer**: Yeah, so, like, "This is what we are seeing on the business side. What are you seeing on the business side? What does the LLM think?" Is that the kind of line that you're towing?

**Participant A**: Yeah, exactly, exactly. You okay?

**Interviewer**: Um, okay, cool. I hope I am not leaving out any question that I want to ask you. Um, so, so if, if I have to, if, if, if I have to, um, give and gauge like readiness, um, you know, should I say data maturity for LLM usage overall at the company on a scale of one to five, what would you score?

**Participant A**: I would maybe score it between a two or three, specifically thinking just about Redshift data, because I don't know the state of other source databases. I don't know if we would use other databases for LLMs or if we would only build LLMs on Redshift. But just because of all the standardization and documentation that needs to be done, I'll probably score it a two at the moment.

**Interviewer**: Okay. And then what I also hear is that there is no clear plan for like a central, um, data. So it's like, okay, so if I ask you now, like, how well does the company utilize big data? What would you rate that? And, and I'm thinking, and I'm saying big data outside, you know, normal business transactional data in, you know, that we see in Redshift, for instance. Like, observability is creating data, different teams are creating data, um, like,

**Participant A**: You know, like, I would, um, I would definitely say it's pretty low, um, especially because our Datadog data, for example, we don't even really have access to that data, um, after two weeks, like, we can't access it via the UI anymore. And then that data isn't actually refreshed anywhere. So yeah, I think the usage of it then is pretty low.

**Interviewer**: So that's like a 1 or 2?

**Participant A**: Yeah, I would say let's call it a 2.

**Interviewer**: I think the last thing I would say is that do you currently feel like we are you have the skills to do all the enormous work? 
**Participant A**: Definitely not. Uh, definitely not. It's very much like learning as we go. Um, yeah, I think the whole space is like so new at the moment. Um, so yeah, just trying to figure it out as we go.

**Interviewer**: And do you think like what what do you think would help overall like I think that's the feedback I've gotten from people but like is there something that the company can do to help with like imbibing these skills? Like

**Participant A**: Um, I think AI month that we're currently having is a great place to start because I feel like all the information we need to learn the skills we need is available. Um, it's just finding the time and the space to actually invest in upskilling. So I think if the company can give us time back to upskill then I think that that's like the biggest thing that they can do to help us. So it might be like like we actually have to deprioritize other work or push the timelines out to make space for this. But I think just time and capacity is the biggest issue we're facing.

**Interviewer**: Okay, that makes sense. Thank you for your time

---

*All company and participant identifiers have been anonymized in accordance with the project’s data ethics and confidentiality commitments.*
