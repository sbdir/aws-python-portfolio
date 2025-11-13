import csv
from pathlib import Path


INPUT_FILE = Path("input.csv")
OUTPUT_FILE = Path("output.csv")


def read_rows(path: Path):
    """CSV を読み込んで list[dict] で返す"""
    with path.open(mode="r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_rows(path: Path, fieldnames, rows):
    """list[dict] を CSV として書き出す"""
    with path.open(mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def add_total_column(rows):
    """
    price と quantity の列がある前提で、
    total = price * quantity の列を追加するサンプル。
    """
    result = []
    for row in rows:
        try:
            price = float(row.get("price", 0) or 0)
            quantity = float(row.get("quantity", 0) or 0)
            total = price * quantity
        except ValueError:
            total = 0

        new_row = dict(row)
        new_row["total"] = f"{total:.2f}"
        result.append(new_row)
    return result


def main():
    if not INPUT_FILE.exists():
        print(f"[ERROR] {INPUT_FILE} が存在しません。まず input.csv を用意してください。")
        return

    rows = read_rows(INPUT_FILE)
    rows_with_total = add_total_column(rows)

    if rows_with_total:
        fieldnames = list(rows_with_total[0].keys())
    else:
        fieldnames = []

    write_rows(OUTPUT_FILE, fieldnames, rows_with_total)
    print(f"[INFO] {OUTPUT_FILE} に書き出しました。")


if __name__ == "__main__":
    main()
