import os
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)

def read_reservation(filename):
    with open(filename, "r", encoding="utf-8") as file:
        line = file.read().strip()
    return [item.strip() for item in line.split("|")]

def format_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.strftime("%d.%m.%Y")

def format_time(time_str):
    time_obj = datetime.strptime(time_str, "%H:%M")
    return time_obj.strftime("%H:%M")

def euros(value):
    return "{:.2f}".format(value).replace(".", ",") + " €"

def main():
    data = read_reservation(os.path.join(BASE_DIR, "reservations.txt"))

    reservation_id = int(data[0])
    booker = data[1]
    date = format_date(data[2])
    start_time = format_time(data[3])
    hours = int(data[4])
    hourly_price = float(data[5])
    paid = data[6] == "True"
    location = data[7]
    phone = data[8]
    email = data[9]

    total_price = hours * hourly_price

    print("Reservation details:\n")
    print(f"Reservation number: {reservation_id}")
    print(f"Booker: {booker}")
    print(f"Date: {date}")
    print(f"Start time: {start_time}")
    print(f"Number of hours: {hours}")
    print(f"Hourly price: {euros(hourly_price)}")
    print(f"Total price: {euros(total_price)}")
    print(f"Paid: {'Yes' if paid else 'No'}")
    print(f"Location: {location}")
    print(f"Phone: {phone}")
    print(f"Email: {email}")

if __name__ == "__main__":
    main()
