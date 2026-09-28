import pytest, os, sys, json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.linter import lint_annotation_item
from src.dataset_inspector import get_dataset_summary

def test_linter_gold_sft():
    gold_path = os.path.join(os.path.dirname(__file__), '../data/sample_annotations_gold.jsonl')
    with open(gold_path) as f:
        for line in f:
            if not line.strip(): continue
            item = json.loads(line)
            errs = lint_annotation_item(item)
            assert len(errs) == 0

def test_dataset_summary():
    summary = get_dataset_summary()
    assert summary['gold_sft_items'] >= 2
    assert summary['krippendorff_alpha'] >= 0.85
