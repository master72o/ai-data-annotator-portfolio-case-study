import json, sys

def lint_annotation_item(item):
    errors = []
    if 'id' not in item and 'prompt_id' not in item:
        errors.append("Missing item ID")
    if 'prompt' not in item:
        errors.append("Missing prompt")
    
    # Check SFT or RLHF
    if 'gold_response' in item:
        resp = item['gold_response']
        if len(resp.strip()) == 0:
            errors.append("Empty gold response")
        if "I'd be happy to help" in resp or "Sure!" in resp:
            errors.append("Contains low-quality conversational boilerplate fluff")
    elif 'chosen' in item and 'rejected' in item:
        if len(item['chosen'].strip()) == 0:
            errors.append("Empty chosen response")
        if len(item.get('rationale', '')) < 15:
            errors.append("RLHF rationale must be at least 15 chars")
    return errors

def main():
    if len(sys.argv) < 2:
        print("Usage: python linter.py <file.jsonl>")
        sys.exit(1)
    fpath = sys.argv[1]
    with open(fpath) as f:
        lines = f.readlines()
    
    total_errs = 0
    for idx, line in enumerate(lines):
        if not line.strip(): continue
        item = json.loads(line)
        errs = lint_annotation_item(item)
        if errs:
            print(f"Line {idx+1} ({item.get('id') or item.get('prompt_id')}): INVALID -> {errs}")
            total_errs += len(errs)
        else:
            print(f"Line {idx+1} ({item.get('id') or item.get('prompt_id')}): PASSED")

    if total_errs == 0:
        print("\nAll items passed linter rules successfully!")
        sys.exit(0)
    else:
        print(f"\nFailed with {total_errs} linter errors.")
        sys.exit(1)

if __name__ == "__main__":
    main()
