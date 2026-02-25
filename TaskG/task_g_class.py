# Copyright (c) 2026 Nikos Eliassi
# Modified according to task requirements

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, date, time
import os


def parse_bool(value: str) -> bool:
    return value.strip() == "True"


@dataclass
class Reservation:
    reservation_id: int
    name: str
    email: str
    phone: str
    reservation_date: date
    reservation_time: time
    duration: int
    price: float
    confirmed: bool
    reserved_resource: str
    created_at: datetime

    def total_price(self) -> float:
        return self.duration * self.price


def convert_reservation(parts: list[str]) -> Reservation:
    return Reservation(
        reservation_id=int(parts[0]),
        name=parts[1],
        email=parts[2],
        phone=parts[3],
        reservation_date=datetime.strptime(parts[4], "%Y-%m-%d").date(),
        reservation_time=datetime.strptime(parts[5], "%H:%M").time(),
        duration=int(parts[6]),
        price=float(parts[7]),
        confirmed=parse_bool(parts[8]),
        reserved_resource=parts[9],
        created_at=datetime.strptime(parts[10].strip(), "%Y-%m-%d %H:%M:%S"),
    )


def fetch_reservations(filename: str) -> list[Reservation]:
    reservations: list[Reservation] = []

    # Automatically read file from same folder as this script
    current_dir = os.path.dirname(__file__)
    filepath = os.path.join(current_dir, filename)

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if len(line) > 1:
                parts = line.strip().split("|")
                reservations.append(convert_reservation(parts))

    return reservations


def confirmed_reservations(reservations: list[Reservation]) -> None:
    for r in reservations:
        if r.confirmed:
            print(
                f"- {r.name}, {r.reserved_resource}, "
                f"{r.reservation_date.strftime('%d.%m.%Y')} at "
                f"{r.reservation_time.strftime('%H.%M')}"
            )


def long_reservations(reservations: list[Reservation]) -> None:
    for r in reservations:
        if r.duration >= 3:
            print(
                f"- {r.name}, {r.reservation_date.strftime('%d.%m.%Y')} at "
                f"{r.reservation_time.strftime('%H.%M')}, "
                f"duration {r.duration} h, {r.reserved_resource}"
            )


def confirmation_statuses(reservations: list[Reservation]) -> None:
    for r in reservations:
        print(f"{r.name} → {'Confirmed' if r.confirmed else 'NOT Confirmed'}")


def confirmation_summary(reservations: list[Reservation]) -> None:
    confirmed = len([r for r in reservations if r.confirmed])
    not_confirmed = len(reservations) - confirmed

    print(f"- Confirmed reservations: {confirmed} pcs")
    print(f"- Not confirmed reservations: {not_confirmed} pcs")


def total_revenue(reservations: list[Reservation]) -> None:
    revenue = sum(r.total_price() for r in reservations if r.confirmed)
    print(
        f"Total revenue from confirmed reservations: "
        f"{revenue:.2f} €".replace(".", ",")
    )


def main() -> None:
    reservations = fetch_reservations("reservations.txt")

    print("1) Confirmed Reservations")
    confirmed_reservations(reservations)

    print("2) Long Reservations (≥ 3 h)")
    long_reservations(reservations)

    print("3) Reservation Confirmation Status")
    confirmation_statuses(reservations)

    print("4) Confirmation Summary")
    confirmation_summary(reservations)

    print("5) Total Revenue from Confirmed Reservations")
    total_revenue(reservations)


if __name__ == "__main__":
    main()