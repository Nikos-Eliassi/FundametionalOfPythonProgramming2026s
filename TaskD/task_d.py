# Copyright (c) 2026 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

from datetime import datetime, date
from pathlib import Path


def convert_data(fields: list) -> list:
    """
    Converts string fields to appropriate data types.

    Returns list in format:
    [datetime, c1_wh, c2_wh, c3_wh, p1_wh, p2_wh, p3_wh]
    """
    dt = datetime.strptime(fields[0].strip(), "%Y-%m-%dT%H:%M:%S")
    values = [int(field.strip()) for field in fields[1:]]
    return [dt] + values


def read_data(filename: str) -> list:
    """
    Reads the CSV file and returns the rows in a suitable structure.

    Parameters:
        filename (str): Name of the file containing the electricity consumption and production

    Returns:
        list: Read and converted consumption and production rows
    """
    consumption_and_production = []
    file_path = Path(__file__).with_name(filename)

    with open(file_path, "r", encoding="utf-8") as f:
        next(f)  # skip header
        for line in f:
            fields = line.strip().split(";")
            if len(fields) >= 7:
                consumption_and_production.append(convert_data(fields))

    return consumption_and_production


def day_information(day: date, database: list) -> str:
    """
    Computes consumption and production totals for one day (kWh, by phase)
    and returns a formatted string for printing.
    """
    consumption_phase1 = 0.0
    consumption_phase2 = 0.0
    consumption_phase3 = 0.0
    production_phase1 = 0.0
    production_phase2 = 0.0
    production_phase3 = 0.0

    for per_hour in database:
        if per_hour[0].date() == day:
            consumption_phase1 += per_hour[1] / 1000
            consumption_phase2 += per_hour[2] / 1000
            consumption_phase3 += per_hour[3] / 1000
            production_phase1 += per_hour[4] / 1000
            production_phase2 += per_hour[5] / 1000
            production_phase3 += per_hour[6] / 1000

    cp1 = f"{consumption_phase1:.2f}".replace(".", ",")
    cp2 = f"{consumption_phase2:.2f}".replace(".", ",")
    cp3 = f"{consumption_phase3:.2f}".replace(".", ",")
    pp1 = f"{production_phase1:.2f}".replace(".", ",")
    pp2 = f"{production_phase2:.2f}".replace(".", ",")
    pp3 = f"{production_phase3:.2f}".replace(".", ",")

    return (
        f"{day.strftime('%d.%m.%Y'):<13}"
        f"{cp1:>8}{cp2:>8}{cp3:>8}"
        f"{pp1:>8}{pp2:>8}{pp3:>8}"
    )


def main() -> None:
    """
    Main function: reads data, computes daily totals, and prints the report.
    """
    database = read_data("week42.csv")

    print("Week 42 electricity consumption and production (kWh, by phase)\n")
    print("Day          Date        Consumption [kWh]          Production [kWh]")
    print("             (dd.mm.yyyy)   v1      v2      v3        v1      v2      v3")
    print("--------------------------------------------------------------------------")

    unique_days = set()
    for row in database:
        unique_days.add(row[0].date())

    finnish_days = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]

    for day in sorted(unique_days):
        day_name = finnish_days[day.weekday()]
        print(f"{day_name:<12} {day_information(day, database)}")


if __name__ == "__main__":
    main()
