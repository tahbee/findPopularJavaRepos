**Instructions to calculate the repository metrics**
1) Make sure to have the BeautifulSoup and Requests python libraries installed, as well as a version of python(3.4 or above) that has the statistics library in the python standard library. ( pip install requests, pip install beautifulsoup4)
2) Run getFinalRepoData.py to get a csv file with the number of commits, stars, and forks for each repository specified in the script
3) After validating that the information in the generated csv file is correct, copy the commit, star, and fork numbers from the csv file into the respective arrays in the calculate_repo_metrics.py script
4) Run the calculate_repo_metrics.py script to get the reposi