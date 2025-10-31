import json

def load_notebook(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_notebook(notebook, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)

def create_markdown_cell(content):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": content if isinstance(content, list) else [content]
    }

print("Loading notebook...")
nb = load_notebook('notebooks/project_deliverable_notebook.ipynb')
print(f"Current cells: {len(nb['cells'])}")

# Analyze current structure
print("\nAnalyzing structure...")
for i, cell in enumerate(nb['cells'][:20], 1):
    cell_type = cell.get('cell_type', 'unknown')
    source = cell.get('source', [])
    first_line = (source[0] if isinstance(source, list) and source else source)[:60]
    print(f"Cell {i:2d} | {cell_type:8s} | {first_line}")

print("\n[INFO] Review the structure above to identify improvements needed")
print("[INFO] The notebook currently has all Phase 1, 2A, 2B, and 2C content")
print("[INFO] Next: Add section summaries and improve markdown formatting")