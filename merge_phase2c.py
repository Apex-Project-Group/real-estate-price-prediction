import json

def load_notebook(path):
    """Load a Jupyter notebook from file"""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_notebook(notebook, path):
    """Save a Jupyter notebook to file"""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)

# Load notebooks
print("Loading notebooks...")
main_nb = load_notebook('notebooks/project_deliverable_notebook.ipynb')
phase2c_nb = load_notebook('notebooks/Phase-2C_Feature_Engineering_Complete.ipynb')

print(f"Main notebook has {len(main_nb['cells'])} cells")
print(f"Phase-2C notebook has {len(phase2c_nb['cells'])} cells")

# Skip the header cells from Phase-2C (first cell is the title)
# We want to add the content starting from the actual work
phase2c_cells_to_add = phase2c_nb['cells'][1:]  # Skip title cell

print(f"\nAdding {len(phase2c_cells_to_add)} cells from Phase-2C...")

# Append Phase-2C cells to main notebook
main_nb['cells'].extend(phase2c_cells_to_add)

print(f"New total cells: {len(main_nb['cells'])}")

# Save the merged notebook
save_notebook(main_nb, 'notebooks/project_deliverable_notebook.ipynb')

print("\n[SUCCESS] Successfully merged Phase-2C into project_deliverable_notebook.ipynb")
print(f"Final notebook has {len(main_nb['cells'])} cells")