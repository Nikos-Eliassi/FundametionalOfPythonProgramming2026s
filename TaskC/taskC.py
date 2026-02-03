from datetime import datetime
from pathlib import Path


HEADERS = [
    "reservationId",
    "name",
    "email",
    "phone",
    "reservationDate",
    "reservationTime",
    "durationHours",
    "price",
    "confirmed",
    "reservedResource",
    "createdAt",
]


def to_bool(s: str) -> bool:
    s = s.strip()
    if s == "True":
        return True
    if s == "False":
        return False
    raise ValueError(f"Invalid bool: {s}")


def parse_time(s: str):
    s = s.strip()
    # accept HH:MM or HH:MM:SS
    for fmt in ("%H:%M:%S", "%H:%M"):
        try:
            return datetime.strptime(s, fmt).time()
        except ValueError:
            pass
    raise ValueError(f"Invalid time: {s}")


def convert_reservation_data(fields: list[str]) -> list:
    fields = [x.strip() for x in fields]

    if len(fields) != 11:
        raise ValueError(f"Expected 11 fields, got {len(fields)}: {fields}")

    return [
        int(fields[0]),                                   # reservationId
        fields[1],                                        # name
        fields[2],                                        # email
        fields[3],                                        # phone
        datetime.strptime(fields[4], "%Y-%m-%d").date(),   # reservationDate
        parse_time(fields[5]),                            # reservationTime
        int(fields[6]),                                   # durationHours
        float(fields[7]),                                 # price
        to_bool(fields[8]),                               # confirmed
        fields[9],                                        # reservedResource
        datetime.strptime(fields[10], "%Y-%m-%d %H:%M:%S") # createdAt
    ]


def fetch_reservations(filename: str) -> list[list]:
    file_path = Path(__file__).with_name(filename)

    reservations = []
    with file_path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                reservations.append(convert_reservation_data(line.split("|")))
    return reservations


def confirmed_reservations(reservations: list[list]) -> None:
    for r in reservations:
        if r[8]:
            print(f"{r[0]} | {r[1]} | {r[9]} | {r[4]} {r[5]}")


def long_reservations(reservations: list[list]) -> None:
    # tulkinta: "long" = vähintään 3 tuntia
    for r in reservations:
        if r[6] >= 3:
            print(f"{r[0]} | {r[1]} | {r[6]}h | {r[4]} {r[5]} | {r[9]}")


def confirmation_statuses(reservations: list[list]) -> None:
    for r in reservations:
        status = "CONFIRMED" if r[8] else "NOT CONFIRMED"
        print(f"{r[0]} | {r[1]} | {status}")


def confirmation_summary(reservations: list[list]) -> None:
    total = len(reservations)
    confirmed = sum(1 for r in reservations if r[8])
    not_confirmed = total - confirmed
    print(f"Total: {total}")
    print(f"Confirmed: {confirmed}")
    print(f"Not confirmed: {not_confirmed}")


def total_revenue(reservations: list[list]) -> None:
    # tulkinta: tulo = vain confirmed varaukset
    total = sum(r[7] for r in reservations if r[8])
    print(f"Total revenue (confirmed only): {total:.2f} EUR")


def main():
    reservations = fetch_reservations("reservations.txt")

    # PART A: näytä data + tyypit (opettajan debug-osuus)
    print(" | ".join(HEADERS))
    print("-" * 72)
    for r in reservations:
        print(" | ".join(str(x) for x in r))
        print(" | ".join(type(x).__name__ for x in r))
        print("-" * 72)

    # PART B: raportit
    print("\n1) Confirmed Reservations")
    confirmed_reservations(reservations)

    print("\n2) Long Reservations (>= 3 hours)")
    long_reservations(reservations)

    print("\n3) Confirmation Statuses")
    confirmation_statuses(reservations)

    print("\n4) Confirmation Summary")
    confirmation_summary(reservations)

    print("\n5) Total Revenue")
    total_revenue(reservations)


if __name__ == "__main__":
    main()
