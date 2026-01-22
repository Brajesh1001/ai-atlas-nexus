from __future__ import annotations

from pathlib import Path

from ai_atlas_nexus import AIAtlasNexus


QUICKSTART_NOTEBOOK_RELATIVE = Path(
    "docs/examples/notebooks/AI_Atlas_Nexus_Quickstart.ipynb"
)
QUICKSTART_GITHUB_URL = (
    "https://github.com/IBM/ai-atlas-nexus/blob/main/"
    "docs/examples/notebooks/AI_Atlas_Nexus_Quickstart.ipynb"
)
DOCS_SITE_URL = "https://ibm.github.io/ai-atlas-nexus/"


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    notebook_path = repo_root / QUICKSTART_NOTEBOOK_RELATIVE

    print("AI Atlas Nexus: Quick Start Guide")
    print(f"Local notebook: {notebook_path}")
    print(f"Notebook exists: {notebook_path.exists()}")
    print(f"GitHub reference: {QUICKSTART_GITHUB_URL}")
    print(f"Docs site: {DOCS_SITE_URL}")

    # Optional: quick sanity check on local data
    ran = AIAtlasNexus()
    risks = ran.get_all_risks()
    print(f"Total risks available: {len(risks)}")
    print("Sample risk IDs:", [r.id for r in risks[:5]])


if __name__ == "__main__":
    main()
