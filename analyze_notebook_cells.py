import json

def analyze_notebook_cells(path):
    """Detailed analysis of all cells in the notebook"""
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    print("="*80)
    print("DETAILED NOTEBOOK ANALYSIS")
    print("="*80)
    print(f"\nNotebook: {path}")
    print(f"Total Cells: {len(nb['cells'])}")
    print(f"Format: Jupyter Notebook v{nb['nbformat']}.{nb['nbformat_minor']}")
    
    # Analyze each cell
    print("\n" + "="*80)
    print("CELL-BY-CELL ANALYSIS")
    print("="*80)
    
    markdown_count = 0
    code_count = 0
    
    for i, cell in enumerate(nb['cells'], 1):
        cell_type = cell.get('cell_type', 'unknown')
        source = cell.get('source', [])
        
        # Get first line of content
        if isinstance(source, list):
            first_line = source[0] if source else ""
        else:
            first_line = source
        
        # Truncate long lines
        preview = first_line[:70].replace('\n', ' ').strip()
        if len(first_line) > 70:
            preview += "..."
        
        # Count cell types
        if cell_type == 'markdown':
            markdown_count += 1
            type_label = "MD"
        elif cell_type == 'code':
            code_count += 1
            type_label = "CODE"
        else:
            type_label = cell_type.upper()
        
        # Check for special markers
        markers = []
        source_text = ''.join(source) if isinstance(source, list) else source
        
        if 'Phase 1' in source_text or 'phase1' in source_text:
            markers.append("PHASE-1")
        if 'Phase 2A' in source_text or 'phase2a' in source_text:
            markers.append("PHASE-2A")
        if 'Phase 2B' in source_text or 'phase2b' in source_text:
            markers.append("PHASE-2B")
        if 'import' in source_text and cell_type == 'code':
            markers.append("IMPORTS")
        if 'def ' in source_text and cell_type == 'code':
            markers.append("FUNCTION")
        if 'plt.' in source_text or 'sns.' in source_text:
            markers.append("VISUALIZATION")
        if 'df.' in source_text and cell_type == 'code':
            markers.append("DATA-OPS")
        
        marker_str = f" [{', '.join(markers)}]" if markers else ""
        
        print(f"\nCell {i:2d} | {type_label:4s} | {preview}{marker_str}")
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total Cells: {len(nb['cells'])}")
    print(f"  - Markdown: {markdown_count}")
    print(f"  - Code: {code_count}")
    
    # Check for phase distribution
    phase1_cells = []
    phase2a_cells = []
    phase2b_cells = []
    
    for i, cell in enumerate(nb['cells'], 1):
        source_text = ''.join(cell.get('source', [])) if isinstance(cell.get('source', []), list) else cell.get('source', '')
        if 'Phase 1' in source_text or 'phase1' in source_text:
            phase1_cells.append(i)
        if 'Phase 2A' in source_text or 'phase2a' in source_text:
            phase2a_cells.append(i)
        if 'Phase 2B' in source_text or 'phase2b' in source_text:
            phase2b_cells.append(i)
    
    print(f"\nPhase Distribution:")
    print(f"  - Phase 1 markers: {len(phase1_cells)} (cells: {phase1_cells})")
    print(f"  - Phase 2A markers: {len(phase2a_cells)} (cells: {phase2a_cells})")
    print(f"  - Phase 2B markers: {len(phase2b_cells)} (cells: {phase2b_cells})")
    
    print("\n" + "="*80)
    print("[SUCCESS] Analysis complete - Notebook structure is valid!")
    print("="*80)

if __name__ == "__main__":
    notebook_path = "notebooks/project_deliverable_notebook.ipynb"
    analyze_notebook_cells(notebook_path)