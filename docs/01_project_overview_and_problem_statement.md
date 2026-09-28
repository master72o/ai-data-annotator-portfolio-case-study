# Module 1: Project Overview & Problem Statement

## 1.1 Business Context & Motivation
High-performing Large Language Models (LLMs) rely fundamentally on high-quality human annotation data for Supervised Fine-Tuning (SFT) and Reinforcement Learning from Human Feedback (RLHF).

Common issues in uncurated datasets include:
- **Fluff & Verbosity**: Models learning repetitive, low-signal boilerplate phrases.
- **Instruction Omission**: Failing to obey negative constraints (e.g. "Do not use the word X").
- **Subtle Factual Hallucinations**: Plausible-sounding but inaccurate technical claims.
- **Formatting Leakage**: Improper Markdown or JSON syntax errors.

---

## 1.2 Project Objectives
1. Design a production-grade **Data Annotation Guidelines Document** for a team of 15+ annotators.
2. Annotate a gold-standard dataset covering 5 core technical domains (Instruction Following, Math, Code, RAG, Safety).
3. Implement a 3-tier Quality Assurance (QA) workflow guaranteeing Krippendorff's Alpha $\ge 0.85$.
4. Perform an empirical Error Analysis to identify and correct data quality bottlenecks.
5. Export production-ready HuggingFace `datasets` format JSONL artifacts.
