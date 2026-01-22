from __future__ import annotations

import argparse
from pathlib import Path

from ai_atlas_nexus import AIAtlasNexus


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="AI Atlas Nexus quickstart (no notebook).",
    )
    parser.add_argument(
        "--risk-id",
        default="atlas-data-bias",
        help="Risk id or tag to inspect (default: atlas-data-bias).",
    )
    parser.add_argument(
        "--export-dir",
        default="",
        help="Optional directory to export ai-risk-ontology.yaml.",
    )
    return parser


def print_header(title: str) -> None:
    print("\n" + title)
    print("-" * len(title))


def main() -> None:
    args = build_parser().parse_args()

    ran = AIAtlasNexus()
    version = ran.get_version().get("version")

    print_header("Library Info")
    print(f"ai-atlas-nexus version: {version}")

    classes = ran.get_all_classes()
    print_header("Available Classes")
    print(f"Total classes: {len(classes)}")
    print(f"Sample classes: {classes[:8]}")

    risks = ran.get_all_risks()
    print_header("Risks Overview")
    print(f"Total risks: {len(risks)}")

    risk = ran.get_risk(id=args.risk_id) or ran.get_risk(tag=args.risk_id)
    if risk is None:
        print(f"Risk not found: {args.risk_id}")
        return

    print_header("Risk Detail")
    print(f"ID: {risk.id}")
    print(f"Name: {risk.name}")
    print(f"Taxonomy: {risk.isDefinedByTaxonomy}")
    print(f"Type: {risk.type}")
    print(f"Tag: {risk.tag}")
    print(f"Description: {risk.description}")

    related_actions = ran.get_related_actions(risk=risk)
    related_controls = ran.get_related_risk_controls(risk=risk)
    related_evaluations = ran.get_related_evaluations(risk=risk)
    related_risks = ran.get_related_risks(risk=risk)

    print_header("Linked Items")
    print(f"Actions: {len(related_actions)}")
    print(f"Risk controls: {len(related_controls)}")
    print(f"Evaluations: {len(related_evaluations)}")
    print(f"Related risks: {len(related_risks)}")

    if related_risks:
        related_ids = [item.id for item in related_risks[:10]]
        print(f"Related risk ids (sample): {related_ids}")

    if args.export_dir:
        export_dir = Path(args.export_dir)
        export_dir.mkdir(parents=True, exist_ok=True)
        ran.export(str(export_dir))
        print_header("Export")
        print(f"Exported ai-risk-ontology.yaml to: {export_dir}")


if __name__ == "__main__":
    main()
