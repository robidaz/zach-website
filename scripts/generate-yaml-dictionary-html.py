from __future__ import annotations

import json
import sys
from pathlib import Path

import openpyxl
import yaml
from jinja2 import Environment, FileSystemLoader

REPO_ROOT = Path(__file__).resolve().parent.parent
_DICT_DIR = REPO_ROOT / "documentation" / "core_design_docs"
_HTML_DIR = _DICT_DIR / "html_visuals"
TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"

_DATA_PREFERRED = [
    "component", "entity", "sub_level", "json_attribute", "json_store",
    "database_table", "database_field", "database_column",
    "is_extended_attribute", "type", "description", "literal_change", "notes",
]
_MSG_PREFERRED = [
    "definition_id", "text", "short_error_text",
    "relevant_extension", "default_error_level", "max_error_level", "min_error_level",
]
_LOC_PREFERRED = ["component", "entity", "key", "value"]

DICTIONARY_CONFIGS: list[dict] = [
    {
        "id": "data",
        "label": "Data Dictionary",
        "input": _DICT_DIR / "masc_data_dictionary.yaml",
        "output": _HTML_DIR / "masc_data_dictionary.html",
        "template": "masc_data_dictionary.html.j2",
        "builder": lambda data: build_data_dataset(data),
    },
    {
        "id": "message",
        "label": "Message Dictionary",
        "input": _DICT_DIR / "masc_message_dictionary.yaml",
        "output": _HTML_DIR / "masc_message_dictionary.html",
        "template": "masc_message_dictionary.html.j2",
        "builder": lambda data: build_message_dataset(data),
    },
    {
        "id": "localization",
        "label": "Localization Dictionary",
        "input": _DICT_DIR / "masc_localization_dictionary.yaml",
        "output": _HTML_DIR / "masc_localization_dictionary.html",
        "xlsx_source": _DICT_DIR / "MASC Localization.xlsx",
        "template": "masc_localization_dictionary.html.j2",
        "builder": lambda data: build_localization_dataset(data),
    },
]

COMBINED_CONFIG: dict = {
    "output": _HTML_DIR / "masc_combined_dictionary.html",
    "template": "masc_combined_dictionary.html.j2",
}


def collect_columns(rows, preferred: list[str] | None = None) -> list[str]:
    order = preferred if preferred is not None else _DATA_PREFERRED
    discovered: list[str] = []
    for row in rows:
        if isinstance(row, dict):
            for key in row.keys():
                if key not in discovered:
                    discovered.append(key)
    ordered = [col for col in order if col in discovered]
    ordered.extend(col for col in discovered if col not in ordered)
    return ordered


def unique_values(rows: list[dict], field_name: str) -> list[str]:
    return sorted(
        {str(row.get(field_name, "")).strip() for row in rows if str(row.get(field_name, "")).strip()},
        key=str.casefold,
    )


def _dict_rows(entity_dictionaries: dict) -> dict:
    rows: dict[str, list] = {}
    for name, payload in entity_dictionaries.items():
        if isinstance(payload, list):
            rows[name] = payload
        elif isinstance(payload, dict):
            rows[name] = payload.get("dictionary", [])
        else:
            rows[name] = []
    return rows


def build_data_dataset(data: dict) -> dict:
    title = data.get("title", "MASC Data Dictionary")

    extended_attributes = data.get("extended_attributes") or []
    extended_columns = collect_columns(extended_attributes, _DATA_PREFERRED)
    extended_components = unique_values(extended_attributes, "component")
    extended_entities = unique_values(extended_attributes, "entity")

    entity_dictionaries = data.get("entity_dictionaries") or {}
    dictionary_names = sorted(entity_dictionaries.keys(), key=str.casefold)
    dictionary_rows = _dict_rows(entity_dictionaries)
    dictionary_columns = collect_columns(
        (row for rows in dictionary_rows.values() for row in rows),
        _DATA_PREFERRED,
    )

    return {
        "title": title,
        "sections": {
            "extended_attributes": {
                "label": "Extended Attributes",
                "description": "View configuration rows grouped by component and filtered by entity.",
                "primaryFilterLabel": "Component",
                "secondaryFilterLabel": "Entity",
                "columns": extended_columns,
                "rows": extended_attributes,
                "primaryOptions": extended_components,
                "secondaryOptions": extended_entities,
                "primaryField": "component",
                "secondaryField": "entity",
                "summaryLabel": "rows",
            },
            "entity_dictionaries": {
                "label": "Entity Dictionaries",
                "description": "Switch across dictionary tabs and inspect each entity mapping in spreadsheet form.",
                "primaryFilterLabel": "Dictionary",
                "secondaryFilterLabel": "Entity",
                "columns": dictionary_columns,
                "rowsByPrimary": dictionary_rows,
                "primaryOptions": dictionary_names,
                "secondaryField": "entity",
                "summaryLabel": "fields",
            },
        },
    }


