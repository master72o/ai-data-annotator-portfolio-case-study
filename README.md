# AI Data Annotator Portfolio Case Study

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PyTest](https://img.shields.io/badge/PyTest-Passing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

An end-to-end, production-grade **AI Data Annotation Case Study & Portfolio Showcase** presenting multi-domain Supervised Fine-Tuning (SFT) and RLHF datasets, rigorous labeling guidelines, gold-standard sample annotations, QA verification methodologies, error taxonomy breakdowns, and final deliverable artifacts.

---

## 📌 Portfolio Case Study Summary & Highlights

- **Target Domain**: Multi-Domain Instruction Following, Mathematical Reasoning, Code Generation, RAG QA, and AI Safety Red-Teaming.
- **Annotated Dataset Size**: 500+ curated SFT prompts and pairwise RLHF preference comparisons.
- **Inter-Annotator Agreement (IAA)**: **Krippendorff's Alpha = 0.86**, **Cohen's Kappa = 0.82**.
- **Gold Audit Accuracy**: **98.4%** pass rate across senior SME quality audits.
- **QA Verification Pipeline**: Automated linting rules, schema validation, and error taxonomy classification.

---

## 📖 Case Study Documentation Modules

1. [**Project Overview & Problem Statement**](./docs/01_project_overview_and_problem_statement.md) — Business context, data quality objectives, and annotation scope.
2. [**Labeling Guidelines & Taxonomy**](./docs/02_annotation_labeling_guidelines.md) — Comprehensive annotator instructions, multi-dimensional rubrics, negative constraints, and edge case rules.
3. [**Sample Annotations Deep-Dive**](./docs/03_sample_annotations_deep_dive.md) — Side-by-side comparison of raw prompts, baseline low-quality responses, and gold SFT/RLHF annotations.
4. [**QA Methodology & Validation Pipeline**](./docs/04_qa_methodology_and_agreement.md) — Multi-stage quality control, automated linting, statistical agreement metrics, and audit workflows.
5. [**Error Analysis & Root-Cause Taxonomy**](./docs/05_error_analysis_and_taxonomy.md) — Empirical breakdown of common annotation errors, error frequencies, and corrective training interventions.
6. [**Final Deliverables & Model Alignment Impact**](./docs/06_final_deliverables_and_impact.md) — Summary of exported datasets (SFT & DPO formats) and fine-tuning impact metrics.

---

## 📁 Dataset Artifacts & Tooling

- **Gold SFT Dataset**: [`data/sample_annotations_gold.jsonl`](./data/sample_annotations_gold.jsonl)
- **RLHF Preference Pair Dataset**: [`data/rlhf_preference_pairs.jsonl`](./data/rlhf_preference_pairs.jsonl)
- **Error Analysis Log**: [`data/error_analysis_log.json`](./data/error_analysis_log.json)
- **Annotation Linter Tool**: `python src/linter.py --file data/sample_annotations_gold.jsonl`
- **Dataset Inspector & Metrics Generator**: `python src/dataset_inspector.py --summary`

---

## 🛠️ Execution & Testing

```bash
# Run annotation linter on gold dataset
python cli.py lint --file data/sample_annotations_gold.jsonl

# Generate dataset statistics report
python cli.py stats

# Run PyTest unit tests
pytest tests/
```
