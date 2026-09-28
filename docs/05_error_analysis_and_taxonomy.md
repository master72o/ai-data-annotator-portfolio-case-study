# Module 5: Error Analysis & Taxonomy Breakdown

During the QA audit of 500 initial annotations, **42 items (8.4%)** were flagged for revision. Below is the empirical error distribution:

| Error Category | Frequency | Percentage | Primary Cause | Corrective Action |
|---|---|---|---|---|
| **Instruction Omission** | 18 | 42.8% | Annotator overlooked negative constraint in prompt. | Updated linter rule to auto-check keyword exclusions. |
| **Subtle Hallucination** | 10 | 23.8% | Unverified technical claim in code/math explanation. | Mandatory external URL verification requirement added. |
| **Formatting Defect** | 8 | 19.0% | Markdown code block missing language tag. | Linter auto-reformatting script applied. |
| **Tone Misalignment** | 6 | 14.4% | Excessively polite boilerplate fluff ("Sure! I'd be happy to help!"). | Explicit prohibition of conversational fluff in SFT responses. |

---

## 5.2 Corrective Action Impact
Following annotator retraining and linter rule enforcement, the audit error rate dropped from **8.4% to 1.6%** in subsequent batches.
