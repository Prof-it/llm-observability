# Appendix B: Interview Transcript of Participant B

**Interview Location:** Lagos, Nigeria  
**Mode:** In-person  
**Date:** 14/05/2025  
**Participant Role:** Lead Engineer at the case fintech

---

**Q: How have observability needs changed as the organization has evolved?**  
A: From a business perspective, as the organization has grown and expanded to multiple markets, one of the key things that partners and merchants and big customers ask for is our uptime. So we need a little bit more instrumentation to be able to tie those things directly, so for me we are able to make those inferences but are we able to make them as quickly as possible? We need the observability stack to catch up with the complexity that comes with scaling.

**Q: How effective do you find current observability practices?**  
A: I think the basics are present, and things are fairly robust for smaller services, but for more complex workflows involving several components, it's quite challenging to quickly identify where something might have broken down. Much of the context is still in people's heads or in Slack threads.

**Q: Is AI or LLM-based observability on the radar?**  
A: There's definitely interest. Our data science team is looking into anomaly detection, and some talks have happened about using AI for log analysis or event correlation, but nothing concrete has been done yet. I do see value in having natural language interfaces that let you ask business-level or system-level questions directly, especially for non-engineers.

**Q: What about connecting observability to business outcomes?**  
A: That’s one area where the current tools don’t do enough. For example, if there’s an API error spike, linking it to changes in transactions or support tickets often needs a lot of digging and sometimes interpolating manually. It would be useful if the system could surface these links automatically.

**Q: Cultural or organizational barriers?**  
A: I think silos are the main challenge. Teams are focused on their own domains, and knowledge isn’t always well-shared. While we’re open to collaborating, the pressure to deliver means context sometimes gets left behind.

**Q: Concerns about LLM/AI adoption?**  
A: My main concern would be trust and reliability. People need to understand how conclusions are reached. I also think there’s risk if the AI misses something, or if people accept AI answers without verification.

**Q: What would help with design or adoption?**
A: Having clear data governance and allowing users to provide feedback on the system’s recommendations would help. There’s also a need for ongoing education to ensure everyone understands both the potential and the limitations.

---

*All company and participant identifiers have been anonymized in accordance with the project’s data ethics and confidentiality commitments.*