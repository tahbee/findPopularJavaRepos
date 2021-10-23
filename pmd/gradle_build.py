import csv
import os
import subprocess
import os.path
from os import path

projects_directory = r'/Users/melissaheredia/metrics-workspace/projects'

if __name__ == '__main__':
    for repo in os.scandir(projects_directory):
        repo_path = repo.path
        print(repo_path)
        if not repo.name.startswith('.'):
            for file in os.scandir(repo_path):
                if file.name.startswith("build.gradle"):
                    print("Gradle Project")
                    process = subprocess.Popen(["gradle", "build"], cwd=repo_path)
                    process.wait()
                elif file.name.startswith("pom.xml"):
                    print("Maven Project")
                    process = subprocess.Popen(["mvn", "build"], cwd=repo_path)
                    process.wait()
                else:
                    print("could not detect project")



