# Copyright (c) 2026 Nikos Eliassi
# License: MIT

from datetime import datetime
from pathlib import Path


def read_file(path: str) -> list[str]:
    with open(path, encoding="utf-8") as file:
        return [row.strip() for row in file if row.strip()]


def build_record(row: str) -> dict:
    fields = row.split("|")

    return {
        "reservation_id": int(fields[0]),
        "customer": fields[1].strip(),
        "contact_email": fields[2].strip(),
        "contact_phone": fields[3].strip(),
        "reservation_date": datetime.strptime(fields[4], "%Y-%m-%d").date(),
        "start_time": datetime.strptime(fields[5], "%H:%M").time(),
        "hours_booked": int(fields[6]),
        "unit_price": float(fields[7]),
        "is_confirmed": fields[8].strip().lower() == "true",
        "item": fields[9].strip(),
        "created_at": datetime.strptime(fields[10], "%Y-%m-%d %H:%M:%S"),
    }


def load_reservations(file_name: str) -> list[dict]:
    lines = read_file(file_name)
    return [build_record(line) for line in lines]


def calculate_revenue(data: list[dict]) -> float:
    total = 0.0
    for entry in data:
        if entry["is_confirmed"]:
            total += entry["hours_booked"] * entry["unit_price"]
    return total


def main() -> None:
    base = Path(__file__).resolve().parent
    file_path = base / "reservations.txt"

    reservations = load_reservations(str(file_path))

    print("=== CONFIRMED RESERVATIONS ===")
    for entry in reservations:
        if entry["is_confirmed"]:
            date_str = entry["reservation_date"].strftime("%d.%m.%Y")
            time_str = entry["start_time"].strftime("%H.%M")
            print(f"{entry['customer']} | {entry['item']} | {date_str} {time_str}")

    print("\n=== LONG BOOKINGS (>= 3h) ===")
    for entry in reservations:
        if entry["hours_booked"] >= 3:
            total_cost = entry["hours_booked"] * entry["unit_price"]
            print(f"{entry['customer']} - {entry['hours_booked']}h - {total_cost:.2f} €")

    total_income = calculate_revenue(reservations)
    print(f"\nTotal confirmed revenue: {total_income:.2f} €")


if __name__ == "__main__":
    main()