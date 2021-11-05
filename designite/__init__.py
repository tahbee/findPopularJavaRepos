import csv
import os
import subprocess

import requests

projects_directory = r'/Users/melissaheredia/metrics-workspace/projects'
metrics_directory = r'/Users/melissaheredia/metrics-workspace/designite/'
map_project_count={}
allKeys=set()

def parse_file():
    file_path = entry.path
    if (file_path.endswith("designCodeSmells.csv") or file_path.endswith(
            "implementationCodeSmells.csv")) and entry.is_file():
        column_index=3
        if file_path.endswith("implementationCodeSmells.csv"):
            column_index=4
        print(entry.name.split(".")[0])
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            # Skip header row
            next(csv_reader)

            for row in csv_reader:
                rule = row[column_index]
                map_rule_count[rule] = map_rule_count.get(rule, 0) + 1




def write_to_results_file():
    all_keys_list=list(allKeys)
    with open('results_designate_analysis_final.csv', mode='w') as result_file:
        writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Project"] + sorted(all_keys_list))

        for project, code_smell_map in map_project_count.items():
            num_code_smell = [project.split(".")[0]]
            for code_smell in all_keys_list:
                if code_smell in code_smell_map:
                    num_code_smell.append(code_smell_map[code_smell])
                else:
                    num_code_smell.append(0)

            writer.writerow(num_code_smell)
if __name__ == '__main__':
    print("Getting Metrics Data!")
    process = subprocess.Popen(["sh", "getDesignateData.sh"])
    process.wait()
    print("Getting Metrics Data Completed!")
    # for repo in os.scandir(projects_directory):
    #     repo_name = repo.name
    #     print(repo_name)
    #     #create project with repo gane and key
    #     r = requests.post('http://localhost:9000/projects/create', data={'name': repo_name, 'key': repo_name,'visibility': 'public' })
    #     print(r)
    #     print(r.text)

        # duplication= requests.get('http://localhost:9000/projects/create', data={ 'key': repo_name})
        # print(duplication.status_code)
        # print(duplication.content)
        # print(duplication.text)
    for repo in os.scandir(metrics_directory):
        repo_name = repo.name
        print(repo_name)
        map_rule_count = {}
        for entry in os.scandir(metrics_directory+repo_name):
            parse_file()
        for key, value in map_rule_count.items():
            allKeys.add(key)
        print(entry.name.split('.')[0])
        map_project_count[repo_name]= map_rule_count
        if 'Long Method' in map_rule_count:
            print('Long Method: ' + str(map_rule_count['Long Method']))

    print(map_project_count)
    write_to_results_file()