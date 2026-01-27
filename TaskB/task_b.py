def print_booker(reservation: list) -> None:
    """
    Prints the reservation number

    Parameters:
        reservation (list): reservation -> columns separated by |
    """
    booker = reservation[1]
    print(f"Booker: {booker}")


def main():
    """
    Reads reservation data from a file and
    prints them to the console using functions
    """

    # Define the file name directly in the code
    reservations = "reservations.txt"

    # Open the file, read it, and split the contents
    with open(reservations, "r", encoding="utf-8") as f:
        reservation = f.read().strip()
        reservation = reservation.split("|")

    # Implement the remaining parts following
    # the function print_booker(reservation)

    # The functions to be created should perform type conversions
    # and print according to the sample output

    # print_reservation_number(reservation)
    print_booker(reservation)
    # print_date(reservation)
    # print_start_time(reservation)
    # print_hours(reservation)
    # print_hourly_rate(reservation)
    # print_total_price(reservation)
    # print_paid(reservation)
    # print_venue(reservation)
    # print_phone(reservation)
    # print_email(reservation)


if __name__ == "__main__": 
    main()
