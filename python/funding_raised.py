import csv
from re import M


class FundingRaised:
    @staticmethod
    def where(options={}):
        csv_data = read_csv_file("../startup_funding.csv")

        funding = []
        if "company_name" in options:
            result = []
            for row in csv_data:
                if row[1] == options["company_name"]:
                    result.append(row)
            csv_data = result

        if "city" in options:
            result = []
            for row in csv_data:
                if row[4] == options["city"]:
                    result.append(row)
            csv_data = result

        if "state" in options:
            result = []
            for row in csv_data:
                if row[5] == options["state"]:
                    result.append(row)
            csv_data = result

        if "round" in options:
            result = []
            for row in csv_data:
                if row[9] == options["round"]:
                    result.append(row)
            csv_data = result

        output = []
        for row in csv_data:
            mapped = create_mapping(row)
            output.append(mapped)

        return output

    @staticmethod
    def find_by(options):
        csv_data = read_csv_file("../startup_funding.csv")

        for option in options:
            valid_options = {"company_name": 1, "city": 4, "state": 5, "round": 9}
            if option in valid_options:
                for row in csv_data:
                    if row[valid_options[option]] == options[option]:
                        return create_mapping(row)

        raise RecordNotFound


def read_csv_file(filename):
    with open(filename, "rt") as csvfile:
        data = csv.reader(csvfile, delimiter=",", quotechar='"')
        # skip header
        next(data)
        csv_data = []
        for row in data:
            csv_data.append(row)
        return csv_data


def create_mapping(row):
    mapped = {}
    mapped["permalink"] = row[0]
    mapped["company_name"] = row[1]
    mapped["number_employees"] = row[2]
    mapped["category"] = row[3]
    mapped["city"] = row[4]
    mapped["state"] = row[5]
    mapped["funded_date"] = row[6]
    mapped["raised_amount"] = row[7]
    mapped["raised_currency"] = row[8]
    mapped["round"] = row[9]
    return mapped


class RecordNotFound(Exception):
    pass
