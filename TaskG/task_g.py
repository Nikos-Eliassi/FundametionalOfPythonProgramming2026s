from pathlib import Path
from read_reservations import (
    fetch_reservations,
    confirmed_reservations,
    long_reservations,
    confirmation_statuses,
    confirmation_summary,
    total_revenue
)


# hakee tämän tiedoston kansion automaattisesti
BASE_DIR = Path(__file__).parent


def main():
    # avaa reservations.txt samasta kansiosta kuin tämä tiedosto
    reservations = fetch_reservations(str(BASE_DIR / "reservations.txt"))

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
