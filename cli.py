import argparse, json, sys, os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from src.dataset_inspector import get_dataset_summary
from src.linter import lint_annotation_item

def main():
    parser = argparse.ArgumentParser(description="AI Data Annotator Case Study CLI")
    subparsers = parser.add_subparsers(dest="command")

    lint_p = subparsers.add_parser("lint", help="Lint JSONL annotations file")
    lint_p.add_argument("--file", required=True, help="Path to JSONL file")

    subparsers.add_parser("stats", help="Display dataset statistics summary")

    args = parser.parse_args()

    if args.command == "lint":
        with open(args.file) as f:
            lines = f.readlines()
        for idx, line in enumerate(lines):
            if not line.strip(): continue
            item = json.loads(line)
            errs = lint_annotation_item(item)
            status = "PASSED ✅" if not errs else f"INVALID -> {errs}"
            print(f"Item {idx+1}: {status}")
    elif args.command == "stats":
        summary = get_dataset_summary()
        print("=== AI Data Annotator Portfolio Case Study Stats ===")
        print(json.dumps(summary, indent=2))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
