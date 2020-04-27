# Relevant articles, with comments

## AI in Security:

1. https://awakesecurity.com/glossary/ai-security/ - definition, "AI security involves leveraging AI to identify and stop cyber threats with less human intervention than is typically expected or needed with traditional security approaches". Basically, using ML to identify security risks

2. https://towardsdatascience.com/cyber-security-ai-defined-explained-and-explored-79fd25c10bfa - also summarizing AI used in Cybersec, expert vs automated cybersec systems. Status of use as of today.

3. https://www.wired.com/wiredinsider/2019/10/how-ai-battles-security-threats-without-humans/ Darktrace, tackling the fact that the threats were detected reactively, after the fact. Based on normal vs abnormal behavior patterns. NOW: work against cyber criminals using AI to launch new attacks. AND using it themselves w/ AI Autonomous Response - machine speed response when humans too slow / unavailable

4. https://www.securitymagazine.com/articles/90871-whats-the-real-role-of-ai-and-ml-in-cybersecurity Role of AI in Cybersec "AI/ML cannot do causation" and causation / understand why is key in cybersec!Major benefit of AI/ML: quantities of data processed, and speed. Augment the sec analyst, used in triage

5. https://hostnoc.com/ai-impact-cybersecurity-in-2020/ "6 Ways in Which AI Will Impact Cybersecurity In 2020" - 
* Training data target, change it
* Email attacks w deepfake audio
* AI-powered malware, analyze the environment
* Deepfake replace biometric (fingerprint)
* Differential privacy, patterns are shared but not the PII-part
* AI Ethics

## Security in AI:

1. https://www.belfercenter.org/publication/AttackingAI AI Attack - attacking AI systems. Main "methods":
* Input
* Poisoning 
Listing vulnerable parts of society, suggesting AI Security Programs and that regulators should mandate compliance for government and high risk use of AI (for the society)
	
2. https://blogs.microsoft.com/on-the-issues/2019/12/06/ai-machine-learning-security/ Microsoft approach, also connected to the AETHER committee. "Failure modes in ML" - make sure we use the same vocabulary. Failure Modes -> Security threats to AI & ML Systems and how to mitigate them. Intentional and unintentional failures. ALL ARTICLES PUBLISHED UNDER THIS UMBRELLA IS A MUST-READ

3. https://www.mckinsey.com/business-functions/mckinsey-analytics/our-insights/confronting-the-risks-of-artificial-intelligence McKinsey-study, risk mitigation framework - used in AI scenario with customer use cases
* Identify risks connected to AI
* Identify mitigation controls, like for the biggest risk in one of the use cases: poor or biased product recommendation -> identify where humans must be "in the loop" Manual approvement check and such. 
Visibility (?)


## AISec Use Case:

"Bridge" case, basis for describing practical use:  https://www.microsoft.com/security/blog/2020/04/16/secure-software-development-lifecycle-machine-learning/ 
* 12 million work items and bugs -> dataset. 
* ML model built from the dataset TITLES only. 
* Separating security from non-security related bugs with 99% accuracy and of the security related ones labeling them into critical and high priority/non-critical (3 or 2, ask!)
