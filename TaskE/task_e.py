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


def parse_dt(value: str) -> datetime:
    """Parse datetime robustly (handles ISO and dd.mm.yyyy formats)."""
    value = value.strip().lstrip("\ufeff")

    # 1) ISO 8601 variants
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        pass

    # 2) dd.mm.yyyy variants (common in these tasks)
    for fmt in ("%d.%m.%Y %H:%M", "%d.%m.%Y %H:%M:%S"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue

    # 3) other common variants if needed
    for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue

    raise ValueError(f"Unknown datetime format: {value!r}")


def parse_number(value: str) -> int:
    """Parse numeric value safely as integer (Wh)."""
    value = value.strip().lstrip("\ufeff")
    # normalize possible decimal commas just in case
    value = value.replace(",", ".")
    return int(float(value))


def convert_data(fields: list) -> list:
    """
    fields -> 7 columns:
    0: datetime
    1..3: consumption V1..V3 (Wh)
    4..6: production  V1..V3 (Wh)
    """
    return [
        parse_dt(fields[0]),
        parse_number(fields[1]),
        parse_number(fields[2]),
        parse_number(fields[3]),
        parse_number(fields[4]),
        parse_number(fields[5]),
        parse_number(fields[6]),
    ]


def read_data(filename: str) -> list:
    """Reads the CSV file and returns rows in a suitable structure."""
    cons_prod = []
    file_path = Path(__file__).with_name(filename)

    with open(file_path, "r", encoding="utf-8") as f:
        # Skip header (first non-empty line)
        header_skipped = False

        for raw in f:
            line = raw.strip().lstrip("\ufeff")
            if not line:
                continue

            if not header_skipped:
                header_skipped = True
                continue

            fields = [x.strip() for x in line.split(";")]
            if len(fields) != 7:
                # ignore unexpected rows safely
                continue

            cons_prod.append(convert_data(fields))

    return cons_prod


def week_header(number: int) -> str:
    header = f"Week {number} electricity consumption and production (kWh, by phase)\n\n"
    header += f"{'Day':<11}{'Date':<13}{'Consumption (kWh)':>26}{'':2}{'Production (kWh)':>26}\n"
    header += f"{'':<24}{'V1':>8}{'V2':>8}{'V3':>8}{'':2}{'V1':>8}{'V2':>8}{'V3':>8}\n"
    return header


def day_information(day: date, database: list) -> str:
    """
    Returns one day totals line:
    consumption V1..V3 + production V1..V3 (kWh)
    """
    cons_v1 = cons_v2 = cons_v3 = 0.0
    prod_v1 = prod_v2 = prod_v3 = 0.0

    for per_hour in database:
        if per_hour[0].date() == day:
            # Wh -> kWh
            cons_v1 += per_hour[1] / 1000.0
            cons_v2 += per_hour[2] / 1000.0
            cons_v3 += per_hour[3] / 1000.0
            prod_v1 += per_hour[4] / 1000.0
            prod_v2 += per_hour[5] / 1000.0
            prod_v3 += per_hour[6] / 1000.0

    def fmt(x: float) -> str:
        return f"{x:.2f}".replace(".", ",")

    day_name = DAYS[day.weekday()]
    date_str = day.strftime("%d.%m.%Y")

    return (
        f"{day_name:<11}{date_str:<13}"
        f"{fmt(cons_v1):>8}{fmt(cons_v2):>8}{fmt(cons_v3):>8}  "
        f"{fmt(prod_v1):>8}{fmt(prod_v2):>8}{fmt(prod_v3):>8}\n"
    )


def write_data(content: str) -> None:
    out_path = Path(__file__).with_name("summary.txt")
    out_path.write_text(content, encoding="utf-8")


def main() -> None:
    file_content = ""

    # Week 41
    db = read_data("week41.csv")
    file_content += week_header(41)
    for i in range(6, 13):
        file_content += day_information(date(2025, 10, i), db)

    # Week 42 (THIS WILL NOW MATCH dd.mm.yyyy dates too)
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
