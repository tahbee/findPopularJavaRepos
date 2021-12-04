import csv

from bs4 import BeautifulSoup
import requests


# def url_generator():
#     with open('urls.txt', 'r') as reader:
#         return reader.readlines()
# def extract_elements_to_csv():
#         page = requests.get(url.strip('\n\r'))
#         soup = BeautifulSoup(page.content, 'html.parser')
#         elements = soup.find_all('a', class_="social-count")
#         starred = elements[0].getText()
#         if 'k' in starred:
#             starred = float(starred.split('k')[0])*1000
#         forked = elements[1].getText()
#         if 'k' in forked:
#             forked = float(forked.split('k')[0]) * 1000
#         commit_elements = soup.find_all('span', class_="d-none d-sm-inline")
#         commits = commit_elements[1].getText().split()[0]
#         license_element = soup.find('a', class_="Link--muted")
#         writer.writerow([url.strip(), int(starred), int(forked), int(commits.strip().replace(",", "")), license_element.getText().strip()])
# def web_scraping():
#     global writer, url
#     githubUrls = url_generator()
#     with open('final_results.csv', mode='w') as result_file:
#         writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         writer.writerow(["url", "starred", "forked", "commits", "license"])
#         for url in githubUrls:
#             extract_elements_to_csv()


def get_repo_info():
    page = requests.get(repo['html_url'])
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        commit_elements = soup.find_all('span', class_="d-none d-sm-inline")
        commits = commit_elements[1].getText().split()[0]
    except IndexError:
        commits= "0" # if coud not find commits set as 0 for now- have to manually find them

    license = "None"
    if repo['license']:
        license = repo['license']['name']
    writer.writerow(
        [repo['name'], repo['html_url'], repo['stargazers_count'], repo['forks_count'], int(commits.replace(",","")), license, repo['updated_at'], repo['size'], repo['visibility'] ])


if __name__ == '__main__':
    with open('results.csv', mode='w') as result_file:
        writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["name", "url", "starred", "forked", "commits", "license", "last-updated", "size", "visibility"])
        for page in range(1, 4):
            response = requests.get("https://api.github.com/search/repositories?q=language:Java&sort=stars&order=desc&per_page=100&page="+str(page))
            print(response.status_code)
            repos = response.json()['items']
            for repo in repos:
                get_repo_info()