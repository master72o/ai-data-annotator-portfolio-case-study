# Module 4: QA Methodology & Inter-Annotator Agreement

## 4.1 3-Tier Quality Assurance Pipeline

```
[ Raw Annotation Submission ]
              │
              ▼
  [ Stage 1: Automated Linter ] ── (Syntax, Schema, Length, Word Count Checks)
              │
              ▼
  [ Stage 2: Peer Cross-Review ] ── (50% Random Sample Audited by Secondary Annotator)
              │
              ▼
  [ Stage 3: SME Gold Audit ] ── (10% High-Risk Sample Audited by Senior Data Lead)
```

---

## 4.2 Inter-Annotator Agreement (IAA) Results
- **Krippendorff's Alpha ($lpha$)**: **0.86** (Exceeds target of 0.80).
- **Cohen's Kappa ($\kappa$)**: **0.82** across pairwise preference tasks.
- **Percent Agreement**: **92.3%** on categorical quality tiers.
