# Module 2: Annotation Labeling Guidelines & Taxonomy

## 2.1 Core Quality Rubrics (1-5 Scale)

| Rubric | 1 (Poor) | 3 (Acceptable) | 5 (Gold Standard) |
|---|---|---|---|
| **Instruction Adherence** | Ignores key constraints or negative rules. | Follows main prompt but misses 1 sub-constraint. | Flawless adherence to all explicit & implicit constraints. |
| **Factuality & Grounding** | Major factual hallucinations or incorrect code. | Factually correct but lacks depth or explanation. | 100% accurate, verified against primary sources, zero hallucination. |
| **Clarity & Formatting** | Messy, unformatted text, bad spacing. | Basic formatting (some bullet points). | Impeccable Markdown, syntax-highlighted code blocks, clear structure. |
| **Conciseness** | Filled with fluff, filler phrases, and repetition. | Slightly wordy. | High signal-to-noise ratio, direct and precise. |

---

## 2.2 Negative Constraint Handling Rules
When a prompt contains negative constraints (e.g., *"Do NOT mention competitor brands"* or *"Do NOT exceed 100 words"*):
- Any violation of a negative constraint MUST result in an **Instruction Adherence score of 1/5**.
- In pairwise preference ranking, a response with zero negative constraint violations ALWAYS wins over a response with a violation, regardless of how well-written the latter is.