def build_message_dataset(data: dict) -> dict:
    title = data.get("title", "MASC Message Dictionary")
    rows = data.get("dictionary") or []
    columns = collect_columns(rows, _MSG_PREFERRED)
    extension_options = unique_values(rows, "relevant_extension")
    return {
        "title": title,
        "sections": {
            "message_dictionary": {
                "label": "Message Dictionary",
                "description": "View and filter FEMA message definitions by extension and error level.",
                "primaryFilterLabel": "Extension",
                "secondaryFilterLabel": "Error Level",
                "columns": columns,
                "rows": rows,
                "primaryOptions": extension_options,
                "primaryField": "relevant_extension",
                "secondaryField": "default_error_level",
                "summaryLabel": "messages",
            },
        },
    }


def convert_localization_xlsx(xlsx_path: Path, yaml_path: Path) -> None:
    wb = openpyxl.load_workbook(str(xlsx_path), read_only=True, data_only=True)
    ws = wb["Localization"]
    rows = []
    for r in ws.iter_rows(min_row=3, values_only=True):
        if not r[0]:
            continue
        rows.append({
            "component": str(r[0]).strip(),
            "entity": str(r[1]).strip() if r[1] else "",
            "key": str(r[2]).strip() if r[2] else "",
            "value": str(r[3]).strip() if r[3] else "",
        })
    data = {"title": "MASC Localization Dictionary", "dictionary": rows}
    yaml_path.write_text(
        yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False),
        encoding="utf-8",
    )
    print(f"Converted {len(rows)} rows: {xlsx_path.name} → {yaml_path.name}")


def build_localization_dataset(data: dict) -> dict:
    title = data.get("title", "MASC Localization Dictionary")
    rows = data.get("dictionary") or []
    columns = collect_columns(rows, _LOC_PREFERRED)
    component_options = unique_values(rows, "component")
    return {
        "title": title,
        "sections": {
            "localization_dictionary": {
                "label": "Localization Dictionary",
                "description": "View localization key-value pairs by component and entity.",
                "primaryFilterLabel": "Component",
                "secondaryFilterLabel": "Entity",
                "columns": columns,
                "rows": rows,
                "primaryOptions": component_options,
                "primaryField": "component",
                "secondaryField": "entity",
                "summaryLabel": "keys",
            },
        },
    }


def build_combined_dataset(built: list[tuple[str, str, dict]]) -> dict:
    return {
        "title": "MASC Dictionary Suite",
        "dictionaries": [
            {"id": did, "label": label, "sections": ds["sections"]}
            for did, label, ds in built
        ],
    }





def _jinja_env() -> Environment:
    return Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=False,
    )


def render_html(template_name: str, dataset: dict) -> str:
    env = _jinja_env()
    template = env.get_template(template_name)
    return template.render(
        title=dataset["title"],
        payload=json.dumps(dataset, ensure_ascii=False),
    )


def main() -> None:
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1]).resolve()
        if input_path.suffix.lower() == ".xlsx":
            xlsx_cfg = next(
                (cfg for cfg in DICTIONARY_CONFIGS
                 if cfg.get("xlsx_source") and cfg["xlsx_source"].resolve() == input_path),
                None,
            )
            if not xlsx_cfg:
                print(f"No registered config found for: {input_path}")
                sys.exit(1)
            convert_localization_xlsx(input_path, xlsx_cfg["input"])
            input_path = xlsx_cfg["input"]
        configs = [
            cfg for cfg in DICTIONARY_CONFIGS
            if cfg["input"].resolve() == input_path
        ]
        if not configs:
            print(f"No registered config found for: {input_path}")
            sys.exit(1)
    else:
        for cfg in DICTIONARY_CONFIGS:
            if cfg.get("xlsx_source") and cfg["xlsx_source"].exists():
                convert_localization_xlsx(cfg["xlsx_source"], cfg["input"])
        configs = DICTIONARY_CONFIGS

    built: list[tuple[str, str, dict]] = []
    for cfg in configs:
        input_path: Path = cfg["input"]
        output_path: Path = cfg["output"]
        if not input_path.exists():
            print(f"Skipping (not found): {input_path}")
            continue
        data = yaml.safe_load(input_path.read_text(encoding="utf-8"))
        dataset = cfg["builder"](data)
        html = render_html(cfg["template"], dataset)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(html, encoding="utf-8")
        print(f"Generated: {output_path}")
        built.append((cfg["id"], cfg["label"], dataset))

    # Build a full set of datasets for the combined file, loading any configs
    # not already processed (e.g. when only one YAML was passed as an argument).
    built_ids = {entry[0] for entry in built}
    combined_entries = list(built)
    for cfg in DICTIONARY_CONFIGS:
        if cfg["id"] in built_ids:
            continue
        if not cfg["input"].exists():
            print(f"Skipping combined (not found): {cfg['input']}")
            combined_entries = []
            break
        data = yaml.safe_load(cfg["input"].read_text(encoding="utf-8"))
        combined_entries.append((cfg["id"], cfg["label"], cfg["builder"](data)))

    if len(combined_entries) == len(DICTIONARY_CONFIGS):
        combined = build_combined_dataset(combined_entries)
        combined_html = render_html(COMBINED_CONFIG["template"], combined)
        combined_out: Path = COMBINED_CONFIG["output"]
        combined_out.parent.mkdir(parents=True, exist_ok=True)
        combined_out.write_text(combined_html, encoding="utf-8")
        print(f"Generated: {combined_out}")


if __name__ == "__main__":
    main()
