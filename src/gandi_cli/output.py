import json
import sys
from typing import Any
from rich.console import Console
from rich.table import Table
from rich import print_json as rich_print_json

console = Console()

def print_table(data: list[dict], columns: list[tuple[str, str]], title: str | None = None) -> None:
    """Print data as a rich table.

    Args:
        data: List of dicts to display
        columns: List of (key, header_label) tuples
        title: Optional table title
    """
    table = Table(title=title, show_lines=False)
    for key, header in columns:
        table.add_column(header, no_wrap=(key in ("fqdn", "domain", "name")))
    for row in data:
        values = []
        for key, _ in columns:
            val = row.get(key, "")
            if isinstance(val, list):
                val = ", ".join(str(v) for v in val)
            elif isinstance(val, dict):
                val = json.dumps(val)
            values.append(str(val) if val is not None else "")
        table.add_row(*values)
    console.print(table)


def print_json_output(data: Any) -> None:
    """Print data as formatted JSON."""
    console.print_json(json.dumps(data, default=str))


def print_plain(data: Any) -> None:
    """Print data as plain text (key=value for dicts, one line per item for lists)."""
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                parts = [f"{k}={v}" for k, v in item.items()]
                print("\t".join(parts))
            else:
                print(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                value = json.dumps(value, default=str)
            print(f"{key}: {value}")
    else:
        print(data)


def print_detail(data: dict, fields: list[tuple[str, str]] | None = None) -> None:
    """Print a single record in key-value detail format using rich.

    Args:
        data: Dict to display
        fields: Optional list of (key, label) tuples. If None, shows all keys.
    """
    if fields is None:
        fields = [(k, k) for k in data.keys()]
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("Field", style="bold cyan", no_wrap=True)
    table.add_column("Value")
    for key, label in fields:
        val = data.get(key, "")
        if isinstance(val, list):
            val = ", ".join(str(v) for v in val)
        elif isinstance(val, dict):
            val = json.dumps(val, default=str, indent=2)
        table.add_row(label, str(val) if val is not None else "")
    console.print(table)


def output(data: Any, fmt: str = "table", columns: list[tuple[str, str]] | None = None,
           detail_fields: list[tuple[str, str]] | None = None, title: str | None = None) -> None:
    """Universal output dispatcher.

    Args:
        data: Data to output (list for table, dict for detail)
        fmt: Output format - "table", "json", or "plain"
        columns: For table format - list of (key, header) tuples
        detail_fields: For dict detail - list of (key, label) tuples
        title: Optional title for table
    """
    if fmt == "json":
        print_json_output(data)
    elif fmt == "plain":
        print_plain(data)
    else:  # table
        if isinstance(data, list) and columns:
            print_table(data, columns, title=title)
        elif isinstance(data, dict):
            print_detail(data, fields=detail_fields)
        else:
            print_json_output(data)
