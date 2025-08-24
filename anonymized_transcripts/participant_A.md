# Appendix F: Interview Transcript of Participant A

**Interview Location:** Zoom  
**Mode:** Online  
**Date:** 12/05/2025  
**Participant Role:** Lead Engineer at the case fintech

---

**Q: Over the years, how have observability practices changed within the company?**  
A: They have changed quite a bit. Initially, we mostly relied on basic logging, which was often informal and inconsistent between teams. Now, there's much more emphasis on structured logging, proactive monitoring, and trying to build a culture where teams are responsible for their own instrumentation.

**Q: What led to those changes?**  
A: I think scaling was a big factor. As we grew, we started seeing more incidents and harder-to-diagnose issues across our systems. It became clear we needed a more robust approach—one that could be shared across teams, but also allowed each team to add what they felt was important for their own services.

**Q: Do you use AI or see AI becoming important in observability?**  
A: We're experimenting. We've started looking at anomaly detection using some existing tools, but nothing company-wide. There are discussions about using AI or LLMs in the future, especially as the volume of logs and metrics increases. The dream is to have a system that can suggest where to look or correlate symptoms across different domains, but we're not really there yet.

**Q: How valuable do you find your current observability stack for daily operations?**  
A: [Pauses] It's useful, but there are gaps. We still spend a lot of time piecing together information from logs, dashboards, or tribal knowledge. For cross-functional incidents, context can be lost. I'd give it a 3 out of 5 for operational value, maybe a bit higher for smaller, well-instrumented services.

**Q: Does the observability system facilitate connecting technical issues to business impact?**  
A: Not easily. Sometimes we spot customer issues quickly, sometimes not. Mapping a spike in API errors to a drop-off in transactions, or figuring out which incidents impact revenue, usually requires digging into multiple tools—sometimes even getting people from different teams in a call to share context.

**Q: Does the engineering culture promote transparency and context sharing?**  
A: We try, but silos can form. People are overloaded, and it's hard to keep up with everything outside your direct scope. There's openness, but sharing knowledge outside your area takes extra effort.

**Q: What's your view on using LLMs or similar AI solutions for holistic observability?**  
A: I'm open to it, but also cautious. There's potential if we can query systems in plain language and pull in business and technical context together. But accuracy, trust, and helping—not confusing—engineers are big concerns.

**Q: Do you have recommendations for the proposed framework?**  
A: Make sure it's easy to integrate with current data sources and doesn't add noise. Also, create guardrails for accuracy and allow humans to provide feedback so the system improves over time.

---

*All company and participant identifiers have been anonymized in accordance with the project’s data ethics and confidentiality commitments.*