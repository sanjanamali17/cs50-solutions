import sys
import csv


def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    infile = sys.argv[1]
    outfile = sys.argv[2]

    students = []

    try:
        with open(infile) as file:
            reader = csv.DictReader(file)

            for row in reader:
                last, first = row["name"].split(", ")
                house = row["house"]

                students.append({
                    "first": first,
                    "last": last,
                    "house": house
                })

    except FileNotFoundError:
        sys.exit(f"Could not read {infile}")

    with open(outfile, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])

        writer.writeheader()
        writer.writerows(students)


if __name__ == "__main__":
    main()
