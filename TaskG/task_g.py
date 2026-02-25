# Copyright (c) 2026 Nikos Eliassi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# Modified by Nikos Eliassi according to given task (Task G - dict version)

"""
A program that prints reservation information according to requirements.

reservationId | name | email | phone | reservationDate | reservationTime | durationHours | price | confirmed | reservedResource | createdAt
---------------------------------------------------------------------------------------------------
201 | Moomin Valley | moomin@whitevalley.org | 0509876543 | 2025-11-12 | 09:00:00 | 2 | 18.50 | True | Forest Area 1 | 2025-08-12 14:33:20
"""

from __future__ import annotations

from datetime import datetime
from typing import Any
import os


def parse_bool(value: str) -> bool:
    """Convert 'True'/'False' string to bool (teacher data uses capitalized values)."""
    return value.strip() == "True"


def convert_reservation(parts: list[str]) -> dict[str, Any]:
    """Convert a split line (11 columns) into a dictionary with correct data types."""
    return {
        "id": int(parts[0]),
        "name": str(parts[1]),
        "email": str(parts[2]),
        "phone": str(parts[3]),
        "date": datetime.strptime(parts[4], "%Y-%m-%d").date(),
        "time": datetime.strptime(parts[5], "%H:%M").time(),
        "duration": int(parts[6]),
        "price": float(parts[7]),
        "confirmed": parse_bool(parts[8]),
        "resource": str(parts[9]),
        "created": datetime.strptime(parts[10].strip(), "%Y-%m-%d %H:%M:%S"),
    }


def fetch_reservations(filename: str) -> list[dict[str, Any]]:
    """
    Read reservations from a file and return converted reservation dictionaries.
    The file is searched from the same folder as this script (TaskG).
    """
    reservations: list[dict[str, Any]] = []

    current_dir = os.path.dirname(__file__)
    filepath = os.path.join(current_dir, filename)

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if len(line) > 1:
                parts = line.strip().split("|")
                reservations.append(convert_reservation(parts))

    return reservations


def is_long(reservation: dict[str, Any]) -> bool:
    return reservation["duration"] >= 3


def total_price(reservation: dict[str, Any]) -> float:
    return reservation["duration"] * reservation["price"]


def print_confirmed(reservations: list[dict[str, Any]]) -> None:
    for r in reservations:
        if r["confirmed"]:
            print(
                f"- {r['name']}, {r['resource']}, "
                f"{r['date'].strftime('%d.%m.%Y')} at {r['time'].strftime('%H.%M')}"
            )


def print_long(reservations: list[dict[str, Any]]) -> None:
    for r in reservations:
        if is_long(r):
            print(
                f"- {r['name']}, {r['date'].strftime('%d.%m.%Y')} at {r['time'].strftime('%H.%M')}, "
                f"duration {r['duration']} h, {r['resource']}"
            )


def print_total_revenue(reservations: list[dict[str, Any]]) -> None:
    revenue = sum(total_price(r) for r in reservations if r["confirmed"])
    print(f"Total revenue from confirmed reservations: {revenue:.2f} €".replace(".", ","))


def main() -> None:
    reservations = fetch_reservations("reservations.txt")

    print("1) Confirmed Reservations")
    print_confirmed(reservations)

    print("2) Long Reservations (≥ 3 h)")
    print_long(reservations)

    print("3) Total Revenue from Confirmed Reservations")
    print_total_revenue(reservations)


if __name__ == "__main__":
    main()