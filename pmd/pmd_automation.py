import csv
import os
import subprocess

projects_directory = r'/Users/melissaheredia/metrics-workspace/metrics/projects'
metrics_directory = r'/Users/melissaheredia/PycharmProjects/pythonProject/pmd/metrics'
project_map={}
allKeys=set()
WMC_VERY_HIGH = 47
FEW_THRESHOLD = 5
ONE_THIRD_THRESHOLD = 1.0/3.0
#based on pmd god class algorithm https://pmd.sourceforge.io/pmd-5.0.1/xref/net/sourceforge/pmd/lang/java/rule/design/GodClassRule.html
def calculate_god_class():
    atfdCounter=0
    wmcCounter-0

def parse_rows(name):
    csv_reader = csv.reader(csvfile)
    # Skip header row
    next(csv_reader)
    map_rule_count = dict()
    for row in csv_reader:
        rule = row[7]
        map_rule_count[rule] = map_rule_count.get(rule, 0) + 1
    # print(map_rule_count)
    project_map[name]= map_rule_count
    for key, value in map_rule_count.items():
        allKeys.add(key)
    #     print(key + ": "+ str(value))
    if 'GodClass' in map_rule_count:
        print('GodClass: '+ str(map_rule_count['GodClass']), end= " ")
    if 'ExcessiveMethodLength' in map_rule_count:
        print('ExcessiveMethodLength: '+ str(map_rule_count['ExcessiveMethodLength']))
    print('\n')



def get_metrics_data():
    print("Getting Metrics Data!")
    process = subprocess.Popen(["sh", "getPmdData.sh"])
    process.wait()
    print("Getting Metrics Data Completed!")


def write_to_results_file():
    with open('results_pmd_analysis.csv', mode='w') as result_file:
        writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Project"] + sorted(all_keys_list))

        for project, code_smell_map in project_map.items():
            num_code_smell = [project.split(".")[0]]
            for code_smell in all_keys_list:
                if code_smell in code_smell_map:
                    num_code_smell.append(code_smell_map[code_smell])
                else:
                    num_code_smell.append(0)

            writer.writerow(num_code_smell)


if __name__ == '__main__':
    # get_metrics_data()

    for entry in os.scandir(metrics_directory):
        file_path = entry.path
        if file_path.endswith(".csv") and entry.is_file():
            print(entry.name.split(".")[0])
            with open(file_path, 'r') as csvfile:
                parse_rows(entry.name)

    all_keys_list= list(allKeys)
    # write_to_results_file()


