"""
Author: Nikos Eliassi
Course: Fundamental of Python Programming
Task: C
Year: 2026

Counts reservations and separates paid and unpaid.
"""

from pathlib import Path


def load_reservations():
    path = Path(__file__).with_name("reservations.txt")
    return path.read_text(encoding="utf-8").splitlines()


def main():
    print("Task C - Reservation overview\n")

    rows = load_reservations()
    print(f"Total reservations: {len(rows)}\n")

    paid_list = []
    unpaid_list = []

    for row in rows:
        data = [p.strip() for p in row.split("|")]
        status = data[6]

        if status == "True":
            paid_list.append(data)
        else:
            unpaid_list.append(data)

    print("Paid reservations:")
    for item in paid_list:
        print(f"- {item[0]} | {item[1]} | {item[2]}")

    print("\nUnpaid reservations:")
    for item in unpaid_list:
        print(f"- {item[0]} | {item[1]} | {item[2]}")


if __name__ == "__main__":
    main()
