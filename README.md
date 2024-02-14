# LLMOps 101

## Welcome to LLMOps 101! 

This project is all about demystifying the process of operating and deploying large language models (LLMs) in production environments. The course is structured into four chapters, each designed to tackle both common and less familiar challenges associated with LLMs. This project provides a mix of conceptual explanations and practical code examples, aiming to assist anyone interested in mastering LLMOps. 

As an open-source project, we encourage contributions from the community to help us improve and expand our collective understanding.

# Table of Contents

- [Chapter 1: Introduction to LLMOps](#chapter-1-introduction-to-llmops)
  - [Lesson 1.1: What, why and who in LLMOps](#lesson-11-what-why-and-who-in-llmops)
  - [Lesson 1.2: LLMOps lifecycle](#lesson-12-llmops-lifecycle)
  - [Lesson 1.3: MLOps versus LLMOps—unique challenges](#lesson-13-mlops-versus-llmopsunique-challenges)
- [Chapter 2: Designing and Developing LLMs for Production](#chapter-2-designing-and-developing-llms-for-production)
  - [Lesson 2.1: LLMOps design](#lesson-21-llmops-design)
  - [Lesson 2.2: Data preparation pipelines](#lesson-22-data-preparation-pipelines)
  - [Lesson 2.3: Prompt engineering](#lesson-23-prompt-engineering)
  - [Lesson 2.4: Fine-tuning](#lesson-24-fine-tuning)
- [Chapter 3: Evaluating LLMs Before Production](#chapter-3-evaluating-llms-before-production)
  - [Lesson 3.1: Benchmarking: General evaluations for LLMs](#lesson-31-benchmarking-general-evaluations-for-llms)
  - [Lesson 3.2: Commit-level model evaluations](#lesson-32-commit-level-model-evaluations)
  - [Lesson 3.3: Pre-deployment model evaluations](#lesson-33-pre-deployment-model-evaluations)
  - [Lesson 3.4: Automating and orchestrating the development phase](#lesson-34-automating-and-orchestrating-the-development-phase)
- [Chapter 4: Deploying and Monitoring LLMs in Production](#chapter-4-deploying-and-monitoring-llms-in-production)
  - [Lesson 4.1: LLM deployment and architecture](#lesson-41-llm-deployment-and-architecture)
  - [Lesson 4.2: Monitoring LLMs](#lesson-42-monitoring-llms)
  - [Lesson 4.3: On-demand model evaluations](#lesson-43-on-demand-model-evaluations)
  - [Lesson 4.4: CI/CD in LLMOps: bringing it all together](#lesson-44-cicd-in-llmops-bringing-it-all-together)

# Chapter 1: Introduction to LLMOps
## Lesson 1.1: What, why and who in LLMOps
### Learning Objectives:
- Learner will be able to define what the concept of LLMOps means.
- Learner will be able to explain why LLMOps is important in efficiently and effectively operating LLMs in production environments, with an emphasis on the benefits of its implementation.
- Learner will be able to identify who are the key stakeholders involved in LLMOps and their respective roles and responsibilities.
- **Terminology introduced**: LLMOps, Production environments, Stakeholders

## Lesson 1.2: LLMOps lifecycle
### Learning Objectives:
- Learner will be able to distinguish the four main phases of the LLMOps lifecycle—Design, Development, Deployment and Monitoring—and the critical activities associated with each phase.
- Learner will be able to recognize the cyclical and interconnected nature of the lifecycle, including how continuous feedback and performance monitoring inform ongoing improvements and refinements.
- **Terminology introduced:** LLMOps Lifecycle, Feedback loops, Design, Development, Deployment and Monitoring

## Lesson 1.3: MLOps versus LLMOps—unique challenges
### Learning Objectives:
- Learner will be able to appraise how LLMOps diverges from traditional MLOps, focusing on the specialized challenges of deploying LLMs, such as hallucinations, consistency, quality, bias and toxicity.
- **Terminology introduced:** MLOps, Model hallucinations, Output consistency, Model quality, Algorithmic bias and Model toxicity

# Chapter 2: Designing and Developing LLMs for Production
## Lesson 2.1: LLMOps design
### Learning Objectives:
- Learner will be able to indicate that the choice of an LLM, whether open-source or proprietary, depends on various factors determined by stakeholders, such as the specific task, budget, latency requirements, privacy concerns, and desired quality.
- Learner will be able to choose between using out-of-the-box pre-trained models and fine-tuning models, depending on which approach best addresses their use cases effectively.
- **Terminology introduced:** Open-source LLMs, Proprietary LLMs, Cost analysis, Performance metrics, Latency, Data privacy, Pre-trained models, Model fine-tuning and Retrieval-Augmented Generation (RAG)

## Lesson 2.2: Data preparation pipelines
### Learning Objectives:
- Learner will be able to describe the role that each component of the data preparation pipeline plays in preparing data for LLMs, including data ingestion, validation, preprocessing, and embedding.
- Learner will be able to value the importance of embeddings in LLMs and learn best practices for generating, using, and storing embeddings in vector databases.
- Learner will be able to explain the stages of data preparation that can be automated and the principles of orchestrating these automated tasks to create efficient workflows.
- **Terminology introduced:** Data pipeline, Ingestion, Data cleaning, Data annotation, Embeddings, Vector database , Data storage, Automation and Orchestration

## Lesson 2.3: Prompt engineering
### Learning Objectives:
- Learner will be able to distinguish between the strategies used for prompting open models and proprietary models.
- Learner will be able to explain the importance of managing and versioning prompts, akin to code versioning, to maintain a history of changes, experiments, and performance variations.
- **Terminology introduced:** Prompt design, Model prompting, Few-shot learning, Zero-shot learning, Prompt version control, Experiment tracking and Performance tracking

## Lesson 2.4: Fine-tuning
### Learning Objectives:
- Learner will be able to describe different methods of fine-tuning LLMs, including techniques such as Low-Rank Adaptation (LoRA) and Quantized Low-Rank Adaptation (Q-LoRA).
- Learner will be able to explain the fundamentals of advanced fine-tuning techniques, such as Reinforcement Learning with Human Feedback (RLHF), and their applications in refining LLM performance.
- **Terminology introduced:** Transfer learning, Low-Rank Adaptation (LoRA), Quantized Low-Rank Adaptation (Q-LoRA), Reinforcement Learning with Human Feedback (RLHF) and Domain adaptation

# Chapter 3: Evaluating LLMs Before Production
## Lesson 3.1: Benchmarking: General evaluations for LLMs
### Learning Objectives:
- Learner will be able to identify and describe the various evaluation methods used for benchmarking LLMs, as well as their evaluation criteria, including MMLU, HellaSwag, HumanEval and ARC.
- Learner will be able to recognize the benefits and limitations of general benchmarking evaluations, acknowledging that they may not fully capture the nuances of specific use cases.
- Learner will be able to justify why it is essential to complement general evaluations with custom, use-case-specific evaluations to ensure that the model meets the desired performance criteria in real-world applications.
- **Terminology introduced:** LLMs Benchmarks, Evaluation frameworks, MMLU, HellaSwag, HumanEval, ARC, Custom evaluations and Performance benchmarks

## Lesson 3.2: Commit-level model evaluations
### Learning Objectives:
- Learners will be able to value the advantages of rule-based evaluations—such as their speed, simplicity, and interpretability for ensuring quality and consistency in development—and recognize the risks of omitting these checks.
- Learner will be able to describe how commit-level model evaluations bolster model reliability and facilitate confident experimentation with rapid iteration, focusing on checks for factual grounding, output formatting (e.g., valid JSON objects), and selective query refusal.
- **Terminology introduced:** Commit-level evaluations, Rule-based checks, Model consistency, Output validation, Error analysis and Quality assurance

## Lesson 3.3: Pre-deployment model evaluations
### Learning Objectives:
- Learner will be able to value the benefits of comprehensive model evaluations prior to deployment, as well as the potential risks and consequences of foregoing them.
- Learner will be able to explain that a combination of human evaluation and model evaluation (evaluation conducted by another LLM) can significantly help in reducing hallucinations (inaccurate, irrelevant, or contradictory outputs), ensuring AI safety, detecting subtle regressions or out-of-context answers, simulating user experiences, and providing quality feedback before deployment.
- **Terminology introduced:** Pre-deployment testing, Human-in-the-loop evaluation, Peer model evaluation, Output hallucination detection, AI safety protocols, User experience simulation and Feedback mechanisms

## Lesson 3.4: Automating and orchestrating the development phase
### Learning Objectives:
- Learner will be able to give examples about the benefits of Continuous Integration (CI) for developers and teams, such as enabling rapid iteration, facilitating fast troubleshooting, simplifying collaboration, and reducing merge conflicts.
- Learner will be able to explain the best practices for automating the different evaluations, as well as the benefits and challenges of orchestrating these automated evaluations and the other automated components from the previous chapter.
- **Terminology introduced:** Continuous Integration (CI), Development automation and Evaluation automation

# Chapter 4: Deploying and Monitoring LLMs in Production
## Lesson 4.1: LLM deployment and architecture
### Learning Objectives:
- Learner will be able to distinguish between using an external LLM provider and self-hosting an open-source model, highlighting the trade-offs such as ease of implementation, cost, quality, scalability, latency, load balancing, privacy concerns, hardware requirements, downtime, rate limiting and compliance issues.
- Learner will be able to explain architectural patterns such as APIs for model interfacing, microservices for modular deployment, and serverless computing for serving LLMs in production environments.
- **Terminology introduced:** Cloud hosting, Scalability, Load balancing, API gateways, Microservice architecture, Serverless functions and Infrastructure as Code (IaC)

## Lesson 4.2: Monitoring LLMs
### Learning Objectives:
- Learner will be able to articulate the rationale behind implementing robust logging systems for LLMs, identify the critical data to log, and understand the best practices for logging and log analysis.
- Learner will be able to list and describe essential performance metrics such as Queries per Second (QPS), latency, and Tokens Per Second (TPS), and discuss methods for monitoring and optimizing these metrics to ensure efficient LLM operation.
- Learner will be able to explain the principles of setting up alerting systems, define thresholds for triggering alerts, and outline effective incident response strategies to maintain LLM stability and reliability.
- **Terminology introduced:** Logging, Log retention policies, Performance metrics, Queries per Second (QPS), Latency measurement, Tokens Per Second (TPS), Alerting systems, Anomaly detection and Incident management

## Lesson 4.3: On-demand model evaluations
### Learning Objectives:
- Learner will be able to explain why on-demand evaluations are critical for maintaining the performance and reliability of LLMs in production environments.
- Learner will be able to identify and assess key areas of concern for LLMs in production, including model performance changes, signs of model degradation, safety and ethical considerations, and establish protocols for rolling back to previous model versions or fallback models in case of evaluation failures.
- **Terminology introduced:** Model drift, Performance degradation, Ethical oversight, Model versioning, Rollback strategies and Fallback models

## Lesson 4.4: CI/CD in LLMOps: bringing it all together
### Learning Objectives:
- Learners will be able to distinguish the roles and purposes of CI and CD within the LLMOps lifecycle, understanding how they complement each other to enhance the development, deployment and monitoring of LLMs.
- Learners will be able to explain the sequential order and interdependencies of components within a CI/CD pipeline, including design, development (with an emphasis on evaluation), deployment, and monitoring, and how each stage ensures the integrity and performance of LLMs in production environments.
- Learners will be able to identify common challenges associated with automating the LLMOps pipeline and discuss best practices for achieving an efficient and reliable end-to-end workflow from design to monitoring.
- **Terminology introduced:** Continuous Deployment (CD), CI/CD pipeline
