"""
Author: Nikos Eliassi
Course: Fundamental of Python Programming
Task: C
Year: 2026

Reads reservations from reservations.txt, separates paid/unpaid,
prints lists and a short summary report.
"""

from pathlib import Path


PAID_INDEX = 6  # Based on TaskA/TaskB file format (Paid field is the 7th value)


def load_lines() -> list[str]:
    path = Path(__file__).with_name("reservations.txt")
    return path.read_text(encoding="utf-8").splitlines()


def split_fields(line: str) -> list[str]:
    # Strip spaces around fields so comparisons work reliably
    return [p.strip() for p in line.split("|")]


def is_paid(value: str) -> bool:
    # Accept a few common representations safely
    v = value.strip().lower()
    return v in ("true", "yes", "y", "1")


def print_list(title: str, items: list[list[str]]) -> None:
    print(title)
    if not items:
        print("  (none)")
        return

    for row in items:
        # Show a compact, readable line: id | name | date | email
        # Adjust fields if your file format differs
        reservation_id = row[0]
        name = row[1]
        date = row[2]
        email = row[9] if len(row) > 9 else "(no email)"
        print(f"  - {reservation_id} | {name} | {date} | {email}")


def main() -> None:
    lines = load_lines()

    paid_rows: list[list[str]] = []
    unpaid_rows: list[list[str]] = []
    invalid_rows: list[str] = []

    for raw in lines:
        if not raw.strip():
            continue

        fields = split_fields(raw)

        # Expecting 10 fields based on TaskA/TaskB format
        if len(fields) < 10:
            invalid_rows.append(raw)
            continue

        paid_flag = is_paid(fields[PAID_INDEX])
        if paid_flag:
            paid_rows.append(fields)
        else:
            unpaid_rows.append(fields)

    total_valid = len(paid_rows) + len(unpaid_rows)

    print("Task C - Reservation report\n")
    print(f"Total lines in file: {len(lines)}")
    print(f"Valid reservations: {total_valid}")
    print(f"Paid: {len(paid_rows)}")
    print(f"Unpaid: {len(unpaid_rows)}")
    print(f"Invalid rows: {len(invalid_rows)}\n")

    print_list("Paid reservations:", paid_rows)
    print()
    print_list("Unpaid reservations:", unpaid_rows)

    if invalid_rows:
        print("\nInvalid rows (not processed):")
        for bad in invalid_rows:
            print(f"  - {bad}")


if __name__ == "__main__":
    main()
