# Copyright (c) 2026 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

from datetime import datetime, date
from pathlib import Path

DAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def convert_data(line: list) -> list:
    """
    Convert data types to meet program requirements

    Parameters:
    line (list): Unconverted line -> 7 columns

    Returns:
    (list): Converted data types
    """
    return [
        datetime.fromisoformat(line[0]),
        int(line[1]),
        int(line[2]),
        int(line[3]),
        int(line[4]),
        int(line[5]),
        int(line[6]),
    ]


def read_data(filename: str) -> list:
    """
    Reads the CSV file and returns the rows in a suitable structure.

    Parameters:
    filename (str): Name of the file containing the electricity consumption and production

    Returns:
    reservations (list): Read and converted consumption and production
    """
    cons_prod = []

    file_path = Path(__file__).with_name(filename)  # <-- löytää CSV:n aina TaskE-kansiosta

    with open(file_path, "r", encoding="utf-8") as f:
        next(f)
        for line in f:
            line = line.strip()
            fields = line.split(";")
            cons_prod.append(convert_data(fields))

    return cons_prod


def day_information(day: date, database: list) -> str:
    """
    Reads the consumption and production per day

    Parameters:
    day (date): Reportable day
    database (list): Consumption and production data + dates

    Returns:
    Printable string
    """
    cons_prod = ["day", "date", 0, 0, 0, 0, 0, 0]

    for per_hour in database:
        if per_hour[0].date() == day:
            for i in range(1, len(per_hour)):
                cons_prod[i + 1] += per_hour[i] / 1000

    cons_prod[0] = DAYS[day.weekday()]
    cons_prod[1] = day

    converted_cons_prod = f"{cons_prod[0]:<11}"
    converted_cons_prod += f"{cons_prod[1].strftime('%d.%m.%Y'):<13}"

    for i, element in enumerate(cons_prod):
        if i > 1:
            two_decimal_to_string = f"{element:.2f}".replace(".", ",")
            converted_cons_prod += f"{two_decimal_to_string:<8}"

    return converted_cons_prod + "\n"


def week_header(number: int) -> str:
    """
    Reads the week number

    Parameters:
    number (int): The week number

    Returns:
    Printable string based on the week number
    """
    header = f"Week {number} electricity consumption and production (kWh, by phase)\n\n"
    header += "Day         Date        Consumption (kWh)        Production (kWh)\n"
    header += "                         (dd.mm.yyyy)  V1      V2      V3      V1      V2      V3\n"
    return header


def write_data(content: str):
    """
    Writes the content to the file.

    Parameters:
    content (str): Content
    """
    out_path = Path(__file__).with_name("summary.txt")  # <-- kirjoittaa summary.txt samaan kansioon
    out_path.write_text(content, encoding="utf-8")


def main() -> None:
    """
    Main function: reads data, computes daily totals, and prints the report.
    """
    file_content = ""

    # Week 41
    db = read_data("week41.csv")
    file_content += week_header(41)
    for i in range(6, 13):
        file_content += day_information(date(2025, 10, i), db)

    # Week 42
    db = read_data("week42.csv")
    file_content += "\n" + week_header(42)
    for i in range(13, 20):
        file_content += day_information(date(2025, 10, i), db)

    # Week 43
    db = read_data("week43.csv")
    file_content += "\n" + week_header(43)
    for i in range(20, 27):
        file_content += day_information(date(2025, 10, i), db)

    write_data(file_content)
    print(file_content)


if __name__ == "__main__":
    main()
