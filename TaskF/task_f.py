# Copyright (c) 2026 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

from datetime import datetime, date
from pathlib import Path


def convert_data(line: list) -> list:
    """
    Convert data types to meet program requirements

    Parameters:
    line (list): Unconverted line -> 4 columns

    Returns:
    list: Converted data types
    """
    return [
        datetime.fromisoformat(line[0]),
        float(line[1].replace(",", ".")),  # consumption
        float(line[2].replace(",", ".")),  # production
        float(line[3].replace(",", ".")),  # temperature
    ]


def read_data(filename: str) -> list:
    """
    Reads the CSV file and returns the rows in a suitable structure.

    Parameters:
    filename (str): Name of the file containing the electricity consumption and production

    Returns:
    cons_prod (list): Read and converted consumption and production
    """
    cons_prod = []

    with open(filename, "r", encoding="utf-8") as f:
        next(f)
        for line in f:
            line = line.strip()
            fields = line.split(";")
            cons_prod.append(convert_data(fields))

    return cons_prod


def show_main_menu() -> str:
    """
    Prints the main menu and returns the user selection as a string.
    """
    print("\nChoose a report type:")
    print("(1) Daily summary for a date range")
    print("(2) Monthly summary for one month")
    print("(3) Full year 2025 summary")
    print("(4) Exit the program")
    return input("Your choice: ")


def show_sub_menu(report: str) -> str:
    """
    Prints the sub menu and returns the user selection as a string.
    """
    print("What would you like to do next?")
    print("(1) Write the report to the file report.txt")
    print("(2) Create a new report")
    print("(3) Exit")

    selection = input("Your choice: ")

    match selection:
        case "1":
            write_report_to_file(report)

    return selection


def create_daily_report(data: list) -> str:
    """
    Builds a daily report for a selected date range.
    """
    start_date_str = input("Enter start date (dd.mm.yyyy): ")
    start_date = datetime.strptime(start_date_str, "%d.%m.%Y").date()

    end_date_str = input("Enter end date (dd.mm.yyyy): ")
    end_date = datetime.strptime(end_date_str, "%d.%m.%Y").date()

    cons = 0
    prod = 0
    temp = 0
    i = 0

    for per_hour in data:
        if start_date <= per_hour[0].date() <= end_date:
            cons += per_hour[1]
            prod += per_hour[2]
            temp += per_hour[3]
            i += 1

    msg = f"\nReport for the period {start_date_str}-{end_date_str}\n"
    msg += f"- Total consumption: + {cons:.2f}".replace(".", ",") + " kWh\n"
    msg += f"- Total production: + {prod:.2f}".replace(".", ",") + " kWh\n"

    if i > 0:
        avg_temp = temp / i
        msg += f"- Average temperature: + {avg_temp:.2f}".replace(".", ",") + " °C\n"
    else:
        msg += "- Average temperature: + 0,00 °C\n"

    return msg


def create_monthly_report(data: list) -> list[str]:
    """Builds a monthly summary report for a selected month."""
    pass


def create_yearly_report(data: list) -> list[str]:
    """Builds a full-year summary report."""
    pass


def print_report_to_console(lines: str) -> None:
    """
    Prints report lines to the console.
    """
    print(lines)


def write_report_to_file(report: str) -> None:
    """
    Writes the report to report.txt
    """
    out_path = Path(__file__).with_name("report.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(report)


def main() -> None:
    csv_path = Path(__file__).with_name("2025.csv")
    db = read_data(str(csv_path))

    while True:
        match show_main_menu():

            case "1":
                daily_report = create_daily_report(db)
                print_report_to_console(daily_report)

                match show_sub_menu(daily_report):
                    case "1":
                        continue
                    case "2":
                        continue
                    case "3":
                        print("Thank you! Bye!")
                        break

            case "2":
                create_monthly_report(db)

            case "3":
                create_yearly_report(db)

            case "4":
                print("Thank you! Bye!")
                break


if __name__ == "__main__":
    main()
