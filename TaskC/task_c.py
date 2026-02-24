from pathlib import Path


def is_confirmed(value: str) -> bool:
    return value.strip().lower() in ("yes", "true", "y", "1")


def main():
    print("Task C\n")

    path = Path(__file__).with_name("reservations.txt")
    lines = path.read_text(encoding="utf-8").splitlines()

    confirmed = []
    not_confirmed = []
    invalid = 0

    for line in lines:
        if not line.strip():
            continue

        parts = [p.strip() for p in line.split("|")]

        if len(parts) < 6:
            invalid += 1
            continue

        if is_confirmed(parts[5]):
            confirmed.append(parts)
        else:
            not_confirmed.append(parts)

    print(f"Total lines: {len(lines)}")
    print(f"Confirmed: {len(confirmed)}")
    print(f"Not confirmed: {len(not_confirmed)}")
    print(f"Invalid rows: {invalid}\n")

    print("Confirmed reservations:")
    for r in confirmed:
        print(f"- {r[0]} | {r[1]} | {r[2]}")

    print("\nNot confirmed reservations:")
    for r in not_confirmed:
        print(f"- {r[0]} | {r[1]} | {r[2]}")


if __name__ == "__main__":
    main()