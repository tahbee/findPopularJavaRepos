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
                    print(file.name)
                    print("Gradle Project")
                    os.path.exists(file.path)
                    process = subprocess.Popen(["./gradlew","clean", "build", "-x", "test"], cwd=repo_path)
                    process.wait()
                    break
                elif file.name.startswith("pom.xml"):
                    print(file.name)
                    print("Maven Project")
                    process = subprocess.Popen(["mvn", "clean","install"], cwd=repo_path)
                    process.wait()
                    break
                else:
                    print("could not detect project")




