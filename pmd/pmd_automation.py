import csv
import os
from collections import defaultdict
if __name__ == '__main__':

    directory = r'/Users/melissaheredia/metrics-workspace/metrics/projects'
    for entry in os.scandir(directory):
        file_path = entry.path
        if file_path.endswith(".csv") and entry.is_file():
            print(entry.name.split(".")[0])
            with open(file_path, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                # Skip header row
                fields = next(csvreader)
                mapRuleCount = dict()
                for row in csvreader:
                    rule = row[7]
                    mapRuleCount[rule]=mapRuleCount.get(rule,0)+1
                print(mapRuleCount)



