import csv
import os


def parse_rows():
    csv_reader = csv.reader(csvfile)
    # Skip header row
    next(csv_reader)
    map_rule_count = dict()
    for row in csv_reader:
        rule = row[7]
        map_rule_count[rule] = map_rule_count.get(rule, 0) + 1
    print(map_rule_count)


if __name__ == '__main__':
    directory = r'/Users/melissaheredia/metrics-workspace/metrics/projects'
    for entry in os.scandir(directory):
        file_path = entry.path
        if file_path.endswith(".csv") and entry.is_file():
            print(entry.name.split(".")[0])
            with open(file_path, 'r') as csvfile:
                parse_rows()



