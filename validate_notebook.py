import json
import sys

def validate_notebook(path):
    """Validate Jupyter notebook structure and content"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        print(f"[OK] Notebook loaded successfully: {path}")
        print(f"[OK] Total cells: {len(nb['cells'])}")
        print(f"[OK] Notebook format version: {nb['nbformat']}.{nb['nbformat_minor']}")
        
        # Analyze cell types
        markdown_cells = sum(1 for cell in nb['cells'] if cell['cell_type'] == 'markdown')
        code_cells = sum(1 for cell in nb['cells'] if cell['cell_type'] == 'code')
        
        print(f"\n[INFO] Cell Distribution:")
        print(f"  - Markdown cells: {markdown_cells}")
        print(f"  - Code cells: {code_cells}")
        
        # Check for issues
        issues = []
        
        # Check each cell
        for i, cell in enumerate(nb['cells'], 1):
            cell_type = cell.get('cell_type', 'unknown')
            
            # Check if source is present
            if 'source' not in cell:
                issues.append(f"Cell {i}: Missing 'source' field")
                continue
            
            source = cell['source']
            
            # Check if source is empty
            if not source or (isinstance(source, list) and len(source) == 0):
                issues.append(f"Cell {i} ({cell_type}): Empty source")
            
            # Check for metadata
            if 'metadata' not in cell:
                issues.append(f"Cell {i}: Missing 'metadata' field")
            
            # For code cells, check outputs
            if cell_type == 'code':
                if 'outputs' not in cell:
                    issues.append(f"Cell {i}: Code cell missing 'outputs' field")
                if 'execution_count' not in cell:
                    issues.append(f"Cell {i}: Code cell missing 'execution_count' field")
        
        # Report issues
        if issues:
            print(f"\n[WARNING] Found {len(issues)} issues:")
            for issue in issues[:20]:  # Show first 20 issues
                print(f"  - {issue}")
            if len(issues) > 20:
                print(f"  ... and {len(issues) - 20} more issues")
        else:
            print(f"\n[OK] No structural issues found!")
        
        # Check for specific content
        print(f"\n[INFO] Content Analysis:")
        
        # Check for phase markers
        phase_markers = []
        for i, cell in enumerate(nb['cells'], 1):
            if cell['cell_type'] == 'markdown':
                source_text = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
                if 'Phase 1:' in source_text or 'phase1' in source_text:
                    phase_markers.append(('Phase 1', i))
                elif 'Phase 2A:' in source_text or 'phase2a' in source_text:
                    phase_markers.append(('Phase 2A', i))
                elif 'Phase 2B:' in source_text or 'phase2b' in source_text:
                    phase_markers.append(('Phase 2B', i))
        
        print(f"  Phase markers found: {len(phase_markers)}")
        for phase, cell_num in phase_markers:
            print(f"    - {phase} at cell {cell_num}")
        
        # Check for imports
        import_cells = []
        for i, cell in enumerate(nb['cells'], 1):
            if cell['cell_type'] == 'code':
                source_text = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
                if 'import' in source_text:
                    import_cells.append(i)
        
        print(f"  Import statements found in {len(import_cells)} cells")
        
        return len(issues) == 0
        
    except json.JSONDecodeError as e:
        print(f"[ERROR] JSON parsing error: {e}")
        return False
    except Exception as e:
        print(f"[ERROR] Error: {e}")
        return False

if __name__ == "__main__":
    notebook_path = "notebooks/project_deliverable_notebook.ipynb"
    is_valid = validate_notebook(notebook_path)
    
    if is_valid:
        print(f"\n[SUCCESS] Notebook is valid and ready to use!")
        sys.exit(0)
    else:
        print(f"\n[WARNING] Notebook has some issues that should be reviewed")
        sys.exit(1)