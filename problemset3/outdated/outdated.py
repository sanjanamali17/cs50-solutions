def main():
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()

            # Format: M/D/YYYY
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

            # Format: Month D, YYYY
            elif "," in date:
                month_day, year = date.split(",")
                month_name, day = month_day.strip().split(" ")
                if month_name not in months:
                    continue

                month = months.index(month_name) + 1
                day = int(day)
                year = int(year.strip())

            else:
                continue

            # Validation
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break

        except (ValueError, IndexError):
            continue


if __name__ == "__main__":
    main()
