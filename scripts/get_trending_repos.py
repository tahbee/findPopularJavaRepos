import csv

from bs4 import BeautifulSoup
import requests

repo_number = 0

def access_repo(url, repo_number):
    response = requests.get(url)
    print(response.status_code)
    repos = response.json()
    for repo in repos:
        repo_number = repo_number + 1
        print("Accessing repo number")
        print(repo_number)
        get_repo_info(repo)

def get_repo_info(repo):
    page = requests.get(repo['url'])
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        commit_elements = soup.find_all('span', class_="d-none d-sm-inline")
        commits = commit_elements[1].getText().split()[0].replace(',', '')
    except IndexError:
        commits= "0" # if coud not find commits set as 0 for now- have to manually find them

    if (int(commits) > 500):
        writer.writerow(
            [
                repo['repositoryName'], 
                repo['url'],
                commits,
                repo['totalStars'],
                repo['forks'],
                repo['rank'],
                repo['since'],
                repo['username']
                ]
        )

if __name__ == '__main__':
    with open('collected_repos.csv', mode='w') as result_file:
        writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["repositoryName", "url", "commits", "totalStars", "forks", "rank", "since", "username"])
        url1 = "https://gh-trending-api.herokuapp.com/repositories/java?since=monthly&spoken_language_code=en"
        url2 = "https://gh-trending-api.herokuapp.com/repositories/java?since=weekly&spoken_language_code=en"
        url3 = "https://gh-trending-api.herokuapp.com/repositories/java?since=daily&spoken_language_code=en"
        access_repo(url1, repo_number)
        access_repo(url2, repo_number)
        access_repo(url3, repo_number)