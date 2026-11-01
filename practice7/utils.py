import csv


def get_contacts_from_csv(path):
    with open(path) as file:
        csv_reader = csv.reader(file, delimiter=",")
        result = []
        for row in csv_reader:
            result.append(tuple(row))

    return result

