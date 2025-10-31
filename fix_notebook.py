import json

def fix_notebook(path):
    """Fix empty cells in the notebook"""
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    print(f"Loaded notebook with {len(nb['cells'])} cells")
    
    # Find and remove empty cells
    empty_cells = []
    for i, cell in enumerate(nb['cells']):
        source = cell.get('source', [])
        if not source or (isinstance(source, list) and len(source) == 0):
            empty_cells.append(i)
    
    print(f"Found {len(empty_cells)} empty cells at positions: {empty_cells}")
    
    # Remove empty cells (in reverse order to maintain indices)
    for idx in reversed(empty_cells):
        print(f"Removing empty cell at position {idx}")
        del nb['cells'][idx]
    
    # Save the fixed notebook
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    
    print(f"\n[SUCCESS] Fixed notebook saved with {len(nb['cells'])} cells")
    return len(nb['cells'])

if __name__ == "__main__":
    notebook_path = "notebooks/project_deliverable_notebook.ipynb"
    total_cells = fix_notebook(notebook_path)
    print(f"Final cell count: {total_cells}")