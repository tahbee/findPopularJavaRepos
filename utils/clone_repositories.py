from git import Repo
projects_directory = 'REPLACE_WITH_PROJECTS_DIRECTORY'

if __name__ == '__main__':
    with open('github_repos_to_clone') as file:
        repos = file.readlines()
        repos = [line.rstrip() for line in repos]
        for repo_url in repos:
            split_url = repo_url.split('/')
            repo_name = '/'+split_url[len(split_url)-1]
            Repo.clone_from(repo_url, projects_directory + repo_name)

