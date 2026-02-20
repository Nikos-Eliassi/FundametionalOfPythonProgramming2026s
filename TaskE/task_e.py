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
    """Parse datetime from different possible formats (robust)."""
    value = value.strip().lstrip("\ufeff")

    # ISO 8601
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        pass

    # Alternatives if needed
    for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M:%S", "%d.%m.%Y %H:%M", "%d.%m.%Y %H:%M:%S"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue

    raise ValueError(f"Unknown datetime format: {value!r}")


def parse_number(value: str) -> int:
    """Parse numeric field as integer (Wh)."""
    value = value.strip().lstrip("\ufeff")
    value = value.replace(",", ".")
    return int(float(value))


def convert_data(line: list) -> list:
    """
    Convert data types to meet program requirements

    line -> 7 columns:
    0: datetime
    1..3: consumption V1..V3 (Wh)
    4..6: production  V1..V3 (Wh)
    """
    return [
        parse_dt(line[0]),
        parse_number(line[1]),
        parse_number(line[2]),
        parse_number(line[3]),
        parse_number(line[4]),
        parse_number(line[5]),
        parse_number(line[6]),
    ]


def read_data(filename: str) -> list:
    """
    Reads the CSV file and returns the rows in a suitable structure.
    """
    cons_prod = []
    file_path = Path(__file__).with_name(filename)

    with open(file_path, "r", encoding="utf-8") as f:
        header_skipped = False

        for raw in f:
            line = raw.strip().lstrip("\ufeff")
            if not line:
                continue

            # skip first non-empty line (header)
            if not header_skipped:
                header_skipped = True
                continue

            fields = [x.strip() for x in line.split(";")]

            # if a weird extra header row exists, ignore it safely
            if len(fields) != 7:
                continue

            cons_prod.append(convert_data(fields))

    return cons_prod


def week_header(number: int) -> str:
    """Create a nicely aligned header so Production V2 and V3 are visible."""
    header = f"Week {number} electricity consumption and production (kWh, by phase)\n\n"
    header += f"{'Day':<11}{'Date':<13}{'Consumption (kWh)':>26}{'':2}{'Production (kWh)':>26}\n"
    header += f"{'':<24}{'V1':>8}{'V2':>8}{'V3':>8}{'':2}{'V1':>8}{'V2':>8}{'V3':>8}\n"
    return header


def day_information(day: date, database: list) -> str:
    """
    Compute day totals (kWh) and return one formatted line.
    """
    # [dayname, date, consV1, consV2, consV3, prodV1, prodV2, prodV3] in kWh
    totals = [None, None, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    for per_hour in database:
        if per_hour[0].date() == day:
            # per_hour[1..6] are Wh -> convert to kWh
            totals[2] += per_hour[1] / 1000.0
            totals[3] += per_hour[2] / 1000.0
            totals[4] += per_hour[3] / 1000.0
            totals[5] += per_hour[4] / 1000.0
            totals[6] += per_hour[5] / 1000.0
            totals[7] += per_hour[6] / 1000.0

    day_name = DAYS[day.weekday()]
    date_str = day.strftime("%d.%m.%Y")

    def fmt(x: float) -> str:
        return f"{x:.2f}".replace(".", ",")

    # IMPORTANT: production V2 and V3 are explicitly printed here (totals[6], totals[7])
    return (
        f"{day_name:<11}{date_str:<13}"
        f"{fmt(totals[2]):>8}{fmt(totals[3]):>8}{fmt(totals[4]):>8}  "
        f"{fmt(totals[5]):>8}{fmt(totals[6]):>8}{fmt(totals[7]):>8}\n"
    )


def write_data(content: str) -> None:
    """Write the content to summary.txt in the same folder."""
    out_path = Path(__file__).with_name("summary.txt")
    out_path.write_text(content, encoding="utf-8")


def main() -> None:
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
