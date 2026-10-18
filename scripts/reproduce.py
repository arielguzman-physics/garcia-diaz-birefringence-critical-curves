"""Execute the numerical notebook and write the associated figures and tables."""

from pathlib import Path

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "notebooks" / "GD_birefringence_critical_curves_es.ipynb"

notebook = nbformat.read(NOTEBOOK, as_version=4)
client = NotebookClient(
    notebook,
    timeout=900,
    kernel_name="python3",
    resources={"metadata": {"path": str(ROOT)}},
)
client.execute()
nbformat.write(notebook, NOTEBOOK)
print(f"Notebook executed: {NOTEBOOK}")
