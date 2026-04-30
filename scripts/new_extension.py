#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import re
from dataclasses import dataclass
from pathlib import Path

TOKEN_PATTERN = re.compile(r"{{\s*([A-Z0-9_]+)\s*}}")


@dataclass(frozen=True)
class Inputs:
    product: str
    ext_id: str
    ext_title: str
    ext_short_name: str
    kind: str
    today: str


# ----------------------------
# VALIDATION
# ----------------------------
def validate_id(value: str, pad_to_2: bool=True) -> str:
    """
    Accept IDs like EX02, TM11, INT11, ABC123.
    Format: 2-3 letters + 1-3 digits.
    """
    value = value.strip().upper()
    m = re.fullmatch(r"([A-Z]{2,3})(\d{1,3})", value)
    if not m:
        raise ValueError(
            "ID must be 2–3 letters followed by 1–3 digits "
            "(e.g., EX02, TM11, INT11, ABC123)."
        )

    prefix, num_str = m.group(1), m.group(2)
    num = int(num_str)

    if pad_to_2 and num < 100:
        return f"{prefix}{num:02d}"
    return f"{prefix}{num}"


def validate_product_name(name: str) -> str:
    """
    Product must be:
    - 1 to 5 characters
    - Letters only
    - Auto-uppercase
    """
    name = name.strip().upper()

    if not name:
        raise ValueError("Product cannot be empty.")

    if not name.isalpha():
        raise ValueError("Product must contain letters only (A–Z).")

    if len(name) > 5:
        raise ValueError("Product must be 5 characters or fewer.")

    return name


def safe_filename(s: str) -> str:
    """
    Keep filenames human-friendly and Windows-safe.
    """
    s = s.strip()
    s = re.sub(r'[<>:"/\\|?*]', "-", s)  # illegal on Windows
    s = re.sub(r"\s+", " ", s)
    return s


# ----------------------------
# TEMPLATE TOKEN HANDLING
# ----------------------------
def extract_tokens(template_text: str) -> set[str]:
    """
    Return unique token names found in the template like {{AUTHOR}}.
    """
    return set(TOKEN_PATTERN.findall(template_text))


def parse_vars(var_args: list[str]) -> dict[str, str]:
    """
    Parse repeated --var KEY=VALUE args into a dict.
    Keys are uppercase.
    """
    out: dict[str, str] = {}
    for item in var_args:
        if "=" not in item:
            raise ValueError(f"--var must be KEY=VALUE. Got: {item!r}")
        k, v = item.split("=", 1)
        k = k.strip().upper()
        v = v.strip()
        if not k:
            raise ValueError(f"--var key cannot be empty. Got: {item!r}")
        out[k] = v
    return out


def resolve_missing_tokens(
    required_tokens: set[str],
    mapping: dict[str, str],
    provided_vars: dict[str, str],
    defaults: dict[str, str] | None=None,
) -> dict[str, str]:
    """
    Merge mapping + defaults + provided_vars, then prompt for anything still missing.
    Precedence: mapping -> defaults -> provided_vars (CLI wins).
    """
    defaults = defaults or {}

    resolved = dict(mapping)

    # Fill from defaults if not already present
    for k, v in defaults.items():
        if k not in resolved and v is not None:
            resolved[k] = v

    # CLI overrides win
    resolved.update(provided_vars)

    missing = sorted(t for t in required_tokens if t not in resolved)
    for token in missing:
        val = input(f"Value for {token}: ").strip()
        if not val:
            raise ValueError(f"Missing required token {token} (blank input).")
        resolved[token] = val

    return resolved


def render_template(template_text: str, mapping: dict[str, str]) -> str:

    def replace(m: re.Match) -> str:
        key = m.group(1)
        if key not in mapping:
            raise KeyError(f"Template token {{{{{key}}}}} has no provided value.")
        return mapping[key]

    rendered = TOKEN_PATTERN.sub(replace, template_text)

    leftover = TOKEN_PATTERN.findall(rendered)
    if leftover:
        raise ValueError(f"Unresolved tokens remain: {sorted(set(leftover))}")

    return rendered


# ----------------------------
# DISCOVERY
# ----------------------------
def discover_templates(templates_dir: Path) -> dict[str, Path]:
    """
    Maps:
        api.md -> api
        ui.md  -> ui
    """
    d: dict[str, Path] = {}
    if not templates_dir.exists():
        return d

    for p in templates_dir.glob("*.md"):
        d[p.stem.lower()] = p.resolve()

    return d


def list_products(extensions_root: Path) -> list[str]:
    """
    Products are folders under extensions/, excluding .templates.
    """
    skip = {".templates"}
    products: list[str] = []
    for p in extensions_root.iterdir():
        if p.is_dir() and not p.name.startswith(".") and p.name not in skip:
            products.append(p.name)
    return sorted(products)


# ----------------------------
# UI HELPERS
# ----------------------------
def choose_from_list(options: list[str], prompt: str) -> str:
    if not options:
        raise ValueError("No options available.")

    print(prompt)
    for i, opt in enumerate(options, start=1):
        print(f"  {i}. {opt}")

    while True:
        raw = input(f"Select 1-{len(options)}: ").strip()
        if raw.isdigit():
            idx = int(raw)
            if 1 <= idx <= len(options):
                return options[idx - 1]
        print("Invalid selection. Try again.")


