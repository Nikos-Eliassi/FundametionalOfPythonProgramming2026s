"""
Author: Nikos Eliassi
Course: Fundamental of Python Programming
Task: B
Year: 2026

Reads reservation data from a file and prints it in a formatted way.
"""

from datetime import datetime
from pathlib import Path


def read_file():
    path = Path(__file__).with_name("reservations.txt")
    with path.open("r", encoding="utf-8") as file:
        return file.readlines()


def format_euros(value):
    return "{:.2f}".format(value).replace(".", ",") + " €"


def show_reservation(data):
    reservation_id = int(data[0])
    name = data[1]
    date = datetime.strptime(data[2], "%Y-%m-%d").strftime("%d.%m.%Y")
    time = datetime.strptime(data[3], "%H:%M").strftime("%H:%M")
    hours = int(data[4])
    price = float(data[5])
    paid = "Yes" if data[6] == "True" else "No"
    location = data[7]
    phone = data[8]
    email = data[9]

    total = hours * price

    print("Reservation details:\n")
    print(f"Reservation number: {reservation_id}")
    print(f"Booker: {name}")
    print(f"Date: {date}")
    print(f"Start time: {time}")
    print(f"Number of hours: {hours}")
    print(f"Hourly price: {format_euros(price)}")
    print(f"Total price: {format_euros(total)}")
    print(f"Paid: {paid}")
    print(f"Location: {location}")
    print(f"Phone: {phone}")
    print(f"Email: {email}")
    print("-" * 30)


def main():
    lines = read_file()

    for line in lines:
        if line.strip():
            parts = [p.strip() for p in line.split("|")]
            show_reservation(parts)


if __name__ == "__main__":
    main()
