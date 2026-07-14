import json
import os
import sys

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

def py_to_ipynb(py_path, ipynb_path):
    with open(py_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cells = []
    current_cell_type = None
    current_lines = []

    def save_current_cell():
        nonlocal current_lines, current_cell_type
        if not current_lines:
            return
        content = "".join(current_lines)
        if current_cell_type == 'markdown':
            md_lines = []
            for l in current_lines:
                if l.startswith('# '):
                    md_lines.append(l[2:])
                elif l == '#\n':
                    md_lines.append('\n')
                else:
                    md_lines.append(l)
            cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": md_lines
            })
        elif current_cell_type == 'code':
            cells.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": current_lines
            })
        current_lines = []

    for line in lines:
        if line.strip() == '# %% [markdown]':
            save_current_cell()
            current_cell_type = 'markdown'
        elif line.strip() == '# %%':
            save_current_cell()
            current_cell_type = 'code'
        else:
            if current_cell_type is None:
                if line.startswith('#'):
                    current_cell_type = 'markdown'
                else:
                    current_cell_type = 'code'
            current_lines.append(line)

    save_current_cell()

    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

    with open(ipynb_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
    print(f"[OK] Created Notebook: {ipynb_path} ({len(cells)} cells)")

if __name__ == '__main__':
    py_to_ipynb('nexus_stadium_ai_lab.py', 'Nexus_2026_Smart_Stadium_AI_Lab_Notebook.ipynb')
    py_to_ipynb('nexus_stadium_db_lab.py', 'Nexus_2026_Smart_Stadium_Database_Lab_Notebook.ipynb')
    py_to_ipynb('nexus_stadium_interactive_dashboard.py', 'Nexus_2026_Interactive_System_Dashboard.ipynb')
