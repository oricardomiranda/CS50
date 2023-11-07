import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        raise ValueError("Usage: python dna.py csvfile txtfile")

    # Read the database file into a variable
    database = read_database(sys.argv[1])

    # Read DNA sequence file into a variable
    with open(sys.argv[2], mode="r") as txtfile:
        sequence = txtfile.read()

    # Find longest match of each STR in DNA sequence
    results = {}
    for i in range(1, len(database[0])):
        subsequence = database[0][i]
        results[subsequence] = longest_match(sequence, subsequence)

    # Check database for matching profiles
    for person in database[1:]:
        person_dna = [int(i) for i in person[1:]]

        if person_dna == list(results.values()):
            print(person[0])
            return

    print("No match")


def read_database(database_file):
    database = []
    with open(database_file, mode="r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            database.append(row)
    return database


def longest_match(sequence, subsequence):
    count = 0
    max_count = 0
    i = 0

    while i < len(sequence):
        if sequence[i : i + len(subsequence)] == subsequence:
            count += 1
            i += len(subsequence)
        else:
            max_count = max(count, max_count)
            count = 0
            i += 1

    return max(max_count, count)


if __name__ == "__main__":
    main()