def prompt_if_missing(value: str | None, label: str) -> str:
    if value and value.strip():
        return value.strip()
    return input(f"{label}: ").strip()


def choose_or_create_product(extensions_root: Path, passed_product: str | None) -> str:
    """
    If passed_product is provided, validate and use it (creating folder if needed).
    Otherwise, prompt user to select an existing product or create a new one.
    """
    if passed_product and passed_product.strip():
        product = validate_product_name(passed_product)
        (extensions_root / product).mkdir(exist_ok=True)
        return product

    products = list_products(extensions_root)
    menu = products + ["+ Create New Product"]

    selection = choose_from_list(menu, "Choose product folder:")
    if selection != "+ Create New Product":
        return selection

    # Create new product
    while True:
        try:
            new_name = input("Enter new product name (≤5 letters): ")
            product = validate_product_name(new_name)
            (extensions_root / product).mkdir(exist_ok=True)
            return product
        except ValueError as e:
            print(f"Error: {e}")


# ----------------------------
# MAIN
# ----------------------------
def main() -> int:
    repo_root = Path.cwd()
    extensions_root = repo_root / "extensions"
    templates_dir = extensions_root / ".templates"

    if not extensions_root.exists():
        raise FileNotFoundError("extensions/ folder not found at repo root.")

    templates = discover_templates(templates_dir)
    if not templates:
        raise FileNotFoundError(
            f"No templates found in {templates_dir}. Expected at least api.md and ui.md."
        )

    parser = argparse.ArgumentParser(description="Create a new extension spec.")
    parser.add_argument("--product", help="Product folder (e.g., MAWM). Can create if it doesn't exist.")
    parser.add_argument("--id", dest="ext_id", help="Extension ID (e.g., INT11, TM11, EX02)")
    parser.add_argument("--title", help="Extension title")
    parser.add_argument("--short-name", help="Short name (optional)")
    parser.add_argument("--kind", help="Template kind (api, ui)")
    parser.add_argument("--list-kinds", action="store_true", help="List template kinds and exit")
    parser.add_argument(
        "--var",
        action="append",
        default=[],
        help='Provide template variables like --var AUTHOR="Zach" (repeatable).',
    )
    args = parser.parse_args()

    if args.list_kinds:
        print("Available template kinds:")
        for k in sorted(templates.keys()):
            print(f"  - {k}")
        return 0

    # Template kind
    kind = (args.kind or "").strip().lower()
    if not kind:
        kind = choose_from_list(sorted(templates.keys()), "Choose template kind:")
    if kind not in templates:
        raise ValueError(f"Unknown template kind '{kind}'. Available: {', '.join(sorted(templates.keys()))}")

    template_path = templates[kind]

    # Product selection / creation
    product = choose_or_create_product(extensions_root, args.product)

    # Primary inputs
    ext_id_raw = prompt_if_missing(args.ext_id, "Extension ID (e.g., INT11)")
    ext_title = prompt_if_missing(args.title, "Extension Title")
    ext_short = args.short_name.strip() if args.short_name and args.short_name.strip() else ext_title

    ext_id = validate_id(ext_id_raw, pad_to_2=True)
    today = dt.date.today().isoformat()

    inputs = Inputs(
        product=product,
        ext_id=ext_id,
        ext_title=ext_title.strip(),
        ext_short_name=ext_short.strip(),
        kind=kind,
        today=today,
    )

    template_text = template_path.read_text(encoding="utf-8")
    required_tokens = extract_tokens(template_text)

    provided_vars = parse_vars(args.var)

    # Base tokens we *always* know
    base_mapping: dict[str, str] = {
        "PRODUCT": inputs.product,
        "EXT_ID": inputs.ext_id,
        "EXT_TITLE": inputs.ext_title,
        "EXT_SHORT_NAME": inputs.ext_short_name,
        "KIND": inputs.kind,
        "DATE": inputs.today,
    }

    # Opinionated defaults (override with --var if desired)
    defaults: dict[str, str] = {
        "CUSTOMER": "FEMA",
        "STATUS": "Draft",
        "VERSION": "1.0",
    }

    final_mapping = resolve_missing_tokens(
        required_tokens=required_tokens,
        mapping=base_mapping,
        provided_vars=provided_vars,
        defaults=defaults,
    )

    rendered = render_template(template_text, final_mapping)

    # Output paths: extensions/<PRODUCT>/<ID>/
    target_dir = extensions_root / inputs.product / inputs.ext_id
    media_dir = target_dir / "media"

    target_dir.mkdir(parents=True, exist_ok=True)
    media_dir.mkdir(parents=True, exist_ok=True)

    # Spec filename: "<ID> - <Title>.md"
    spec_filename = safe_filename(f"{inputs.ext_id} - {inputs.ext_title}.md")
    spec_path = target_dir / spec_filename

    if spec_path.exists():
        raise FileExistsError(f"Spec already exists: {spec_path.relative_to(repo_root)}")

    spec_path.write_text(rendered, encoding="utf-8")

    print("\nCreated:")
    print(f"  Kind:   {inputs.kind}")
    print(f"  Folder: {target_dir.relative_to(repo_root)}")
    print(f"  Spec:   {spec_path.relative_to(repo_root)}")
    print(f"  Media:  {media_dir.relative_to(repo_root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
