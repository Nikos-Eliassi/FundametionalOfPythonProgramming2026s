# Copyright (c) 2026 Nikos Eliassi 
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

# Modified by nnn according to given task

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, date, time
from typing import Iterable


TRUE_VALUES = {"true", "1", "yes", "y", "kylla", "kyllä"}


def to_bool(text: str) -> bool:
    return text.strip().lower() in TRUE_VALUES


def parse_date(text: str) -> date:
    return datetime.strptime(text.strip(), "%Y-%m-%d").date()


def parse_time(text: str) -> time:
    return datetime.strptime(text.strip(), "%H:%M").time()


def parse_dt(text: str) -> datetime:
    return datetime.strptime(text.strip(), "%Y-%m-%d %H:%M:%S")


@dataclass(frozen=True)
class Reservation:
    rid: int
    customer_name: str
    email: str
    phone: str
    day: date
    start: time
    hours: int
    hourly_price: float
    confirmed: bool
    resource: str
    created_at: datetime

    def total(self) -> float:
        return self.hours * self.hourly_price

    def is_long(self, min_hours: int = 3) -> bool:
        return self.hours >= min_hours


def reservation_from_parts(parts: list[str]) -> Reservation:
    # Expected order in file:
    # id|name|email|phone|YYYY-MM-DD|HH:MM|duration|price|confirmed|resource|YYYY-MM-DD HH:MM:SS
    return Reservation(
        rid=int(parts[0]),
        customer_name=parts[1].strip(),
        email=parts[2].strip(),
        phone=parts[3].strip(),
        day=parse_date(parts[4]),
        start=parse_time(parts[5]),
        hours=int(parts[6]),
        hourly_price=float(parts[7]),
        confirmed=to_bool(parts[8]),
        resource=parts[9].strip(),
        created_at=parse_dt(parts[10]),
    )


def read_reservations(path: str, sep: str = "|") -> list[Reservation]:
    results: list[Reservation] = []
    with open(path, "r", encoding="utf-8") as file:
        for raw in file:
            raw = raw.strip()
            if not raw:
                continue
            parts = raw.split(sep)
            results.append(reservation_from_parts(parts))
    return results


def confirmed_only(items: Iterable[Reservation]) -> list[Reservation]:
    return [r for r in items if r.confirmed]


def long_only(items: Iterable[Reservation], min_hours: int = 3) -> list[Reservation]:
    return [r for r in items if r.is_long(min_hours)]


def print_confirmed(items: Iterable[Reservation]) -> None:
    print("Confirmed reservations:")
    for r in items:
        print(f"- {r.customer_name}, {r.resource}, {r.day:%d.%m.%Y} at {r.start:%H.%M}")


def print_long(items: Iterable[Reservation]) -> None:
    print("\nLong reservations (duration >= 3h):")
    for r in items:
        print(f"- {r.customer_name} ({r.hours}h), total {r.total():.2f} €")


def revenue(items: Iterable[Reservation]) -> float:
    return sum(r.total() for r in items)


def main() -> None:
    all_reservations = read_reservations("reservations.txt")

    confirmed = confirmed_only(all_reservations)
    print_confirmed(confirmed)

    long_res = long_only(all_reservations, min_hours=3)
    print_long(long_res)

    total_rev = revenue(confirmed)
    print(f"\nTotal revenue (confirmed): {total_rev:.2f} €")


if __name__ == "__main__":
    main()